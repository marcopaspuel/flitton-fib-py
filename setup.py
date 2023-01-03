from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flitton_fib_py",
    version="0.0.1",
    author="Marco Paspuel",
    author_email="marco.paspuel@outlook.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_context_type="text/markdown",
    url="https://github.com/marcopaspuel/flitton-fib-py",
    install_requires=[],
    packages=find_packages(exclude="tests,"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programing Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    test_require=['pytest'],
)
