from setuptools import setup, find_packages

setup(
    name='ppta_common',
    version='0.1.21',
    packages=find_packages(),
    install_requires=[
        'mongoengine',
        'tzlocal',
        'pytz',
        'boto3',
        'blinker',
        'pydantic',
        'python-jose',
        'imap_tools'
    ],
    description='Prepa Compta common module',
    author='Peter',
    url='https://github.com/code-zys/ppta_common',
)
