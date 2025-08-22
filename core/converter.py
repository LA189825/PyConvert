from typing import Union
from models.unit import Unit
from core.registry import UnitRegistry
from utils.exceptions import ConversionError

class UltimateConverter:
    
    def __init__(self):
        self.registry = UnitRegistry()
    
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        try:
            source_unit = self.registry.get_unit(from_unit)
            target_unit = self.registry.get_unit(to_unit)
            
            if source_unit.category != target_unit.category:
                raise ConversionError(
                    f"Conversion impossible entre {source_unit.category} et {target_unit.category}"
                )
            
            if source_unit.is_temperature:
                return self._convert_temperature(value, source_unit, target_unit)
            
            base_value = value * source_unit.conversion_factor
            
            result = base_value / target_unit.conversion_factor
            
            return result
            
        except KeyError as e:
            raise ConversionError(f"Unité inconnue: {str(e)}")
        except Exception as e:
            raise ConversionError(f"Erreur de conversion: {str(e)}")
    
    def _convert_temperature(self, value: float, from_unit: Unit, to_unit: Unit) -> float:
        celsius = from_unit.conversion_factor(value)
        
        if to_unit.symbol == "C":
            return celsius
        elif to_unit.symbol == "F":
            return celsius * 9/5 + 32
        elif to_unit.symbol == "K":
            return celsius + 273.15
        elif to_unit.symbol == "R":
            return (celsius + 273.15) * 9/5
        else:
            raise ConversionError(f"Conversion de température non supportée: {to_unit.symbol}")
    
    def get_compatible_units(self, unit_symbol: str) -> list:
        unit = self.registry.get_unit(unit_symbol)
        return [u.symbol for u in self.registry.get_units_by_category(unit.category)]
