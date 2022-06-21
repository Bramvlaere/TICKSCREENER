from setuptools import setup

setup(
    name = 'FinScraper',
    version = '0.1.0',
    packages = ['FinScraper'],
    entry_points = {
        'console_scripts': [
            'FinScraper = FinScraper.__main__:main'
        ]
    })
