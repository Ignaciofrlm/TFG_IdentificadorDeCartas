import json
import requests
import time
import os

#Crear rutas:
#if not os.path.exists("ImgTrainingClases/" + i["name"]):
                    #os.mkdir("ImgTrainingClases/" + i["name"])

total = 115800
inicio = 0
doble_layouts = ["transform","modal_dfc","double_faced_token","reversible_card"]

with open("default-cards-20260612210941.json", 'r',encoding="utf8") as jsoncartas:
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
                if not os.path.exists(".\ArtSeries\\" + i["id"] + "\\" + i["id"] + ".jpg"):
                    if i["card_faces"][0].get("image_uris"):
                        img = requests.get(i["card_faces"][0]["image_uris"]["small"])
                        os.makedirs(".\ArtSeries\\" + i["id"], exist_ok=True)
                        with open(".\ArtSeries\\" + i["id"] + "\\" + i["id"] + ".jpg", 'wb') as file:
                            file.write(img.content)  
            elif i["layout"] in doble_layouts:
                face = 1
                for f in i["card_faces"]:
                    if not os.path.exists(".\Dataset\\" + i["id"] + f"-face{face}"):
                        img = requests.get(f["image_uris"]["small"])
                        os.makedirs(".\Dataset\\" + i["id"] + f"-face{face}", exist_ok=True)
                        with open(".\Dataset\\" + i["id"] + f"-face{face}" + "\\" + i["id"] + f"-face{face}" + ".jpg", 'wb') as file:
                            file.write(img.content)   
                        face += 1    
            else:
                if not os.path.exists(".\Dataset\\" + i["id"] + "\\" + i["id"] +".jpg"):
                    img = requests.get(i["image_uris"]["small"])
                    os.makedirs(".\Dataset\\" + i["id"], exist_ok=True)
                    with open(".\Dataset\\" + i["id"] + "\\" + i["id"] +".jpg", 'wb') as file:
                        file.write(img.content)      

            #time.sleep(0.1)

