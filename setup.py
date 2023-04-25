from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#this function will used to check what all the packages in the requirements.txt and return requriements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        
#-e . should not be come to requirements list
    

#meta data about the project
setup(
name='mlproject',
version='0.0.1',
author='nikhil',
author_email='aletinikhilreddy759@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
 
)