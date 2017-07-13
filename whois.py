import pythonwhois
import json
import sys

json_data = pythonwhois.net.get_whois_raw(sys.argv[1], with_server_list=False)

parse = pythonwhois.parse.parse_raw_whois(json_data, True)

a = json.dumps(parse, ensure_ascii=True, indent=4, encoding="utf-8", sort_keys=False)

print a


obj = open("data_whois.json", 'wb')
obj.write(a)
obj.close

