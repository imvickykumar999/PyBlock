from setuptools import setup, find_packages
import os
import re

requirements = [r.strip() for r in open('requirements.txt').readlines() if not r.startswith('--')]
requirements = [r if ('git+' not in r) else re.sub(r".*egg=(.*)", r"\1", r).strip() for r in requirements]

setup(
    name='PyBlock',
    install_requires=['NBT@git+git://github.com/twoolie/NBT@f9e892'],
    version=open('VERSION.txt').read().strip(),
    author='Alexander Dietz',
    author_email='alexander.dietz17@gmail.com',
    packages=find_packages(where='.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={}, 
    scripts=['bin/mccoord', 'bin/mcblock'],
    license=open('LICENSE.txt').read().strip(),
    description='Tool to analyze block in minecraft maps.',
    long_description="Tool to analyze block in minecraft maps.",
    include_package_data=True,
    install_requires=['NBT@git+git://github.com/twoolie/NBT@f9e892'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
