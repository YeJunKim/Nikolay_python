import pythonwhois
import json
import sys



json_data = pythonwhois.net.get_whois_raw(sys.argv[1], with_server_list=False)

a = json.dumps(json_data[0], indent=4)

_data = a.split("\\n")

data = json.dumps(_data, indent=4)

print data


obj = open("data_whois.json", 'wb')
obj.write(data)
obj.close


