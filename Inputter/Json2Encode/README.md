## Instruction
if you haven't install click, run:
```
sudo pip3 install Click 
```
Once you have click installed, make sure you are in the ```/Inputter/Json2Encode```
Run: <br>
```python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON>``` <br>
or <br>
```python3 json2encode.py --i <FIX_ME_WITH_YOUR_INPUT_JSON>```<br>

If you have a output path you want to output to, run:<br>
```python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON> --output <FIX_ME_WITH_YOUR_OUTPUT_PATH>``` <br>
or <br>
```python3 json2encode.py --i <FIX_ME_WITH_YOUR_INPUT_JSON> --o <FIX_ME_WITH_YOUR_OUTPUT_PATH>```<br>
<br>
See sample.json and sample.json-output.json for example.<br>
<br>
NOTE: <br>
1. This program takes JSON file.
2. The default output path is inputfilename-output.json if not specify.

## TODO:
- [ ] How to deal with BR RET instruction
- [ ] Count the Instruction per function or per document