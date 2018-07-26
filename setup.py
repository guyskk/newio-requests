import os.path
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'src/newio_requests', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=__doc__,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'httptools',
        'yarl',
        'newio>=0.6.1',
        'requests',
        'namedlist',
    ],
    extras_require={
        'dev': [
            'pre-commit==1.10.2',
            'tox==2.9.1',
            'flake8==3.5.0',
            'pytest==3.3.2',
            'pytest-cov==2.5.1',
            'codecov==2.0.13',
            'pytest-httpbin==0.3.0',
            'invoke==0.22.0',
            'twine==1.9.1',
            'wheel==0.30.0',
            'bumpversion==0.5.3',
        ],
    },
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
