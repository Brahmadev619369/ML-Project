from setuptools import find_packages , setup
from typing import List


def get_requirements(file):
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="Brahma",
    packages=find_packages(),
    install_requires =get_requirements("requirement.txt")
)