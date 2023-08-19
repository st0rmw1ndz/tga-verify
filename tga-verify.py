import struct
import msvcrt as m
import os

def wait():
    m.getch()
   
def readbyte(file):
    return struct.unpack('B', file.read(1))[0]
 
def readu16le(file):
    return struct.unpack('<H', file.read(2))[0]
 
def readu32le(file):
    return struct.unpack('<I', file.read(4))[0]


files = {
    'iconTex.tga': [128, 128, 32],
    'bootLogoTex.tga': [170, 42, 32],
    'bootDrcTex.tga': [854, 480, 24],
    'bootTvTex.tga': [1280, 720, 24]
}

dimensions_values = ['Width', 'Height', 'Bit-depth']

valid = True
for file, dimensions in files.items():
    if not os.path.exists(file):
        print(f"'{file}' not found")
        continue

    with open(file, 'rb+') as f:
        header = readu32le(f)
        if header != 0x00020000:
            print(f"WARNING: '{file}' is compressed")
            valid = False
            
        f.seek(12)

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


    # if dimensions != read_dimensions:
    #     print(f"WARNING: {file} has incorrect dimensions, correct dimensions are: {dimensions[0]}x{dimensions[1]} with {dimensions[2]}-bit depth")
    #     valid = False
    # print(file)
    # print(dimensions)

# for i in range(len(tgas)):
#     tga = tgas[i]
#     dimension = dimensions[i]
#     if os.path.exists(tga):
#         with open(tga,"rb+") as f:
#             header = readu32le(f)
#             if header != 0x00020000:
#                 print(tga + "is compressed. it cant be compressed!")
#                 break
#             f.seek(12)
#             actDimensions = [readu16le(f),readu16le(f),readByte(f)]
#             hasHadBadDiment = False
#             for j in range(len(actDimensions)):
#                 if j == 0:
#                     type = "width"
#                 elif j == 1:
#                     type = "height"
#                 else:
#                     type = "depth"
#                 diment = dimension[j]
#                 actDiment = actDimensions[j]
#                 if diment != actDiment:
#                     if not hasHadBadDiment:
#                         hasHadBadDiment = True
#                         print("dimensions are not valid for: " + tga)
#                     print(type + " is: " + str(actDiment) + " should be: " + str(diment))
#             if hasHadBadDiment:
#                 break
#             f.seek(1,1)
#             f.seek(actDimensions[0]*actDimensions[1]*(actDimensions[2]//8),1)
#             f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00TRUEVISION-XFILE\x2E\x00")
#     else:
#         print(tga + " could not be found!")
# print("All TGA's verified!")
# print("Press any key to exit...")
# #todo verifiy bootovie.h264
# wait()