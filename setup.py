from setuptools import setup, find_packages

setup(
    name='directory_synchronizer',
    version='0.1',
    description='A module for synchronizing directories',
    author='Rui Sousa',
    author_email='contact@ruisousa.me',
    packages=find_packages(),  # Finds all packages in the directory structure
    entry_points={
        'console_scripts': [
            'sync-folders=app.main:main',  # This creates a command-line tool named 'sync-folders'
        ],
    },
)
