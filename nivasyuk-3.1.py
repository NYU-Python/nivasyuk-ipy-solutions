
"""
Write a "file list" program that reads a directory (or optionally, a directory tree) and then presents the "top n" files sorted by one of three criteria:  filename, file size or last modification time.
a.     From the command line (using argparse or sys.argv), take user input for directory location, sort criteria ('size', 'mtime' or 'name'), # of results and sort direction ('ascending' or 'descending').
b.    Make sure to test (or make sure argparse will test) to see that the sort criteria is one of the three options and that the sort direction is one of the two directions.  Also make sure that all required options are specified.  You can make some options optional with a default to be used if not specified.
c.     Use try/except to ensure that the directory path is correct (i.e., capture the error if the directory can't be read).
d.    Use os.listdir() to read a directory, or os.walk() to traverse a directory tree.  For each file, find out its size and last modification time.  Also, use os.path.basename() to grab the bare filename (without the path info), and store that within the dict.
e.    Add each file into a dictionary of dictionaries (or you may use a dictionary of lists) so that each file in the tree has three values associated with it:  bare filename, file size and last modification time.
"""

import argparse
import os
import time

#---------------------------------------------------------------------------#

def summarize(file_data, criterion, top_n, sort_direction):
    """
    produces results summary - given the file data, criterion and sort direction
    :param file_data: dict mapping file paths to file info
    :param criterion: one of size, mtime, or name
    :param top_n: number of results to display
    :param sort_direction: ascending or descending
    """

    if sort_direction == 'descending':
        sorted_data = sorted(file_data,
                             key=lambda path: file_data[path][criterion],
                             reverse=True)
    else:
        sorted_data = sorted(file_data,
                             key=lambda path: file_data[path][criterion])

    for path in sorted_data[:top_n]:
        print "{0}:\t{1} bytes. Last modified on: {2}".format(
            file_data[path]['name'],
            file_data[path]['size'],
            time.ctime(file_data[path]['mtime'])
        )

#---------------------------------------------------------------------------#

def get_file_data(file_paths):
    """
    given the file-paths, returns a dict of paths' data (size, mod time and name)
    :param file_paths: list of file paths
    :return: dict mapping file paths to file info
    """

    file_data = {}

    for path in file_paths:
        statinfo = os.stat(path)
        size = statinfo.st_size
        mtime = statinfo.st_mtime
        name = os.path.basename(path)

        file_data[path] = {'size': size,
                            'mtime': mtime,
                            'name': name}

    return file_data

#---------------------------------------------------------------------------#

def get_file_paths(directory):
    """
    given a directory, walks through it, returns all file paths of directory.
    :param directory: directory path
    :return: list of all file paths (on all levels)
    """

    list_paths = []

    for path, dirs, files in os.walk(directory):
        file_paths = [path + '/' + file for file in files]
        list_paths += file_paths

    return list_paths

#---------------------------------------------------------------------------#

def main(directory, criterion, top_n, sort_direction):
    """
    main function implementing the assignment
    :param directory: full directory path to traverse
    :param criterion: one of size, mtime, or name
    :param top_n: number of results to display
    :param sort_direction: ascending or descending
    """

    if not os.path.exists(directory):
        raise ValueError("Invalid path: {0}".format(directory))

    file_paths = get_file_paths(directory)
    file_data = get_file_data(file_paths)
    summarize(file_data, criterion, top_n, sort_direction)

#---------------------------------------------------------------------------#

### define and verify args with argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='homework.3.1')
    parser.add_argument('directory', type=str, help= '- path; directory location')
    parser.add_argument('criterion', type=str, choices=('size', 'mtime', 'name'),
                        help= '- sort criterion: size, mtime, or name')
    parser.add_argument('top_n', type=int, help='- number of results to return')
    parser.add_argument('--sort_direction', type=str, choices=('ascending', 'descending'),
                        help='- ascending or descending', default='descending')

    args = parser.parse_args()
    print args

    try:
        main(args.directory, args.criterion, args.top_n, args.sort_direction)

    except ValueError as e:
        print "Error: ", e
        parser.print_usage()
