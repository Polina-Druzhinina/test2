from setuptools import( 
    setup, 
    find_packages
)

setup(
    name="task-tracker-cli-dev",
    version="0.1.2",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url = "https://github.com/Polina-Druzhinina/test2/tree/feature/testpypi/task-tracker",
    package_dir={"":"src"},
    packages=find_packages(where="src")
)