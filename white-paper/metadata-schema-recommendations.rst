.. _pidinst-metadata-schema-recommendations:

Recommendations using the PIDINST metadata schema
=================================================

We recommend that an instrument’s associated metadata is published in
a common language, specifically US English to enable its reuse.  In
the following section, we provide advanced recommendations on how to
specify the values in the PIDINST metadata and discuss special cases.

.. _pidinst-metadata-schema-terminologies:

Using common terminologies
--------------------------

Common terminologies such as controlled vocabularies, taxonomies or
ontologies, are sets of standardised terms that solve the problem of
ambiguities associated with metadata markup and enable records to be
shared and interpreted semantically by computers.  Many terminologies
exist, covering a broad spectrum of disciplines and their best
practices.  The PIDINST schema is designed to complement
multidisciplinary best practices for property values.  Many properties
allow for soft-typing (e.g., *ownerName*), giving users the ability to
use values of their choice, such as free text or domain-specific
terminologies.  Property attributes enable users and machines to
understand the context of the value (e.g., *ownerIdentifier*,
*ownerIdentifierType*), again using free text or standardised
terminologies.  While free text is allowed, institutions should
consider using common terminologies where practical to enhance the
(semantic) interoperability of PID records, particularly where they
form part of domain-specific best practice.  For example, a
comprehensive set of terminologies that describe *instrumentType* (via
*instrumentTypeIdentifier*) or *Model* (via *modelIdentifier*) are
used widely in the Earth science marine domain
(`http://vocab.nerc.ac.uk/collection/L22/current/ <http://vocab.nerc.ac.uk/collection/L22/current/>`_,
`http://vocab.nerc.ac.uk/collection/L05/current/ <http://vocab.nerc.ac.uk/collection/L05/current/>`_).
An example of the use of common terminologies in ePIC records is shown
in :numref:`tab-schema-handle-record`.

