import requests
from cachetools import TTLCache

# Create a cache with an expiration time of 10 seconds
cache = TTLCache(maxsize=100, ttl=10)


def get_page(url: str) -> str:
    # Check if the URL is already cached
    if url in cache:
        # Return the cached content
        return cache[url]

    # If not cached, make a request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text

        # Store the content in the cache with the URL as the key
        cache[url] = content

        # Increment the count for this URL
        count_key = f"count:{url}"
        count = cache.get(count_key, 0)
        cache[count_key] = count + 1

        return content

    return f"Failed to fetch URL: {url}"


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"

    for _ in range(5):
        print(get_page(url))

    print(f"Access count for {url}: {cache.get(f'count:{url}', 0)}")
