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
with open("eng_words.txt", "r", encoding='utf-8') as f_eng:
	for line in f_eng:
		eng_words.append(line[:-1])
 
swe_words = []
with open("swe_words.txt", "r", encoding='utf-8') as f_swe:
	for line in f_swe:
		swe_words.append(line[:-1])

print(len(swe_words))
new_words = []

for i in range(len(swe_words)):
	if swe_words[i] not in eng_words:
		new_words.append(swe_words[i])

with open("asdf.txt", "w", encoding="utf-8") as f:
	for i in range(len(new_words)):
		f.write(new_words[i] + "\n")

