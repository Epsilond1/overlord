# encoding: utf-8
import pip
from pip.req import parse_requirements
from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='overlord',
    version=__version__,
    description=u'',
    url='https://github.yandex-team.ru/Epsilond1/overlord',
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    long_description=open('README.md').read(),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=map(lambda r: str(r.req),
                         parse_requirements('requirements/overlord_server.txt', session=pip.download.PipSession())),
    tests_require=map(lambda r: str(r.req),
                         parse_requirements('requirements/overlord_agent.txt', session=pip.download.PipSession())),
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['overlord = overlord.start:cli']
    }
)