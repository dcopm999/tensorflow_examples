"""Console script for tensorflow_examples."""
import sys
import click

from tensorflow_examples import tutor1
from tensorflow_examples.settings import logging

logger = logging.getLogger(__name__)


@click.command()
@click.option('--example', default='example01', help='execute example')
def main(example, args=None):
    """Console script for tensorflow_examples."""
    click.echo(f'execute example: {example}')
    result = getattr(tutor1, example)
    click.echo(f'Result {example}: {result()}')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
