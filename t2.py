import yaml
import pprint
f=open("books.yaml")
data=yaml.safe_load(f)
f.close()
pprint.pprint(data)
for b in data['books']:
    print ("Get "+b)
