from interfaces.cli import MissionControl

def main():
    """Point d'entrée mission critique"""
    mission = MissionControl()
    mission.launch()

if __name__ == "__main__":
    main()