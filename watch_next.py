#=========================== TASK 2 : MOST SIMILAR MOVIE  ======================
# import spacy library
import spacy
#  The function should take in the description as a parameter and return the
# itle of the most similar movie

def most_similar_movie(description):
    # Load the spaCy advanced English model
    nlp = spacy.load("en_core_web_md")
    
    # Read the movie descriptions from the file
    with open("movies.txt", "r") as f:
        movies = f.readlines()
    
    # Calculate  similarity between the input description and each movie description
    similarities = []
    for movie in movies:
        
        # strip and split each line of movies and remove the title and leave the description
        movie_description = movie.split(":")[1].strip()
        
        #create nlp doc objects
        doc1 = nlp(description)
        doc2 = nlp(movie_description)

        
        # calculate the similarity between the given description and each movie description
        similarity = doc1.similarity(doc2)
        similarities.append(similarity)
    
    # Find the index of the most similar movie
    max_index = similarities.index(max(similarities))
    
    # print the movie description
    print(movies[max_index].split(":")[1].strip())
    
    # Return the title of the most similar movie
    return movies[max_index].split(":")[0].strip()
    

# output the result
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print("\nMost similar movie :" + " " + most_similar_movie(description))