.. table:: Handle record of instrument identifier
	   http://hdl.handle.net/21.T11998/0000-001A-3905-F displaying
	   the use of common terminologies to identify instrument
	   metadata compliant with the PIDINST schema as implemented
	   by ePIC.  The terminologies used are published on the `NERC
	   Vocabulary Server (NVS) <NVS_>`_.  The data for each
	   metadata property is provided in JSON.  The Handle record
	   can be viewed at
	   http://hdl.handle.net/21.T11998/0000-001A-3905-F?noredirect
    :name: tab-schema-handle-record
    :class: longtable

    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | Type                               | Data                                                                                                         |
    +====================================+==============================================================================================================+
    | URL                                | .. code-block:: JSON                                                                                         |
    |                                    |                                                                                                              |
    |                                    |     "https://linkedsystems.uk/system/instance/TOOL0022_2490/current/"                                        |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/8eb858ee0b12e8e463a5   | .. code-block:: JSON                                                                                         |
    | | (Identifier)                     |                                                                                                              |
    |                                    |     {                                                                                                        |
    |                                    |       "identifierValue":"http://hdl.handle.net/21.T11998/0000-001A-3905-F",                                  |
    |                                    |       "identifierType":"Handle"                                                                              |
    |                                    |     }                                                                                                        |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/f5e68cc7718a6af2a96c   | .. code-block:: JSON                                                                                         |
    | | (SchemaVersion)                  |                                                                                                              |
    |                                    |     "1.0"                                                                                                    |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/9a15a4735d4bda329d80   | .. code-block:: JSON                                                                                         |
    | | (LandingPage)                    |                                                                                                              |
    |                                    |     "https://linkedsystems.uk/system/instance/TOOL0022_2490/current/"                                        |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/709a23220f2c3d64d1e1   | .. code-block:: JSON                                                                                         |
    | | (Name)                           |                                                                                                              |
    |                                    |     "Sea-Bird SBE 37-IM MicroCAT C-T Sensor"                                                                 |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/4eaec4bc0f1df68ab2a7   | .. code-block:: JSON                                                                                         |
    | | (Owners)                         |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "owner": {                                                                                             |
    |                                    |         "ownerName":"National Oceanography Centre",                                                          |
    |                                    |         "ownerContact":"louise.darroch@bodc.ac.uk",                                                          |
    |                                    |         "ownerIdentifier":{                                                                                  |
    |                                    |           "ownerIdentifierValue":                                                                            |
    |                                    |             "http://vocab.nerc.ac.uk/collection/B75/current/ORG00009/",                                      |
    |                                    |           "ownerIdentifierType":"URL"                                                                        |
    |                                    |         }                                                                                                    |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/1f3e82ddf0697a497432   | .. code-block:: JSON                                                                                         |
    | | (Manufacturers)                  |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "manufacturer":{                                                                                       |
    |                                    |         "manufacturerName":"Sea-Bird Scientific",                                                            |
    |                                    |         "manufacturerIdentifier":{                                                                           |
    |                                    |           "manufacturerIdentifierValue":                                                                     |
    |                                    |             "http://vocab.nerc.ac.uk/collection/L35/current/MAN0013/",                                       |
    |                                    |           "manufacturerIdentifierType":"URL"                                                                 |
    |                                    |         }                                                                                                    |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/c1a0ec5ad347427f25d6   | .. code-block:: JSON                                                                                         |
    | | (Model)                          |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "modelName":"Sea-Bird SBE 37 MicroCat IM-CT with optional pressure (submersible) CTD sensor series",   |
    |                                    |       "modelIdentifier":{                                                                                    |
    |                                    |         "modelIdentifierValue":                                                                              |
    |                                    |           "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0022/",                                        |
    |                                    |         "modelIdentifierType":"URL"                                                                          |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/55f8ebc805e65b5b71dd   | .. code-block:: JSON                                                                                         |
    | | (Description)                    |                                                                                                              |
    |                                    |     "A high accuracy conductivity and temperature recorder with an optional                                  |
    |                                    |     pressure sensor designed for deployment on moorings. The IM model has an                                 |
    |                                    |     inductive modem for real-time data transmission plus internal flash memory                               |
    |                                    |     data storage."                                                                                           |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/f76ad9d0324302fc47dd   | .. code-block:: JSON                                                                                         |
    | | (InstrumentType)                 |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "instrumentTypeName":"water temperature sensor",                                                       |
    |                                    |       "instrumentTypeIdentifier":{                                                                           |
    |                                    |         "instrumentTypeIdentifierValue":                                                                     |
    |                                    |           "http://vocab.nerc.ac.uk/collection/L05/current/134/",                                             |
    |                                    |         "instrumentTypeIdentifierType":"URL"                                                                 |
    |                                    |       }                                                                                                      |
    |                                    |     },{                                                                                                      |
    |                                    |       "instrumentTypeName":"salinity sensor",                                                                |
    |                                    |       "instrumentTypeIdentifier":{                                                                           |
    |                                    |         "instrumentTypeIdentifierValue":                                                                     |
    |                                    |           "http://vocab.nerc.ac.uk/collection/L05/current/350/",                                             |
    |                                    |         "instrumentTypeIdentifierType":"URL"                                                                 |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |                    
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/72928b84e060d491ee41   | .. code-block:: JSON                                                                                         |
    | | (MeasuredVariables)              |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "measuredVariable":{                                                                                   |
    |                                    |         "variableMeasured":                                                                                  |
    |                                    |           "http://vocab.nerc.ac.uk/collection/P01/current/CNDCPR01/"                                         |
    |                                    |       }                                                                                                      |
    |                                    |     },{                                                                                                      |
    |                                    |       "measuredVariable":{                                                                                   |
    |                                    |         "variableMeasured":                                                                                  |
    |                                    |           "http://vocab.nerc.ac.uk/collection/P01/current/PSALPR01/"                                         |
    |                                    |       }                                                                                                      |
    |                                    |     },{                                                                                                      |
    |                                    |       "measuredVariable":{                                                                                   |
    |                                    |         "variableMeasured":                                                                                  |
    |                                    |           "http://vocab.nerc.ac.uk/collection/P01/current/TEMPPR01/"                                         |
    |                                    |       }                                                                                                      |
    |                                    |     },{                                                                                                      |
    |                                    |       "measuredVariable":{                                                                                   |
    |                                    |         "variableMeasured":                                                                                  |
    |                                    |           "http://vocab.nerc.ac.uk/collection/P01/current/PREXMCAT/"                                         |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/22c62082a4d2d9ae2602   | .. code-block:: JSON                                                                                         |
    | | (Dates)                          |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "date":{                                                                                               |
    |                                    |         "dateValue":"1999-11-01",                                                                            |
    |                                    |         "dateType":"Commissioned"                                                                            |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/eb3c713572f681e6c4c3   | .. code-block:: JSON                                                                                         |
    | | (AlternateIdentifiers)           |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "alternateIdentifier":{                                                                                |
    |                                    |         "alternateIdentifierValue":"2490",                                                                   |
    |                                    |         "alternateIdentifierType":"serialNumber"                                                             |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+
    | | 21.T11148/178fb558abc755ca7046   | .. code-block:: JSON                                                                                         |
    | | (RelatedIdentifiers)             |                                                                                                              |
    |                                    |     [{                                                                                                       |
    |                                    |       "relatedIdentifier":{                                                                                  |
    |                                    |         "relatedIdentifierValue":                                                                            |
    |                                    |           "https://www.bodc.ac.uk/data/documents/nodb/pdf/37imbrochurejul08.pdf",                            |
    |                                    |         "relatedIdentifierType": "URL",                                                                      |
    |                                    |         "relationType":"IsDescribedBy "                                                                      |
    |                                    |       }                                                                                                      |
    |                                    |     }]                                                                                                       |
    +------------------------------------+--------------------------------------------------------------------------------------------------------------+

Using other PIDs
----------------

The PIDINST metadata may contain references to related entities at
various places.  Obviously, these references should preferably use
persistent identifiers whenever applicable.  Different types of PIDs
are recommended depending on the nature of the referenced entity.  The
most common cases are:

+ other instruments may be referenced in several cases.  The most
  common PID types are Handles and DOIs here.

+ organizations that may appear as owner or manufacturer may be
  referenced using a `ROR`_.

+ the most common PID for individuals that may appear as owner or
  manufacturer is the `ORCID`_ iD.

+ the `RRID`_ is common in the biological sciences and may be used to
  reference a class of instruments, see next subsection.


RRIDs
~~~~~

In a similar way to common terminologies, persistent identifiers have
been created to help users classify and accurately describe physical
objects.  The research resource identifier (RRID) can be used to
identify classes of instruments (models) and is thus related to
PIDINST, which identifies instrument instances.\ [#bandrowski2016]_
This work is undertaken by the `UsedIT`_ group, which is extending the
RRID to instrument classes that could be used to describe the *Model*
(via *modelIdentifier*) property (:numref:`tab-schema-use-rrid`).
RRIDs are not described in detail here, but it is envisioned that the
RRID metadata schema, which was described in detail
previously,\ [#bandrowski2012]_ and extended by UsedIT, will be
interoperable with instrument instance (PIDINST) PIDs.  This
interoperability should enable any project to quickly download data
about the model to consistently fill mapped fields.

Why RRIDs? RRIDs are currently used in about 1000 journals to tag
classes of research resources (including reagents like antibodies or
plasmids, organisms, cell lines, and a relatively broad category of
“tools” which includes software tools and services such as university
core facilities, but recently has been extended to physical tools such
as models of sequencers or microscopes).  Because RRIDs were created
as an agreement between a group of biological journals and the
National Institutes of Health, they are most commonly found and linked
in the biological sciences literature (e.g., Cell, eLife), they are
part of the JATS NISO standard, STAR Methods, and the MDAR
pan-publisher reproducibility checklist, resolved by identifiers.org
and the n2t resolver and echoed by some of the major reagent providers
(e.g., Thermo Fisher, Addgene, and the MMRRC mouse repository).

.. table:: Example showing the use of RRIDs in the PIDINST metadata schema.
    :name: tab-schema-use-rrid

    +----------+------------------------+---------------+---------+----------------------------------------------------+--------------------------------------------+
    |          |                        |               |         |                                                    |                                            |
    | ID       | Property               | Obligation    | Occ.    | Definition                                         | Allowed values, constraints, remarks       |
    +==========+========================+===============+=========+====================================================+============================================+
    |          |                        |               |         |                                                    |                                            |
    | 6        | Model                  | R             | 0-1     | Name of the model or type of device as attributed  | Element                                    |
    |          |                        |               |         | by the manufacturer                                |                                            |
    +----------+------------------------+---------------+---------+----------------------------------------------------+--------------------------------------------+
    |          |                        |               |         |                                                    |                                            |
    | 6.1      | modelName              | R             | 1       | Full name of the model                             | Name field from RRID                       |
    |          |                        |               |         |                                                    |                                            |
    |          |                        |               |         |                                                    | E.g.                                       |
    |          |                        |               |         |                                                    |                                            |
    |          |                        |               |         |                                                    | ‘Illumina HiSeq 3000/HiSeq 4000 System’    |
    +----------+------------------------+---------------+---------+----------------------------------------------------+--------------------------------------------+
    |          |                        |               |         |                                                    |                                            |
    | 6.2      | modelIdentifier        | O             | 0-1     | Persistent identifier of the model                 | RRID identifier                            |
    |          |                        |               |         |                                                    |                                            |
    |          |                        |               |         |                                                    | E.g.                                       |
    |          |                        |               |         |                                                    |                                            |
    |          |                        |               |         |                                                    | ‘RRID:SCR_016386’                          |
    +----------+------------------------+---------------+---------+----------------------------------------------------+--------------------------------------------+
    |          |                        |               |         |                                                    |                                            |
    | 6.2.1    | modelIdentifierType    | O             | 1       | Type of the identifier                             | Free text; must be identifier type         |
    |          |                        |               |         |                                                    |                                            |
    |          |                        |               |         |                                                    | E.g. ‘RRID’                                |
    +----------+------------------------+---------------+---------+----------------------------------------------------+--------------------------------------------+

Dealing with unknown information
--------------------------------

There are situations where it is not possible or not appropriate to
provide some piece of information that should normally be present in
the metadata.  This may for instance happen, if this information is
simply unknown, if a property has not or not yet been assigned a
value, or if it is not appropriate to disclose some piece of
information.  As an example for the latter case, consider a person
that contributes measurements to a citizen science project, but who
prefers to remain anonymous for privacy reasons.  That person might
not want to be named as the owner of the instrument taking the data.

In all these cases it is still useful to make it at least explicit
that this information has not been omitted inadvertently and also to
give a reason why it is missing.  For this purpose, PIDINST adopts the
*standard values for unknown information* from DataCite, see Appendix
3 in the DataCite Metadata Schema Documentation.\ [#datacite2019]_

.. code-block:: XML
    :name: snip-schema-unknown-xml
    :caption: Encoding unknown values in the instrument PID metadata using XML

      <name>:tba</name>
      <owners>
         <owner>
            <ownerName>:unal</ownerName>
         </owner>
      </owners>
      <manufacturers>
         <manufacturer>
            <manufacturerName>:unav</manufacturerName>
         </manufacturer>
      </manufacturers>

:numref:`snip-schema-unknown-xml` demonstrates the use of standard
values for unknown information in the metadata of an instrument PID.
It shows an instrument that has not yet been assigned a name, e.g. it
may be assumed that the metadata record will be updated at a later
point in time including a name.  The owner of the instrument is
refused to be disclosed and the manufacturer is not known.

.. _NVS:
   https://www.bodc.ac.uk/resources/products/web_services/vocab/

.. _ROR: https://ror.org/

.. _ORCID: https://orcid.org/

.. _RRID: https://www.rrids.org/

.. _UsedIT:
   http://myweb.fsu.edu/aglerum/usedit/usedit-about.html

.. [#bandrowski2016]
   Bandrowski A, Brush M, Grethe JS, Haendel MA, Kennedy DN, Hill S, Hof
   PR, Martone ME, Pols M, Tan SC, Washington N, Zudilova-Seinstra E,
   Vasilevsky N. `The Resource Identification Initiative: A Cultural
   Shift in Publishing. <https://pubmed.ncbi.nlm.nih.gov/26599696/>`__ J
   Comp Neurol. 2016 Jan 1;524(1):8-22.
   https://doi.org/10.1002/cne.23913

.. [#bandrowski2012]
   Bandrowski AE, Cachat J, Li Y, Müller HM, Sternberg PW, Ciccarese P,
   Clark T, Marenco L, Wang R, Astakhov V, Grethe JS, Martone ME. A
   hybrid human and machine resource curation pipeline for the
   Neuroscience Information Framework. Database (Oxford). 2012 Mar
   20;2012:bas005. https://doi.org/10.1093/database/bas005

.. [#datacite2019]
   DataCite Metadata Working Group (2019).  DataCite Metadata Schema
   Documentation for the Publication and Citation of Research Data.
   Version 4.3.  DataCite e.V.  https://doi.org/10.14454/7xq3-zf69
