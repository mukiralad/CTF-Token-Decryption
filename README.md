# 🔐 Fetch Backend CTF Token Decryption Toolkit

*A Python implementation for decrypting Fetch CTF tokens using NaCl SecretBox*

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview
This repository contains a verified solution for decrypting Fetch CTF challenge tokens using Python and the NaCl cryptography library. The implementation demonstrates proper handling of:
- Base64 encoding/decoding
- NaCl SecretBox decryption
- Cryptographic payload validation
- Error troubleshooting

## 🚀 Features
- Complete decryption workflow for 4 CTF tokens
- Padding correction for malformed base64 inputs
- Cryptographic integrity verification
- Detailed error handling
- Compatible with Python 3.10+

## ⚙️ Installation
Clone repository
```
git clone https://github.com/mukiralad/ctf-token-decryption.git
cd fetch-ctf-decryptor
```

Install dependencies

```pip install pynacl==1.5.0```

### Payload Structure
First Payload (192 bytes):
[24B nonce][168B ciphertext][16B MAC]

Second Payload (90 bytes):
[24B nonce][66B ciphertext][16B MAC]

## 🚨 Troubleshooting
**Common Errors & Solutions:**
CryptoError: Decryption failed
Cause: Incorrect nonce handling or payload corruption
Fix: Use raw payload values without manual nonce separation

ValueError: Incorrect padding
Cause: Missing base64 '=' padding characters
Fix: Our code includes automatic padding correction

ImportError: No module named 'nacl'
Solution: ```pip install pynacl==1.5.0```
