import string

LOWERCASE_OFFSET = ord("a")               # 97 offset
ALPHABET = string.ascii_lowercase[:16]    # first 16 letters of

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))       # convert to binary
		enc += ALPHABET[int(binary[:4], 2)]     # converts first 4 bits of string to base 2
		enc += ALPHABET[int(binary[4:], 2)]		# converts bits after 4th to base 2
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
