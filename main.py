import argparse

# create the top level parser
parser = argparse.ArgumentParser(
    prog='Terminal task manager',
    description='A simple and lightweight task manager for the terminal'
)
command_parser = parser.add_subparsers(
    title='commands',
    description='specify which action to take on the tasks',
    dest="command"
)

# the 'add' parser
add_parser = command_parser.add_parser(
    name='add',
    help="add a new task with title with the specified optional parameters"
)
add_parser.add_argument(
    '-t', '--title',
    help='the title of the task to add'
)
add_parser.add_argument(
    '-d', '--description',
    help='the description of the task'
)

# Handles the arguments parsed
args = parser.parse_args()
if args.command == "add":
    newTask = {
        'Title': None,
        'Description': None
    }
    if args.title:
        newTask["Title"] = args.title
    if args.description:
        newTask["Description"] = args.description
    print("The task " + str(newTask) + " was created successfully")
