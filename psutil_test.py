"""print the memory info of this machine"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import psutil

print(psutil.virtual_memory())
print(psutil.swap_memory())
