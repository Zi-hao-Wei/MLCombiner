import json
import click

tracker = {}

def parsing(instruction, counter):
    instruction = instruction.strip().upper()
    instruction = instruction.replace("I32","i32")
    instruction = instruction.replace("I64","i64")
    instruction = instruction.replace(",","")
    if instruction.find('=') != -1:
        tracker[instruction[0:instruction.find('=')-1]] = "I"+str(counter)
        instruction = "I"+str(counter)+": "+instruction[instruction.find('=')+2:]
    else:
        instruction = "I"+str(counter)+": "+instruction
    return instruction

# [-------Main function-------]

def run(input):
    with open(r"{}".format(input)) as f: # Replace "sample.json" with your file
        data = json.loads(f.read())
        
        for function in data:
            function["unopt-encode"] = []
            function["opt-encode"] = []
            #  handle optimized instruction
            print("[-------Unoptimized Encode-------]")
            line = function["unoptimized"].split('\n')
            counter = 1
            for instruction in line:
                if instruction != '' and instruction != '\n' and instruction != '}':
                    instruction = parsing(instruction, counter)
                    counter += 1
                    for word in tracker:
                        instruction = instruction.replace(word, tracker[word])
                    print(instruction)
                    function["unopt-encode"].append(instruction)
            print("[-------Optimized Encode-------]")
            #  handle optimized instruction
            line = function["optimized"].split('\n')
            counter = 1
            for instruction in line:
                if instruction != '' and instruction != '\n' and instruction != '}':
                    instruction = parsing(instruction, counter)
                    counter += 1
                    for word in tracker:
                        instruction = instruction.replace(word, tracker[word])
                    print(instruction)
                    function["opt-encode"].append(instruction)
    return data


@click.command()
@click.option('-i','--input', required=True)
@click.option('-o','--output', required=False, default="")
def main(input,output):
    # input = "sample.json" # Replace "sample.json" with your file
    if output == "":
        output = "{}-output.json".format(input)
    # Write JSON data to a file
    with open(output, 'w') as file:
        json.dump(run(input), file, indent=4)
    
    # the final json format:
    # json = [
    #             {
    #                 "name": "",
    #                 "unoptimized": "",
    #                 "optimized": "",
    #                 "unopt-encode": "",
    #                 "opt-encode": "",
    #             }
    #         ]


if __name__ == "__main__":
    main()