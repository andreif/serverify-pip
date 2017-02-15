#!/usr/bin/env python
from setuptools import setup
import serverify

repo = 'https://github.com/andreif/serverify-pip'
version = serverify.__version__

setup(
    name='serverify-pip',
    version=version,
    author='Andrei Fokau',
    author_email='andrei@5monkeys.se',
    description=serverify.parser.description,
    url=repo,
    download_url='%s/tarball/%s' % (repo, version),
    keywords=['pip', 'requirements', 'server', 'vcs'],
    license='BSD',
    zip_safe=False,
    py_modules=[
        'serverify',
    ],
    install_requires=[
        'pip',
    ],
    entry_points={
        'console_scripts': [
            'serverify-pip = serverify:main',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
