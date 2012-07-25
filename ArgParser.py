#!/usr/bin/env python

import os, sys

USAGE = """ser.py [search root] [thing to find] [mode (--file | --folder | --ext)] [--verbose] [--loose]
examples:
ser.py C:\\ foo.txt
ser.py C:\\ foobar folder
ser.py C:\\ bar ext true"""

class Parser:
    LOOSE_FLAGS = ['--loose', '-l', '--l']
    MODE_FLAGS = ['--file', '--folder', '--ext']
    VERBOSE_FLAGS = ['--verbose', '-v']
    MODES = ['file', 'folder', 'ext']
    _INVALID_ROOT = 'Invalid search root, defaulting to {!s}'
    
    def __init__(self, args):
        self.args = args
    
    def __str__(args):
        s = ''
        for key in sorted(args):
            s += '{!s}={!s}'.format(key, args[key])
        print(s)
    
    def validate_args(self):
        if len(self.args) > 1:
            if not os.path.exists(self.args[0]) or not os.path.isdir(self.args[0]):
                print(USAGE)
                sys.exit(2) # error code 2 for bad root directory
        else:
            print(USAGE)
            sys.exit(1) # error code 1 is too few args
        
    def parse(self):
        args = {}
        args['root'] = self.args[0]
        args['target'] = self.args[1]
        args['mode'] = 'any'
        for MODE_FLAG in self.MODE_FLAGS:
            if MODE_FLAG in self.args:
                args['mode'] = self.MODES[self.MODE_FLAGS.index(MODE_FLAG)]
        args['verbose'] = False
        for VERBOSE_FLAG in self.VERBOSE_FLAGS:
            if VERBOSE_FLAG in self.args:
                args['verbose'] = True
        args['loose'] = False
        for LOOSE_FLAG in self.LOOSE_FLAGS:
            if LOOSE_FLAG in self.args and not args['mode'] == 'ext':
                args['loose'] = True
        return args
