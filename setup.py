import setuptools

VERSION = "0.0.1"

NAME = "st-notion-connection"

INSTALL_REQUIRES = [
    "streamlit>=1.22.0",
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Streamlit Connection for Notion API.",
    url="https://github.com/marks/streamlit-notion-connection",
    author="Dylan Lu",
    author_email="dnplus@gmail.com",
    license="MIT",
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["streamlit_notion"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)