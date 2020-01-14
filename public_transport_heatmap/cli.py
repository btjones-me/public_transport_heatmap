"""Console script for public_transport_heatmap."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for public_transport_heatmap."""
    click.echo("Replace this message by putting your code into "
               "public_transport_heatmap.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
