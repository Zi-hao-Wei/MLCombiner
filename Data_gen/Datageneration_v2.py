import subprocess
import re 
import json
import os
from tqdm import tqdm
def compile_with_clang(file_path, optimization_level):
    output_file = f"original.ll"
    subprocess.run(["clang", "-Xclang", "-emit-llvm","-Xclang", "-disable-O0-optnone", "-o", output_file, "-c", file_path])
    return output_file

def optimzie_with_opt(file_path):
    output_file = f"optimized.ll"
    subprocess.run(["opt", "-passes=instcombine", "-S", file_path, "-o", output_file])
    return output_file

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def compare_ll(file1, file2):
    content1 = read_file(file1)
    content2 = read_file(file2)

def extract_functions(file_content):
    """
    Extracts functions from the LLVM IR file content.
    Returns a dictionary where keys are function names and values are function bodies.
    """
    functions = {}
    pattern = r"define.*\{"
    
    matches = re.finditer(pattern, file_content, re.DOTALL)
    
    for match in matches:
        func_start = match.start()
        func_begin = file_content.find("{", func_start) + 1
        func_end = file_content.find("}", func_start) + 1
        func_ir = file_content[func_begin:func_end]
        func_name = file_content[func_start:func_begin]
        functions[func_name] = func_ir
    print(functions)
    return functions

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


def compare_functions(o_functions, c_functions):
    """
    Compares functions between two sets and generates a JSON structure.
    """
    compared_functions = []
    for func_name in o_functions:
        if func_name in c_functions:
            #print("Has Function")
            #print(o_functions[func_name].lower())
            #print(c_functions[func_name].lower())
            #exit()
            if o_functions[func_name].lower() != c_functions[func_name].lower():
                compared_functions.append({
                    "name": func_name,
                    "unoptimized": o_functions[func_name],
                    "optimized": c_functions[func_name]
                })
            #print(compared_functions)
            #   exit()
    return compared_functions

if __name__ == "__main__":
    files = os.listdir("./benchmark/Total_C")
    for c_file_o in tqdm(files):
        try:
            c_file = "./benchmark/Total_C/{}".format(c_file_o)  # Replace with your C file
            original_file_path = compile_with_clang(c_file, 0)        
            combine_file_path = optimzie_with_opt(original_file_path)
            with open(original_file_path, 'r') as file:
                original_content = file.read()
            with open(combine_file_path, 'r') as file:
                combine_content = file.read()
            o_functions = extract_functions(original_content)
            c_functions = extract_functions(combine_content)
        #exit()
        except:
            continue
        # Compare functions
        compared_functions = compare_functions(o_functions, c_functions)
        if (len(compared_functions)>0):
            # Path for the output JSON file
            output_json_path = "./preprocessed_2/{}.json".format(c_file_o)
            # Write JSON data to a file
            with open(output_json_path, 'w') as file:
                json.dump(compared_functions, file, indent=4)
        # except:
            # pass 
