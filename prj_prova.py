import json
import os
import itertools

def getListOfDir(dirname):
    l = []
    for root, dirs, files in os.walk('.'):
        if any(file.endswith('.vhd') for file in files):
            l.append(os.path.abspath(root))
    return l

def main():

    dirName = '.';

    # Get the list of all files directories with .vhd files
    listOfDir = getListOfDir(dirName)

    #create prj file
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

