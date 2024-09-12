from setuptools import setup, find_packages

setup(
    name='ppta_common',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'mongoengine',
        'tzlocal',
        'pytz'
    ],
    description='Prepa Compta common module',
    author='Peter',
    url='https://github.com/code-zys/ppta_common',
)
