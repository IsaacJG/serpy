#!/usr/bin/env python

from ArgParser import Parser
from sys import argv

INFO_STOP = 'Press ctrl+c to stop the search at any time'
SEARCH_COMPLETE = 'Search complete! Showing {0:d} results:'
LOOSE_COMPATIBLE_MODES = ['any', 'file', 'folder']
POSITIVE_CHOICES = ['yes', 'y', 'Y']
NEGATIVE_CHOICES = ['no', 'n', 'N']

def publish_results(results):
    print(SEARCH_COMPLETE.format(len(results)))
    for result in results:
        print(result)

def main(args):
    print(INFO_STOP)
    if args['mode'] == 'ext':
        from Search import ExtSearch as ext_search
        search = ext_search(args['root'], args['target'], args['verbose'])
    else:
        if not args['loose']:
            from Search import Search as reg_search
            search = reg_search(args['root'], args['target'], args['mode'], args['verbose'])
        else:
            from Search import LooseSearch as loose_search
            search = loose_search(args['root'], args['target'], args['mode'], args['verbose'])
            
    search.search()
    publish_results(search.results)
    if args['mode'] in LOOSE_COMPATIBLE_MODES and not args['loose']:
        choice = raw_input('Would you like to search again using the loose search method? [Y/n]')
        if choice in POSITIVE_CHOICES:
            from Search import LooseSearch as loose_search
            search = loose_search(args['root'], args['target'], args['mode'], args['verbose'])
            search.search()
            publish_results(search.results)

if __name__ == '__main__':
    parser = Parser(argv[1:])
    args = parser.parse()
    print(args)
    main(args)
