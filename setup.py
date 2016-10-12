from setuptools import setup, find_packages
from os.path import join, dirname
import logmon.view

setup(
    name='logmon.view',
    version=logmon.view.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    install_requires=[
        'PyQt5',
    ],

    entry_points={
        'console_scripts': [
            'logmon = logmon.view.view:main',
        ]
    },
    # include_package_data=True,
    # test_suite='tests',
)
