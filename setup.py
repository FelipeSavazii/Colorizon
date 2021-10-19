from setuptools import setup
import re

version = '1.0.0'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

packages = [
    'colorizon',
]

setup(name='colorizon',
      author='Felipe Savazi',
      author_email="dev@felipesavazi.com",
      url='https://github.com/FelipeSavazii/Colorizon',
      project_urls={
        "Documentation": "https://github.com/FelipeSavazii/Colorizon/tree/main/docs",
        "Issue tracker": "https://github.com/FelipeSavazii/Colorizon/issues",
      },
      version=version,
      packages=packages,
      license='MIT',
      description='A small library to make it easy to use colors in Python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      include_package_data=True,
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
      ]
)
