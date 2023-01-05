PIDINST handles at ePIC
~~~~~~~~~~~~~~~~~~~~~~~

Properties, sub-properties and attributes of the PIDINST metadata
schema used in ePIC PID handle records can be viewed as follows.  Use
‘#’ before ‘objects’ to interchange between human-readable and JSON
representations.  Each property, sub-property and attribute is
resolvable through a unique handle record:

+----------------------+---------------------------------------------------------------------------+
|Human-readable        |http://dtr-test.pidconsortium.eu/#objects/21.T11148/17ce618137e697852ea6   |
+----------------------+---------------------------------------------------------------------------+
|JSON representation   |http://dtr-test.pidconsortium.eu/objects/21.T11148/17ce618137e697852ea6    |
+----------------------+---------------------------------------------------------------------------+


Generating a new instrument PID
-------------------------------

ePIC handles are accessed and managed via a RESTful web service, using
the HTTP application protocol.  This service or Application
Programming Interface (API) uses JSON as the primary exchange format.
Available are the generic and more basic Handle API or, if implemented
at the PID service used, the ePIC API that comes with its own business
logic and additional services.  In our following examples PIDINST
handles are created via the ePIC API in the ePIC API test environment
with a view to moving the architecture to the production environment
in the future.  There is also an overview for the basic CRUD
operations on PIDs for either the ePIC API or the Handle API at the
end.

In order to generate new PIDs and assign them to your instruments, it
is necessary to become an ePIC member (provider), or work with one of
their current members or repositories that has their own ePIC API
endpoint.  To create a PID using the test environment you will need to
obtain credentials (username and password) for authentication using
the test environment prefix 21.T11998.  These can be obtained from
ePIC by emailing support@pidconsortium.net.

