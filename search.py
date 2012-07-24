#!/usr/bin/env python

import os, sys

class Search:
	win_priorities = [os.path.join('C:', 'Windows', 'System32'), os.path.join('C:', 'Users')]
	nix_priorities = [os.path.join(os.path.sep, 'etc'), os.path.join(os.path.sep, 'media'),
			os.path.join(os.path.sep, 'home')]

	def __init__(self, root, file):
		"""Init an instance with the root of your search, along with the file to be searched for"""
		self.root = root
		self.file = file
		self.results = []
		self.priorities = self.win_priorities if 'win' in sys.platform else self.nix_priorities
	def __str__(self):
		return 'search object for finding %s starting at %s' % (self.file, self.root)
	def _search(self, root):
		for folder, sub_folders, files in os.walk(root, followlinks=True):
			if self.file in sub_folders or self.file in files:
				self.results.append(folder)
	def search(self):
		try:
			for priority in self.priorities:
				self._search(priority)
			self._search(self.root)
			return self.results
		except KeyboardInterrupt:
			pass
