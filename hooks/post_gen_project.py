#!/usr/bin/env python
import os
from datetime import datetime

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def replace_contents(filename, what, replacement):
    filename = os.path.join(PROJECT_DIRECTORY, filename)
    print(filename)

    with open(filename) as fh:
        target_file = fh.read()

    with open(filename, 'w') as fh:
        fh.write(target_file.replace(what, replacement))


if __name__ == "__main__":
    print("Created project.")

    if '{{ cookiecutter.date_created }}' == 'now':
        now = datetime.now()

        replace_contents('{{ cookiecutter.project_slug }}.ipynb', '<DATE>', now.strftime("%Y-%m-%d"))
