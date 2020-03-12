from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TimedTask",
    version="0.0.1",
    author="Peter Somers",
    author_email="st164174@stud.uni-stuttgart.com",
    description="A Python module for running a task on its own thread at a set time interval",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.tik.uni-stuttgart.de/psomers/TimedTask",
    packages='.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3',
)
