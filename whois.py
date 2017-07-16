import pythonwhois
import json
import sys

class ComplexEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, complex):
             return [obj.real, obj.imag]
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)

filename = sys.argv[1]

f = open(filename, "r")
lines = f.readlines()

for line in lines:
    print line

    
    json_data = pythonwhois.net.get_whois_raw(line, with_server_list=False)
    a = json.dumps(json_data[0], indent=4)
    _data = a.split("\\n")
    data = json.dumps(_data, indent=4, default=ComplexEncoder)
    print data


    obj = open("data_whois.json", 'ab')
    obj.write(line)
    obj.write(data)
    obj.close
f.close()

