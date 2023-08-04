import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart_factory_faker",  # Replace with your own username
    version="0.10.0",
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

    install_requires=[
        'matplotlib==3.7.1',				# version 명시 안 함
        'graphviz==0.20.1',		# 정확한 version 명시
        'pandas==1.5.2',		# 최소 version 명시
        'scipy',
        'sympy',
        'scikit-learn',

    ],
    python_requires='>=3.10',
)
