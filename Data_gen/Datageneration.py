import subprocess
import re 
import json
import os
from tqdm import tqdm
def compile_with_clang(file_path, optimization_level):
    output_file = f"{file_path.split('.')[0]}_{optimization_level}.ll"
    subprocess.run(["clang", "-c", "-S", "-emit-llvm", f"-O{optimization_level}", file_path, "-o", output_file])
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

    return functions


def compare_functions(o0_functions, o3_functions):
    """
    Compares functions between two sets and generates a JSON structure.
    """
    compared_functions = []
    for func_name in o0_functions:
        if func_name in o3_functions:
            compared_functions.append({
                "name": func_name,
                "unoptimized": o0_functions[func_name],
                "optimized": o3_functions[func_name]
            })
    return compared_functions

if __name__ == "__main__":
    files = os.listdir("./benchmark/Total_C")
    for c_file_o in tqdm(files):
        try:
            c_file = "./benchmark/Total_C/{}".format(c_file_o)  # Replace with your C file
            o0_file_path = compile_with_clang(c_file, 0)
            o3_file_path = compile_with_clang(c_file, 3)
            with open(o0_file_path, 'r') as file:
                o0_content = file.read()
            with open(o3_file_path, 'r') as file:
                o3_content = file.read()
            o0_functions = extract_functions(o0_content)
            o3_functions = extract_functions(o3_content)
            # Compare functions
            compared_functions = compare_functions(o0_functions, o3_functions)
            if (len(compared_functions)>0):
                # Path for the output JSON file
                output_json_path = "./preprocessed/{}.json".format(c_file_o)
                # Write JSON data to a file
                with open(output_json_path, 'w') as file:
                    json.dump(compared_functions, file, indent=4)
        except:
            pass 