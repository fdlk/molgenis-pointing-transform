from setuptools import setup, find_packages
setup(
    name='PointingTransform',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    author='Connor Stroomberg',
    license='GNU Lesser General Public License 3.0',
    test_suite='nose.collector',
    tests_require=['nose', 'parameterized']
)