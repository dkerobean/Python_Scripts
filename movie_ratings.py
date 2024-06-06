
import requests

API_KEY = 'e25d2434'

base_url = f"https://www.omdbapi.com/?i=tt3896198&apikey={API_KEY}"

header = {
    "accept": "application/json",
}


def get_movie_rating(title):
    url = base_url + f"t={title}"
    response = requests.get(url, headers=header)
    data = response.json()

    if 'Error' in data:
        return "Error: Movie not found"
    else:
        movie_info = {
            "Title": data.get("Title", ""),
            "Year": data.get("Year", ""),
            "Genre": data.get("Genre", ""),
            "imdbRating": data.get("imdbRating", ""),
            "imdbVotes": data.get("imdbVotes", ""),
            "Plot": data.get("Plot", "")
        }
        return movie_info


title = input("Enter movie title: ")
movie_info = get_movie_rating(title)
print(movie_info)
