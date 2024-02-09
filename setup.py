import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kaggle-colab',
    version='0.1.0',
    author="Pablo García Mesa",
    author_email="pgmesa.sm@gmail.com",
    description="A minimalistic tool for setting up Kaggle and Google Colab environments from a GitHub repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgmesa/kaggle_colab",
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )