import os
import struct

def readbyte(file):
    return struct.unpack('B', file.read(1))[0]

def readu16le(file):
    return struct.unpack('<H', file.read(2))[0]

def readu32le(file):
    return struct.unpack('<I', file.read(4))[0]

# Image filenames, with valid resolutions
files = {
    'iconTex.tga': [128, 128, 32],
    'bootLogoTex.tga': [170, 42, 32],
    'bootDrcTex.tga': [854, 480, 24],
    'bootTvTex.tga': [1280, 720, 24]
}

# Resolution values for dimensions
dimensions_values = ['Width', 'Height', 'Bit-depth']

valid = True
for file, dimensions in files.items():
    if not os.path.exists(file): # File wasn't found
        print(f"NOTE: '{file}' not found")
        continue
    
    with open(file, 'rb+') as f:
        header = readu32le(f)
        if header != 0x00020000: # Checking if it's compressed or not
            print(f"WARNING: '{file}' is compressed")
            valid = False

        f.seek(12)

        # Checking if the correct resolutions are matching the file's resolutions
        read_dimensions = [readu16le(f), readu16le(f), readbyte(f)]
        for i, (e1, e2) in enumerate(zip(dimensions, read_dimensions)):
            if e1 != e2:
                print(f"WARNING: {dimensions_values[i]} is incorrect on '{file}'")
                valid = False
                
        f.seek(1, 1)
        f.seek(read_dimensions[0] * read_dimensions[1] * (read_dimensions[2] // 8), 1)
        f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00TRUEVISION-XFILE\x2E\x00")

print()
if valid:
    print("All files are valid, you're good to go.")
else:
    print("One or more files have issues, please fix.")