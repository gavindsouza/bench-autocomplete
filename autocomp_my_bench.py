from __future__ import annotations
import jinja2
import click
import os


groups = []
commands = []
commands_dict = {}


def escape(word: str):
    if type(word) == str:
        return word.replace("'", '"')


def clean(word: str):
    return word.lower().replace(" ", "-")


def generate_file(commands: dict):
    template_name = 'zsh.template.jinja'
    file = open(template_name, 'r').read()

    template = jinja2.Template(file)
    content = template.render(commands=commands, escape=escape, clean=clean)

    return content


def write_file(content: str, file_name='_bench'):
    with open(file_name, 'w') as f:
        f.write(content)
    print("Autocomplete script saved under {}".format(os.path.abspath(file_name)))


def generate_dict(bench_command: click.core):
    """This function is specific to bench's CLI architecture. Creates a dict from a click group object"""
    for command, function in bench_command.commands.items():
        if type(function) == click.core.Command:
            commands.append(function)

    commands_dict['bench'] = commands

    for command, function in bench_command.commands.items():
        if type(function) == click.core.Group:
            commands_dict[command] = []

            for _command, _function in function.commands.items():
                commands_dict[command].append(_function)

    return commands_dict


if __name__ == '__main__':
    from bench.commands import bench_command

    commands_dict = generate_dict(bench_command)
    file_data = generate_file(commands_dict)
    write_file(file_data)
