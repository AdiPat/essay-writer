from setuptools import setup, find_packages


setup(
    name="essay-writer",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "python-dotenv==1.0.1",
        "pydantic==2.10.6",
        "pydantic-settings==2.7.1",
        "pydantic_core==2.27.2",
        "rich==13.9.4",
        "openai==1.61.1",
    ],
    author="Aditya Patange (AdiPat)",
    author_email="contact.adityapatange@gmail.com",
    description="A minimal package for students to generate essays.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thehackersplaybook/auxknow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license_files=("LICENSE",),
)
