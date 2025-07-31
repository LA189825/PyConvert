# ultimate_converter/interfaces/cli.py

import sys
from rich.console import Console
from rich.prompt import Prompt, FloatPrompt
from rich.table import Table
from rich.panel import Panel

from core.converter import UltimateConverter
from core.registry import UnitRegistry
from utils.exceptions import ConversionError

class MissionControl:
    
    def __init__(self):
        self.console = Console()
        self.converter = UltimateConverter()
        self.registry = UnitRegistry()
    
    def launch(self):
        """Lancement principal"""
        self._display_header()
        
        while True:
            try:
                self._conversion_cycle()
                if not self._continue_prompt():
                    break
            except KeyboardInterrupt:
                self._exit_gracefully()
            except Exception as e:
                self.console.print(f"[red]Erreur: {e}[/red]")
    
    def _display_header(self):
        self.console.print(Panel("[bold blue]Convertisseur d'Unités ULTIME[/bold blue]", expand=False))
    
    def _conversion_cycle(self):
        # Sélection catégorie
        category = self._select_category()
        
        # Affichage unités
        self._show_units(category.name)
        
        # Paramètres conversion
        value = FloatPrompt.ask("Valeur")
        from_unit = self._get_valid_unit("Unité source")
        to_unit = self._get_valid_unit("Unité cible")
        
        # Conversion
        try:
            result = self.converter.convert(value, from_unit, to_unit)
            self.console.print(f"[green]{value} {from_unit} = {result:.8f} {to_unit}[/green]")
        except ConversionError as e:
            self.console.print(f"[red]Erreur: {e}[/red]")
    
    def _select_category(self):
        categories = self.registry.get_categories()
        
        table = Table(show_header=True)
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Catégorie", style="white")
        
        for i, cat in enumerate(categories, 1):
            table.add_row(str(i), cat.display_name)
        
        self.console.print(table)
        
        while True:
            try:
                choice = Prompt.ask("Catégorie", choices=[str(i) for i in range(1, len(categories) + 1)])
                return categories[int(choice) - 1]
            except Exception:
                self.console.print("[red]Choix invalide[/red]")
    
    def _show_units(self, category_name: str):
        units = self.registry.get_units_by_category(category_name)
        
        table = Table(title=f"Unités: {category_name}")
        table.add_column("Symbole", style="green")
        table.add_column("Nom", style="blue")
        
        for unit in units:
            table.add_row(unit.symbol, unit.name)
        
        self.console.print(table)
    
    def _get_valid_unit(self, prompt_text: str) -> str:
        while True:
            unit = Prompt.ask(prompt_text)
            try:
                self.registry.get_unit(unit)
                return unit
            except KeyError:
                self.console.print("[red]Unité inconnue[/red]")
    
    def _continue_prompt(self) -> bool:
        choice = Prompt.ask("Continuer? (o/n)", choices=["o", "n"], default="o")
        return choice.lower() == "o"
    
    def _exit_gracefully(self):
        self.console.print("[blue]Au revoir[/blue]")
        sys.exit(0)
