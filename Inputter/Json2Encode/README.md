## Instruction
if you haven't install click, run:
```
sudo pip3 install Click 
```
Once you have click installed, make sure you are in the ```/Inputter/Json2Encode```
Run ```python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON>```
If you have a output path you want to output to, run:
```python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON> --```

See sample.json and sample.json-output.json for example.
NOTE: 
1. This program takes JSON file.
2. The default output path is inputfilename-output.json if not specify.

## TODO:
- [ ] How to deal with BR RET instruction
- [ ] Count the Instruction per function or per document