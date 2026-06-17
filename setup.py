from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="coding-cli",
    version="0.1.0",
    description="CLI Coding Assistance Tool using Llama",
    author="Your Name",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "coding-cli=main:cli",
        ],
    },
    python_requires=">=3.8",
)
