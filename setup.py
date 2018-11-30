try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup, find_packages


setup(
    name='poll',
    version='1.0',
    author="Benjamin Hodgson",
    author_email="benjamin.hodgson@huddle.net",
    url="https://github.com/benjamin-hodgson/poll",
    description="Utilities for polling, retrying, and exception handling",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=["setuptools"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
