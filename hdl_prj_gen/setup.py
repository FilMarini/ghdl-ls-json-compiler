import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HDL-PRJ",
    version="0.0.1",
    author="Filippo Marini",
    author_email="marinifil@gmail.com",
    description="Generate the hdl-prj.json file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    #install_requires=[
    #    'rootpy',
    #    'tabletext'
    #],
    entry_points={
        'console_scripts': [
            'hdl-prj-gen=src.hdl_prj_gen:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: Unix",
    ],
)

