from setuptools import setup, find_packages

def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file:
        requirements = file.readlines()


    
    # Remove any whitespace characters like `\n` at the end of each line
    requirements = [req.strip() for req in requirements if req.strip()]

    if('-e .' in requirements):
        requirements.remove('-e .')
    # print(requirements)
    return requirements

get_requirements('requirements.txt')

setup(
    name='mlproject',
    version='0.0.1',
    author='shiva',
    author_email='pasulashivachetanreddy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)