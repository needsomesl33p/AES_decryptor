# AES_decryptor

It only works with `CBC` block cipher operation mode. Also IV have to be provided.

## Usage:

```
usage: AES_decryptor [-h] -i IV -k KEY -c CIPHERTEXT

Decrypts AES encrypted ciphertext.

optional arguments:
  -h, --help            show this help message and exit
  -i IV, --iv IV        Base64 encoded format of the IV
  -k KEY, --key KEY     Base64 encoded format of the key
  -c CIPHERTEXT, --ciphertext CIPHERTEXT
                        Base64 encoded format of the ciphertext
```

## Example:

```
python3 AES_decryptor.py -i tLUEC-mFLZc2cOePjn1dkA== -k 9_HyqVNkXbAP3-CL5wIzzgy63xoYymaZl206TQD-Ijw= -c JyXZ5YCUhwxquDzKurjUabuU-hY7auO7GwZu1Ypn5P8=
```


## Output:

```
The decrypted text is: api-key-0558453465
```
