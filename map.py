import os
import json
import pandas as pd

path = "C:\\Users\\rpsar\\Downloads\\pulse-master\\pulse-master\\data\\map\\insurance\\hover\\country\\india\\state"

data = []

for state in os.listdir(path):
    state_path = os.path.join(path, state)

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)

            with open(file_path, "r") as f:
                d = json.load(f)

                try:
                    for i in d["data"]["hoverDataList"]:
                        name = i["name"]
                        count = i["metric"][0]["count"]
                        amount = i["metric"][0]["amount"]

                        data.append([state, year, file.replace(".json",""), name, count, amount])
                except:
                    pass

df = pd.DataFrame(data, columns=["state","year","quarter","district","count","amount"])

df.to_csv("map_insurance.csv", index=False)

print("Map data extracted successfully!")
df.to_csv("map_insurance.csv", index=False)