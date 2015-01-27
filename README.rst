============
simplestatus
============


.. image:: https://travis-ci.org/necrolyte2/simplestatus.svg
     :target: https://travis-ci.org/necrolyte2/simplestatus

.. image:: https://coveralls.io/repos/necrolyte2/simplestatus/badge.svg
     :target: https://coveralls.io/r/necrolyte2/simplestatus

Do very simple check on hosts to make sure they are up
This is a very bare minimum check and only does a TCP connect on a given port to see if it succeeds

Install
=======

.. code-block:: bash

    $> cp hosts.py.example hosts.py
    $> python setup.py install

Usage
=====

.. code-block:: bash

    $> python simplestatus.py

TODO
====

* Change the project so it actually allows you to specify a hosts.py
* Allow UDP|DGRAM
* Allow port ranges
