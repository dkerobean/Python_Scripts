# Movie Rating Script

This script allows you to retrieve ratings and other information about movies using the OMDb API.

## Prerequisites

Before running this script, ensure you have Python installed on your system.

## Setup

1. Clone this repository to your local machine.

2. Install the required dependencies by running: pip install -r requirements.txt

3. Obtain an API key from [OMDb API](https://www.omdbapi.com/) and set it as an environment variable named `OMDB_API_KEY`.

4. Optionally, set the IMDb ID of your choice as an environment variable named `IMDB_ID`.

## Usage

1. Run the script by executing: python movie_rating.py

2. Enter the title of the movie when prompted.

3. The script will fetch and display the ratings and other information for the entered movie.

## Example

$ python movie_rating.py
Enter movie title: The Dark Knight
Title: The Dark Knight
Year: 2008
Genre: Action, Crime, Drama, Thriller
imdbRating: 9.0
imdbVotes: 2,485,633
Plot: When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.


