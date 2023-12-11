import json

with open(r"./extr_loop.c_gomp_loop_ordered_static_start.c.json") as f:
    json = json.loads(f.read())

for function in json:
    print("=================head=================")
    print(function["name"].strip())
    print("=================unoptimized=================")
    print(function["unoptimized"].strip())
    print("=================optimized=================")
    print(function["optimized"].strip())