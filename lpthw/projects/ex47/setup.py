try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'ex47',
    'version': '1.0',
    'description': "My Project",

    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',

    'author': 'My Name',
    'author_email': 'My email',

    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],

}

setup(**config)
