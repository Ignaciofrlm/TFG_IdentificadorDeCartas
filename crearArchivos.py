import numpy as np
from PIL import Image 
import json

ids = np.load('ids.npy')

print(type(ids))
print(len(ids))

n = []

with open("all-cards-20250121102112.json", 'r',encoding="utf8") as jsoncartas:
    jsonstring = jsoncartas.read()
    data = json.loads(jsonstring)
    total = len(ids)
    j = 0
    for id in ids:
        j = j + 1
        per = (j/total)*100
        bar = '#'*int(per/10)
        print(f"\r[{bar.ljust(10)}] {per}%",end = '                    ', flush = True)
        encontrado = False
        for i in data:
            if i["id"] == id[:36]:
                n.append(i["name"])
                encontrado = True
        if not encontrado:
            n.append("Name not found")

n = np.array(n)
np.save("nombres.npy",n)
    
