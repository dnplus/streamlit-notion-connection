""" Setup file for the package. """
import setuptools

VERSION = "0.0.2"

NAME = "st-notion-connection"

INSTALL_REQUIRES = [
    "streamlit>=1.28.0",
]

with open("README.md", "r", encoding="UTF-8") as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Streamlit Connection for Notion API.",
    url="https://github.com/dnplus/streamlit-notion-connection",
    author="Dylan Lu",
    author_email="dnplus@gmail.com",
    license="MIT",
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["streamlit_notion"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)