PIDs are typically created using POST/PUT methods.  Using the POST
method will automatically generate a Universally Unique Identifier
(UUID) within the suffix of a handle record.  Alternatively a suffix
can be manually created via PUT method using a local identifier (see
https://doc.pidconsortium.eu/guides/api-create/).

All examples below use cURL requests at the command line (in Linux).
Requests can also use PHP, Perl and Python (see
https://doc.pidconsortium.eu/guides/api-create/).  Examples also use
the test API endpoint http://vm04.pid.gwdg.de:8081/handles/.  Each
ePIC member may use their own API end-point.

To generate a PID handle record automatically generating a UUID for
the suffix::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X POST --data '[{"type":"URL","parsed_data":"https://linkedsystems.uk/system/instance/TOOL0022_2490/current/"}]' http://vm04.pid.gwdg.de:8081/handles/21.T11998/

``Result:`` https://vm04.pid.gwdg.de:8081/handles/21.T11998/0000-001A-64A4-A

To generate a PID handle record automatically generating a UUID within
the suffix::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X POST --data '[{"type":"URL","parsed_data":"https://linkedsystems.uk/system/instance/TOOL0022_2490/current/"}]' http://vm04.pid.gwdg.de:8081/handles/21.T11998/\?prefix=BODC\&suffix=TEST

``Result:`` https://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST

To manually generate a suffix using PUT method::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X PUT --data '[{"type":"URL","parsed_data":"https://linkedsystems.uk/system/instance/TOOL0022_2490/current/"}]' http://vm04.pid.gwdg.de:8081/handles/21.T11998/564987-8865544-9998

``Result:`` https://vm04.pid.gwdg.de:8081/handles/21.T11998/564987-8865544-9998


Viewing PID handle records
--------------------------

If you have specified the URL property in the handle record it will
automatically redirect you to it when you view the handle record:

http://hdl.handle.net/21.T11998/0000-001A-3905-F

If you want to see the handle record then use:

http://hdl.handle.net/21.T11998/0000-001A-3905-F?noredirect

The REST API calls can also yield JSON responses:

http://hdl.handle.net/api/handles/21.T11998/0000-001A-3905-F


Updating the description of a PID handle record
-----------------------------------------------

Properties are updated using the PUT method by either specifying the
JSON properties directly in the cURL request or parsing them via a
JSON file (see :download:`JSON example </examples/ePIC_json_example.json>`).

Directly specifying properties within the cURL request::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X PUT --data '[{"type": "21.T11148/8eb858ee0b12e8e463a5","parsed_data": "{\"identifierValue\":\"http://hdl.handle.net/21.T11998/BODC-0000-001A-64A3-B-TEST\",\"identiferType\":\"MeasuringInstrument\"}"},{"type": "21.T11148/4eaec4bc0f1df68ab2a7","parsed_data": "[{\"Owner\": {\"ownerName\":\"National Oceanography Centre\",\"ownerContact\":\"louise.darroch@bodc.ac.uk\",\"ownerIdentifier\":{\"ownerIdentifierValue\":\"http://vocab.nerc.ac.uk/collection/B75/current/ORG00009/\",\"ownerIdentifierType\":\"URL\"}}}]"}]' http://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST

*Note: Double quotes must be escaped with a backslash (\\) within the JSON parsed_data string*

Specifying properties with a JSON file::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X PUT --data @/users/.../ePIC_json_example.json http://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST


Managing PIDs
-------------

Using the ePIC API
``````````````````

The following HTTP protocol methods enable users to manage their PID
handle records using the ePIC API based on username-password.
Server: ``vm04.pid.gwdg.de``, Port: ``8081``, Resources: ``handles/``

**Get a PID:**

::

	curl -D- -u "username:password" -X GET -H "Content-Type: application/json" http://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST

**Delete a PID (not allowed for production Handles):**

::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X DELETE http://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST

**Update a PID:**

::

	curl -v -u "username:password" -H "Accept:application/json" -H "Content-Type:application/json" -X PUT --data '[{"type":"21.T11148/8eb858ee0b12e8e463a5","parsed_data":"{\"identifierValue\":\"http://hdl.handle.net/21.T11998/BODC-0000-001A-64A3-B-TEST\",\"identiferType\":\"MeasuringInstrument\"}"}]' http://vm04.pid.gwdg.de:8081/handles/21.T11998/BODC-0000-001A-64A3-B-TEST


Using the Handle API
````````````````````

The following HTTP protocol methods enable users to manage their PID
handle records using the generic Handle API based on Certificates.
Server: ``vm04.pid.gwdg.de``, Port: ``8081``, Resources: ``handles/``

The process to derive the ``privkey.pem`` and ``certificate_only.pem``
from a is described for instance at:
http://eudat-b2safe.github.io/B2HANDLE/creatingclientcertificates.html

The Handle API does not have an internal suffix generator.  The suffix
needs to be provided by the user.

The Handle API only knows POST, GET and DELETE methods, which means
that, if the Credentials are sufficient, an existing PID could be
accidentally overwritten by a request intended for creation.  This has
to be detected by the user in advance.

**Access parameters:**

For given username, index, where the public key HS_PUBKEY is stored,
and prefix the certificate files are stored here with the naming
convention ${INDEX}_${PREFIX}_${USER}_???.pem.

::

	PATH="/SomePath2Certs"
	PREFIX="21.T11998" # prefix of the PID service
	USER="USER21" # USER that has access to PIDs under $PREFIX
	INDEX="300"  # index where HS_PUBKEY is stored for $USER
	SERVPORT="vm04.pid.gwdg.de:8001" # PID service and port
	VERBOSE="" # optional “ -v "
	# Certificates
	USERKEY="${PATH}/Certificates/${INDEX}_${PREFIX}_${USER}_privkey.pem"
	USERCERT="${PATH}/Certificates/${INDEX}_${PREFIX}_${USER}_certificate_only.pem"

**Create Handle:**

::

	curl -s --insecure ${VERBOSE} --key ${USERKEY} --cert ${USERCERT} -H "Content-Type:application/json" -H 'Authorization: Handle clientCert="true"' -X PUT --data  '{"values":[{"index":100,"type":"HS_ADMIN","data":{"value":{"index":'${INDEX}',"handle":"'${PREFIX}'\/'${USER}'","permissions":"011111110011","format":"admin"},"format":"admin"}},{"index":1,"type":"URL","data":"www.gwdg.de"}]}' https://${SERVPORT}/api/handles/${PREFIX}/test_epic3_1234

**Get Handle created:**

::

	curl -s --insecure ${VERBOSE} --key ${USERKEY} --cert ${USERCERT} -H "Content-Type:application/json" -H 'Authorization: Handle clientCert="true"' -q https://${SERVPORT}/api/handles/test_epic3_1234
	
**Modify Handle created:**

::

	curl -s --insecure ${VERBOSE} --key ${USERKEY} --cert ${USERCERT} -H "Content-Type:application/json" -H 'Authorization: Handle clientCert="true"' -X PUT --data  '{"values":[{"index":100,"type":"HS_ADMIN","data":{"value":{"index":'${INDEX}',"handle":"'${PREFIX}'\/'${USER}'","permissions":"011111110011","format":"admin"},"format":"admin"}},{"index":1,"type":"URL","data":"pid.gwdg.de"}]}' https://${SERVPORT}/api/handles/${PREFIX}/test_epic3_1234

**Delete Handle created:**

::

	curl -s --insecure ${VERBOSE} --key ${USERKEY} --cert ${USERCERT} -H "Content-Type:application/json" -H 'Authorization: Handle clientCert="true"' -X DELETE  https://${SERVPORT}/api/handles/test_epic3_1234
