from channelmanagerlib import channel_manager
import setuptools
a = channel_manager()

setuptools.setup(
    name="channelmanagerlib",
    version="1.4.3",
    author="Kunode",
    author_email="kunodedev@gmail.com",
    description="API for Channel Manager LIB",
    long_description="negro",
    long_description_content_type="text/markdown",
    url="https://github.com/xDarkWhite/channelmanagerlib",
    project_urls={
        "Tracker": "https://github.com/xDarkWhite/channelmanagerlib",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    packages=setuptools.find_packages(),
)
