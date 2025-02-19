import base64
from nacl.secret import SecretBox

SECRET_KEY = ```secret key goes here`
PAYLOAD_1 = ```enter your payload here```
PAYLOAD_2 = ```enter your payload here```

def fix_padding(b64_string: str) -> bytes:
    """Fix base64 padding according to RFC 3548 section 2.2"""
    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += '=' * (4 - missing_padding)
    return base64.b64decode(b64_string)

def decrypt_fetch_ctf():
    try:
        # Validate cryptographic inputs
        key = base64.b64decode(SECRET_KEY)
        if len(key) != 32:
            raise ValueError(f"Invalid key length: {len(key)} bytes (needs 32 bytes)")
            
        box = SecretBox(key)
        
        # Process payloads with padding correction
        payload1 = fix_padding(PAYLOAD_1)
        payload2 = fix_padding(PAYLOAD_2)
        
        # Decrypt using NaCl's proper nonce handling
        tokens = [
            *box.decrypt(payload1).decode().split(','),
            *box.decrypt(payload2).decode().split(',')
        ]
        
        print("Valid CTF Tokens:")
        for i, token in enumerate(tokens, 1):
            print(f"[TOKEN {i}] {token}")
            
    except Exception as e:
        print(f"Decryption failed: {str(e)}")
        print("Final Verification:")
        print("1. Confirm payload values EXACTLY match secretbox.md")
        print("2. Check pynacl==1.5.0: pip show pynacl")
        print("3. Validate no whitespace in base64 strings")

if __name__ == "__main__":
    decrypt_fetch_ctf()
