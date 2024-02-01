.. _landing-page-encoding:

Landing page encoding
=====================

Landing page web resources can be written in any format (e.g. HTML,
XML). Although not obligatory, ideally resources should be encoded in
formats that not only improve syntactic interpretation of information
but semantic understanding of the information. In other words, machines
can not only read but understand the meaning of the information
presented in web resources, enhancing interoperability and integration
between systems. Below are some examples of landing page encodings.

Examples
--------

JSON-LD
~~~~~~~

There is a strong relation between PIDs with values of types that are
defined in a data type registry (DTR) as for instance in the
example in :numref:`tab-schema-handle-record` and linked data. First
of all a PID with a type value is a triple where the PID plays the
role of the subject, the type definition is the predicate and the
value is the object. Secondly the type definition itself can refer to
sub types also defined in a DTR. If this construction of types out of
other types is done in a consistent and machine actionable way, as it
is done for instance in the ePC DTR, these subtypes may be referred by
human readable names. The names are disambiguated by the type
definition, because each subtype used in a type is identified by a
PID. Such PIDs with types defined upon sub types span a graph of
metadata around the PID. PIDs with types are in other words a specific
representation of linked data.

It is therefore obvious to ask for other, more a common linked data
representation like RDF or JSON-LD of such PIDs with types. Such a
conversion can be done by a simple backtracking algorithm that crawls
from the PID through all its type and subtypes definitions to identify
the used names by the type PIDs and to collect this information for the
LD representation. This way the whole graph is explored and this graph
can be mapped into a linked data representation. In the following a
respective representation in JSON-LD of the schema example shown in
:numref:`tab-schema-handle-record` is shown in
:numref:`snip-landing-encoding-json-ld`.

