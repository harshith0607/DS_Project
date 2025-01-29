from setuptools import find_packages,setup
from typing import List

hypen_dot_e='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements if req.strip()]
        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)
    
    return requirements

setup(
name='DS_project',
version='0.0.1',
author='Harshith Kothagundla',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)