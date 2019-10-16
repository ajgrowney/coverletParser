import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coverlet-coverage-parser-ajgrowney",
    version="0.0.1",
    author="Andrew Growney",
    author_email="ajgrowney@gmail.com",
    description="When using coverlet.msbuild, you read out a coverage.json file. This package takes that long nasty file and makes it meaningful in your testing process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajgrowney/coverlet-coverage-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