.. code-block:: JSON
    :name: snip-landing-encoding-json-ld
    :caption: representation in JSON-LD of the example of
	      :numref:`tab-schema-handle-record`.

      {
        "@context" : {
          "ARK-Identifier" : "dti:21.T11148/7af6f46512fb4c190d01",
          "AlternateIdentifier" : "dti:21.T11148/d87a75c52c68b06e9a18",
          "AlternateIdentifierValue" : "dti:21.T11148/38330bcc6a40ca85e5b4",
          "AlternateIdentifiers" : "dti:21.T11148/eb3c713572f681e6c4c3",
          "Bibcode-Identifier" : "dti:21.T11148/6c2fc7682e48ac7160b5",
          "DOI-Identifier-General" : "dti:21.T11148/d93427e3c56173e9dc08",
          "Date" : "dti:21.T11148/eb9a4bc1c0c153e4e4b0",
          "Dates" : "dti:21.T11148/22c62082a4d2d9ae2602",
          "Description" : "dti:21.T11148/55f8ebc805e65b5b71dd",
          "Handle-Identifier-ASCII" : "dti:21.T11148/3626040cadcac1571685",
          "ISAN-Identifier" : "dti:21.T11148/48cfce4482166a103c50",
          "ISBN-Identifier" : "dti:21.T11148/2ff8ad6cdd4e46622944",
          "ISNI-Identifier" : "dti:21.T11148/cff32964e132c14fc56f",
          "ISRC-Identifier" : "dti:21.T11148/2719170925ff2bfb5157",
          "ISSN-Identifier" : "dti:21.T11148/7e689432354610f388c0",
          "ISTC-Identifier" : "dti:21.T11148/1f0df9ef66774b2e2aa1",
          "ISWC-Identifier" : "dti:21.T11148/698fba7e1c659fcfdcdd",
          "InstrumentType" : "dti:21.T11148/f76ad9d0324302fc47dd",
          "LandingPage" : "dti:21.T11148/9a15a4735d4bda329d80",
          "Manufacturer" : "dti:21.T11148/7adfcd13b3b01de0d875",
          "Manufacturers" : "dti:21.T11148/1f3e82ddf0697a497432",
          "MeasuredVariable" : "dti:21.T11148/1fcb0dad9aced457d67e",
          "MeasuredVariables" : "dti:21.T11148/72928b84e060d491ee41",
          "Name" : "dti:21.T11148/709a23220f2c3d64d1e1",
          "Owner" : "dti:21.T11148/89ff31225c5f042fff61",
          "Owners" : "dti:21.T11148/4eaec4bc0f1df68ab2a7",
          "PMCID-Identifier" : "dti:21.T11148/e94bec7d7f1c63dd00cd",
          "PMID-Identifier" : "dti:21.T11148/234c084bac48480bfe5d",
          "RelatedIdentifier" : "dti:21.T11148/ec9f00af0761a065dbd0",
          "RelatedIdentifierType" : "dti:21.T11148/015dc79a77940fb65aa4",
          "RelatedIdentifierValue" : "dti:21.T11148/38330bcc6a40ca85e5b4",
          "RelatedIdentifiers" : "dti:21.T11148/178fb558abc755ca7046",
          "URN-Identifier" : "dti:21.T11148/d22b6854df3503df7831",
          "VariableMeasured" : "dti:21.T11148/f1627ce85386d8d75078",
          "alternateIdentifierType" : "dti:21.T11148/015dc79a77940fb65aa4",
          "arXiv-Identifier" : "dti:21.T11148/d66f8368c3d305941a2e",
          "date" : "dti:21.T11148/be707495360a234ef049",
          "dateType" : "dti:21.T11148/2f0e608b621a5a97e0d9",
          "dti" : "http://hdl.handle.net/",
          "identifier-general-with-type" : "dti:21.T11148/8eb858ee0b12e8e463a5",
          "identifierType" : "dti:21.T11148/015dc79a77940fb65aa4",
          "identifierValue" : "dti:21.T11148/38330bcc6a40ca85e5b4",
          "manufacturerIdentifier" : "dti:21.T11148/5b240e16ea32ea25cf65",
          "manufacturerIdentifierType" : "dti:21.T11148/015dc79a77940fb65aa4",
          "manufacturerIdentifierValue" : "dti:21.T11148/38330bcc6a40ca85e5b4",
          "manufacturerName" : "dti:21.T11148/798588c5a1ec532f737b",
          "modelName" : "dti:21.T11148/798588c5a1ec532f737b",
          "other" : "dti:21.T11148/f40cb15558a7c1546c91",
          "ownerContact" : "dti:21.T11148/a88b7dcd1a9e3e17770b",
          "ownerIdentifier" : "dti:21.T11148/1e3c17ac2a3e7ebf466a",
          "ownerIdentifierType" : "dti:21.T11148/015dc79a77940fb65aa4",
          "ownerIdentifierValue" : "dti:21.T11148/38330bcc6a40ca85e5b4",
          "ownerName" : "dti:21.T11148/798588c5a1ec532f737b",
          "relationType" : "dti:21.T11148/292a53bd9ee27a242082"
        },
        "@id" : "dti:21.T11998/0000-001A-3905-F",
        "AlternateIdentifiers" : [
          {
            "AlternateIdentifier" : {
              "AlternateIdentifierValue" : "2490",
              "alternateIdentifierType" : "serialNumber"
            }
          }
        ],
        "Dates" : [
          {
            "date" : {
              "date" : "1999-11-01",
              "dateType" : "Commissioned"
            }
          }
        ],
        "Description" : "A high accuracy conductivity and temperature recorder with an optional pressure sensor designed for deployment on moorings. The IM model has an inductive modem for real-time data transmission plus internal flash memory data storage.",
        "InstrumentType" : "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0022/",
        "LandingPage" : "https://linkedsystems.uk/system/instance/TOOL0022_2490/current/",
        "Manufacturers" : [
          {
            "Manufacturer" : {
              "manufacturerIdentifier" : {
		"manufacturerIdentifierType" : "URL",
		"manufacturerIdentifierValue" : "http://vocab.nerc.ac.uk/collection/L35/current/MAN0013/"
              },
              "manufacturerName" : "Sea-Bird Scientific",
              "modelName" : "SBE 37-IM"
            }
          }
        ],
        "MeasuredVariables" : [
          {
            "MeasuredVariable" : {
              "VariableMeasured" : "http://vocab.nerc.ac.uk/collection/P01/current/CNDCPR01/"
            }
          },
          {
            "MeasuredVariable" : {
              "VariableMeasured" : "http://vocab.nerc.ac.uk/collection/P01/current/PSALPR01/"
            }
          },
          {
            "MeasuredVariable" : {
              "VariableMeasured" : "http://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/"
            }
          },
          {
            "MeasuredVariable" : {
              "VariableMeasured" : "http://vocab.nerc.ac.uk/collection/P01/current/PREXMCAT/"
            }
          }
        ],
        "Name" : "Sea-Bird SBE 37-IM MicroCAT C-T Sensor",
        "Owners" : [
          {
            "Owner" : {
              "ownerContact" : "louise.darroch@bodc.ac.uk",
              "ownerIdentifier" : {
		"ownerIdentifierType" : "URL",
		"ownerIdentifierValue" : "http://vocab.nerc.ac.uk/collection/B75/current/ORG00009/"
              },
              "ownerName" : "National Oceanography Centre"
            }
          }
        ],
        "RelatedIdentifiers" : [
          {
            "RelatedIdentifier" : {
              "RelatedIdentifierType" : "URL",
              "RelatedIdentifierValue" : "https://www.bodc.ac.uk/data/documents/nodb/pdf/37imbrochurejul08.pdf",
              "relationType" : "IsDescribedBy "
            }
          }
        ],
        "identifier-general-with-type" : {
          "identiferType" : "MeasuringInstrument",
          "identifierValue" : "http://hdl.handle.net/21.T11998/0000-001A-3905-F"
        }
      }

