try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
import sys

if sys.version_info[:3] < (3, 0, 0):
    sys.stdout.write("Requires Python 3 to run.")
    sys.exit(1)

with open("README.md", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="pyreserve",
    version="1.0.0a1",
    description="Create a template Python package and reserve a name on PyPi with just one command",
    #long_description=readme,
    #long_description_content_type="text/markdown",
    url="https://github.com/shobrook/pyreserve",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    #classifiers=[
    #    "Environment :: Console",
    #    "Intended Audience :: Developers",
    #    "Topic :: Software Development",
    #    "Natural Language :: English",
    #    "License :: OSI Approved :: MIT License",
    #    "Programming Language :: Python"
    #],
    keywords="pypi python package reserve template project generator",
    include_package_data=True,
    packages=["pyreserve"],
    entry_points={"console_scripts": ["pyreserve = pyreserve.pyreserve:main"]},
    install_requires=[],
    requires=[],
    python_requires=">=3",
    license="MIT"
)
