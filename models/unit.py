from dataclasses import dataclass
from typing import Callable, Optional, Union

@dataclass(frozen=True)
class Unit:
    symbol: str
    name: str
    conversion_factor: Union[float, Callable]
    category: str
    description: str = ""
    
    def __post_init__(self):
        if not self.symbol or not self.name:
            raise ValueError("Symbol et name sont requis")
    
    @property
    def is_temperature(self) -> bool:
        return callable(self.conversion_factor)
    
    def __str__(self) -> str:
        return f"{self.symbol} ({self.name})"