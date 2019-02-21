import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (without loading it)
with open(join(dirname(__file__), 'subjectsgeneration', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S)\
        .match(v_file.read()).group(1)

dependencies = [
    'khayyam',
    'easycli', 'pyperclip'
]


setup(
    name='subject-generator',
    version=package_version,
    author='Shiva Nouri',
    author_email='shiva@carrene.com',
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'subjectsgeneration = subjectsgeneration.cli:Main'
        ]
    },
    packages=find_packages(),
)
