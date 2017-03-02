#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='init_server')
    parser.add_argument('-i', '--ini', type=str, required=True, help='ini filename')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false')
    parser.set_defaults(dry_run=True)
    args = parser.parse_args()
    return args


def main(args):
    pass


if __name__ == '__main__':
    args = parse_args()
    main(args)
