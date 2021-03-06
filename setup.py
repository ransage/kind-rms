#!/usr/bin/env python

import subprocess

try:
    with open('./venv/bin/pip'):
        subprocess.call("./venv/bin/pip install -r requirements.txt",shell=True)
except IOError:
    print '''
Unable to open ./venv/bin/pip - did you run:
  virtualenv venv
???
'''

subprocess.call("cp kindrms/db.sqlite3.example kindrms/db.sqlite3",shell=True)


print '''


This should be cleaned up to follow standard setup.py paradigms

Also, the example database was copied over the sqlite database.
  Admin user: test
  Password:   password
'''

# from setuptools import setup, find_packages
# DESCRIPTION = ("DOORS'-style Requirements Management System - KIND Is Not DOORS")

# setup(
#     name='KIND',
#     version='0.0-dev',
#     description=DESCRIPTION,
#     url='https://github.com/ransage/kind',
#     packages=['kindrms'],
#     install_requires=['setuptools'],
#     tests_require=['nose'],
#     test_suite='src'
# )
