import os
import struct

def readbyte(file):
    return struct.unpack('B', file.read(1))[0]

def readu16le(file):
    return struct.unpack('<H', file.read(2))[0]

def readu32le(file):
    return struct.unpack('<I', file.read(4))[0]

def process_files(files: dict) -> bool:
    valid = True

    # Resolution values for dimensions
    dimensions_values = ['Width', 'Height', 'Bit-depth']

    for file, dimensions in files.items():
        # File wasn't found
        if not os.path.exists(file):
            print(f"NOTE: '{file}' not found")
            continue
        
        with open(file, 'rb+') as f:
            header = readu32le(f)
            # Checking if it's compressed or not
            if header != 0x00020000:
                print(f"WARNING: '{file}' is compressed")
                valid = False

            f.seek(12)

            # Checking if the correct resolutions are matching the file's resolutions
            read_dimensions = [readu16le(f), readu16le(f), readbyte(f)]
            for i, (e1, e2) in enumerate(zip(dimensions, read_dimensions)):
                if e1 != e2:
                    print(f"WARNING: {dimensions_values[i]} is incorrect on '{file}'")
                    valid = False

            # Skipping the image data
            f.seek(1, 1)
            f.seek(read_dimensions[0] * read_dimensions[1] * (read_dimensions[2] // 8), 1)
            # Writing the TGA footer
            f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00TRUEVISION-XFILE\x2E\x00")

    return valid

def main():
    # Image filenames, with valid resolutions
    files = {
        'iconTex.tga': [128, 128, 32],
        'bootLogoTex.tga': [170, 42, 32],
        'bootDrcTex.tga': [854, 480, 24],
        'bootTvTex.tga': [1280, 720, 24]
    }
    
    valid = process_files(files)

    if valid:
        print("\nAll files are valid, you're good to go.")
    else:
        print("\nOne or more files have issues, please fix.")

if __name__ == '__main__':
    main()