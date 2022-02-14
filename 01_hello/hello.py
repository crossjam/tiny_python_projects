#!/usr/bin/env python3

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--name', '-n', default="World")
def main(name):
    """Say Hello"""
    print(f'Hello, {name}!')

if __name__ == '__main__':
    main()