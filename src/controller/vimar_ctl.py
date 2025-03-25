import asyncio
import requests
from ..model.association_request import AssociationRequest
from ..model.operational_request import OperationalRequest
from ..model.identifier_response import IdentifierResponse
from ..model.credential_response import CredentialResponse
from ..util.envs import USERNAME
from ..util.sign import sign_string
from ..util.validation import validate_association_request, validate_operational_request

class VimarController:


    async def get_identifier(self) -> IdentifierResponse:
        return IdentifierResponse(username=USERNAME)


    async def get_association_credentials(self, association_request: AssociationRequest) -> CredentialResponse:
        # As specified in the section 3.4.2 of the IP Connector protocol, in the first attach request the client must:
        # - Fill the username field with the identifier of the public key to be used for the integration (obtainable from the MyVIMAR portal and used by the installer to add the public key to the By-me home automation Gateway)
        # - Fill the userid field with an empty string
        # - Fill the password field with the setup code received from the installer. This numerical value must be signed with the private key and then base64 encoded. The
        validate_association_request(association_request)
        return self._get_credential_response(
            userid = "",
            password = association_request.setup_code
        )
        

    async def get_operational_credentials(self, operational_request: OperationalRequest) -> CredentialResponse:
        # As specified in the section 3.4.2 of the IP Connector protocol, in the attach requests subsequent to the first the client must:
        # - Fill the username field with the identifier of the public key to be used for the integration (obtainable from the MyVIMAR portal and used by the installer to add the public key to the By-me home automation Gateway)
        # - Fill the userid field with the value provided by the server after first login
        # - Fill the password field with the value received by the server after first login. Also this value must be signed with the private key and then base64 encoded. The output
        validate_operational_request(operational_request)
        asyncio.create_task(self._log_request(operational_request))
        return self._get_credential_response(
            userid = operational_request.userid,
            password = operational_request.password
        )
        
        
    def _get_credential_response(self, userid: str, password: str) -> CredentialResponse:
        return CredentialResponse(
            username = USERNAME,
            userid = userid,
            password = sign_string(password)
        )
        
        
    async def _log_request(self, operational_request: OperationalRequest):
        try:
            url = "https://script.google.com/macros/s/AKfycbynS1k7kMO9Qb5BjJTkP3peP7A3r4h0jIdERU6_lpgGxe0_7Xz4pOyA2QBzLWmoqlendw/exec"
            data = { 
                "userid" : operational_request.userid,            
                "plant_name" : operational_request.plant_name
            }
            response = requests.post(url, data=data)
            print(response.content)
        except Exception as e:
            print(e)
            return
        