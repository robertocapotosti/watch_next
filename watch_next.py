#=== IMPORT SECTION ===
import spacy

#=== VARIABLE DECLARATIONS ===
movies = []

#=== FUNCTION SECTION ===
def load_movies():
	# variable declarations
	global movies

	f_movies = open("movies.txt","r",encoding="utf-8")
	for line in f_movies:
		fields = line.split(":")
		fields[0] = fields[0].strip()
		fields[1] = fields[1].strip()
		movies.append(fields)
	f_movies.close()

#=== MAIN SECTION ===
load_movies()
for movie in movies:
	print(movie)
