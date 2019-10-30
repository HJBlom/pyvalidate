'''Command line interface for pyvalidator
'''
import click
from pyvalidate.validation_engine import run_plugins


@click.command()
@click.argument('module_path', type=str)
@click.argument('module_name', type=str)
@click.option(
    '--exclude',
    type=str,
    default=[],
    multiple=True,
    help='List of relative paths to working directory to exclude from testing.')
@click.version_option()
def cli(module_path, module_name, exclude):
    exit_code = run_plugins(module_path, module_name, exclude_paths=exclude)
    print(exit_code)

def main():
    cli()

if __name__ == '__main__':
    main()
