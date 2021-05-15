from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="encrypter",
    version="0.0.1",
    description="Encrypt file using fernet",
    py_modules=["encrypter"],
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    # install_requires=["blessings ~= 1.7"] e.g. if blessings was required for the installation
)