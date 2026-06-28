import os
import zlib

def load_compile(filename):
    with open(filename, "rb") as f:
        comp = f.read()
    return zlib.decompress(comp)

print("\033c\033[47;31m")
print("Give me a compile file (.rtfcx)?")
a = input().strip()

if not os.path.isfile(a):
    print("File not found.")
    exit()

# Nome do bitmap recuperado
b = os.path.splitext(a)[0] + "_s.rtf"

# Descomprime
bitmap = load_compile(a)

# Grava o bitmap
with open(b, "wb") as f:
    f.write(bitmap)

print("rtf restored as:", b)