import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyCoverlet",
    version="0.0.1",
    author="Andrew Growney",
    author_email="ajgrowney@gmail.com",
    description="When using coverlet.msbuild, you read out a coverage.json file. This package takes that long nasty file and makes it meaningful in your testing process.",
    py_modules=["pycoverlet"],
    package_dir={'': 'pyCoverlet'},
    long_description="Use the package and provide the path to your coverage.json file to use during the testing for code coverage process",
    long_description_content_type="text/markdown",
    url="https://github.com/ajgrowney/coverletParser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
