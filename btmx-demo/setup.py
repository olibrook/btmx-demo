from setuptools import setup, find_packages

setup(
    name="btmx-demo",
    version="0.0.1",
    packages=find_packages(exclude=['*tests']),
    install_requires=[
        "requests==2.10.0",
        "betamax==0.7.0",
        "pytest==2.8.5",
    ],
)
