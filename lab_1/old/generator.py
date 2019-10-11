from random import randint, shuffle


class Game():
	def __init__(self):
		self.name = None
		self.date = None
		self.genre = None
		self.age_restriction = None
		self.engine = None



def generate_games(filename, amount):
	years = [1999, 2019]

	genres = ["Platformer", "Shooter", "Fighting", "Stealth", "Survival", "Battle Royale", "Rhythm",
	"Survival horror", "Metroidvania", 
	"Text adventures", "Visual novel", "Interactive movie",
	"Action RPG", "MMORPG", "Roguelike", "Tactical RPG", "Sandbox RPG",
	"Simulator", "Real-time strategy", "Real-time tactics", "MOBA", "Turn-based strategy",
	"Turn-based tactics", "Sport", "Racing", "MMO", "MMORPG"]

	age_levels = ["0+", "6+", "12+", "16+", "18+"]

	engines = ["Source", "Source 2", "HaVok", "Unreal Engine", "Unreal Engine 2",
	"Unreal Engine 3", "Unreal Engine 4", "Unreal Engine 5", "Unity", "CryEngine",
	"CryEngine 2", "CryEngine 3", "GameMaker", "RPGMaker", "Ren'Py", "id Tech",
	"id Tech 2", "id Tech 3", "id Tech 4", "Serious Engine", "RAGE", "Frostbite Engine",
	"Creation Engine", "Core", "4A Engine", "Illusion Engine", "Crystal Tools",
	"Alamo", "Allegro", "Build ngine", "Cocos2d", "Decima", "Fox Engine", "HeroEngine", 
	"IW engine", "MonoGame"]

	names = []

	of_pattern = []
	of_pattern.append(["call", "man", "war", "game", "age", "champions",
		"gate", "world", "day", "heroes", "legends", "ghost", "sword",
		"guns", "illusion", "kings", "temple", "kingdom", "army", "ruins",
		"life", "hearts"])
	of_pattern.append(["duty", "mayhem", "war", "death", "gods", "darkness",
		"souls", "light", "the stars", "time", "magic", "eternity", "sin",
		"hope", "hell", "heaven", "fear", "fate", "infinity", "the fallen",
		"mystery", "doom"])

	adj_noun = []
	adj_noun.append(["epic", "cruel", "eternal", "high", "amazing", "american",
		"endless", "killing", "dark", "lethal", "dead", "blood", "burning",
		"frozen", "metal", "new", "old", "cyber", "zero", "roaring", "fallen",
		"magic", "last", ])
	adj_noun.append(["war", "quest", "legacy", "legend", "heroes", "world",
		"story", "apocalypse", "tale", "attack", "way", "saga", "battle", 
		"blade", "storm", "souls", "force", "chaos", "power", "night",
		"life", "dawn", ])

	def two_of():
		word_1 = of_pattern[0][randint(0, len(of_pattern[0]) - 1)]
		word_2 = of_pattern[1][randint(0, len(of_pattern[1]) - 1)]

		return word_1 + " of " + word_2

	def two_adj_noun():
		word_1 = adj_noun[0][randint(0, len(adj_noun[0]) - 1)]
		word_2 = adj_noun[1][randint(0, len(adj_noun[1]) - 1)]

		return word_1 + " " + word_2

	def three_words():
		word_1 = adj_noun[0][randint(0, len(adj_noun[0]) - 1)]
		word_2 = of_pattern[0][randint(0, len(of_pattern[0]) - 1)]
		word_3 = of_pattern[1][randint(0, len(of_pattern[1]) - 1)]

		return word_1 + " " + word_2 + " of " + word_3

	#print(len(of_pattern[0]) * len(of_pattern[1]))
	#print(len(adj_noun[0]) * len(adj_noun[1]))
	#print(len(adj_noun[0]) * len(of_pattern[0]) * len(of_pattern[1]))

	def fill_names(mul, func):
		for i in range(round(amount * mul)):
			while(True):
				title = func()

				if title not in names:
					names.append(title)
					break


	fill_names(0.25, two_of)
	fill_names(0.25, two_adj_noun)
	fill_names(0.2, three_words)

	shuffle(names)

	left = round(amount * 0.3)
	choosed = round(left * 0.4)
	sequels = [0 for i in range(choosed)]
	rome_nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
	for i in range(left):
		sequels[randint(0, len(sequels) - 1)] += 1

	for i in range(len(sequels)):
		rome = randint(0, 1)

		for j in range(sequels[i]):
			if rome:
				r_num = "X" * (j // 10) + rome_nums[(j + 1) % 10]
				names.append(names[i] + " " + r_num)
			else:
				names.append(names[i] + " " + str(j + 2))


	names.sort()

	
	for i in range(len(names)):
		print(names[i])
	print(len(names))



	with open(filename, "w") as f:
		pass
			




if __name__ == "__main__":
	generate_games("test.txt", 200)
