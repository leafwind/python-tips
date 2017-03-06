"""docstring"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse

def parse_args():
    """ parse input args."""
    parser = argparse.ArgumentParser(description='init_server')
    parser.add_argument('-i', '--ini', type=str, required=True, help='ini filename')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false')
    parser.set_defaults(dry_run=True)
    return parser.parse_args()


def main(args):
    """ main """
    print(args.dry_run)


if __name__ == '__main__':
    main(parse_args())
