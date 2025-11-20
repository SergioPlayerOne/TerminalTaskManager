import argparse
from taskmanager import add_task, list_tasks

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
    'title',
    help='the title of the task to add'
)
add_parser.add_argument(
    '-d', '--description',
    help='the description of the task'
)

# The 'list' parser
list_parser = command_parser.add_parser(
    name='list',
    help='list all of the current uncompleted tasks'
)
list_parser.add_argument(
    '-ft', '--filter-title',
    help='filter in tasks that contain the word specified'
)
list_parser.add_argument(
    '-fd', '--filter-description',
    help='filter in tasks that contain the word specified'
)

# Handles the arguments parsed
args = parser.parse_args(['list'])
if args.command == "add":
    add_task(args.title, args.description)
if args.command == 'list':
    list_tasks(args.filter_title, args.filter_description)

