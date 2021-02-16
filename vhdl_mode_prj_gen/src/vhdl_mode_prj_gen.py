import os
import itertools
import argparse


def getListOfDir(dirname):
    listDirs = []
    for root, dirs, files in os.walk('.'):
        if any(file.endswith('.vhd') for file in files):
            listDirs.append(os.path.abspath(root))
    return listDirs


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action='store', dest='root_proj',
                        help='path to the root project')
    results = parser.parse_args()

    dirName = results.root_proj

    prjName = os.path.basename(os.path.normpath(results.root_proj))
    fileName = "VHDL-Project"

    # Get the list of all files directories with .vhd files
    listOfDir = getListOfDir(dirName)

    # Create prj file
    with open(results.root_proj + "/" + fileName + '.prj', 'w') as p:
        # Set proj name
        # p.write('(setq vhdl-project "Example")\n')
        p.write('(setq vhdl-project "')
        p.write(prjName)
        p.write('")\n')
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
            p.write('/"')
        p.write(')')
        p.write("\n")
        p.write(' ""\n')
        p.write(' (("ModelSim" "-87 \\\\2" "-f \\\\1 top_level" nil)\n')
        p.write('  ("Synopsys" "-vhdl87 \\\\2" "-f \\\\1 top_level"\n')
        p.write('   ((".*/datapath/.*" . "-optimize \\\\3")\n')
        p.write('    (".*_tb\\\\.vhd"))))\n')
        p.write(' "lib/" "work" "lib/example3/" "Makefile_\\\\2" ""))')


if __name__ == '__main__':
    main()
