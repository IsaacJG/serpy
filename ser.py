#!/usr/bin/env python

######################
#     Deprecated     #
######################

__author__ = 'Isaac Grant'

import os, sys

usage = """ser.py [root folder to search] [file/folder name] [optional mode (file | folder | any)] [optional verbosity (true | false)]
by Isaac Grant"""

search_complete = False
search_results = []

def finish_search(kwargs):
    print('\n\n')
    print('Search complete! %s results:' % len(search_results))
    for folder in search_results:
        print(folder)
    return

def notify(name, folder):
    print('Found %s in %s!' % (name, folder))
    search_results.append(os.path.join(folder, name))

def search(kwargs):
    try:
        for folder, sub_folders, files in os.walk(kwargs['root'], followlinks=True):
            if kwargs['verbose']:
                for sub_folder in sub_folders: print(os.path.join(folder, sub_folder))
                for f in files: print(os.path.join(folder, f))
            if kwargs['mode'] == 'file':
                if kwargs['name'] in files:
                    notify(kwargs['name'], folder)
            elif kwargs['mode'] == 'folder':
                if kwargs['name'] in sub_folders:
                    notify(kwargs['name'], folder)
            elif kwargs['mode'] == 'any':
                if kwargs['name'] in files or kwargs['name'] in sub_folders:
                    notify(kwargs['name'], folder)
        else:
            if len(search_results) == 0:
                print('Could not find %s in %s...' % (kwargs['name'], kwargs['root']))
        finish_search(kwargs)
    except KeyboardInterrupt:
        print('Search stopped (keyboard interrupt)')
        finish_search(kwargs)

def validate_args(args):
    if len(args) > 1:
        if not os.path.exists(args[0]) or not os.path.isdir(args[0]):
            if 'linux' in sys.platform:
		args[0] = os.path.sep
            elif 'win' in sys.platform:
                args[0] = os.path.join('C:', '')
	if len(args) > 2:
            if not args[2] == 'file' and not args[2] == 'folder':
                args[2] == 'any'
            if len(args) == 4:
                if args[3] == 'true' or args[3] == 't':
                    args[3] = True
                elif args[3] == 'false' or args[3] == 'f':
                    args[3] = False
                else:
                    args[3] = False
        elif len(args) == 2:
            args.append('any')
            args.append(False)
    else:
        print(usage)
        sys.exit(0)

def get_kwargs(args):
    kwargs = {}
    kwargs['root'] = args[0]
    kwargs['name'] = args[1]
    kwargs['mode'] = args[2]
    kwargs['verbose'] = args[3]
    return kwargs

def main(args):
    validate_args(args)
    kwargs = get_kwargs(args)
    s = ''
    for key in sorted(kwargs):
        s += '%s=%s,' % (key, kwargs[key])
    print(s)
    print('Press ctrl+c to stop the search at any time')
    search(kwargs)

if __name__ == '__main__':
    main(sys.argv[1:])
