.. PySmali documentation master file, created by
   sphinx-quickstart on Wed Mar 8 22:33:21 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PySmali's documentation
=======================

Welcome to the documentation for `pysmali`, a Python3 package designed for parsing,
transforming and generating Smali source code files, as well as interpreting source
code files. This documentation is intended to provide an overview of the package's
features, installation instructions, and usage examples to help you get started with
using the package in your Python projects.

Using this library
------------------

:doc:`installation`
   How to install the python package locally or in a virtal environment.

:doc:`Using the Smali API <api/smali/index>`
   Introduction into Smali and the provided Smali API.

:doc:`Using the Smali-Emulator <api/smali/bridge>`
   Introduction into the provided Smali-Interpreter.

:ref:`supported-dependencies`
   Supported project dependencies.

Development
-----------

:doc:`contributing`
    How to contribute changes to the project.

:doc:`Development guidelines <development>`
    Guidelines the theme developers use for developing and testing changes.

:doc:`changelog`
    The package development changelog.

.. toctree::
   :maxdepth: 3
   :caption: General Documentation
   :hidden:

   installation
   api/smali/language
   development
   contributing
   changelog

.. Hidden TOCs

.. toctree::
   :maxdepth: 3
   :caption: Smali API Documentation
   :hidden:
   :numbered:

   api/smali/index
   api/smali/reader
   api/smali/writer
   api/smali/visitor
   api/smali/base


.. toctree::
   :maxdepth: 3
   :caption: Smali Bridge
   :hidden:
   :numbered:

   api/smali/bridge
   api/smali/bridge_api
   api/smali/shell



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
