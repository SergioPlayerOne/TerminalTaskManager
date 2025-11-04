import argparse

# create the top level parser
parser = argparse.ArgumentParser(
    prog='Terminal task manager',
    description='A simple and lightweight task manager for the terminal')
command_parser = parser.add_subparsers()

# the 'add' parser
add_parser = command_parser.add_parser(
    name='add')

# Argument tests
parser.parse_args(["-h"])
