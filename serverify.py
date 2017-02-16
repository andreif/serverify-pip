#!/usr/bin/env python
"""
Run `serverify-pip -h` for help.
"""
import argparse
import logging
import os
import sys

import pip.index
import pip.req
from pip._vendor.packaging.requirements import Requirement

__version__ = '1.0.1'

parser = argparse.ArgumentParser(
    description='Serverify Requirements - export VCS dependencies locally')
parser.add_argument('-d', '--download-to', required=True, metavar='SRC_DIR',
                    help='Directory for exporting source files')
parser.add_argument('--debug', action='store_true',
                    help='Sets logging level to DEBUG')
parser.add_argument('reqs', nargs='+', metavar='requirements.txt',
                    help='Path to requirements file')


def serverify(download_to, *req_files):
    abs_download_to = os.path.abspath(download_to)
    if not os.path.exists(abs_download_to):
        os.makedirs(abs_download_to)

    for req_file in req_files:
        for r in pip.req.parse_requirements(req_file, session=True):
            if isinstance(r.link, pip.index.Link):
                ir = pip.req.InstallRequirement(
                    req=r, link=r.link, comes_from=None,
                    markers=True, editable=True)
                s = '{}/{}/'.format(download_to, ir.name.lower())
                ir.source_dir = '{}/{}'.format(abs_download_to, ir.name.lower())
                ir.update_editable(obtain=False)
            else:
                assert isinstance(r.req, Requirement), r.req.__class__
                s = r.req
            print(s)
            sys.stdout.flush()


def main():
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.ERROR)

    serverify(args.download_to, *args.reqs)


if __name__ == '__main__':
    main()
