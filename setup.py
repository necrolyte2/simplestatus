from setuptools import setup, find_packages
import setuptools

setup(
    name = 'simplestatus',
    version = '0.0.1',
    py_modules = ['status'],
    setup_requires = [
        'nose',
        'python-coveralls',
    ],
    tests_require = [
        'nose',
        'mock',
    ],
    entry_points = {
        'console_scripts': [
            'simplestatus = simplestatus:main'
        ]
    },
    author = 'Tyghe Vallard',
    author_email = 'vallardt@gmail.com',
    description = 'Quick and dirty status checks for hosts',
    license = 'GPLv2',
    keywords = 'status, host, check',
    url = 'https://github.com/necrolyte2/simplestatus'
)
