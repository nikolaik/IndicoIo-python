try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name = "IndicoIo",
	version = '0.2.6',
	packages = [
            "IndicoIo",
            "IndicoIo.text",
            "IndicoIo.images",
        ],
	license = "MIT License (See LICENSE)",
	long_description = open("README").read(),
	url = "https://github.com/IndicoDataSolutions/IndicoIo-python",
	author = "Alec Radford, Slater Victoroff",
	author_email = "Alec Radford <alec@indicodatasolutions.com>, Slater Victoroff <slater@indicodatasolutions.com>",
)
