## Setup
if you haven't install click, run:
```
sudo pip3 install Click 
```
## Execution
Once you have click installed, make sure you are in the ```/Inputter/Json2Encode``` <br>
Run:
```
python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON>
```
or 
```
python3 json2encode.py --i <FIX_ME_WITH_YOUR_INPUT_JSON>
```


If you have a output path you want to output to, run:
```
python3 json2encode.py --input <FIX_ME_WITH_YOUR_INPUT_JSON> --output <FIX_ME_WITH_YOUR_OUTPUT_PATH>
```
or 
```
python3 json2encode.py --i <FIX_ME_WITH_YOUR_INPUT_JSON> --o <FIX_ME_WITH_YOUR_OUTPUT_PATH>
```
<br>

See ```sample.json``` and ```sample.json-output.json``` for example.<br>
<br>
NOTE: <br>
1. This program takes JSON file.
2. The default output path is ```input_filename-output.json``` if not specify.

## TODO:
- [x] How to deal with BR RET instruction
- [x] Count the Instruction per function or per document