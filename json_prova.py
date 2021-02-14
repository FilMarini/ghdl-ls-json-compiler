import json
import os
import itertools
'''
    For the given path, get the List of all files in the directory tree
'''
def def_ext(x):
    return {
        ".vhd": "vhdl",
        ".v": "verilog",
        ".sv": "systemverilog"
    }.get(x)

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
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
        elif file_extension == ".vhd" or file_extension == ".v" or file_extension == ".sv":
            allFiles.append(fullPath)
            allExt.append(def_ext(file_extension))
    return allFiles, allExt

def getListOfDir(dirname):
    l = []
    for root, dirs, files in os.walk('.'):
        if any(file.endswith('.vhd') for file in files):
            l.append(os.path.abspath(root))
    return l

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

    dirName = '.';

    # Get the list of all files in directory tree at given path
    listOfFiles, listOfExt = getListOfFiles(dirName)
    listOfDir = getListOfDir(dirName)
    #for (filename, fileext) in zip(listOfFiles, listOfExt):
        #print filename
        #print fileext
    #print "****"
    #for filename in listOfFiles:
        #print filename
    #print "****"
    #for fileext in listOfExt:
        #print fileext
    hdl_prj = createJson(listOfFiles, listOfExt)

    #output the json
    with open('hdl-prj.json', 'w') as outfile:
        json.dump(hdl_prj, outfile)

    with open('name.prj', 'w') as p:
        #set proj name
        p.write('(setq vhdl-project "Example")\n')
        p.write("(vhdl-aput 'vhdl-project-alist vhdl-project\n")
        p.write("'")
        p.write('("Source files in two directories, custom library name, VHDL')
        p.write("'")
        p.write('87" "./"\n')
        p.write('(""')
        p.write("\n")
        p.write("\n")
        for direc in listOfDir:
            p.write("\n")
            p.write('"')
            p.write(direc)
            p.write('"')
        p.write(')')
        p.write("\n")
        p.write(' ""\n')
        p.write(' (("ModelSim" "-87 \\\\2" "-f \\\\1 top_level" nil)\n')
        p.write('  ("Synopsys" "-vhdl87 \\\\2" "-f \\\\1 top_level"\n')
        p.write('   ((".*/datapath/.*" . "-optimize \\\\3")\n')
        p.write('    (".*_tb\\\\.vhd"))))\n')
        p.write(' "lib/" "example3_lib" "lib/example3/" "Makefile_\\\\2" ""))')


if __name__ == '__main__':
    main()

