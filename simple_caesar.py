# This is a very simple (or rather banal) implementation of the regular cesar cipher encryption

import random

def cesar(plain_text, key):
  #...using the ASCII range
  # key = random.randint(1, 25)
  cipher_text = ''
  for i in plain_text:
    cipher_text += ((ord(i) + key) if (ord(i) + key) <= 127 else (ord(i) + key) % 127)
    
# BE BACK LATER...
