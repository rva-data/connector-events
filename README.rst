================
connector-events
================

.. image:: https://badge.fury.io/py/connector-events.png
    :target: https://badge.fury.io/py/connector-events

.. image:: https://travis-ci.org/rva-data/connector-events.png?branch=master
    :target: https://travis-ci.org/rva-data/connector-events

.. image:: https://coveralls.io/repos/rva-data/connector-events/badge.png?branch=master
    :target: https://coveralls.io/r/rva-data/connector-events?branch=master

Connector events is a Django application for tracking events. It was designed
as a component for a 'connector' project, tracking events for a community from
multiple sources. However it can also be used on it's own.

.. Documentation
.. -------------

.. The full documentation is at https://connector-events.readthedocs.org.

Quickstart
----------

Install connector-events::

    pip install connector-events

Then add events to your project's `INSTALLED_APPS`.

Overview
--------

You can store and display information about events, including start and end
times, descriptions written in Markdown, and location. Locations can be stored
in both plain form, e.g.

    100 Main St, Richmond, VA, USA

and in basic geocoded format. The *current* format for storing geographic
location uses two separate decimal database fields for latitude and longitude
respectively. This is suboptimal compared to using a `single point field
<https://docs.djangoproject.com/en/1.6/ref/contrib/gis/model-api/#pointfield>`_
but does not entail any special database requirements.
