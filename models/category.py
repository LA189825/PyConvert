from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Category:
    name: str
    display_name: str
    description: str = ""
    
    def __str__(self) -> str:
        return self.display_name

LENGTH = Category("length", "Longueur", "Mesures de distance dans l'espace")
MASS = Category("mass", "Masse", "Mesures de masse stellaire")
TEMPERATURE = Category("temperature", "Température", "Mesures thermiques cosmiques")
TIME = Category("time", "Temps", "Mesures temporelles relativistes")
ENERGY = Category("energy", "Énergie", "Mesures énergétiques")
POWER = Category("power", "Puissance", "Mesures de puissance")
PRESSURE = Category("pressure", "Pression", "Mesures de pression atmosphérique")
AREA = Category("area", "Surface", "Mesures de superficie")
VOLUME = Category("volume", "Volume", "Mesures de volume")
SPEED = Category("speed", "Vitesse", "Mesures de vélocité")
FREQUENCY = Category("frequency", "Fréquence", "Mesures de fréquence")
DATA = Category("data", "Données", "Mesures de données numériques")
