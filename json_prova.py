import json


data = {}

data['files'] = []
data['files'].append({
    'file1': 'ciao'
})
data['files'].append({
    'file2': 'ciao2'
})

data2 = {}
data2['options'] = {}
data2['options']['ghdl_analysis'] = []
data2['options']['ghdl_analysis'].append('--workdir=work')
data2['options']['ghdl_analysis'].append('--ieee=synopsys')
data2['options']['ghdl_analysis'].append('-fexplicit')


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
