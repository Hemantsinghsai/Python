from search import search_web
from colorama import Fore, Style
from termcolor import cprint
from pyfiglet import figlet_format
from rich.console import Console
from rich.progress import track
import time

# ASCII Banner
cprint(figlet_format("Mr. Researcher"), "cyan")

# Simulated Loading
cprint("\n[1] Fetching search results...", "yellow")
for _ in track(range(10), description="Searching..."):
    time.sleep(0.1)

# Display Results
results = search_web("AI tools for research")
console = Console()

console.print("\n[bold green]🔍 Search Results:[/bold green]\n")
for r in results:
    console.print(f"[bold magenta]{r['title']}[/bold magenta]")
    console.print(f"[blue]{r['link']}[/blue]")
    console.print(f"[dim]{r['snippet']}[/dim]\n")