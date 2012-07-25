#!/usr/bin/env python

import os, sys

USAGE = """ser.py [search root] [thing to find] [mode (file | folder | ext | any)] [verbose (true | false) --loose
examples:
ser.py C:\\ foo.txt
ser.py C:\\ foobar folder
ser.py C:\\ bar ext true"""

class Parser:
    LOOSE_FLAGS = ['--loose', '-l', '--l']
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
                if 'linux' in sys.platform:
                    self.args[0] = os.path.sep
                elif 'win' in sys.platform:
                    self.args[0] = os.path.join('C:', os.path.sep)
                print(self._INVALID_ROOT.format(self.args[0]))
            if len(self.args) > 2:
                if not self.args[2] == 'file' and not self.args[2] == 'folder' and not self.args[2] == 'ext':
                    self.args[2] == 'any'
                if len(self.args) >= 4:
                    if self.args[3] == 'true' or self.args[3] == 't':
                        self.args[3] = True
                    elif self.args[3] == 'false' or self.args[3] == 'f':
                        self.args[3] = False
                    else:
                        self.args[3] = False
                    if len(self.args) == 5:
                        if self.args[4] in self.LOOSE_FLAGS:
                            self.args[4] = self.LOOSE_FLAGS[0]
                else:
                    self.args.append(False)
            elif len(self.args) == 2:
                self.args.append('any')
                self.args.append(False)
        else:
            print(USAGE)
            sys.exit(1) # error code 1 is too few args
    
    def parse(self):
        self.validate_args()
        args = {}
        args['root'] = self.args[0]
        args['target'] = self.args[1]
        args['mode'] = self.args[2]
        args['verbose'] = self.args[3]
        args['loose'] = True if self.args[4] == self.LOOSE_FLAGS[0] else False
        return args
