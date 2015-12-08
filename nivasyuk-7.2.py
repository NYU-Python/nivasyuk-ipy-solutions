#!/usr/bin/env python

import sys
import subprocess


def main():
    result = subprocess.check_output(['curl', sys.argv[1]])
    print result

if __name__ == '__main__':
    main()
