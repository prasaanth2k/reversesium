from setuptools import setup, find_packages
# for test fix
setup(
    name="reverser",
    version="0.4",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "reverser = reverser.reversercli:main",
        ],
    },
    install_requires=[
        "rich",
    ],
    python_requires=">=3.6",
    author="Prasaanth Sakthivel",
    author_email="prasaanth@gmail.com",
    description="Reversesium is complete framware for all types of reverse engineering concepts and we can hook the binary and analysis the binary in isolate environment with effective way",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prasaanth2k/reversesium",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
