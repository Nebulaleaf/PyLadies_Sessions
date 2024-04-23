def hello(count, name, indent=False):
    """Simple program that greets 'name' for a total of 'count' times and optionally indents."""
    for _ in range(count):
        if indent:
            print("    ", end="")
        print(f"Hello {name}!")

count = 5
name = "Tyna"
indent = True
hello(count, name, indent)

import argparse

parser = argparse.ArgumentParser(description='argparse greeting')
parser.add_argument('-n', '--name', help='a name to repeat', required=True)
parser.add_argument('-c', '--count', help='how many times', required=True, type=int)
parser.add_argument("--indent", action="store_true", help=("name will be indented by 4 spaces"))

def hello(count, name, indent=False):
    """Simple program that greets 'name' for a total of 'count' times and optionally indents."""
    for _ in range(count):
        if indent:
            print("    ", end="")
        print(f"Hello {name}!")

args = parser.parse_args()
hello(args.count, args.name, args.indent)

