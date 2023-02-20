# most_similar_movie
The function should take in the description as a parameter and return the title of the most similar movie.


#  Projec Name
most_similar_movie

# A brief description of the project
This project aim to create a function that will take a description based on previous movie watched and suggest the next movie to watch from a movie file


 ## Installation

 - Clone  the repository
 
 git clone https://github.com/MaxxwellG/most_similar_movie.git

 -Install the required packages by running in the command prompt or terminal and run:

pip install -r requirements.txt

or go to the root of the repository directory and run the pip  command to automatically  create the requirements.txt file:

pip freeze > requirements.txt

# Usage
This project can be used to analise similarities between sentences based on model 'en_core_web_md' and make suggestions based on previous data.
The function will take a movie description as argument, read a movie file and and calculate the similarities  against each line representaing a movie description and return the highest similarity which is the most similar movie and suggest the next movie to watch 

# ------------ Working with spaCy-------

# Before we proceed with spacy it must be installed
pip install spacy

# spaCy is an open-source natural language processing library that is designed to be fast and efficient.
# spaCy provides a wide range of functionalities for various natural language processing tasks such as tokenization, named entity recognition, dependency parsing, and more. This project will focus on finding  similarities between paragraphs

# Here's a simple example of how we can find similarities  sentences,paragraphs using spacy

# import spacy(ony after installing spacy)
import spacy

# Downnload the simple English model
python3 -m spacy download en_core_web_sm

# Downnload the advanced  English model
python3 -m spacy download en_core_web_md


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
    
 # Contributing 
 Contributions are welcome!

# Authors
Maxime HT
# Version History

    0.2
        Various bug fixes and optimizations
        See commit change or See release history
    0.1
        Initial Release

 # License
 Distributed under the GNU license. see 'LICENSE'  for more information.


