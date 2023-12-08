import os
import json
import re
from tqdm import tqdm
def separate_into_basic_blocks(llvm_ir):
    # Regular expression to match labels
    label_pattern = re.compile(r'^(\d+):')

    # Split the LLVM IR into lines
    lines = llvm_ir.split('\n')

    # Initialize a list to store basic blocks
    basic_blocks = []
    current_basic_block = []

    # Iterate through lines
    for line in lines:
        # Check if the line contains a label
        match = label_pattern.match(line)
        if match:
            # If a new label is found, start a new basic block
            if current_basic_block:
                basic_blocks.append('\n'.join(current_basic_block))
                current_basic_block = []
        
        # Add the line to the current basic block
        current_basic_block.append(line)

    # Add the last basic block
    if current_basic_block:
        basic_blocks.append('\n'.join(current_basic_block))

    return basic_blocks


for files in os.listdir("../preprocessed_2")[:10000]:
    input_files = "./../preprocessed_2/"+files
    with open(input_files, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
    for function in fcc_data:
        x1 = separate_into_basic_blocks(function["unoptimized"][3:])
        x2 = separate_into_basic_blocks(function["optimized"][3:])
        if (len(x1) == len(x2)):
            compared_BB = []
            output_files = "./BB_level/"+files
            for (b1,b2) in zip(x1,x2):
                pattern = r"\d+:\s*; preds = (?:%\d+\s*,\s*)*%\d+\s*"
                b1 = re.sub(pattern, "", b1)
                b2 = re.sub(pattern, "", b2)
                compared_BB.append({"unoptimized":b1,"optimized":b2})
            with open(output_files, 'w') as file:
                json.dump(compared_BB, file, indent=4)