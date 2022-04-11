import pandas as pd
import pickle



def get_recommendations(title):

    #importing the model
    filename = 'model_recc.sav'
    cosine_sim = pickle.load(open(filename, 'rb'))

    #loading the metadata
    metadata = pd.read_csv('data/movies_metadata.csv', low_memory=False)

    #getting the indices of the movie from the metadata
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]