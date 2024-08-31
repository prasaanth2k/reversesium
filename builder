#!/usr/bin/python3
from arguments import Arguments
from buildhelper import Environment
args = Arguments()
environ = Environment()
if __name__ == "__main__":
    if args.hasCommands(['make']):
        environ.build()
    if args.hasCommands(['shell']) and args.hasOptions(['--host']):
        environ.get_shell(hostname=args.getOptionValue('--host'))