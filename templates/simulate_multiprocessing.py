"""Benchmark time performance on multi-processes environments.
   Especially for throughput in shared resources like LMDB.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from multiprocessing import Pool
import argparse
import math
import itertools
import time

def parse_args():
    """ parse input args."""
    parser = argparse.ArgumentParser(description='init_server')
    parser.add_argument('-n', type=int, required=True, help='number of processes')
    parser.add_argument('-m', '--mode', type=int, required=True, help='0: hit mode, 1: miss mode')
    return parser.parse_args()


def _now_ms():
    return time.time() * 1000


def func(params):
    """ any function that can be replaced."""
    # load / prepare / transform input data
    _, max_iterations = params

    start = _now_ms()
    for i in itertools.count():
        time.sleep(0.0001)  # 0.1ms
        if i >= max_iterations:
            duration = _now_ms() - start
            return duration


def main(n_process, iterations, mode):
    """ main """
    pool = Pool(processes=n_process)
    duration_list = pool.map(func, [(mode, iterations)] * n_process)
    total_duration = sum(duration_list)
    avg_ms_per_query = (total_duration / n_process) / iterations
    print("use {:3d} processes, total {:5d} iterations, avg. {:5.3f} ms."
          .format(n_process, iterations, avg_ms_per_query))


if __name__ == '__main__':
    args = parse_args()  # pylint: disable=invalid-name
    SCALE = 4  # the number of your model records
    for i in range(2, SCALE + 1):
        n_iterations = int(math.pow(10, i))
        main(args.n, n_iterations, args.mode)

