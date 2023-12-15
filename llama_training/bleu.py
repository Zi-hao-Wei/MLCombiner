from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
import nltk
import json
import numpy as np
nltk.download('punkt')

def calculate_bleu_score(reference, candidate):
    reference_tokenized = word_tokenize(reference)
    candidate_tokenized = word_tokenize(candidate)

    # Calculate BLEU score
    score = sentence_bleu([reference_tokenized], candidate_tokenized)
    return score

# Example usage
root ="/gpfs/accounts/chaijy_root/chaijy0/owenhji/FastChat/data/test.json"
target = "/gpfs/accounts/chaijy_root/chaijy0/owenhji/FastChat/data/out_8.json"

with open(root,"r") as f:
    root_data = json.load(f)
with open(target,"r") as f:
    target_data = json.load(f)
bleu_scores=[]
for i,target_ in enumerate(target_data):
    root_ = root_data[i]["conversations"][1]["value"]
    score = calculate_bleu_score(target_, root_)
    # print(score)
    # if score ==0:
    #     continue
    bleu_scores.append(score)
bleu_scores = np.array(bleu_scores)
print(f"BLEU Score: {bleu_scores.mean()}")
