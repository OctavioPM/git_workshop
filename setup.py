from setuptools import setup

install_requires = open("requirements.txt").read().strip().split("\n")

setup(
    name="tutorial",
    version="0.1",
    py_modules=["tutorial"],
    python_requires=">=3.8",
    install_requires=install_requires,
)
