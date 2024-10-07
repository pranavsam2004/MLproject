from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements 
    '''
    requirements =[]
    with open(file_path) as file_obj:
        repr=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name = "mlproject",
    version ="0.0.1",
    author="pranavsam2004",
    author_email="pranavsam2004@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)