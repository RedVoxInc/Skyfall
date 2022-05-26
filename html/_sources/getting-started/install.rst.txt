Set up your software environment
------------------------------------

Clone the Skyfall Github repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In a terminal, use the following command to clone the `Skyfall Github repository <https://github.com/RedVoxInc/Skyfall>`_:

.. code-block:: console

    git clone git@github.com:RedVoxInc/Skyfall.git

For more details, please check the `Instructions on how to clone a GitHub repository
<https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository>`_.

Install requirements
^^^^^^^^^^^^^^^^^^^^^
To install the necessary requirements to run the Skyfall example:

.. code-block:: console

    pip install -r /path/to/requirements.txt

The libraries featured in requirements are:

.. code-block:: console

    redvox[full] >= 3.1.7
    libquantum >= 1.3.0
    redvox-pandas >= 1.3.3

.. note::

    These libraries run on python version(s) 3.8+

We are ready to start :doc:`../running-skyfall/index`.