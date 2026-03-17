import os
import json
import pandas as pd

path = r"C:\Users\rpsar\Downloads\pulse-master\pulse-master\data\aggregated\insurance\country\india"

data = []

for year in os.listdir(path):

    year_path = os.path.join(path, year)

    if os.path.isdir(year_path):

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                quarter = file.replace(".json","")

                with open(os.path.join(year_path, file)) as f:

                    data_json = json.load(f)

                    try:
                        count = data_json["data"]["transactionData"][0]["paymentInstruments"][0]["count"]
                        amount = data_json["data"]["transactionData"][0]["paymentInstruments"][0]["amount"]

                        data.append({
                            "year": year,
                            "quarter": quarter,
                            "count": count,
                            "amount": amount
                        })

                    except:
                        pass

df = pd.DataFrame(data)

print(df.head())
df.to_csv("aggregated_insurance.csv", index=False)