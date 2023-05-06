import click
from provisioning.main import start

@click.group(invoke_without_command=True, no_args_is_help=True)
@click.version_option()
def entrypoint():
    pass

@entrypoint.command()
def detect_model():
    print("Model detecting ...")

@entrypoint.command()
@click.argument("model_name", type=click.STRING)
def provision(model_name: str):
    print(f"Provisioning '{model_name}' device...")
    start(model_name)