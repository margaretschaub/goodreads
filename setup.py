from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='goodreads_scraper',
    version='0.0.1',
    description="A scraper for GoodReads 'read' shelf",
    author='Margaret Schaub',
    author_email='margaretcschaub@outlook.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/margaretschaub/goodreads',
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',

)
