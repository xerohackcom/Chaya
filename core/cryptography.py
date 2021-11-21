from Crypto.Cipher import AES
#from Crypto.Random import get_random_bytes
#from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# Function > AES 256 GCM Encryption
def AES_256_GCM_Encrypt(secret_key, secret_message):

    # encode the key and message to utf-8
    secret_key = secret_key.encode('utf8')
    secret_message = secret_message.encode('utf8')

    # array for temp storage
    secrets = []
    
    # create cipher mode
    cipher = AES.new(secret_key, AES.MODE_GCM)
   
    # encrypt and digest
    secret_message, auth_tag = cipher.encrypt_and_digest(secret_message)
    
    # convert to Base64 and decode by UTF-8
    secret_message = b64encode(secret_message).decode('utf8')
    auth_tag = b64encode(auth_tag).decode('utf8')
    cipher_nonce = b64encode(cipher.nonce).decode('utf8')
    
    # append to secrets array
    secrets.append(secret_message)
    secrets.append(auth_tag)
    secrets.append(cipher_nonce)

    # return secrets
    return secrets


# Function > AES 256 GCM Decryption
def AES_256_GCM_Decrypt(secret_key, secret_message, auth_tag, cipher_nonce):

    # encode the key and message to utf-8
    secret_key = secret_key.encode('utf8')

    # base 64 decode the message, tag and nonce
    secret_message = b64decode(secret_message)
    auth_tag = b64decode(auth_tag)
    cipher_nonce = b64decode(cipher_nonce)

    # create cipher mode
    cipher = AES.new(secret_key, AES.MODE_GCM, cipher_nonce)

    # decrypt secret message and verify
    secret_message = cipher.decrypt_and_verify(secret_message, auth_tag)

    # convert decoded message to utf-8
    secret_message = secret_message.decode('utf8')
    
    # return the decoded secret message
    return secret_message

