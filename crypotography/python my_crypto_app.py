import os
from cryptography.fernet import Fernet

message = "Follow Evolve Data"
print("Original:", message)

# Generate a new encryption key (for demonstration purposes ONLY)
key = Fernet.generate_key()
print("Generated Key (INSECURE - DO NOT USE IN PRODUCTION):", key.decode())

# Create a Fernet cipher object using the key
fernet = Fernet(key)

# Ensure the message is encoded to bytes before encryption
message_bytes = message.encode()
encrypted_message = fernet.encrypt(message_bytes)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message_bytes = fernet.decrypt(encrypted_message)
# Decode the decrypted bytes back to a string
decrypted_message = decrypted_message_bytes.decode()
print("Decrypted:", decrypted_message)

