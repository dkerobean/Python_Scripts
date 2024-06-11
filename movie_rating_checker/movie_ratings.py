import requests
import config
import logging
from datetime import timedelta
import requests_cache

# Retrieve the API key from the environment variable
API_KEY = config.OMDB_API_KEY
IBMD_ID = config.IBMD_ID

# implement logging
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'

logging.basicConfig(filename="rating.log", level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger()

if not API_KEY:
    raise ValueError("API key not found. Set the OMDB_API_KEY environment variable.")


base_url = f"https://www.omdbapi.com/?i={IBMD_ID}&apikey={API_KEY}"

header = {
    "accept": "application/json",
}

# Configure requests-cache
requests_cache.install_cache('omdb_cache', expire_after=timedelta(hours=1))


def get_movie_rating(title):
    url = base_url + f"&t={title}"
    log.info(f"Requesting URL: {url}")

    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        data = response.json()
        log.info("Recieved response from API")

        if 'Error' in data:
            log.error("Movie not found")
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
            log.info(f"Retrieved movie info {movie_info}")
            return movie_info

    except requests.exceptions.RequestException as e:
        log.error(f"Request failed: {e}")
        return "Error: Request failed"


if __name__ == "__main__":
    title = input("Enter movie title: ")
    movie_info = get_movie_rating(title)

    if isinstance(movie_info, dict):
        for key, value in movie_info.items():
            print(f"{key}: {value}")
    else:
        print(movie_info)


