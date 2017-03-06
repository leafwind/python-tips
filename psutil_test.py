"""print the memory info of this machine"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import os
import argparse
import psutil

VM_LOG_FILE = 'vm.log'  # virtual mem
SM_LOG_FILE = 'sm.log'  # swap mem
MODE_STDOUT = 0
MODE_LOG_FILE = 1

def print_log(interval):
    '''print log to stdout.'''
    while True:
        print(psutil.virtual_memory())
        print(psutil.swap_memory())
        time.sleep(interval)


def write_log(interval):
    '''write log into files.'''
    while True:
        if not os.path.exists(VM_LOG_FILE):
            f = open(VM_LOG_FILE, 'w')
            f.write('total,available,percent,used,free,active,inactive,wired' + '\n')
            f.close()

        if not os.path.exists(SM_LOG_FILE):
            f = open(SM_LOG_FILE, 'w')
            f.write('total,used,free,percent,sin,sout' + '\n')
            f.close()

        f = open(VM_LOG_FILE, 'a')
        vm = psutil.virtual_memory()
        vm_csv_str = ','.join([str(s) for s in vm])
        f.write(vm_csv_str + '\n')
        f.close()

        f = open(SM_LOG_FILE, 'a')
        sm = psutil.swap_memory()
        sm_csv_str = ','.join([str(s) for s in sm])
        f.write(sm_csv_str + '\n')
        f.close()

        time.sleep(interval)


def parse_args():
    """ parse input args."""
    parser = argparse.ArgumentParser(description='init_server')
    parser.add_argument('-i', '--interval', type=int, required=True, help='interval sec.')
    parser.add_argument('-m', '--mode', type=int, required=True, help='0: stdout, 1: write file')
    return parser.parse_args()


def main(args):
    """ main """
    if args.mode == MODE_STDOUT:
        print_log(args.interval)
    elif args.mode == MODE_LOG_FILE:
        write_log(args.interval)
    else:
        return 0

if __name__ == '__main__':
    main(parse_args())
