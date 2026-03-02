from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements."""
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = [req.strip() for req in file_obj.readlines() if req.strip() and not req.startswith('#')]
            if '-e .' in requirements:
                requirements.remove('-e .')
    except FileNotFoundError:
        pass
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Harsh',
    author_email='harshupadhyayofficial5@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt')
)