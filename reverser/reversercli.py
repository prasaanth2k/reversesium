import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from relib.arguments import Arguments
from relib.buildhelper import Environment
from relib.managers import Managers
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
class Reverser:
    def __init__(self, args):
        self.args = args
        if args.hasOptions(['--help']) or args.hasOptions(['-h']):
            self.helpmessage()

    def helpmessage(self):
        console = Console()
        table = Table(show_header=False, box=None)
        table.add_column("Option", width=30)
        table.add_column("Description")
        table.add_row(" ", " ")
        table.add_row(" ", "Reversesium", style="purple bold")
        table.add_row(" ", " ")
        table.add_row("-h, --help", "Show this help message and exit.")
        table.add_row(
            "build --tag <tagname> --path <path to Dockerfile>",
            (
                "Builds a Docker image. The optional '--tag' argument specifies the tag name "
                "(default is 'reversesium:v1'). The optional '--path' argument specifies the path "
                "to the Dockerfile (default is the current directory)."
            ),
        )
        table.add_row(
            "startsession --session=<session_name> --host=<hostname> --network=<true/false> --username=<username>",
            (
                "Starts a new session inside a container. The '--session' option specifies the session name, "
                "'--host' specifies the container hostname, '--network' allows network access if set to true, "
                "and '--username' specifies the username inside the container."
            ),
        )
        table.add_row(
            "stopsession --session=<session_name>",
            (
                "Stops the specified session. Note: The session name must match the name used "
                "when starting the session."
            ),
        )
        table.add_row(
            "shell --session=<session_name> --username=<username>",
            (
                "Launches a shell inside the specified session. Use '--session' to specify the session name "
                "and '--username' to specify the username."
            ),
        )
        table.add_row(
            "trace --cmd=<command>",
            (
                "Traces the system calls made by the specified command. For example, use '--cmd=/usr/bin/ls' "
                "to trace the system calls of the 'ls' command."
            ),
        )
        panel = Panel(table, title="[bold white]Options[/bold white]", title_align="left", border_style="bold white")
        console.print(panel)


def main():
    args = Arguments(sys.argv[1:])
    reverser = Reverser(args)
    environment = Managers(args)

if __name__ == "__main__":
    main()