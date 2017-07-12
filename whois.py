import pythonwhois
import json
import sys

json_data = pythonwhois.net.get_whois_raw(sys.argv[1], with_server_list=False)

parse = pythonwhois.parse.parse_raw_whois(json_data, True)

jsonarray = json.dumps(parse, ensure_ascii=True, indent=4, separators=None, encoding="utf-8", default=False, sort_keys=True)

print jsonarray


obj = open("whois_data.json", 'wb')
obj.write(jsonarray)
obj.close

