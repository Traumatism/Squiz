from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='squiz',
    version='1.0.0',
    description='A random OSINT project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/traumatism/Squiz',
    author='toastakerman',
    author_email='cpastoast@protonmail.co',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='sample, setuptools, development',  # Optional
    package_dir={'': '.'},
    packages=find_packages(where='.'),
    python_requires='>=3.8, <4',
    project_urls={
        'Source': 'https://github.com/traumatism/Squiz',
    },
)
