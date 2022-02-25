import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='squiz',
    version='1.0.0',
    description='A random OSINT project',
    url='https://github.com/traumatism/Squiz',
    author='toastakerman',
    author_email='cpastoast@protonmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8, <4',
)
