import setuptools
from njord import version

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
        name="njord",
        version=version,
        author="antipatico",
        author_email="me@antipatico.ml",
        description="An AirVPN CLI manager.",
        url="https://antipatico.ml",
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
        ],
        packages=setuptools.find_packages(),
        #packages=["wslvpn",],
        entry_points={
            "console_scripts": [
                "njord = njord.cli:main",
            ],
        },
        install_requires=["docopt>=0.6"],
)
