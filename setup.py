from setuptools import setup
import re

version = '1.0.0'

packages = [
    'colorizon',
]

setup(name='colorizon',
      author='Felipe Savazi',
      url='https://github.com/FelipeSavazii/Colorizon',
      project_urls={
        "Documentation": "https://github.com/FelipeSavazii/Colorizon/tree/main/docs",
        "Issue tracker": "https://github.com/FelipeSavazii/Colorizon/issues",
      },
      version=version,
      packages=packages,
      license='MIT',
      description='A small library to make it easy to use colors in Python',
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
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]
)
