# crypotography
# Simple Encryption/Decryption with Fernet

This Python script demonstrates basic symmetric encryption and decryption using the `cryptography` library's `Fernet` module.  It's a simple example to show how Fernet works.

## Description

The script performs the following actions:

1.  **Imports:** Imports the necessary modules: `os` (though not directly used in this specific code) and `cryptography.fernet.Fernet`.
2.  **Defines a message:** Sets the original message string.
3.  **Generates an encryption key:** Uses `Fernet.generate_key()` to create a new symmetric key.
    * **Important Security Warning:** The script prints this generated key.  **This is highly insecure and should NEVER be done in a production environment.** Key generation and storage are critical security concerns.
4.  **Creates a Fernet object:** Initializes a `Fernet` cipher object with the generated key.  This object is used for the encryption and decryption.
5.  **Encrypts the message:**
    * Encodes the message string into bytes using `.encode()`.
    * Encrypts the byte representation of the message using the `fernet.encrypt()` method.
6.  **Decrypts the message:**
    * Decrypts the encrypted bytes using `fernet.decrypt()`.
    * Decodes the resulting bytes back into a string using `.decode()`.
7.  **Prints the original, encrypted, and decrypted messages.**

## Prerequisites

-   **Python 3.6+** (May work on earlier 3.x versions, but not tested)
-   **Cryptography Library:** Install this using pip:

    ```bash
    pip install cryptography
    ```

## Usage

1.  **Save the script:** Save the Python code to a file (e.g., `encrypt_decrypt.py`).
2.  **Run the script:** Execute it from your terminal:

    ```bash
    python encrypt_decrypt.py
    ```

    The script will print the original message, the (insecurely displayed) generated key, the encrypted message (as bytes), and the decrypted message.

## Output Example

Original: Follow Evolve DataGenerated Key (INSECURE - DO NOT USE IN PRODUCTION): your_encryption_key_hereEncrypted: b'gAAAAAB...'  #  The encrypted message (will vary)Decrypted: Follow Evolve Data
## Security Warning - VERY IMPORTANT

**The way this script handles the encryption key is extremely insecure and is for demonstration purposes only!**

* The key is generated within the script.
* The key is printed to the console.

