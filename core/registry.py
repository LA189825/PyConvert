from typing import Dict, List
from models.unit import Unit
from models.category import *

class UnitRegistry:
    
    _instance = None
    _units: Dict[str, Unit] = {}
    _categories: Dict[str, Category] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialize_registry()
        return cls._instance
    
    @classmethod
    def _initialize_registry(cls):
        # Ajout des catégories
        for cat in [LENGTH, MASS, TEMPERATURE, TIME, ENERGY, POWER, 
                   PRESSURE, AREA, VOLUME, SPEED, FREQUENCY, DATA]:
            cls._categories[cat.name] = cat
        
        # Unités de longueur
        cls._register_unit(Unit("m", "mètre", 1.0, LENGTH.name, "Unité SI de longueur"))
        cls._register_unit(Unit("km", "kilomètre", 1000.0, LENGTH.name))
        cls._register_unit(Unit("cm", "centimètre", 0.01, LENGTH.name))
        cls._register_unit(Unit("mm", "millimètre", 0.001, LENGTH.name))
        cls._register_unit(Unit("μm", "micromètre", 1e-6, LENGTH.name))
        cls._register_unit(Unit("nm", "nanomètre", 1e-9, LENGTH.name))
        cls._register_unit(Unit("in", "pouce", 0.0254, LENGTH.name))
        cls._register_unit(Unit("ft", "pied", 0.3048, LENGTH.name))
        cls._register_unit(Unit("yd", "yard", 0.9144, LENGTH.name))
        cls._register_unit(Unit("mi", "mile", 1609.344, LENGTH.name))
        cls._register_unit(Unit("nmi", "mille nautique", 1852.0, LENGTH.name))
        cls._register_unit(Unit("ly", "année-lumière", 9.4607304725808e15, LENGTH.name))
        cls._register_unit(Unit("au", "unité astronomique", 149597870700.0, LENGTH.name))
        
        # Unités de masse
        cls._register_unit(Unit("g", "gramme", 1.0, MASS.name, "Unité SI de masse"))
        cls._register_unit(Unit("kg", "kilogramme", 1000.0, MASS.name))
        cls._register_unit(Unit("mg", "milligramme", 0.001, MASS.name))
        cls._register_unit(Unit("μg", "microgramme", 1e-6, MASS.name))
        cls._register_unit(Unit("t", "tonne", 1e6, MASS.name))
        cls._register_unit(Unit("lb", "livre", 453.592, MASS.name))
        cls._register_unit(Unit("oz", "once", 28.3495, MASS.name))
        cls._register_unit(Unit("ct", "carat", 0.2, MASS.name))
        cls._register_unit(Unit("st", "stone", 6350.29, MASS.name))
        
        # Unités de température
        cls._register_unit(Unit("C", "Celsius", lambda x: x, TEMPERATURE.name))
        cls._register_unit(Unit("F", "Fahrenheit", lambda x: (x - 32) * 5/9, TEMPERATURE.name))
        cls._register_unit(Unit("K", "Kelvin", lambda x: x - 273.15, TEMPERATURE.name))
        cls._register_unit(Unit("R", "Rankine", lambda x: (x - 491.67) * 5/9, TEMPERATURE.name))
        
        # Unités de temps
        cls._register_unit(Unit("s", "seconde", 1.0, TIME.name, "Unité SI de temps"))
        cls._register_unit(Unit("ms", "milliseconde", 0.001, TIME.name))
        cls._register_unit(Unit("μs", "microseconde", 1e-6, TIME.name))
        cls._register_unit(Unit("ns", "nanoseconde", 1e-9, TIME.name))
        cls._register_unit(Unit("min", "minute", 60.0, TIME.name))
        cls._register_unit(Unit("h", "heure", 3600.0, TIME.name))
        cls._register_unit(Unit("d", "jour", 86400.0, TIME.name))
        cls._register_unit(Unit("week", "semaine", 604800.0, TIME.name))
        cls._register_unit(Unit("year", "année", 31536000.0, TIME.name))
        
        # Unités d'énergie
        cls._register_unit(Unit("J", "joule", 1.0, ENERGY.name, "Unité SI d'énergie"))
        cls._register_unit(Unit("kJ", "kilojoule", 1000.0, ENERGY.name))
        cls._register_unit(Unit("cal", "calorie", 4.184, ENERGY.name))
        cls._register_unit(Unit("kcal", "kilocalorie", 4184.0, ENERGY.name))
        cls._register_unit(Unit("Wh", "watt-heure", 3600.0, ENERGY.name))
        cls._register_unit(Unit("kWh", "kilowatt-heure", 3600000.0, ENERGY.name))
        cls._register_unit(Unit("BTU", "British Thermal Unit", 1055.06, ENERGY.name))
        cls._register_unit(Unit("eV", "électronvolt", 1.60218e-19, ENERGY.name))
        
        # Unités de puissance
        cls._register_unit(Unit("W", "watt", 1.0, POWER.name, "Unité SI de puissance"))
        cls._register_unit(Unit("kW", "kilowatt", 1000.0, POWER.name))
        cls._register_unit(Unit("MW", "mégawatt", 1e6, POWER.name))
        cls._register_unit(Unit("GW", "gigawatt", 1e9, POWER.name))
        cls._register_unit(Unit("hp", "cheval-vapeur", 745.7, POWER.name))
        cls._register_unit(Unit("PS", "Pferdestärke", 735.5, POWER.name))
        
        # Unités de pression
        cls._register_unit(Unit("Pa", "pascal", 1.0, PRESSURE.name, "Unité SI de pression"))
        cls._register_unit(Unit("kPa", "kilopascal", 1000.0, PRESSURE.name))
        cls._register_unit(Unit("bar", "bar", 100000.0, PRESSURE.name))
        cls._register_unit(Unit("mbar", "millibar", 100.0, PRESSURE.name))
        cls._register_unit(Unit("psi", "pound per square inch", 6894.76, PRESSURE.name))
        cls._register_unit(Unit("atm", "atmosphère", 101325.0, PRESSURE.name))
        cls._register_unit(Unit("mmHg", "millimètre de mercure", 133.322, PRESSURE.name))
        cls._register_unit(Unit("inHg", "pouce de mercure", 3386.39, PRESSURE.name))
        
        # Unités de surface
        cls._register_unit(Unit("m²", "mètre carré", 1.0, AREA.name, "Unité SI de surface"))
        cls._register_unit(Unit("km²", "kilomètre carré", 1e6, AREA.name))
        cls._register_unit(Unit("cm²", "centimètre carré", 0.0001, AREA.name))
        cls._register_unit(Unit("mm²", "millimètre carré", 1e-6, AREA.name))
        cls._register_unit(Unit("ha", "hectare", 10000.0, AREA.name))
        cls._register_unit(Unit("ac", "acre", 4046.86, AREA.name))
        cls._register_unit(Unit("sqin", "pouce carré", 0.00064516, AREA.name))
        cls._register_unit(Unit("sqft", "pied carré", 0.092903, AREA.name))
        
        # Unités de volume
        cls._register_unit(Unit("m³", "mètre cube", 1.0, VOLUME.name, "Unité SI de volume"))
        cls._register_unit(Unit("L", "litre", 0.001, VOLUME.name))
        cls._register_unit(Unit("mL", "millilitre", 1e-6, VOLUME.name))
        cls._register_unit(Unit("cm³", "centimètre cube", 1e-6, VOLUME.name))
        cls._register_unit(Unit("gal", "gallon (US)", 0.00378541, VOLUME.name))
        cls._register_unit(Unit("gal_uk", "gallon (UK)", 0.00454609, VOLUME.name))
        cls._register_unit(Unit("qt", "quart (US)", 0.000946353, VOLUME.name))
        cls._register_unit(Unit("pt", "pinte (US)", 0.000473176, VOLUME.name))
        cls._register_unit(Unit("fl_oz", "once liquide (US)", 2.95735e-5, VOLUME.name))
        
        # Unités de vitesse
        cls._register_unit(Unit("m/s", "mètre par seconde", 1.0, SPEED.name, "Unité SI de vitesse"))
        cls._register_unit(Unit("km/h", "kilomètre par heure", 1/3.6, SPEED.name))
        cls._register_unit(Unit("mph", "mile par heure", 0.44704, SPEED.name))
        cls._register_unit(Unit("kn", "nœud", 0.514444, SPEED.name))
        cls._register_unit(Unit("ft/s", "pied par seconde", 0.3048, SPEED.name))
        cls._register_unit(Unit("c", "vitesse de la lumière", 299792458.0, SPEED.name))
        
        # Unités de fréquence
        cls._register_unit(Unit("Hz", "hertz", 1.0, FREQUENCY.name, "Unité SI de fréquence"))
        cls._register_unit(Unit("kHz", "kilohertz", 1000.0, FREQUENCY.name))
        cls._register_unit(Unit("MHz", "mégahertz", 1e6, FREQUENCY.name))
        cls._register_unit(Unit("GHz", "gigahertz", 1e9, FREQUENCY.name))
        cls._register_unit(Unit("THz", "térahertz", 1e12, FREQUENCY.name))
        
        # Unités de données
        cls._register_unit(Unit("B", "octet", 1.0, DATA.name, "Unité de base de donnée"))
        cls._register_unit(Unit("KB", "kilooctet", 1000.0, DATA.name))
        cls._register_unit(Unit("MB", "mégaoctet", 1e6, DATA.name))
        cls._register_unit(Unit("GB", "gigaoctet", 1e9, DATA.name))
        cls._register_unit(Unit("TB", "téraoctet", 1e12, DATA.name))
        cls._register_unit(Unit("KiB", "kibioctet", 1024.0, DATA.name))
        cls._register_unit(Unit("MiB", "mébioctet", 1048576.0, DATA.name))
        cls._register_unit(Unit("GiB", "gibioctet", 1073741824.0, DATA.name))
        cls._register_unit(Unit("TiB", "tébioctet", 1099511627776.0, DATA.name))
    
    @classmethod
    def _register_unit(cls, unit: Unit):
        if unit.symbol in cls._units:
            raise ValueError(f"Unité déjà enregistrée: {unit.symbol}")
        cls._units[unit.symbol] = unit
    
    @classmethod
    def get_unit(cls, symbol: str) -> Unit:
        if symbol not in cls._units:
            raise KeyError(f"Unité inconnue: {symbol}")
        return cls._units[symbol]
    
    @classmethod
    def get_units_by_category(cls, category: str) -> List[Unit]:
        return [unit for unit in cls._units.values() if unit.category == category]
    
    @classmethod
    def get_categories(cls) -> List[Category]:
        return list(cls._categories.values())
    
    @classmethod
    def get_category(cls, name: str) -> Category:
        if name not in cls._categories:
            raise KeyError(f"Catégorie inconnue: {name}")
        return cls._categories[name]