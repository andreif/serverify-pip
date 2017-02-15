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

    $ serverify-pip \
        --download-to=./__server__/ \
        ./requirements_test.txt \
        ./requirements_extra.txt \
        > ./__server__/requirements.txt
