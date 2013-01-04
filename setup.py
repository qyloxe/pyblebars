from distutils.core import setup

from pyblebars import __version__

setup(
    name="pyblebars",
    version=__version__,
    description="Generate text by template. For lazy developers with code automation ambitions",
    author="Qyloxe",
    author_email="qyloxe@gmail.com",
    url="https://github.com/qyloxe/pyblebars",
    keywords=["pyblebars"],
    py_modules=['pyblebars'],
    classifiers=[
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    ],
)