import os
import sys
from setuptools import setup, find_packages

description = "A command-line interface to the GitHub Issues API v2."
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
    long_description = description

# needed for importing github.version
sys.path.insert(0, os.path.join(cur_dir, 'src'))
from github.version import get_version

pkg_requires = ['setuptools', ]
# simplejson is included in the standard library since Python 2.6 as json, but
# unfortunately it is too old.  We can use stdlib json with Python 2.7.
if sys.version_info[0] < 3 and sys.version_info[1] < 7:
    pkg_requires.append('simplejson >= 2.0')

setup(
    name = "github-cli",
    version = get_version('short'),
    url = 'http://packages.python.org/github-cli',
    license = 'BSD',
    description = description,
    long_description = long_description,
    author = 'Sander Smits',
    author_email = 'jhmsmits@gmail.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = pkg_requires,
    entry_points="""
    [console_scripts]
    ghi = github.issues:main
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
    ],
    test_suite = 'nose.collector',
)
