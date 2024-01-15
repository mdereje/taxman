from rich.console import Console
class Logger:
    def __init__(self, logger_name, log_file=None):
        self.console = Console()
        self.logger_name = logger_name
        if log_file is not None:
            self.log_file = log_file
            self.console.print(f"[bold green]Logging to {log_file}[/bold green]",justify="center")
            self.log = open(log_file, 'a')
        else:
            self.log = None
        
    def error(self, message):
        self.console.print(f"[red]ERROR[/red]: {self.logger_name}: {message}",justify="left")
        if self.log is not None:
            self.log.write(f"[ERROR] {message}\n")
        
    def warn(self, message):
        self.console.print(f"[yellow]WARN[/yellow]: {self.logger_name}: {message}",justify="left")
        if self.log is not None:
            self.log.write(f"[WARN] {message}\n")
        
    def info(self, message):
        self.console.print(f"[green]INFO[/green]: {self.logger_name}: {message}",justify="left")
        if self.log is not None:
            self.log.write(f"[INFO] {message}\n")