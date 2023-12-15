import os
from tqdm import tqdm
root="data/BB_level"

print(len(os.listdir(root)))
data = []
import json
count=0
for i,file in tqdm(enumerate(os.listdir(root))):
    path = os.path.join(root,file)
    count+=1
    # print(file)
    with open(path,"r") as f:
        datapoint = json.load(f)
    for point in datapoint:
        new_data={
            "id": "id_"+str(i),
            "conversations":[{
                        "from": "human",
                        "value": "Now I want you to help me do an instruction combination of the following code: "+ point["unoptimized"]
                },
                
                {
                    "from": "gpt",
                    "value": point["optimized"]
                },
            ]
        }
    # print(new_data)
    # exit()
        
        data.append(new_data)
print()
print(len(data))
target="data/data.json"
with open(target,"w") as file:
    json.dump(data,file,indent=4)