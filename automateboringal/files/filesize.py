import os

def fileSize(dir, totalSize):
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            totalSize += os.path.getsize(os.path.join(dirpath, filename))
    
    return totalSize

# As stated in the doc, os.walk generates file names in a directory tree by walking the tree top-down

dir = 'D:\\test\\DARK SOULS - Prepare To Die Edition\\DATA'
totalSize = 0
print(fileSize(dir, totalSize))


"""
# inferior
def fileSize(totalSize):
    for fileName in os.listdir('D:\\test\\DARK SOULS - Prepare To Die Edition\\DATA'):
        if not os.path.isfile(os.path.join('D:\\test\\DARK SOULS - Prepare To Die Edition\\DATA', fileName)):
            continue
        totalSize += os.path.getsize(os.path.join('D:\\test\\DARK SOULS - Prepare To Die Edition\\DATA', fileName))

totalSize = 0
print(fileSize(totalSize))
"""