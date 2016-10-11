from setuptools import setup, find_packages
from os.path import join, dirname
import logview

setup(
    name='logview',
    version=logview.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    install_requires=[
        'PyQt5',
    ],

    entry_points={
        'console_scripts': [
            'logmon-start = logview.view:main',
        ]
    },
    # include_package_data=True,
    # test_suite='tests',
)
