from setuptools import setup, find_packages


setup(
    author='Pete Graham',
    classifiers=['Private :: Do Not Upload'],
    description='API requests logging',
    entry_points={
        'console_scripts': [
            'logstar = logstar.app:run_app',
            'logstar_install = logstar.database:init_db',
            'logstar_test_request = logstar:test_request',
        ]
    },
    install_requires=['Flask', 'gunicorn', 'psycopg2-binary', 'SQLAlchemy', 'requests'],
    name='logstar',
    packages=find_packages(),
    url='https://github.com/pxg/logstar',
    version='1.0.0',
)
