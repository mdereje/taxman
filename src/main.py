import requests
from rich.console import Console

req = requests.request('GET', 'https://httpbin.org/get')

console = Console()
console.print(f"[u][bold cyan]{req.content}[/bold cyan][/u]",justify="center")