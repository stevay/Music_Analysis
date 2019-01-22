# Music EDA Passion Project

Purpose of this project is to look at the Billboard Hot 100 songs from 1950-2018 and see how music has evolved over the last 65+ years. 

To gather both artist and track names associated with the Billboard Hot 100 charts, we will be using a dataset curated and shared by Kevin Schaich ([github page available](https://github.com/kevinschaich/billboard/tree/master/data/years)) as well as Wikipedia (for Billboard Hot 100 charts between 2016-[2018](https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2018))

We will also use the Spotify API to get additional audio features (e.g. instrumentalness) associated with the songs of interest. Connecting to the Spotify API is done via a Python library called [Spotipy](https://spotipy.readthedocs.io/en/latest/).

A Flask app will be built that allows end-users to:
- Look up Billboard Hot 100 singles (any song between 1950 to 2018)
- Provide statistics associated with searched song (e.g. tempo; year on Billboard Hot 100 chart)
- Based on searched song, recommend four other popular songs based on song lyrics

Blog post associated with project can be found [here](https://stevay.github.io/Music-Analysis/)
