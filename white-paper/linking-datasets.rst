Linking instrument PIDs to datasets
===================================

One major purpose of PIDINST is to ease tracking the scientific output
of the instrument.  In order to benefit from this, it is important to
establish the relation between the datasets and the instrument being
used to collect the data in a machine readable way.

DataCite metadata
-----------------

Datasets are usually published with a DataCite DOI.  The `DataCite
Metadata Schema`_ allows to link the instrument from the metadata
registered with that DOI for a data publication using the
*relatedIdentifier* property.  The recommended *relationType* is
*IsCompiledBy* in this case.  :numref:`fig-link-hzb` shows an example
for a dataset published by HZB (https://doi.org/10.5442/ND000001).
The data has been collected using neutron diffraction with the E2 -
Flat-Cone Diffractometer beamline at BER II.  The image show a
screenshot of the data publication landing page which links the PID of
the instrument.  :numref:`snip-link-dataset-datacite-xml` shows a
section of the DOI metadata from the same data publication containing
this link.

.. figure:: /images/ND000001-landing.png
    :name: fig-link-hzb
    :alt: HZB dataset

    Landing page of a dataset published by HZB which links the PID of
    the instrument.

.. code-block:: XML
    :name: snip-link-dataset-datacite-xml
    :caption: Use of the relatedIdentifier property in the DOI
          metadata from a data publication.  The second entry links
          the PID of the instrument.

      <relatedIdentifiers>
        <relatedIdentifier relatedIdentifierType="DOI" relationType="References">10.17815/jlsrf-4-110</relatedIdentifier>
        <relatedIdentifier relatedIdentifierType="DOI" relationType="IsCompiledBy">10.5442/NI000001</relatedIdentifier>
        <relatedIdentifier relatedIdentifierType="DOI" relationType="IsCitedBy">10.1103/physrevb.99.174111</relatedIdentifier>
      </relatedIdentifiers>

schema.org
----------

:numref:`fig-link-pangea` shows an example of marine dataset
(https://doi.org/10.1594/PANGAEA.887579) published through PANGAEA. The
metadata of the dataset includes descriptive information about the
dataset and its related entities (e.g., scholarly article, project). The
dataset was gathered through sensors attached to an autonomous
underwater vehicle (AWI AUV Polar Autonomous Underwater Laboratory),
which was deployed as part of a cruise campaign (MSM29). The vehicle is
identified through a persistent identifier assigned by
https://sensor.awi.de/. The landing page of the instrument contains
metadata of the instrument such as description, manufacturer, model,
contact, calibration information. :numref:`fig-link-model` depicts
schema.org types and properties that may be used to model the
dataset’s observation event (e.g., cruise campaign) and instrument
deployed (AUV). :numref:`fig-link-schema-org` shows the snippet of
actual schema.org representation. External vocabularies (NERC SeaVoX
Platform Categories and GeoLink Schema) are used to indicate the
additional type for Event and Vehicle. In Schema.org, ‘Event’ refers
to an occurrence at a specific time and location, for example a social
event. As such, new types and properties are required to support the
description of observation events and related scientific instruments
to ensure full compliance with Schema.org functionality.

.. figure:: /images/image2.png
    :name: fig-link-pangea
    :alt: PANGAEA dataset

    An example of a dataset published by PANGAEA which includes its
    instrument identifier
    (https://doi.pangaea.de/10013/sensor.664525cf-45b9-4969-bb88-91a1c5e97a5b)

.. figure:: /images/image1.png
    :name: fig-link-model
    :alt: Conceptual model

    Conceptual model of Event and Specific Instrument Type (Vehicle)

.. figure:: /images/image3.png
    :name: fig-link-schema-org
    :alt: Schema.org

    Snippet of schema.org representation of event and instrument
    associated with the dataset in :numref:`fig-link-pangea`.

.. _section-1:

NetCDF4
-------

State-of-the-art research ships are multimillion-pound floating
laboratories which operate diverse arrays of high-powered,
high-resolution sensors around-the-clock (e.g. sea-floor depth, weather,
ocean current velocity and hydrography etc.). The National Oceanography
Centre (NOC)\ [#uk_noc]_ and British Antarctic Survey (BAS)\ [#uk_bas]_
are currently working together to improve the integrity of the data
management workflow from these sensor systems to end-users across the UK
National Environment Research Council (NERC) large research vessel
fleet, as part of a UK initiative, I/Ocean. In doing so, we can make
cost effective use of vessel time while improving the
FAIRness,\ [#wilkinson2016]_ and in turn, access of data from these
sensor arrays. The initial phase of the solution implements common
NetCDF formats across ships enabling harmonised access to data for
researchers on board while reducing ambiguity using common metadata
standards. The formats are based on NetCDF4 and comply with Climate
Forecast conventions. NetCDF4 groups are used to include rich
information about the instruments used to derive parameter streams. Data
streams are linked to the instruments which produced them using the
variable attribute *instrument* from Attribute Convention for Data
Discovery (ACDD) 1-3 (:numref:`snip-link-netcdf-cdl`). Each instrument
is identified as a group where their properties are expressed in
variables including the instrument’s PID. Each property is defined
using common terminologies published on the NERC Vocabulary Server. In
this way, users can express properties of their choice. Through
groups, other information relating to parameter streams or instruments
could be expressed, such as calibralibrations and instrument reference
frames and orientations.

.. code-block:: default
    :name: snip-link-netcdf-cdl
    :caption: Truncated CF-NetCDF4 CDL file. Note some terminologies
          are in development.

      netcdf iocean_example {
      dimensions:
         INSTANCE = UNLIMITED ; // (1 currently)
         MAXT = 6 ;
      variables:
         float seatemp(INSTANCE, MAXT) ;
            seatemp:_FillValue = -9.f ;
            seatemp:long_name = "sea surface temperature" ;
            seatemp:standard_name = "sea_surface_temperature" ;
            seatemp:units = "degC" ;
            seatemp:sdn_parameter_urn = "SDN:P01::TEMPHU01" ;
            seatemp:sdn_uom_urn = "SDN:P06::UPAA" ;
            seatemp:sdn_parameter_name = "Temperature of the water body by thermosalinograph hull sensor and NO verification against independent measurements" ;
            seatemp:sdn_uom_name = "Degrees Celsius" ;
            seatemp:instrument = "/instruments/SBE_2490" ;

      // global attributes:
            :_NCProperties = "version=2,netcdf=4.7.2,hdf5=1.10.5" ;
      data:

       seatemp =
        7.4809, 7.439, _, 7.403, 7.3647, 7.3497 ;

      group: instruments {
        dimensions:
         NCOLUMNS = 1 ;

        group: SBE_2490 {
          variables:
            string instrument_pid(NCOLUMNS) ;
               instrument_pid:long_name = "PIDINST PID" ;
               instrument_pid:sdn_variable_name = "TBC" ;
               instrument_pid:sdn_variable_urn = "TBC" ;
            string uuid(NCOLUMNS) ;
               uuid:long_name = "UUID" ;
               uuid:sdn_variable_name = "Universally Unique Identifier (UUID)" ;
               uuid:sdn_variable_urn = "SDN:W07::IDEN0007" ;
            string instrument_name(NCOLUMNS) ;
               instrument_name:long_name = "Instrument name" ;
               instrument_name:sdn_variable_name = "Long name" ;
               instrument_name:sdn_variable_urn = "SDN:W07::IDEN0002" ;
            string serial_number(NCOLUMNS) ;
               serial_number:long_name = "Instrument serial number" ;
               serial_number:sdn_variable_name = "Serial Number" ;
               serial_number:sdn_variable_urn = "SDN:W07::IDEN0005" ;
            string model_id(NCOLUMNS) ;
               model_id:long_name = "Model Name Identifier" ;
               model_id:sdn_variable_name = "Model name" ;
               model_id:sdn_variable_urn = "SDN:W07::IDEN0003" ;
            float accuracy_temperature(NCOLUMNS) ;
               accuracy_temperature:long_name = "Instrument accuracy of temperature" ;
               accuracy_temperature:units = "degC" ;
               accuracy_temperature:sdn_variable_name = "Accuracy" ;
               accuracy_temperature:sdn_variable_urn = "SDN:W04::CAPB0001" ;
               accuracy_temperature:variable_parameter = "/seatemp" ;
               accuracy_temperature:sdn_uom_urn = "SDN:P06::UPAA" ;
               accuracy_temperature:sdn_uom_name = "Degrees Celsius" ;

          // group attributes:
               :date_valid_from = "2020-01-31T00:00:00Z" ;
               :metadata_link = "https://linkedsystems.uk/system/instance/TOOL0022_2490/current/" ;
               :comment = "\n2020-06-26T13:29:42Z: Instrument cleaned on 2020-02-10T13:04:00Z" ;
          data:

           instrument_pid = "http://hdl.handle.net/21.T11998/0000-001A-3905-F" ;

           uuid = "TOOL0022_2490" ;

           instrument_name = "SBE 37-IM MicroCAT s/n 2490" ;

           serial_number = "2490" ;

           model_id = "http://vocab.nerc.ac.uk/collection/L22/current/TOOL0022/" ;

           accuracy_temperature = 0.002 ;
          } // group SBE_2490
        } // group instruments
      }

The National Centres for Environmental Information (NCEI) at the
National Oceanic and Atmospheric Administration (NOAA) in the US, also
report instruments in CF-NetCDF files but as empty data variables within
the root group of the NetCDF file instead of sub groups. The PID
instrument identifier may be expressed as an instrument attribute e.g.
:numref:`snip-link-pidinst-netcdf`. Ideally, blank separated lists
should be used if linking more than one instrument.

.. code-block:: default
    :name: snip-link-pidinst-netcdf
    :caption: Addition of a instrument PID attribute to NCEI CF-NetCDF
          files.

      int instrument_parameter_variable;
         instrument_parameter_variable:long_name = "" ;
         instrument_parameter_variable:comment = "" ;
         instrument_parameter_variable:instrument_pid = "" ;

OpenAIRE CERIF metadata
-----------------------

The *OpenAIRE Guidelines for CRIS Managers* [#crisguidelines2023]_ provide orientation for Research Information System (CRIS) managers
to expose their metadata in a way that is compatible with the OpenAIRE
infrastructure as well as the European Open Science Cloud (EOSC). These
Guidelines also serve as an example of a CERIF-based (Common European Research Information Format)
standard for information interchange between individual CRISs and other
research e-Infrastructures.

The metadata format described by the Guidelines are includes Equipment
which could contain Instruments as well via the `GeneratedBy property`_.

.. _snip-link-product-oaire-cerif-xml:
.. code-block:: XML
    :caption: Use of the equipment entity for an instrument in
          exposed in a product (dataset) metadata record.
          Detailed `product (dataset) example`_ at *OpenAIRE
          Guidelines for CRIS Managers repository on GitHub*.

      <GeneratedBy>
        <Equipment id="82394876">
            <Name xml:lang="en">E2 - Flat-Cone Diffractometer</Name>
            <Identifier type="DOI">https://doi.org/10.5442/NI000001</Identifier>
            <Description xml:lang="en">A 3-dimensional part of the reciprocal space can be scanned in less then five steps by combining the “off-plane Bragg-scattering” and the flat-cone layer concept while using a new computer-controlled tilting axis of the detector bank. Parasitic scattering from cryostat or furnace walls is reduced by an oscillating \"radial\" collimator. The datasets and all connected information is stored in one independent NeXus file format for each measurement and can be easily archived. The software package TVneXus deals with the raw data sets, the transformed physical spaces and the usual data analysis tools (e.g. MatLab). TVneXus can convert to various data sets e.g. into powder diffractograms, linear detector projections, rotation crystal pictures or the 2D/3D reciprocal space.</Description>
        </Equipment>
      </GeneratedBy>

The products (dataset) relates internal to the Equipment record via
the *id* attribute, eg. 82394874.  The metadata for the equipment
itself is exposed via equipment metadata record and described in the
`Equipment entity`_.

.. _snip-link-equipment-oaire-cerif-xml:
.. code-block:: XML
    :caption: Use of the equipment entity for an instrument in
          exposed in a product (dataset) metadata record.
          Detailed `equipment example`_ at *OpenAIRE Guidelines for
          CRIS Managers repository on GitHub*.

      <Equipment xmlns="https://www.openaire.eu/cerif-profile/1.2/" id="82394876">
        <Name xml:lang="en">E2 - Flat-Cone Diffractometer</Name>
        <Identifier type="DOI">https://doi.org/10.5442/NI000001</Identifier>
        <Description xml:lang="en">A 3-dimensional part of the reciprocal space can be scanned in less then five steps by combining the “off-plane Bragg-scattering” and the flat-cone layer concept while using a new computer-controlled tilting axis of the detector bank. Parasitic scattering from cryostat or furnace walls is reduced by an oscillating \"radial\" collimator. The datasets and all connected information is stored in one independent NeXus file format for each measurement and can be easily archived. The software package TVneXus deals with the raw data sets, the transformed physical spaces and the usual data analysis tools (e.g. MatLab). TVneXus can convert to various data sets e.g. into powder diffractograms, linear detector projections, rotation crystal pictures or the 2D/3D reciprocal space.</Description>
        <Owner>
          <OrgUnit id="OrgUnits/350002">
            <Acronym>HZB</Acronym>
            <Name xml:lang="de">Helmholtz-Zentrum Berlin Für Materialien Und Energie</Name>
            <Name xml:lang="en">Helmholtz-Zentrum Berlin</Name>
            <RORID>https://ror.org/02aj13c28</RORID>
          </OrgUnit>
        </Owner>
      </Equipment>


.. _DataCite Metadata Schema: https://schema.datacite.org/

.. _OpenAIRE Guidelines for CRIS Managers: https://doi.org/10.5281/zenodo.8050936

.. _GeneratedBy property: https://openaire-guidelines-for-cris-managers.readthedocs.io/en/v1.2.0/cerif_xml_product_entity.html#generatedby

.. _Equipment entity: https://openaire-guidelines-for-cris-managers.readthedocs.io/en/v1.2.0/cerif_xml_equipment_entity.html

.. _product (dataset) example: https://github.com/openaire/guidelines-cris-managers/blob/cb96b925159655adfd97fb11c4a93f3d20c8cbef/samples/openaire_cerif_xml_example_products.xml#L30

.. _equipment example: https://github.com/openaire/guidelines-cris-managers/blob/cb96b925159655adfd97fb11c4a93f3d20c8cbef/samples/openaire_cerif_xml_example_equipments.xml#L18C1-L29C17

.. [#uk_noc]
   British Oceanographic Data Centre (BODC) and National Marine
   Facilities (NMF) divisions

.. [#uk_bas]
   Uk Polar Data Centre division

.. [#wilkinson2016]
   Wilkinson, M., Dumontier, M., Aalbersberg, I. *et al.* The FAIR
   Guiding Principles for scientific data management and stewardship.
   *Sci Data* 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18

.. [#crisguidelines2023]
   Dvořák, Jan, Czerniak, Andreas, & Ivanović, Dragan. (2023). OpenAIRE
   Guidelines for CRIS Managers 1.2 (1.2.0). *Zenodo*.
   https://doi.org/10.5281/zenodo.8050936
