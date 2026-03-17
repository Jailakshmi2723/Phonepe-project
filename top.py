import os
import json
import pandas as pd

# 🔁 Path to TOP dataset
path = "C:\\Users\\rpsar\\Downloads\\pulse-master\\pulse-master\\data\\top\\insurance\\country\\india\\state"

data = []

# 🔄 Loop through states → years → quarters
for state in os.listdir(path):
    state_path = os.path.join(path, state)

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)

            with open(file_path, "r") as f:
                d = json.load(f)

                try:
                    # 🔑 Extract TOP data (pincodes)
                    for i in d["data"]["pincodes"]:
                        pincode = i["entityName"]
                        count = i["metric"]["count"]
                        amount = i["metric"]["amount"]

                        data.append([
                            state,
                            int(year),
                            int(file.replace(".json", "")),
                            pincode,
                            count,
                            amount
                        ])
                except:
                    pass


df = pd.DataFrame(data, columns=[
    "state", "year", "quarter", "pincode", "count", "amount"
])

print(df.head())

df.to_csv("top_insurance.csv", index=False)

print("Top data extracted successfully!")