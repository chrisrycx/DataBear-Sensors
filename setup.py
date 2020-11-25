'''
DataBear-Sensors package setup
'''

import setuptools

setuptools.setup(
    name="databear-sensors",
    version="0.1",
    author="Chris Cox",
    author_email="chrisrycx@gmail.com",
    description="Sensor classes for DataBear",
    url="https://github.com/chrisrycx/DataBear-Sensors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)