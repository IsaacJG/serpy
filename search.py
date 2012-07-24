#!/usr/bin/env python

import os, sys

class Search:
    win_priorities = [os.path.join('C:', 'Windows', 'System32'), os.path.join('C:', 'Users')]
    nix_priorities = [os.path.join(os.path.sep, 'etc'), os.path.join(os.path.sep, 'media'),
            os.path.join(os.path.sep, 'home')]

    _NO_PRIORITIES = False

    def __init__(self, root, target, verbose=False):
        """Init an instance with the root of your search, along with the file to be searched for"""
        self.root = root
        self.target = target
        self.verbose = verbose
        self.results = []
        self.priorities = self.win_priorities if 'win' in sys.platform else self.nix_priorities
    def __str__(self):
        return 'search object for finding %s starting at %s' % (self.target, self.root)
    def _notify(self, name, folder):
        self.results.append(os.path.join(folder, name))
        if verbose:
            print('Found %s in %s!' % (name, folder))
    def _search(self, root):
        for folder, sub_folders, files in os.walk(root, followlinks=True):
            if self.target in sub_folders or self.target in files:
                self._notify(self.target, folder)
    def search(self):
        try:
            self._search(self.root)
            if not self._NO_PRIORITIES:
                for priority in self.priorities:
                    self._search(priority)
            return self.results
        except KeyboardInterrupt:
            return self.results

class LooseSearch(Search):
    _NO_PRIORITIES = True
    
    def _search(self, root):
        for folder, sub_folders, files in os.walk(root, followlinks=True):
            if self.target in sub_folders or self.target in files:
                self._notify(self.target, folder)
            for sub_folder in sub_folders:
                if self.target in sub_folder:
                    self._notify(sub_folder, folder)
            for f in files:
                if self.target in f:
                    self._notify(f, folder)

class ExtSearch(Search):
    _NO_PRIORITIES = True

    def _search(self, root):
        for folder, sub_folders, files in os.walk(root, followlinks=True):
            for f in files:
                try:
                    if f.split(os.path.extsep)[1] == self.target:
                        self._notify(f, folder)
                except IndexError:
                    pass
