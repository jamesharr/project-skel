#!/usr/bin/env python3

import argparse


def main():
    args = parse_args()
    return


def parse_args():
    parser = argparse.ArgumentParser(
        description="What do here"
    )
    parser.add_argument(
        '-f', '--foo',
        dest='foo', type=int, default=123,
        help='foo help'
    )
    args = parser.parse_args()
    return parser.parse_args()


if __name__ == "__main__":
    main()
