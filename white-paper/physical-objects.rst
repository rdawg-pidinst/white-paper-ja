Linking physical objects
========================

Instruments and their individual configuration represent the major
reference for the origin of a broad spectrum of data. As such, both
become part of the Internet of Things (IoT) and therefore it is of key
importance for related identification mechanisms to enable physical
access to these objects in addition to their digital representations or
catalogue metadata. Thus, to ultimately allow the “mapping the real
world into the virtual world”.\ [#atzori]_ This kind of access is
essential to reproduce science as it allows us to compare experimental
setup and to repeat analyses.

The most trivial but failsafe method to link physical objects with their
virtual representation would be to permanently label an instrument by
writing or engraving its PID onto it or its container along with its
inventory number and serial number. Because space for labels is limited
on smaller sensors, modern QR tags or barcodes may be more convenient as
they offer the possibility to encode any identifying information in a
machine readable way. A recommended way would be to use QR codes to
embed a PID’s actionable URIs (:numref:`fig-objects-qr`). Ideally such
a QR badge additionally displays the PID as well as the inventory
number and serial number in a human readable way. Some QR code
generators now allow users to integrate images like organisation logos
or track scanning activity such as the GPS position when the label is
scanned.

In case neither labelling of physical objects with barcodes or PID
strings is possible, linking of instruments with their digital
representation can be maintained by providing appropriate metadata
records. For instruments such linking can be achieved by capturing
identifiers which uniquely identify an instrument such as serial number
or inventory number.

While PIDINST schema metadata does not provide explicit fields for
serial numbers or inventory numbers, it currently offers a generic way
to capture any kind of identifier which can be used for this purpose.
*AlternateIdentifier* can be used to record any identifier string and
*alternateIdentifierType* to specify an identifier type
(:numref:`snip-objects-serial`). PIDINST schema recommends the use of
the terms *serialNumber* and *inventoryNumber.* There is on-going
discussion regarding the use of explicit fields for these properties
in PIDINST.

.. _fig-objects-qr:
.. figure:: /images/image4.png
    :alt: QR code

    An example of a webpage QR code that includes an organisation logo
    and re-directs the scanner to the PID URL
    (http://hdl.handle.net/21.T11998/0000-001A-3905-F).

.. _snip-objects-serial:
.. code-block:: XML
    :caption: An instrument serial number expressed in XML

      <AlternateIdentifiers>
         <AlternateIdentifier alternateIdentifierType="serialNumber">7351-349l-mn24-019f</AlternateIdentifier>
      </AlternateIdentifiers>

Besides storing e.g. serial numbers in PIDINST schema metadata, it is
highly recommended to store the instrument PID within an institutional
sensor management or inventory system immediately after PID
registration. This ensures the maintenance of links between physical
objects and their virtual representation at both endpoints, the
institutional sensor management system as well as the PID registry, and
will ensure the persistence of object linking in case of failures on
either side.

.. [#atzori]
   Atzori, Luigi & Iera, Antonio & Morabito, Giacomo. (2010). The
   Internet of Things: A Survey. Computer Networks. 2787-2805.
   10.1016/j.comnet.2010.05.010.
