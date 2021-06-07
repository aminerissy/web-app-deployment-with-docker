# distutils doesn't support install_requires param
# from distutils.core import setup
import setuptools

setuptools.setup(
    # Application name:
    name="application",
    # Version number (initial):
    version="",
    # Application author details:
    author="Amine",
    author_email="amine@gmail.com",
    # Packages
    packages=setuptools.find_packages(exclude=['yourapp/tests']),
    package_data={},
    # Include additional files into the package
    include_package_data=True,
    # license="LICENSE.txt",
    description="Simple web application with flask",
    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ]
)
