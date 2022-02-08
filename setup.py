import setuptools
from setuptools import find_packages, setup


def get_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="asaas-sdk",
    version="0.1.0",
    url="https://github.com/marlonjsilva/asaas_sdk_python",
    author="Marlon Silva",
    author_email="marlon230496@gmail.com",
    description="The unofficial Asaas SDK in Python",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    install_requires=[
        "httpx >= 0.15.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "asaas"},
    packages=setuptools.find_packages(where="asaas"),
    python_requires=">=3.7",
)
