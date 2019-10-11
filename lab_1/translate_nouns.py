from translate import Translator
from random import shuffle

"""
eng_nouns = []
tr = Translator(to_lang="sv")

with open("nounlist.txt", "r") as f_in:
	for line in f_in:
		eng_nouns.append(line)

count = 0
para = ""
translation_str = ""

for i in range(len(eng_nouns)):
	para += eng_nouns[i]
	count += 1

	if count > 40 or i == len(eng_nouns) - 1:
		para = tr.translate(para)
		translation_str += " " + para
		para = ""
		count = 0

sve_nouns = translation_str.split()

print(sve_nouns)
"""

eng_words = []
with open("eng_words.txt", "r") as f_eng:
	for line in f_eng:
		eng_words.append(line)
 
swe_words = []
with open("swe_words.txt", "r", encoding='utf-8') as f_swe:
	for line in f_swe:
		swe_words.append(line)

print(eng_words)

