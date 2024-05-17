from setuptools import setup, find_packages

setup(
    name='databotics',
    version='0.1.0',
    description='A package for a circular buffer implementation',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
