Registration
============

Central registration at PID providers
-------------------------------------

The following resources (:numref:`tab-register-guidance`) provide
technical guidance for institutions to publish and manage PID records
at PID providers compliant with RDA PIDINST recommendations.

.. table:: Technical guidance for publishing and managing instrument
           PIDs at PID providers compliant with RDA PIDINST
           recommendations. The table provides links to the relevant
           metadata schema that accompanies PID records at PID
           providers.
    :name: tab-register-guidance

    +--------------+--------------------------+--------------------------------------------------------------------------------------------------+
    | PID provider | Technical resource       | Metadata schema                                                                                  |
    +==============+==========================+==================================================================================================+
    | ePIC         | :ref:`epic-cookbook`     | `PIDINST <https://github.com/rdawg-pidinst/schema/blob/master/schema.rst>`_                      |
    +--------------+--------------------------+--------------------------------------------------------------------------------------------------+
    | DataCite     | :ref:`datacite-cookbook` | `PIDINST to DataCite <https://github.com/rdawg-pidinst/schema/blob/master/schema-datacite.rst>`_ |
    +--------------+--------------------------+--------------------------------------------------------------------------------------------------+


Local registration at institutional instrument providers
--------------------------------------------------------

In order to register instrument PIDs at a provider service,
institutional instrument providers must publish a landing page for each
instrument PID to resolve to. These publications might be encoded using
standard markup languages (e.g. HTML), structured, machine-actionable
web resources (e.g. World Wide Consortium’s (W3C) Linked Data), or
specialist standards for describing instruments and their inherited
properties and processes (e.g. Open Geospatial Consortium’s (OGC)
SensorML, W3C Semantic Sensor Network (SSN) ontology). Whichever method
of publication is used, it is necessary to ensure there is enough
metadata on landing pages to unambiguously identify the instrument (see
:ref:`landing-page-content`). The URL address is also used to populate
the *LandingPage* property of the `PIDINST schema`_, adding this
locator to the PID’s metadata record.


.. _PIDINST schema:
   https://github.com/rdawg-pidinst/schema/blob/master/schema.rst
