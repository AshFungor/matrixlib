from setuptools import find_packages, setup

setup(
    name='matrixlib',
    packages=find_packages(include=['matrixlib.matrix']),
    version='0.0b0',
    description='matrix algebra python library',
    author='AshFungor',
    license='MIT',
    install_requires=[],
    test_suite='tests',
)
