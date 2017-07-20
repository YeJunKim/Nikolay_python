import ctypes

import operator 


def seek(offset):
    f.seek(offset - offset % BytesPerSector)
    f.read(offset % BytesPerSector)

f = file('\\\\.\\C:', 'rb')


print ("Jump Instruction: ", f.read(3))
print ("OEM ID: ", f.read(8))
print ("Byte Per Sector: ", f.read(2))
print ("Sectors Per Cluster: ", f.read(1))
print ("Reserved Sectors: ", f.read(2))
print ("Always 0: ", f.read(3))
print ("Unused: ", f.read(2))
print ("Media descriptor: ", f.read(1))
print ("Always 0: ", f.read(2))
print ("Sector Per Track: ", f.read(2))
print ("Number Of Heads: ", f.read(2))
print ("Hidden Sectors: ", f.read(4))
print ("Unused: ", f.read(4))
print ("Unused: ", f.read(4))
print ("Total Sectors: ", f.read(8))
print ("Logical Cluster Number For The File $MFT: ", f.read(8))
print ("Logical Cluster Number For The File $MFTMirr: ", f.read(8))
print ("Clusters per file record segment: ", f.read(4))
print ("Clusters Per Index Block: ", f.read(4))
print ("Volume Serial Number: ", f.read(8))
print ("Checksum: ", f.read(4))
print ("Boot Code And Error Message: ", f.read(426))
print ("Signature: ", f.read(2))
