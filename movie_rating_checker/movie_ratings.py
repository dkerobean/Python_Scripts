import requests
import config

# Retrieve the API key from the environment variable
API_KEY = config.OMDB_API_KEY
IBMD_ID = config.IBMD_ID

if not API_KEY:
    raise ValueError("API key not found. Set the OMDB_API_KEY environment variable.")


base_url = f"https://www.omdbapi.com/?i={IBMD_ID}&apikey={API_KEY}"

header = {
    "accept": "application/json",
}


def get_movie_rating(title):
    url = base_url + f"&t={title}"
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


if __name__ == "__main__":
    title = input("Enter movie title: ")
    movie_info = get_movie_rating(title)
    print(movie_info)
