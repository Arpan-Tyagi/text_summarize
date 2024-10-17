import setuptools
with open("README.md","r",encoding="utf-8")as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="text_summarize"
AUTHOR_USER_NAME="Arpan-Tyagi"
SRC_REPO='text_summarize'
AUTHOR_EMAIL="arpantyagi88@gmail.com"


import setuptools

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{}/{}".format(AUTHOR_USER_NAME, REPO_NAME),  # Fixed here

    project_urls={
        "Bug Tracker": "https://github.com/{}/{}/issues".format(AUTHOR_USER_NAME, REPO_NAME),  # Fixed here
    },
    package_dir={"": "src"},  # Fixed here
    packages=setuptools.find_packages(where="src"),
)
