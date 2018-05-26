from argparse import ArgumentParser

from . import commands


def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    commands.ios_icons.register(subparsers)
    args = parser.parse_args()

    try:
        func = args.func
    except AttributeError:
        parser.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()
