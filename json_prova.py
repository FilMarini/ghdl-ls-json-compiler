import json

files = []
files.append("file1")
files.append("file2")


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


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
