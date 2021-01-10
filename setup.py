import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolbox_file_converter",
    version="0.0.1",
    author="Sabrina Yu",
    author_email="sabrinayu7@gmail.com",
    description="Module for converting SLI Toolbox files to Readalongs compatible xml files",  # noqa: #501
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saltyseadawg/toolbox-file-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
