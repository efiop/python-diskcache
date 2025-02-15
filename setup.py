from io import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

import diskcache


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        errno = tox.cmdline(self.test_args)
        exit(errno)


with open('README.rst', encoding='utf-8') as reader:
    readme = reader.read()

setup(
    name=diskcache.__title__,
    version=diskcache.__version__,
    description='Disk Cache -- Disk and file backed persistent cache.',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='http://www.grantjenks.com/docs/diskcache/',
    project_urls={
        'Documentation': 'http://www.grantjenks.com/docs/diskcache/',
        'Funding': 'https://gum.co/diskcache',
        'Source': 'https://github.com/grantjenks/python-diskcache',
        'Tracker': 'https://github.com/grantjenks/python-diskcache/issues',
    },
    license='Apache 2.0',
    packages=['diskcache'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    python_requires='>=3',
    install_requires=[],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)
