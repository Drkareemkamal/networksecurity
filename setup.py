"""
the setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in olfer Python versions)to define the configuration 
of our project, such as its metadata , dependencies , and more
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function is used to get all the required packages
    """
    requirements_list:list = [] 
    try :
        with open('requirements.txt', 'r') as f:
            # read lines from the file
            lines = f.readlines()
            ## proccess each line
            for line in lines :
                requirements = line.strip()
                ## ignore empty lines and -e .
                if requirements and requirements != "-e .":
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirements_list

setup (
    name = 'NetworkSecurity',
    version = '0.0.1',
    author='Dr.Kareem Kamal',
    author_email='kareemkamal@kareemkamal.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)
