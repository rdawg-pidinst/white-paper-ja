Dealing with duplication
========================

Duplication between identifier records is not a new problem and is
common to many applications (e.g. bibliographic, medical records).
While PIDINST identifiers are considered globally persistent it is
accepted that duplication may occur particularly where institutions
loan instruments to other organisations or provide access to
specialised facilities (e.g. large scale synchrotrons, medical
laboratories, computational facilities).  Such duplication may lead to
inaccurate statistics or reporting about instrument assets.

It is recommended that owners of instruments try to employ workflows
and procedures that avoid duplication in the first instance.  Where
this has not been possible, it is recommended that instrument owners
employ deduplication, effectively merging duplicate records into one
representative record by ensuring links between them.  This can be
achieved using the PIDINST metadata schema *relatedIdentifier*
property with a *relationType* attribute *IsIdenticalTo* as shown in
:numref:`snip-dub-merge-xml` and :numref:`%s <snip-dub-merge-json>`.

.. code-block:: XML
    :name: snip-dub-merge-xml
    :caption: Merging duplicate instrument PID records using XML

      <relatedIdentifiers>
         <relatedIdentifier relatedIdentifierType="DOI" relationType="IsIdenticalTo">10.4232/10.CPoS-2013-02en</relatedIdentifier>
      </relatedIdentifiers>

.. code-block:: JSON
    :name: snip-dub-merge-json
    :caption: Merging duplicate instrument PID records using JSON

    [{
      "RelatedIdentifier":{
        "RelatedIdentifierValue":"10.4232/10.CPoS-2013-02en",
        "RelatedIdentifierType": "DOI",
        "relationType":"IsIdenticalTo"
      }
    }]

Recent advances in technologies are expanding to algorithms that
automatically detect and resolve deduplication.  While such
methodologies have been known to improve the efficiency of detection
in large collections such as Google Scholar or `OpenAIRE Graph`_,
algorithms may be limited by heterogeneous representations for
example, by the use of differing semantics.  While automatic detection
is encouraged, the PIDINST schema is designed to complement
multidisciplinary best practices for property values and many
properties allow for soft-typing, giving users the ability to use
values of their choice, such as free text or domain-specific
standards.


.. _OpenAIRE Graph: https://graph.openaire.eu
