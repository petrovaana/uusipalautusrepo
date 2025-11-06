import requests
from player import Player
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich.color import Color


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.players()


    def players(self):
        response = requests.get(self.url).json()
        players = []


        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players


    def top_scorers_by_nationality(self, nationality):
        nat_fil = []
        for player in self.players:
            if player.nationality == nationality:
                nat_fil.append(player)


        return sorted(nat_fil ,key= lambda x: x.pisteet, reverse=True)


def main():
    console = Console()
    console.print(Rule("[bold magenta] NHL Statistics [/bold magenta]"))
    szn = console.input("Seazon: ")
    country = console.input("Country: ")

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")


    table = Table(title=f"[bold]Top players from {country} ({szn})[/bold]")
    table.add_column("Name", style="white", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="blue")
    table.add_column("Assists", style="blue")
    table.add_column("Points", style="green")


    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.pisteet))
    console.print(table)


if __name__ == "__main__":
    main()