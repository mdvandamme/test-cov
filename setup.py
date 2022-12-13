# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

current_path = os.path.abspath(os.path.dirname(__file__))

requirements = ()

dev_requirements = ("pytest", "pytest-cov")


setup(
    name="test-cov",
    version="1.0.0",
    description="Test",
    long_description="Test",
    url="https://github.com/mdvandamme/test-cov",
    author="Marie-Dominique Van Damme",
    author_email="todo@ensg.eu",
    license="cecill-c",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(include=["test"]),
    install_requires=requirements,
    #test_suite="tests",
    extras_require={"dev": dev_requirements},
)
