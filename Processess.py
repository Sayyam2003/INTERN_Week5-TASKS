from multiprocessing import Pool, cpu_count
import time

# Function to square a number
def square(x):
    return x * x

if __name__ == '__main__':
    # Create a large list of numbers (e.g., 10 million)
    numbers = list(range(10_000_000))

    # Measure start time
    start_time = time.time()

    # Create a Pool using all available CPUs
    with Pool(processes=cpu_count()) as pool:
        # Map the square function to the list
        results = pool.map(square, numbers)

    # Measure end time
    end_time = time.time()

    print(f"First 10 results: {results[:10]}")
    print(f"\nTotal time taken with multiprocessing: {end_time - start_time:.2f} seconds")
