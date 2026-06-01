import json
import requests
import time
import os

#Crear rutas:
#if not os.path.exists("ImgTrainingClases/" + i["name"]):
                    #os.mkdir("ImgTrainingClases/" + i["name"])

total = 335278
inicio = 8850
doble_layouts = ["transform","modal_dfc","double_faced_token","reversible_card"]

with open("all-cards-20250121102112.json", 'r',encoding="utf8") as jsoncartas:
    jsonstring = jsoncartas.read()
    data = json.loads(jsonstring)
    total = len(data)
    j = inicio
    for i in data[inicio:]:
        if i["object"] == "card":
            j += 1
            per = (j*100/total)
            print(f"\r{j} of {total} ({per}%) cardId:"+ i["id"] + " layout: " + i["layout"] + "         ",end = ' ', flush = True)

            if i["layout"] == "art_series":
                if i["card_faces"][0].get("image_uris"):
                    img = requests.get(i["card_faces"][0]["image_uris"]["small"])
                    with open("E:\ArtSeries\\" + i["id"] + ".jpg", 'wb') as file:
                        file.write(img.content)  
            elif i["layout"] in doble_layouts:
                face = 1
                for f in i["card_faces"]:
                    img = requests.get(f["image_uris"]["small"])
                    with open("E:\DatasetTFG\\" + i["id"] + f"-face{face}" + ".jpg", 'wb') as file:
                        file.write(img.content)   
                    face += 1    
            else:
                img = requests.get(i["image_uris"]["small"])
                with open("E:\DatasetTFG\\" + i["id"] + ".jpg", 'wb') as file:
                    file.write(img.content)      

            #time.sleep(0.1)

