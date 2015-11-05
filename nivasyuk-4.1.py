#!/usr/bin/env python

"""
Create a module mylib that includes one or both of the following classes:
    a. class Logger:  this class constructs objects that can be used to log events at varying priority levels.
    b. class Config:  this class reads and writes configuration text files that may also be hand-editable.
"""
import sys, os, time
# --------------------------------------------------------------------------- #

class Logger:

    def __init__(self, filename, priority, print_datetime, print_scriptname):

        self.filename = filename
        self.priority = priority
        self.print_datetime = print_datetime
        self.print_scriptname = print_scriptname

        self.fh = open(filename, 'w')

    def print_message(self, msg, level):

        self.fh.write(level)

        if self.print_datetime:
            self.fh.write(time.ctime() + " - ")

        if self.print_scriptname:
            self.fh.write(os.path.basename(__file__) + " - ")

        self.fh.write(msg + '\n')

    def debug(self, msg):

        if self.priority == 'DEBUG':
            self.print_message(msg, 'Debug: ')

    def info(self, msg):

        if self.priority == 'DEBUG' or self.priority == 'INFO':
            self.print_message(msg, 'Info: ')

    def warning(self, msg):

        if self.priority == 'DEBUG' or self.priority == 'INFO' \
                or self.priority == 'WARNING':
            self.print_message(msg, 'Warning: ')

    def error(self, msg):

        if self.priority == 'DEBUG' or self.priority == 'INFO' \
                or self.priority == 'WARNING' or self.priority == 'ERROR':
            self.print_message(msg, 'Error: ')

    def critical(self, msg):

        if self.priority == 'DEBUG' or self.priority == 'INFO' \
                or self.priority == 'WARNING' or self.priority == 'ERROR' \
                or self.priority == 'CRITICAL':
            self.print_message(msg, 'Critical: ')


# --------------------------------------------------------------------------- #

if __name__ == '__main__':

    filename = sys.argv[1]

    try:
        log = Logger(filename, priority='DEBUG', print_datetime=True, print_scriptname=True)

        log.debug('DEBUG msg')
        log.info('INFO msg')
        log.warning('WARNING msg')
        log.error('ERROR msg')
        log.critical('CRITICAL msg')

    except IOError as e:
        print e
