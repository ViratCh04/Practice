import os

pathh = 'C:\\Users\\USER\\Desktop\\Coding'
for folderName, subFolders, fileNames in os.walk(pathh):            # os.walk(path) returns three different values on each iteration, naming each and every subfolder inside the main folder iteration by iteration
    print('The Folder name is ' + folderName)
    print('Subfolders in folder ' + folderName + ' are ' + str(subFolders))
    print('Subfolders in folder ' + folderName + ' are ' + str(fileNames))
