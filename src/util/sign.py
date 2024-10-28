import subprocess
import base64
from .envs import PEM_PATH

NAME = __name__

def sign_string(code: str) -> str:
    private_key_pem = PEM_PATH
    return _sign_code_openssl(code, private_key_pem)    

def _sign_code_openssl(code: str, private_key_path: str) -> str:    
    # output of the signing and encoding procedure performed by the client must be equal to the output of the following command (executed in a Linux environment):
    # echo -n <SETUP-CODE/PASSWORD> | openssl pkeyutl -sign -inkey <PRIVATE-KEY> | base64 | tr -d '\n'
    command = ["openssl", "pkeyutl", "-sign", "-inkey", private_key_path]
    result = subprocess.run(
        command,
        input=code.encode('utf-8'),
        capture_output=True,
        check=True
    )

    signature = result.stdout
    signature_b64 = base64.b64encode(signature).decode('utf-8')
    return signature_b64