As one can see in this result the context is over complete in the sense
that all possible sub types are resolved and referred in @context, but
not all of them are actually used by the types occuring in the PID. This
could be pruned by an additional step of the algorithm to a version
reduced to the necessary and sufficient sub types. Such a pruning is
also automatically done by LD converters\ [#ld_converters]_ as one can
see in the following snippet with a conversion into Turtle Terse RDF
that results into the following serialization
(:numref:`snip-landing-encoding-turtle`), where only the values remain
and the names used in the type definitions are replaced by their type
PID suffixes:

.. code-block:: turtle
    :name: snip-landing-encoding-turtle
    :caption: representation in Turtle Terse RDF of the NERC example
	      of :numref:`tab-schema-handle-record` that was generated
	      by a JSON-LD to RDF converter from the JSON-LD in
	      :numref:`snip-landing-encoding-json-ld`.

      @prefix ns0: <http://hdl.handle.net/21.T11148/> .
      @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

      <http://hdl.handle.net/21.T11998/0000-001A-3905-F>
        ns0:178fb558abc755ca7046 [ ns0:ec9f00af0761a065dbd0 [
         ns0:015dc79a77940fb65aa4 "URL"^^xsd:string ;
         ns0:292a53bd9ee27a242082 "IsDescribedBy "^^xsd:string ;
         ns0:38330bcc6a40ca85e5b4 "https://www.bodc.ac.uk/data/documents/nodb/pdf/37imbrochurejul08.pdf"^^xsd:string
         ] ] ;
        ns0:1f3e82ddf0697a497432 [ ns0:7adfcd13b3b01de0d875 [
         ns0:5b240e16ea32ea25cf65 [
            ns0:015dc79a77940fb65aa4 "URL"^^xsd:string ;
            ns0:38330bcc6a40ca85e5b4 "http://vocab.nerc.ac.uk/collection/L35/current/MAN0013/"^^xsd:string
         ] ;
         ns0:798588c5a1ec532f737b "Sea-Bird Scientific"^^xsd:string, "SBE 37-IM"^^xsd:string
         ] ] ;
        ns0:22c62082a4d2d9ae2602 [ ns0:be707495360a234ef049 [
         ns0:2f0e608b621a5a97e0d9 "Commissioned"^^xsd:string ;
         ns0:be707495360a234ef049 "1999-11-01"^^xsd:string
         ] ] ;
        ns0:4eaec4bc0f1df68ab2a7 [ ns0:89ff31225c5f042fff61 [
         ns0:1e3c17ac2a3e7ebf466a [
            ns0:015dc79a77940fb65aa4 "URL"^^xsd:string ;
            ns0:38330bcc6a40ca85e5b4 "http://vocab.nerc.ac.uk/collection/B75/current/ORG00009/"^^xsd:string
         ] ;
         ns0:798588c5a1ec532f737b "National Oceanography Centre"^^xsd:string ;
         ns0:a88b7dcd1a9e3e17770b "louise.darroch@bodc.ac.uk"^^xsd:string
         ] ] ;
        ns0:55f8ebc805e65b5b71dd "A high accuracy conductivity and temperature recorder with an optional pressure sensor designed for deployment on moorings. The IM model has an inductive modem for real-time data transmission plus internal flash memory data storage."^^xsd:string ;
        ns0:709a23220f2c3d64d1e1 "Sea-Bird SBE 37-IM MicroCAT C-T Sensor"^^xsd:string ;
        ns0:72928b84e060d491ee41 [ ns0:1fcb0dad9aced457d67e [ ns0:f1627ce85386d8d75078 "http://vocab.nerc.ac.uk/collection/P01/current/CNDCPR01/"^^xsd:string ] ], [ ns0:1fcb0dad9aced457d67e [ ns0:f1627ce85386d8d75078 "http://vocab.nerc.ac.uk/collection/P01/current/PSALPR01/"^^xsd:string ] ], [ ns0:1fcb0dad9aced457d67e [ ns0:f1627ce85386d8d75078 "http://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/"^^xsd:string ] ], [ ns0:1fcb0dad9aced457d67e [ ns0:f1627ce85386d8d75078 "http://vocab.nerc.ac.uk/collection/P01/current/PREXMCAT/"^^xsd:string ] ] ;
        ns0:8eb858ee0b12e8e463a5 [ ns0:38330bcc6a40ca85e5b4 "http://hdl.handle.net/21.T11998/0000-001A-3905-F"^^xsd:string ] ;


.. _landing-page-encoding-swe:

Sensor web enablement (SWE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Global standards have been developed which enable the web-based
discovery, exchange and processing of sensors and their observations.
Many developers using standards, such as the Open Geospatial
Consortium’s (OGC) Sensor Web Enablement (SWE), publish formal,
machine-readable descriptions of sensors and their technical information
as web resources using URLs, identifying the instrument locally.
Web-based sensor descriptions published using SensorML, part of the SWE
specifications, and may be used as a URL to the landing page of the
instrument registered at a PID provider. A SensorML landing page example
has been published at the British Oceanographic Data Centre (BODC) via
the ePIC PID provider service
(http://hdl.handle.net/21.T11998/0000-001A-3905-F). To view the Handle
record directly see
http://hdl.handle.net/21.T11998/0000-001A-3905-F?noredirect or
:numref:`tab-schema-handle-record` in this document.

In SensorML (version 2.0), sensors are identified using a unique ID
within the *gml:identifier* element and institutions may choose to use
an instrument PID to assure uniqueness. Alternatively, an instrument PID
may be declared as metadata within a SensorML description using the
*sml:identifier* property (:numref:`snip-landing-encoding-sensorml`).
While the latter is simpler to implement, it may limit the global
discoverability of sensors and their observations within the Sensor
Observation Service (SOS) web Application Programming Interface (API),
part of the SWE standard. Web-based enquiries, requests or
transactions made for sensors using this service are typically based
on *gml:identifier* element in SensorML (expressed as a *procedure*),
thus identifying sensors using local identifiers rather than global
instrument PIDs directly. The link between local identifiers and
instrument PIDs can be found indirectly using a combination of
*GetCapabilities* and *DescribeSensor* operational requests to a SOS
server.

.. code-block:: xml
    :name: snip-landing-encoding-sensorml
    :caption: An example of expressing an instrument PID
	      (http://hdl.handle.net/21.T11998/0000-001A-3905-F) as
	      identifying metadata within a SensorML technical
	      description using the *sml:identifier* property for a
	      SeaBird Scientific SBE 37 Conductivity, temperature and
	      depth sensor.

      <sml:identifier>
        <sml:Term definition="http://www.example.com/definitions/pidinst/">
           <sml:label>Instrument persistent identifier</sml:label>
           <sml:value>http://hdl.handle.net/21.T11998/0000-001A-3905-F</sml:value>
        </sml:Term>
      </sml:identifier>

The list of properties that can be expressed in SensorML to describe
sensors is not particularly restrictive and it is recommended that
institutional instrument providers follow the PIDINST guidance on
landing page content (see :ref:`landing-page-content`).  Recently, the
`Marine SWE Profiles`_ initiative specified a comprehensive metadata
profile to improve the semantic interoperability of SensorML in the
Earth Science marine domain by developing sets of sensor specific
terminologies.

Content negotiation
-------------------

We recommend using content negotiation where instrument landing pages
are not easily consumed for human reading (such as XML schemas). PIDINST
does not specify the form of negotiation that produces human-readable
content from machine-readable representations. Other groups, such as the
W3C Dataset Exchange Working Group (DXWG) are currently drafting
recommendations on content negotiation from different information
models.\ [#w3_dxwg]_


.. _Marine SWE Profiles:
   https://github.com/ODIP/MarineProfilesForSWE/blob/master/docs/02_SensorML.md

.. [#ld_converters]
   as for instance: http://www.easyrdf.org/converter

.. [#w3_dxwg]
   https://www.w3.org/TR/dx-prof-conneg/#dfn-data-profile
