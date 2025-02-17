# lucam/setup.py

"""Lucam package setuptools script."""

import sys
import re

from setuptools import setup

with open("lucam/lucam.py") as fh:
    code = fh.read()

version = re.search(r'__version__ = "(.*?)"', code).groups()[0]

description = re.search(r'"""(.*)\.(?:\r\n|\r|\n)', code).groups()[0]

readme = re.search(
    r'(?:\r\n|\r|\n){2}"""(.*)"""(?:\r\n|\r|\n){2}__version__',
    code,
    re.MULTILINE | re.DOTALL,
).groups()[0]

readme = "\n".join([description, "=" * len(description)] + readme.splitlines()[1:])

license = re.search(
    r'(# Copyright.*?(?:\r\n|\r|\n))(?:\r\n|\r|\n)+""',
    code,
    re.MULTILINE | re.DOTALL,
).groups()[0]

license = license.replace("# ", "").replace("#", "")

if "sdist" in sys.argv:
    with open("LICENSE", "w") as fh:
        fh.write("BSD 3-Clause License\n\n")
        fh.write(license)
    with open("README.rst", "w") as fh:
        fh.write(readme)

setup(
    name="lucam",
    version=version,
    description=description,
    long_description=readme,
    author="Chris Kuethe",
    author_email="chris.kuethe@gmail.com",
    url="https://github.com/ckuethe/lucam-ng",
    project_urls={
        "Bug Tracker": "https://github.com/ckuethe/lucam-ng/issues",
        "Source Code": "https://github.com/ckuethe/lucam-ng",
        # 'Documentation': 'https://',
    },
    packages=["lucam-ng"],
    python_requires=">=3.7",
    install_requires=["numpy>=1.15.1"],
    license="BSD",
    platforms=["Windows", "Posix"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
