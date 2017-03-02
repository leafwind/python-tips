"""docstring"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool, TimeoutError
import argparse

def parse_args():
    """ parse input args."""
    parser = argparse.ArgumentParser(description='init_server')
    parser.add_argument('-n', type=int, required=True, help='number of processes')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false')
    parser.set_defaults(dry_run=True)
    return parser.parse_args()


def f(n):
    """ any function that can be replaced."""
    print n
    return n


if __name__ == '__main__':
    args = parse_args()

    pool = Pool(processes=args.n)

    try:
        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(f, (i,)) for i in range(args.n)]
        # print [res.get(timeout=1) for res in multiple_results]
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"


