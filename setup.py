# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='protobuf3-to-dict',
    description=('Ben Hodgson: A teeny Python library for creating Python dicts from '
                 'protocol buffers and the reverse. Useful as an intermediate '
                 'step before serialisation (e.g. to JSON). '
                 'Kapor: upgrade it to PB3 and PY3, rename it to protobuf3-to-dict'),
    version='0.1.5',
    author='Kapor Zhu',
    author_email='kapor.zhu@gmail.com',
    url='https://github.com/kaporzhu/protobuf-to-dict',
    license='Public Domain',
    keywords=['protobuf', 'json', 'dict'],
    install_requires=['protobuf>=2.3.0', 'six'],
    package_dir={'': 'src'},
    py_modules=['protobuf_to_dict'],
    tests_require=['nose>=1.0', 'coverage', 'nosexcover'],
    test_suite='nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
