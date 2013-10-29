"""
 py2app/py2exe build script for Freedom Flies.

 Will automatically ensure that all build prerequisites are available
 via ez_setup

 Usage (Mac OS X):
     python setup.py py2app

 Usage (Windows):
     python setup.py py2exe
"""

#import ez_setup
#ez_setup.use_setuptools()

import sys
from setuptools import setup

NAME='Ballistic Missile Simulator'
VERSION='1.0'
mainscript = 'gui.py'
data_files = ['icon/tintin.icns','presets.txt']

if sys.platform == 'darwin':
    plist = dict(
        CFBundleIconFile='tintin.icns',
        CFBundleName=NAME,
        CFBundleShortVersionString=VERSION,
        CFBundleGetInfoString=' '.join([NAME, VERSION]),
        CFBundleExecutable=NAME,
        CFBundleIdentifier='com.levinger.josh',
    )
    
    extra_options = dict(
        setup_requires=['py2app'],
        app=[mainscript],
        options=dict(py2app=dict(argv_emulation=True,
                                 iconfile='icon/tintin.icns',
                                 plist=plist)),
        data_files=data_files
    )
    
    
elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[mainscript],
        data_files=data_files
    )
    
    
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        scripts=[mainscript],
        data_files=data_files
    )

setup(
    name=NAME,
    **extra_options
)
