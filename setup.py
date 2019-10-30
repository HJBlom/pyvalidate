from setuptools import setup, find_packages


setup(
    name='pyvalidate',
    version=open('version').read().strip(),
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'pyvalidate=pyvalidate.cli:main'
        ]
    }
)
