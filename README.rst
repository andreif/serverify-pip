Serverify-pip
=============

A tiny utility which replaces VCS dependencies in requirements files by
local directories where it stores VCS checkout exports.

Installing

.. code:: sh

    $ pip install serverify-pip

Help

.. code:: sh

    $ serverify-pip -h
    usage: serverify-pip [-h] -d SRC_DIR [--debug]
                         requirements.txt [requirements.txt ...]

    Serverify Requirements - export VCS dependencies locally

    positional arguments:
      requirements.txt      Path to requirements file

    optional arguments:
      -h, --help            show this help message and exit
      -d SRC_DIR, --download-to SRC_DIR
                            Directory for exporting source files
      --debug               Sets logging level to DEBUG

Example

.. code:: sh

    $ cat ./requirements.txt
    -e git+https://github.com/django/django.git@master#egg=Django
    psycopg2==2.6.2

    $ cat ./requirements_server.txt
    -r requirements.txt
    gunicorn==19.6.0

    $ cat ./requirements_test.txt
    flake8==3.3.0

    $ serverify-pip \
        --download-to=./__server__/ \
        ./requirements_server.txt \
        ./requirements_test.txt \
        > ./__server__/requirements.txt

    $ ls -l ./__server__
    total 2
    drwxr-xr-x  27 andrei  staff   918 Feb 13 13:37 django
    -rw-r--r--   1 andrei  staff    66 Feb 13 13:37 requirements.txt

    $ cat ./__server__/requirements.txt
    __server__/django/
    psycopg2==2.6.2
    gunicorn==19.6.0
    flake8==3.3.0

    # Now copy __server__ directory to your server/image and then run
    $ pip install -r ./__server__/requirements.txt
