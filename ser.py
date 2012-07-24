#!/usr/bin/env python

from ArgParser import Parser
from sys import argv

INFO_STOP = 'Press ctrl+c to stop the search at any time'
SEARCH_COMPLETE = 'Search complete! Showing {0:d} results:'

def publish_results(results):
	print(SEARCH_COMPLETE.format(len(results)))
	for result in results:
		print(result)

def main(args):
	if args['mode'] == 'ext':
		from Search import ExtSearch as ext_search
		print(INFO_STOP)
		search = ext_search(args['root'], args['target'], args['verbose'])
	else:
		from Search import Search as reg_search
		search = reg_search(args['root'], args['target'], args['mode'], args['verbose'])
	search.search()
	publish_results(search.results)

if __name__ == '__main__':
	parser = Parser(argv[1:])
	args = parser.parse()
	print(args)
	main(args)