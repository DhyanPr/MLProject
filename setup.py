## It is responsible for setting up the package and its dependencies and for machine learning model training and evaluation.
## first we consider entire ml project as a package and we will use setup.py to define the package structure, dependencies, and other metadata. This will allow us to easily install and distribute the package, as well as manage its dependencies.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements'''
    requirements=[] 
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req. replace("\n","") for req in requirements ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name='mlproject',
    version='0.1',
    author='Dhyan',
    author_email='dhyangec@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)