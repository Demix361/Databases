from translate import Translator

"""
with open("nounlist.txt", "r") as f_in:
	with open("swedish_nouns.txt", "w", encoding='utf-8') as f_out:
		tr = Translator(to_lang="sv")

		for line in f_in:
			f_out.write(tr.translate(line[:-1]) + "\n")
"""
eng_nouns=[]
tr = Translator(to_lang="sv")

with open("nounlist.txt") as f_in:
	for line in f_in:
		eng_nouns.append(line)

count = 0
para = ""

for i in range(len(eng_nouns)):
	if count > 50:

	para += eng_nouns[i]
	count += 1

print(tr.translate(para))