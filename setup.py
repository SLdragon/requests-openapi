import io
import os
import re

from setuptools import find_packages, setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="oai-requestor",
    version="0.0.1",
    url="https://github.com/wy-z/oai-requestor",
    license="MIT",
    author="weiyang",
    author_email="weiyang.ones@gmail.com",
    description="OAIRequestor is a python client for OpenAPI 3.0",
    long_description=read("README.md"),
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests", "pyyaml"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
