from setuptools import setup, find_packages

setup(
    name="lib_name",
    version="0.1.0",
    description="Example of an internal Python library that can be used within a Data Team.",
    author="Andrew P",
    install_requires=[
        "slacker", 
        "python-dotenv"
    ],
    packages=find_packages()
)