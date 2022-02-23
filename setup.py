from setuptools import setup, find_packages

setup(
    name='pybank',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='none',
    description='An example python package with functions simulating depositing and withdrawing cash from a bank account',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/Addalin-CP3445/Python_Package.git',
    author='Addalin',
    author_email='60094638@cna-qatar.edu.qa'
)