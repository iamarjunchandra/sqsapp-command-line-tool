"""SQSAPP entry point script."""

from . import appsetup


def main():
    appsetup.app(prog_name='sqsapp')

if __name__ == "__main__":
    main()