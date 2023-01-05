.. _pidinst-metadata-schema:

PIDINST metadata schema
=======================

The metadata that is to be registered with an instrument PID needs to
contain enough information to unambiguously identify the
instrument across networks and infrastructures. It should also allow
linking related resources to the instrument, thus providing a means
to aggregate information about the instrument. The PIDINST working group defined 
a schema of metadata that can be registered alongside instrument PIDs at 
PID providers to help meet these criteria. Version 1.0 has been endorsed
as an RDA recommendation\ [#pidinst2022v1_0]_.

Currently, two variants of the metadata schema exist.  The original
`PIDINST schema`_, based on the evaluation of use cases collected by
the working group, is used for prototypical implementation of metadata
properties in the ePIC infrastructure.  A second variant provides a
`mapping between PIDINST metadata properties and DataCite Metadata
Schema 4.3 <PIDINST DataCite schema_>`_.  In the following, we
describe the properties in the original PIDINST schema and discuss
their semantics:

`Identifier`
  The PID of the instrument.  The subproperty
  `identifierType` contains the type of the PID, e.g. `Handle` or
  `DOI` in the case of an ePIC Handle or a DataCite DOI respectively.

`SchemaVersion`
  The version number of the PIDINST schema used to create a record.

`LandingPage`
  The URL of the landing page that the PID resolves to.

`Name`
  The name by which this instrument is known.  It should preferably be
  meaningful and unique within the organization that manages it.

`Owner`
  The organization or individual that manages the instrument.  This
  may or may not be the legal owner.  It could also be an organization
  that hosts or operates the instrument, manages its deployment, or
  provides access to it.  In case of doubt, it would be the instance
  that a potential user would reach out to in order to get access.
  There may be more then one owner registered in the metadata.

  `Owner` is a complex property having at least the subproperty
  `ownerName` and optionally a contact address in `ownerContact` and a
  common identifier of the owner in `ownerIdentifier` and its type in
  `ownerIdentifierType`.

`Manufacturer`
  The organization or individual that built the instrument.  In the
  case of an off the shelf product, this will probably be a commercial
  company that put the instrument on the market.  In the case of an
  custom built instrument, the manufacturer may be the same as the
  owner.  In the latter case, they would be registered as both, owner
  and manufacturer.  In case of doubt, the manufacturer would be the
  instance that defined the technical specification of the instrument.
  Again, there may be more then one manufacturer registered in the
  metadata.

  In the same way as `Owner`, `Manufacturer` is a complex property
  with subproperties `manufacturerName`, `manufacturerIdentifier` and
  `manufacturerIdentifierType`.

`Model`
  The name of the model or type of the instrument.  In the
  case of an off the shelf product, this may be a brand name
  attributed by the manufacturer.  In the case of a custom built
  instrument, it may not have a model name.  Hence this property is
  not mandatory, but recommended if the value can be obtained.  `Model` has
  optional subproperties `modelIdentifier` and `modelIdentifierType` to be used 
  if an identifier for the model is known.

`Description`
  A textual description of the device and its capabilities.  This is
  mostly targeted to a human reader and should provide a notion of
  what this instrument is and what it can do.

`InstrumentType`
  A classification of the type of the instrument.  Hierarchical 
  classification enables grouping of instrument records.

  In the same way as `Owner`, `Manufacturer` and `Model`, `InstrumentType` is 
  a complex property with subproperties `instrumentTypeName`, 
  `instrumentTypeIdentifier` and `instrumentTypeIdentifierType`.

`MeasuredVariable`
  The variables or physical properties that the instrument measures or
  observes. Some communities have established terminologies 
  to identify measured variables that are specific to their respective domain 
  (see :ref:`pidinst-metadata-schema-terminologies`).  If such a 
  standard is applicable, it should be used for for `MeasuredVariable`.
  Otherwise, a textual description may be used.

`Date`
  Relevant events pertaining to this instrument instance, such as when
  it has started and ended to be in operation.  Each `Date` need to
  have a `dateType` subproperty to specify the nature of the event.

`RelatedIdentifier`
  This can be used to establish links to related resources, such as
  documents describing the instrument or external metadata records,
  possibly using other metadata standards to provide more details
  about the instrument.

  Another application might be, if an instrument has been
  substantially modified, it would make sense to issue a new PID for
  the modified instrument with a new metadata record.  In this case
  both PIDs should relate to each other to indicate that one is a new
  version of the other.

  Furthermore, in the case of a complex instrument, it can make sense
  to issue PIDs for individual components, such as an individual
  detector in a larger experimental station.  In this case, the
  relation between the complex instrument and its components should be
  established by creating links between the respective PIDs.

  The links established using this property are particuarly useful as
  they allow the automatic aggregation of a rich set of information
  about the instrument.  Each `RelatedIdentifier` needs to have
  subproperties `relatedIdentifierType` and `relationType` to specify
  the type of the related identifier and the type of the relation
  respectively.

`AlternateIdentifier`
  If the instrument instance is also registered elsewhere, aside from
  the persistent identifier, `AlternateIdentifier` is the place to
  store a reference to these register entries.  Common use cases are
  the serial number attributed by the manufacturer or inventory number
  used by the owner.  But also other instrument databases or access
  portals may hold an entry for the instrument that should be
  referenced from the PIDINST metadata.

  The subproperty `alternateIdentifierType` needs to specify the kind
  of the alternate identifier.  Standardized values should be used
  where applicable.  For serial and inventory numbers, the suggested
  values are `serialNumber` and `inventoryNumber` respectively.

.. _PIDINST schema:
   https://github.com/rdawg-pidinst/schema/blob/master/schema.rst

.. _PIDINST DataCite schema:
   https://github.com/rdawg-pidinst/schema/blob/master/schema-datacite.rst

.. [#pidinst2022v1_0]
   Krahl, R., Darroch, L., Huber, R., Devaraju, A., Klump, J., Habermann, T., 
   Stocker, M., & The Research Data Alliance Persistent Identification of 
   Instruments Working Group members (2022). Metadata Schema for the 
   Persistent Identification of Instruments (1.0). Research Data Alliance. 
   DOI: https://doi.org/10.15497/RDA00070
