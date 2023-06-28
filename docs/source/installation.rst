Installation
===============

.. autosummary::
   :toctree: generated

.. warning::
  ``absbox`` is heavily using ``match clause`` which was introduced in Python 3.10. Please make sure you are using *Python3.10* and after

Using pip
--------------

.. code-block:: console

    pip install absbox

Upgrade `absbox` package to latest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``absbox`` is evolving rapidly, please make sure you are using the latest one. 

.. code-block:: console

    pip install -U absbox

Check version
^^^^^^^^^^^^^^^

.. code-block:: console 

    pip show absbox 

which shows current version of `absbox` 

.. image:: img/package_version.png
  :width: 500
  :alt: version

.. warning::
   Version matters !! As `absbox` is calling RESTful service from `Hastructure`. 
   The message format for both shall be compatible to each other. i.e `absbox 0.8.5` is compatible with `Hastructure 0.8.6`.
   A general rule is that the "MINOR" part shall be same. ( here the ``8`` )
   

Github
--------------

User can install from Github.com as it is actively fixing new bugs and developing new features.
Documents and sample code in this site are being test against with code from github.com

.. code-block:: console

    pip install -U git+https://github.com/yellowbean/AbsBox.git@main


Public Server vs Self-hosted
-----------------------------

``absbox`` needs connecting to an ``Hastructure`` engine. User can choose a public one or use it's own if user is keen on privacy and performance.

.. image:: img/user_choose_server.png
  :width: 600
  :alt: user_choose_server

Connect to a engine 
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from absbox import API
   localAPI = API("https://absbox.org/api/latest")

   # optinally adding a `english` to request all responces in English
   localAPI = API("https://absbox.org/api/latest",'english')

Use Public Server
^^^^^^^^^^^^^^^^^^^^^

For public server list, please visit `absbox.org <https://absbox.org>`_

.. note ::
  
  Public server may provide less calculation performance and high network IO and doesn't ganrantee the SLA. Pls don't use it in production.


Use Private/In-House Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If user want to have a self-hosted server 
  * user can build one from source code `Hastructure <https://github.com/yellowbean/Hastructure>`_
  * or using docker by one-line solution

    .. code-block:: bash

      docker pull yellowbean/hastructure
      docker run yellowbean/hastructure
      # by default the server expose its port at 8081


.. note ::
  
  ``absbox`` uses ``pandas`` , ``requests`` for data processing and service call.