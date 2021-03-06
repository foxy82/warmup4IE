Introduction
============

This is a library for communicating with a wifi-enabled home thermostat made by
`Warmup <https://www.warmup.co.uk/>`_. At the time of writing, this only 
includes the `warmup 4IE <https://www.warmup.co.uk/thermostats/smart/4ie-underfloor-heating>`_.

This code is inspired by a project for SmartThingsHub, see `here <https://github.com/alyc100/SmartThingsPublic/blob/master/devicetypes/alyc100/warmup-4ie.src/warmup-4ie.groovy>`_. Many Thanks to alyc100 for the great work!

Warmup Plc was not involved in the creation of this
software and has not sanctioned or endorsed it in any way.

License
=======

This software is available under Apache license. Please see LICENSE.txt.


Usage
=====
The library is primary intended to interface the 4IE with home assistant, but may also be used standalone.

Home Assistant
---------------
To setup this component, you need to register to warmup first.
see https://my.warmup.com/login

Then copy the folder `warmup_cc <https://github.com/alex-0103/warmup4IE/blob/master/warmup_cc>`_ to your "*custom_components*" folder in your "*config*" dir.

Then add to your
configuration.yaml:

.. code-block:: yaml

  climate:
    - platform: warmup_cc
      name: YOUR_DESCRIPTION
      username: YOUR_E_MAIL_ADDRESS
      password: YOUR_PASSWORD
      location: YOUR_LOCATION_NAME
      room: YOUR_ROOM_NAME

* **name** (optional): the description of the device, as seen by the user in the front end
* **username** (required): the username used to login to the warmup web site
* **password** (required): the password used to login to the warmup web site; may be moved to the secrets.yaml file. See `secrets <https://www.home-assistant.io/docs/configuration/secrets/>`_
* **location** (required): the location name used in the warmup web site
* **room** (required): the room name of the device used in the warmup web site

After restarting home assistant, the component will be loaded automatically.

Standalone
----------
You may install the library via pip using

>>> pip install warmup4ie

After that, import the library, and away we go.

    >>> import warmup4ie
    >>> device = warmup4ie.Warmup4IEDevice('<e-mail>', '<password>', 
    '<location>', '<room>', <inital target temp>)
    >>> device.get_current_temmperature()
    {'raw': 21.0}

Device Versions
---------------

Supported models:

- 4IE

Since I only have access to the 4IE, that is the model that the development 
has occured with. 

Supported Features
------------------

At the moment the library supports reading current temperature and setting the target temperature, switching between manual, automatic and frost protection mode, and switching the device off.

Release Notes
=============

0.1.0
-----

- inital release

0.1.1
-----

- bug fixes

0.1.2
-----

- bug fixes

0.1.3
-----

- changed http-request to use the new api.
- adapted file names to comply with the new naming structure of HA introduced with 0.92
