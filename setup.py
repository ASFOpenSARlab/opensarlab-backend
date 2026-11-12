from setuptools import setup, find_packages
import pathlib


# Get the long description from the GitHub README file
def read_github_readme():
    here = pathlib.Path(__file__).resolve().parent
    with open(here / "README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="opensarlab-backend",
    version="1.0.5",
    description="Backend python modules for OpenSARLab",
    long_description_content_type="text/markdown",
    long_description=read_github_readme(),
    url="https://github.com/ASFOpenSARlab/opensarlab-backend",
    author="Alaska Satellite Facility OpenSARLab Team",
    author_email="uaf-jupyterhub-asf@alaska.edu",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        'BSD 3-Clause "New" or "Revised" License',
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
    ],
)
