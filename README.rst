Colorizon
==========

.. image:: https://discord.com/api/guilds/833158978962849833/embed.png
   :target: https://discord.gg/hnmA4ScM3d
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/colorizon.svg
   :target: https://pypi.python.org/pypi/colorizon
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/colorizon.svg
   :target: https://pypi.python.org/pypi/colorizon
   :alt: PyPI supported Python versions

An easy to use library for putting colors into the terminal written in Python.

Installing
----------

**Python 3.8 or higher is required**

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U colorizon

    # Windows
    py -3 -m pip install -U colorizon

Or install from GitHub:

.. code:: sh

    $ git clone https://github.com/FelipeSavazii/Colorizon
    $ cd Colorizon
    $ python3 -m pip install -U

Quick Example
--------------

.. code:: py

    from colorizon.backgrounds import Backgrounds
    from colorizon.colors import Colors
    from colorizon.formattings import Formattings

    print(Backgrounds().black('Hello, World!'))
    print(Colors().pink('I love you, Ariana Grande.'))
    print(Formattings().bold('Excuse me, i love you!'))

Links
------

- Documentation: Coming soon
- `Official Discord Server <https://discord.gg/hnmA4ScM3d>`_
