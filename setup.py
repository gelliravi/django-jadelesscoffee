#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-jadelesscoffee',
    version='0.1.2',
    description='Django middleware class that executes the Node.js JadeLessCoffee compiler on a `src` folder in the TEMPLATE_DIRS directory.',
    author='Oliver Wilkerson, Matthew Wells, Jeff Andrews, Nuu Logic LLC',
    author_email='oliver.wilkerson@nuulogic.com',
    url='http://github.com/nuulogic/django-jadelesscoffee/',
    
    # what to install
    packages=['jadelesscoffee', 'jadelesscoffee.django'],
    
    # searches and classifications
    keywords='django,jade,less,lesscss,coffeescript,nodejs,node,npm,coffee,jlc,middleware',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: TBD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    
    # dependencies
    install_requires=[
        'django >= 1.3',
    ],
)
