import requests 
import json
apiclass = requests.get("https://api.publicapis.org/entries")
apijot = apiclass.json()["entries"] 
#Note:   entries serve as the key in this instance in the apipheny.io site 
verify = []
verit = []
for jots in apijot:
    aps = jots["Category"]
    apt = jots ["Description"]
    verify.append(aps)
    verit.append(apt)
    #print(apt)
listeth = " " .join(verit)
lister = " " . join(verify)

# files = open("apiii.csv", "w")
# files.write(listeth)
# files.close()

files = open("apiii.csv", "w")
files.write(lister)
files.close() 