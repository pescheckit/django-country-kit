"""
Setup configuration for the customersatisfactionmetrics package.

This script is used to handle the packaging and distribution of the
'customersatisfactionmetrics' package, including metadata, dependencies,
and other necessary package information.
"""

from setuptools import setup

# Using 'with' statement for safe file handling
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-country-kit',
    version="0.0.9",
    author='Pescheck IT',
    author_email='devops@pescheck.io',
    description='Countries for django',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/pescheckit/django-country-kit',
    packages=["django_country_kit"],
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
    ],
    keywords=[
        'django',
        'country',
    ],
    license='MIT',
)
