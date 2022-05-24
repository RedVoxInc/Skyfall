Update the Configuration File
------------------------------

In the newly cloned `Skyfall Github repository <https://github.com/RedVoxInc/Skyfall>`_, open ``skyfall_config_file.py``
(view in `Github <https://github.com/RedVoxInc/Skyfall/blob/main/skyfall_config_file.py>`_)
and update the value of ``SKYFALL_DIR = "path/to/download/data/folder"`` on line 5 to match the directory where you
downloaded the Skyfall data (the directory will have a folder named *api900*).

.. note::

    An example path for Linux/Mac:

    ``SKYFALL_DIR = "/path_to/your/downloaded_data"``

    An example path for Windows:

    ``SKYFALL_DIR = "\\path_to\\your\\downloaded_data"``

.. note::

    For example if the Skyfall data is in a folder (perhaps named *aa5869b632b24f0f8908ad4122d63cd0*) located in Desktop,
    then ``SKYFALL_DIR`` should be
    ``SKYFALL_DIR = "path/to/Desktop/aa5869b632b24f0f8908ad4122d63cd0"`` without including the *api900* folder.