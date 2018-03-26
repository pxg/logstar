from setuptools import setup, find_packages


setup(
    author='Pete Graham',
    classifiers=['Private :: Do Not Upload'],
    description='API requests logging',
    entry_points={'console_scripts': ['logstar = logstar.app:run_app']},
    name='logstar',
    packages=find_packages(),
    url='https://github.com/mypackage.git',
    version='0.0.1',
)
