class UltimateConverterError(Exception):
    pass

class ConversionError(UltimateConverterError):
    pass

class UnitNotFoundError(UltimateConverterError):
    pass

class CategoryNotFoundError(UltimateConverterError):
    pass