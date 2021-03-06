#!/usr/bin/env python
VERSION = "1.2.0"

from setuptools import setup, find_packages
import os.path, sys
from stat import ST_MTIME

if 'py2exe' in sys.argv:
    import py2exe

import modulefinder, csc.util, csc.divisi2
for p in sys.path:
   modulefinder.AddPackagePath(__name__, p)
sys.path.append('luminoso/lib')

classifiers=[
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: C',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development',
    'Topic :: Text Processing :: Linguistic',]

INCLUDES = ["sip", "PyQt4.QtCore", "PyQt4.Qt", "PyQt4.QtGui", "PyQt4",
            'csc.util', 'csc.divisi2', 'spyderlib', 'standalone_nlp.nl', 'standalone_nlp.lang_en', 'standalone_nlp.euro', 'standalone_nlp.trie', 'jinja2', 'numpy',
            'chardet']
DATA_FILES = ['icons']

setup(
    name="Luminoso",
    version = VERSION,
    maintainer='MIT Media Lab, Software Agents group',
    maintainer_email='conceptnet@media.mit.edu',     
    url='http://launchpad.net/luminoso/',
    license = "http://www.gnu.org/copyleft/gpl.html",
    platforms = ["any"],
    description = "A Python GUI for semantic analysis using Divisi",
    classifiers = classifiers,
    ext_modules = [],
    packages=find_packages()+['icons', 'study_skel'],
    app=['luminoso/run_luminoso.py'],
    scripts=['luminoso/run_luminoso.py'],
    windows=[{'script': 'luminoso/run_luminoso.py'}],
    install_requires=['csc-utils >= 0.4.2', 'divisi2', 'ipython >= 0.9.1', 'jinja2', 'chardet'],
    package_data={'csc.nl': ['mblem/*.pickle', 'en/*.txt']},
    include_package_data=True,
    #data_files=DATA_FILES,
    options={'py2exe': {
            'skip_archive': True,
            'includes': INCLUDES,
            'excludes': ["Tkconstants","Tkinter","tcl"]
        },
        'py2app': {
            "argv_emulation": True,
            'includes': INCLUDES,
        },
    },

    entry_points={'gui_scripts': ['luminoso = luminoso.run_luminoso:main']},
)
