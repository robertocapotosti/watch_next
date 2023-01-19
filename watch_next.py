#=== IMPORT SECTION ===
import spacy

#=== VARIABLE DECLARATIONS ===
movies = []
nlp = object()
movie_watched = ""
movie_description = "" 

#=== FUNCTION SECTION ===
# function to load the movies.txt file in memory
def load_movies():
	# variable declarations
	fields = []
	f_movies = object()
	line = ""
	global movies

	try:
		f_movies = open("movies.txt","r",encoding="utf-8")
	# manage the erro of not finding the movie file in the CWD
	except FileNotFoundError:
		print("Error: file movies.txt not found; now exiting.")
		exit()
	try:
		# loop for wach line of the movie file
		for line in f_movies:
			# create a list of two elements
			fields = line.split(":")
			# remove possible spaces but also test that
			# the file format is correct
			fields[0] = fields[0].strip()
			fields[1] = fields[1].strip()
			# add a 3rd fields where to store the score,
			# just for our records and debugging
			fields.append(0.0)
			# add the movie to the movies list
			movies.append(fields)
	# manage possible format error in the movie.txt file
	except IndexError:
		print("Error: the movie.txt file is not formatted correctly\n"
			"Please, for each line of the file, use the format movie_name:movie description\n",
			"Now exiting.")
		exit()
	f_movies.close()

# function takes in the description of an already seen movie
# and return the title of the most similar movie
def watch_next(movie_description):
	# variable declarations
	index1 = 0
	found = 0
	top_score = 0.0
	model_current = object()
	movie = []
	global movies

	# create the tokens of the current movie
	model_current = nlp(movie_description)
	# loop each movie 
	for movie in movies:
		# store the similarity score of the description of current movie
		# with the description of the movie choosen from the movie list
		movie[2] = nlp(movie[1]).similarity(model_current)
		# if the score is higher of the previous to score then
		# save the movie index and it is the new top score
		if movie[2] > top_score:
			top_score = movie[2]
			found = index1
		# increment the movie index
		index1 += 1
	# return the title of the most similar movie
	return movies[found][0]
	
#=== MAIN SECTION ===
# load the medium English language, which is the minimum requirement
# for correctly using the method similarity
nlp = spacy.load('en_core_web_md')
# load the movies in memory, in the movies list
load_movies()
# set the variables for last movie watched
movie_watched = "Planet Hulk"
movie_description = '''Will he save \
their world or destroy it? When the Hulk becomes too dangerous for the \
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to \
planet where the Hulk can live in peace. Unfortunately, Hulk land on the \
planet Sakaar where he is sold into slavery and trained as a gladiator.'''
# give to the user a suggestion about which movie to watch next
print(f"You recently watched the movie '{movie_watched}' and",
	"for this reason we suggest you to watch next the movie '",
	watch_next(movie_description)+"'")