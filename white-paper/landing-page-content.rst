.. _landing-page-content:

Landing page content
====================

It is recommended that instrument providers use enough information
(metadata) on landing pages to unambiguously identify the instrument.
Ideally, landing pages should include the metadata specified in the
schema for PID providers and use common terminology where practical to
aid interoperability (see :ref:`pidinst-metadata-schema-terminologies`).
Institutions should also consider providing links to the metadata record
that accompanies PIDs published at PID providers to aid metadata
exchange (e.g. DataCite XML).

:numref:`Tables %s <tab-landing-content-inst>` and
:numref:`%s <tab-landing-content-events>` provide recommendations for
some additional, more descriptive metadata that can be published on
landing pages. Together with the PIDINST metadata schema, they are
designed to complement the administration and discovery of
instruments; to enable users to put data into context; and to automate
instrument metadata into data workflows.

.. table:: Descriptive landing page metadata describing measuring
           instruments. To be used in conjunction with the core
           instrument metadata used in the PIDINST schema.
    :name: tab-landing-content-inst

    +-------------------+-------------------------------------------------+
    | **Metadata type** | **Comments**                                    |
    +===================+=================================================+
    | Model version     | A variant of an instrument model. While the     |
    |                   | design of an instrument remains largely the     |
    |                   | same, variants are available with minor changes |
    |                   | to suit different applications. For example, an |
    |                   | instrument may be available with different      |
    |                   | housing material from the standard design,      |
    |                   | allowing the instrument to be used in more      |
    |                   | dynamic environments such as extreme pressures  |
    |                   | or weather conditions.                          |
    +-------------------+-------------------------------------------------+
    | Documents         | Descriptive or supporting documentation such as |
    |                   | manuals, data sheets, scientific references     |
    |                   | etc.                                            |
    +-------------------+-------------------------------------------------+
    | Classifications   | Properties that categorise instruments. In      |
    |                   | addition to instrument type, these properties   |
    |                   | can describe aspects such as the intended       |
    |                   | applications, operating principles, whether the |
    |                   | instrument is a compound instrument or a        |
    |                   | component etc.                                  |
    +-------------------+-------------------------------------------------+

.. table:: Descriptive, landing page metadata that describes the
           history of events, operations or changes during the
           lifetime of an instrument. This kind of metadata should be
           associated to dates and ideally accompanied by comments. To
           be used in conjunction with the core instrument metadata
           used in the PIDINST schema.
    :name: tab-landing-content-events

    +--------------------+------------------------------------------------+
    | **Metadata type**  | **Comments**                                   |
    +====================+================================================+
    | Calibrations       | Many instruments are calibrated to convert raw |
    |                    | outputs to meaningful units or to correct for  |
    |                    | data uncertainty. It is highly recommended to  |
    |                    | store the calibration date and type. It may    |
    |                    | also be useful to store the coefficients,      |
    |                    | algorithm used and calibration certificates.   |
    +--------------------+------------------------------------------------+
    | Capabilities       | Capabilities are properties that further       |
    |                    | quantify or qualify an instrument’s outputs    |
    |                    | (e.g. detection limits, accuracy, precision,   |
    |                    | operating ranges etc.).                        |
    +--------------------+------------------------------------------------+
    | Characteristics    | Properties that describe features and          |
    |                    | qualities belonging to an instrument. (e.g.    |
    |                    | weight, size, housing material, components,    |
    |                    | firmware etc.).                                |
    +--------------------+------------------------------------------------+
    | Servicing          | Descriptions of maintenance procedures carried |
    |                    | out on the instrument.                         |
    +--------------------+------------------------------------------------+
    | Funding references | Identifiers or names of funding resources      |
    +--------------------+------------------------------------------------+
    | Ownership dates    | Ownership start and end dates                  |
    +--------------------+------------------------------------------------+
