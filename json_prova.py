import json
import os
'''
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # Retrieve file extension
        filename, file_extension = os.path.splitext(fullPath)
        # If entry is a directory then get the list of files in this directory
        if file_extension == ".vhd":
            allFiles.append(fullPath)
        elif os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
    return allFiles

def createJson(files):
    data = {}

    data['files'] = []
    for filename in files:
        data['files'].append({
            'language': 'vhdl', 'file': filename
        })

    data['options'] = {}
    data['options']['ghdl_analysis'] = []
    data['options']['ghdl_analysis'].append('--workdir=work')
    data['options']['ghdl_analysis'].append('--ieee=synopsys')
    data['options']['ghdl_analysis'].append('-fexplicit')
    return data

def main():

    dirName = '.';

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    #for filename in listOfFiles:
    #    print filename
    hdl_prj = createJson(listOfFiles)

    #output the json
    with open('hdl-prj.json', 'w') as outfile:
        json.dump(hdl_prj, outfile)


if __name__ == '__main__':
    main()

