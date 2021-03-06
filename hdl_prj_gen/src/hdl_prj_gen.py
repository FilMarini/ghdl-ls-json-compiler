import json
import os
import argparse
import itertools


def def_ext(x):
    return {
        ".vhd": "vhdl",
        ".vhdl": "vhdl",
        ".v": "verilog",
        ".sv": "systemverilog"
    }.get(x)


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    extList = [".vhd", ".vhdl", ".v", ".sv"]
    listOfFile = os.listdir(dirName)
    allFiles = list()
    allExt = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # Retrieve file extension
        filename, file_extension = os.path.splitext(fullPath)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)[0]
            allExt = allExt + getListOfFiles(fullPath)[1]
        elif (file_extension in extList) and not (os.path.islink(fullPath)):
            allFiles.append(fullPath)
            allExt.append(def_ext(file_extension))
    return allFiles, allExt


def createJson(files, exts):
    data = {}

    data['files'] = []
    for (filename, extname) in zip(files, exts):
        data['files'].append({
            'language': extname, 'file': filename
        })

    data['options'] = {}
    data['options']['ghdl_analysis'] = []
    data['options']['ghdl_analysis'].append('--workdir=work')
    data['options']['ghdl_analysis'].append('--ieee=synopsys')
    data['options']['ghdl_analysis'].append('-fexplicit')
    return data


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action='store', dest='root_proj',
                        help='path to the root project')
    results = parser.parse_args()
    dirName = results.root_proj

    # Get the list of all files in directory tree at given path
    listOfFiles, listOfExt = getListOfFiles(dirName)
    # for item in listOfFiles:
    # print(os.path.basename(item))
    hdl_prj = createJson(listOfFiles, listOfExt)

    # Output the json
    with open(results.root_proj + '/hdl-prj.json', 'w') as outfile:
        json.dump(hdl_prj, outfile, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
