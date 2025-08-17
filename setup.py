from setuptools import setup, Extension, find_packages

# Define the C extension
encoder_extension = Extension(
    name="fdShape.encoder",                    # This creates fdShape/encoder.so|pyd
    sources=["fdShape/encoder.c"],
    language="c",
)

setup(
    name="fdShape",
    version="0.1.0",
    author="Augusto",
    author_email="dev.augusto.ferreira@gmail.com",
    description="Fast and deterministic shape encoding/decoding using C extensions.",
    url="https://github.com/redkiil/fdShape",  # Change this
    packages=find_packages(),
    ext_modules=[encoder_extension],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "fiona",  # Required for reading shapefiles
        "kaitaistruct"
    ],
)
