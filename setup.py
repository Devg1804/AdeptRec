from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:

    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    # with open("requirements.txt", "r") as file:
    #     for line in file:
    #         line = line.strip()
    #         # Ignore comments and empty lines
    #         if line and not line.startswith("#"):
    #             requirement_list.append(line)
        
    return requirement_list

setup(
    name='Chatbot',
    version='0.0.1',
    author='Dev',
    author_email='devg4754@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)