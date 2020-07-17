from Crypto.Cipher import AES
import base64
import argparse

class AES_Decryptor():

    def __init__(self, IV:str, key:str, encrypted_data:str, modes_of_operations:int):
        self.IV = IV
        self.key = key
        self.encrypted_data = encrypted_data
        self.modes_of_operations = modes_of_operations
    
    def base64_decode(self):
        self.IV = base64.urlsafe_b64decode(self.IV)
        self.key = base64.urlsafe_b64decode(self.key)
        self.encrypted_data = base64.urlsafe_b64decode(self.encrypted_data)
    
    def decrypt(self) -> str:
        AES_cipher = AES.new(self.key, AES.MODE_CBC, self.IV)
        decrypted_data = AES_cipher.decrypt(self.encrypted_data)
        return decrypted_data

    def box_PKCS5Padding(self, bytes_object:bytes, block_size=16) -> bytes:
        """Block size: 128 bit / 8 => 16 bytes
        3 bytes: FDFDFD           --> FDFDFD0505050505
        7 bytes: FDFDFDFDFDFDFD   --> FDFDFDFDFDFDFD01"""
        padding_multiplier = block_size - len(bytes_object) % block_size
        padding_byte = bytes(chr(padding_multiplier), "UTF-8")
        return bytes_object + padding_multiplier * padding_byte

    def unbox_PKCS5Padding(self, byte_object) -> bytes:
        padding_multiplier = byte_object[-1]
        return byte_object[0:-padding_multiplier]

def parse():
    parser = argparse.ArgumentParser(prog="AES_decryptor", description="Decrypts AES encrypted ciphertext.")
    parser.add_argument('-i', '--iv', help="Base64 encoded format of the IV", required=True)
    parser.add_argument('-k', '--key', help="Base64 encoded format of the key", required=True)
    parser.add_argument('-c', '--ciphertext', help="Base64 encoded format of the ciphertext", required=True)
    return parser.parse_args()

def main():
    args = parse()
    AES_decryptor = AES_Decryptor(args.iv, args.key, args.ciphertext, AES.MODE_CBC)
    AES_decryptor.base64_decode()
    plaintext = AES_decryptor.decrypt()

    print(f"The decrypted text is: {plaintext.decode()}")

if __name__ == "__main__":
    main()
