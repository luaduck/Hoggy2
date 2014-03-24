import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.install import install

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'description': 'Hoggy2 is the next evolution in IRC bots with web connectors for Hoggit.  Or something like that.',
    'author': 'Jeremy Smitherman',
    'url': 'http://hoggit.us',
    'download_url': '',
    'author_email': 'jeremysmitherman@gmail.com',
    'version': '0.1',
    'packages': ['Hoggy2', 'tests','Hoggy2.utils', 'Hoggy2.models'],
    'name': 'Hoggy2',
    'license':"GPL3",
    'long_description': read('README.md'),
    'test_suite':'tests',
    'install_requires':[
        'praw',
        'flask',
        'sqlalchemy',
        'twisted',
        'pytest',
        'mock'
    ],
    'entry_points': {
        'console_scripts':[
            'Hoggy2_irc = Hoggy2.app_irc:main',
            'Hoggy2_web = Hoggy2.app_web:main'
        ]
    }

}
setup(**config)