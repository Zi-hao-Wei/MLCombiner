from llvmlite import ir

def write_to_ll_file(llvm_ir, output_filename):
    # Create LLVM module from LLVM IR string
    module = ir.Module.from_assembly(llvm_ir)

    # Write the module to a .ll file
    with open(output_filename, "w") as f:
        f.write(str(module))

# Example LLVM IR strings
llvm_ir_string1 = """
define i32 @function1() {
    ; Your LLVM IR code for function1 here
    ret i32 0
}
"""

write_to_ll_file(llvm_ir_string1, "output_file1.ll")