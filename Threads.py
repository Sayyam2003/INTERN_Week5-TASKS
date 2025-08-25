import threading
import requests
import time

# List of 5 URLs to download
urls = [
    'https://example.com',
    'https://www.python.org',
    'https://www.wikipedia.org',
    'https://www.openai.com',
    'https://httpbin.org/get'
]

# Function to download and save a single URL
def download_and_save(url, index):
    try:
        response = requests.get(url)
        with open(f'file_{index}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Downloaded {url} into file_{index}.html")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Measure start time
start_time = time.time()

# Create and start threads
threads = []
for i, url in enumerate(urls):
    thread = threading.Thread(target=download_and_save, args=(url, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Measure end time
end_time = time.time()

# Print total time taken
print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")
