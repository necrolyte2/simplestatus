============
simplestatus
============


.. image:: https://travis-ci.org/necrolyte2/simplestatus.svg
     :target: https://travis-ci.org/necrolyte2/simplestatus

.. image:: https://coveralls.io/repos/necrolyte2/simplestatus/badge.svg
     :target: https://coveralls.io/r/necrolyte2/simplestatus

Do very simple check on hosts to make sure they are up by simply issuing a TCP connect to the given host and port.

Not really a replacement for say Nagios, but for quick and dirty, it works well

Install
=======

.. code-block:: bash

    $> cp hosts.py.example hosts.py
    $> python setup.py install

Usage
=====

.. code-block:: bash

    $> simplestatus hosts.py

Example
=======

Here we will just use the hosts.py.example that comes with this package to show what the output looks like
with hosts that are up and hosts that are down

.. code-block:: bash

    $> simplestatus hosts.py.example 
    Sanity check with Google HTTP - UP
    This port is down - DOWN
        www.google.com on port 99 seems down: [Errno 111] Connection refused

Hosts.py
========

Because I'm lazy, this is just a python file that has a variable in it instead of an actual yaml file or cfg file
All you need to do is add all your hosts to the hosts list

Each host needs to be a 3 item tuple as follows::

    ('hostname or ip', tcpport, 'Description of check')

TODO
====

* Allow UDP|DGRAM
* Allow port ranges
