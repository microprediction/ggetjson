import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="ggetjson",
    version="0.0.1",
    description="Request JSON data en masse with backoff and failover",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/ggetjson",
    author="microprediction",
    author_email="info@microprediction.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ggetjson"],
    test_suite='pytest',
    tests_require=['pytest','grequests'],
    include_package_data=True,
    install_requires=["grequests"],
    entry_points={
        "console_scripts": [
            "ggetjson=ggetjson.__main__:main",
        ]
     },
     )
