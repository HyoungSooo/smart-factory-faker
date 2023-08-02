import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_factory_faker",  # Replace with your own username
    version="0.8.0",
    author="HyoungSooo",
    author_email="aaa57403@gmail.com",
    description="Smart-Factory-Faker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HyoungSooo/smart-factory-faker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
