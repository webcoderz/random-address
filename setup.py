from setuptools import setup


with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='random-address',
    version='0.0.2',
    description='Tool to retrieve a real random address '
                'that geocode successfully',
    py_modules=['random_address'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    url='https://github.com/neosergio/random-address',
    author='Sergio Infante',
    author_email='raulsergio9@gmail.com',
)
