import click
from pathlib import Path
from dispatcher import scan_folder

@click.command()
@click.option("--root", type=click.Path(exists=True, file_okay=False), required=True)
def main(root):
    files = list(scan_folder(Path(root)))
    click.echo(f"Found {len(files)} files")

if __name__ == "__main__":
    main()
