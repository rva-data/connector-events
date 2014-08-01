================
connector-events
================

.. image:: https://badge.fury.io/py/connector-events.png
    :target: https://badge.fury.io/py/connector-events

.. image:: https://travis-ci.org/rva-data/connector-events.png?branch=master
    :target: https://travis-ci.org/rva-data/connector-events

.. image:: https://coveralls.io/repos/rva-data/connector-events/badge.png?branch=master
    :target: https://coveralls.io/r/rva-data/connector-events?branch=master

Connector events is a Django application for tracking events. It has
the typical list and detail views you expect and an iCal feed for
easily sharing event data.

It was designed as a component for a 'connector' project, tracking
events for a community from multiple sources. However it can also be
used on it's own.

.. Documentation
.. -------------

.. The full documentation is at https://connector-events.readthedocs.org.

Quickstart
----------

Install connector-events::

    pip install connector-events

Then add events to your project's `INSTALLED_APPS`::

    INSTALLED_APPS = (
        'events',
    )

And into your URL configuration::

    urlpatterns = patterns('',
        url(r'^events/', include('events.urls')),
    )

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

The feed is available via the URL `/ical/`, relative to the root URL where you
have configured the event URLs.

Settings
--------

Three settings are worth calling out.

`TIME_ZONE`
~~~~~~~~~~~

This is a `default Django setting
<https://docs.djangoproject.com/en/1.6/ref/settings/#time-zone>`_ that
you should pay attention to, as the ics feed makes uses of this.

`EVENTS_UID_STRING`
~~~~~~~~~~~~~~~~~~~

This is a string that will be formatted with a keyword argument named `pk`. It
used to provide a default `UID` value for an event if none is otherwise
provided (e.g. through a calendar import, which is beyond the scope of this
application itself).

The default value is::

    "event_{pk}"

A replacement might be::

    "event_{pk}@mydomain.com"

The `iCalendar specification <http://www.kanzaki.com/docs/ical/uid.html>`_
requires that this be a *globally unique* identifier which is why it's a good
idea to use your site name/domain in conjunction with the event primary key
(unique on your site).

`EVENTS_PRODUCT_ID`
~~~~~~~~~~~~~~~~~~~

This is a string that identifies the product generating the iCalendar feed. It
populates the `PRODID` field in the feed.

The default is::

    "-//django-connector//connector-events//EN"

See the `iCalendar specification
<http://www.kanzaki.com/docs/ical/prodid.html>`_ for more information about
this field.
