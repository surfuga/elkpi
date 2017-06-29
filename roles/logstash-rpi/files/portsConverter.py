import json
import yaml

f = open('ports.json','rw')

ports_dict = json.loads(f.read())

ports_dict = ports_dict["ports"]
result_dict = {}

for k,v in ports_dict.items():

  result_dict[k] = ""
  if isinstance(v, dict):
    if v["tcp"]:
      result_dict[k] = v["description"]
  elif isinstance(v, list):
    for elem in v:
      if elem["tcp"]:
        result_dict[k] += elem["description"]


# new line
f2 = open('ports.yml','w')
result_string = json.dump(result_dict, f2, indent=0)
f2.close()

# get rid of , { and } characters
f3 = open('ports.yml','r')
filestr = f3.read()
f3.close()
filestr = filestr.replace(",","")
filestr = filestr.replace("{","")
filestr = filestr.replace("}","")
f4 = open('ports2.yml','w')
f4.write(filestr)
f4.close()
