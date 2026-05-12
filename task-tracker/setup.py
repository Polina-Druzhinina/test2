from setuptools import( 
    setup, 
    find_packages
)

setup(
    name="task-tracker-cli-dev",
    version="0.1.1",
    long_description="Task tracker application",
    long_description_content_type="text/markdown",
    url = "https://github.com/Polina-Druzhinina/test2/tree/feature/testpypi/task-tracker",
    package_dir={"":"src"},
    packages=find_packages(where="src")
)