import json

with open(r"sample.json") as f:
    json = json.loads(f.read())
    tracker = {}
    counter = 1
    for function in json:
        line = function["unoptimized"].split('\n')
        for instruction in line:
            if instruction != '' and instruction != '\n' and instruction != '}':
                instruction = instruction.strip().upper()
                instruction = instruction.replace("I32","i32")
                instruction = instruction.replace("I64","i64")
                instruction = instruction.replace(",","")
                if instruction.find('=') != -1:
                    tracker[instruction[0:instruction.find('=')-1]] = "I"+str(counter)
                    instruction = "I"+str(counter)+": "+instruction[instruction.find('=')+2:]
                else:
                    instruction = "I"+str(counter)+": "+instruction
                counter += 1
                for word in tracker:
                    instruction = instruction.replace(word, tracker[word])
                print(instruction)