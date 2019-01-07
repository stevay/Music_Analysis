import flask
import numpy as np
import pandas as pd
import pickle

#---------- MODEL IN MEMORY ----------------#

# Read the data on soccer match outcomes + team attributes,
# Build a Random Forest predictor on it


# load pickle files

# Nearest Neighbor outcome for songs
with open('data/nn_list.pkl', 'rb') as f:
    closest_song_ex = pickle.load(f)

# load dataframe, without audio features, but no missing lyrics
df_final_set = pd.read_pickle("data/billboard_tracks_1950_2018_FINAL_v2.pkl")



# Function to find similar artists related to main artist search
def find_artists(artist,track):
    
    final_dict = {}
    temp_list = []
    counter = 0
    
    # first get details for main song
    results = df_final_set[(df_final_set['artist']==artist) & (df_final_set['title']==track)] \
    [['track_album_cover_art','track_preview_url','artist','title','agg_genre','num_words', \
    'num_syllables','difficult_words','f_k_grade','sentiment_compound','tempo', \
    'acousticness','instrumentalness','loudness','speechiness','valence','year']].values
    
    
    # put main song details into a temporary list
    for i in range(17):
    	temp_list.append(results[0][i])

    # include main song features into a dictionary
    final_dict[str(counter)] = temp_list
    counter+=1
    
    # get song index of main song user searched
    song_index = df_final_set[(df_final_set['artist']==artist) & (df_final_set['title']==track)].index[0]
    
    # find similar songs with nearest neighbor
    close_songs = closest_song_ex[song_index][0][1:]
    
    # iterate through each similar track and gather details
    for i in close_songs:
        temp_list = []
        track_details = df_final_set.iloc[i,][['track_album_cover_art','track_preview_url','artist','title','agg_genre','num_words', \
        'num_syllables','difficult_words','f_k_grade','sentiment_compound','tempo', \
    	'acousticness','instrumentalness','loudness','speechiness','valence','year']]

    	# put each song's details into a temporary list
        for j in range(16):
        	temp_list.append(track_details[j])
        temp_list.append(str(track_details[16])) # weird behavior where year would append as an integer

        # include song features into a dictionary
        final_dict[str(counter)] = temp_list
        counter += 1
    
    return final_dict

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("index.html", 'r') as viz_file:
        return viz_file.read()

@app.route("/recommender")
def recommender():
    with open("recommender.html",'r') as viz_file:
        return viz_file.read()



# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"]) # url '/score' and method 'POST' is defined in the $.ajax section of recommender.html file
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """

    # Get decision score for our example that came with the request
    data = flask.request.json
    
    # grab artist details
    artist = data['artist']
    track = data['track']

    # find track details on main artist + similar artists
    results = find_artists(artist,track)

    # return results to web app
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)