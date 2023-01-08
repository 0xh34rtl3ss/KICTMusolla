import random
import time

import json

def generate_incremental_int():
    # Set the initial value of the counter
    counter = 0

    # Use a while loop to generate incremental integers
    while True:
        counter += 1  # Increment the counter
        yield counter  # Yield the current value of the counter

def return_json():
    # Call the generate_incremental_int function
    generator = generate_incremental_int()

    # Get the next value from the generator
    value = next(generator)

    # Return the value in a JSON format
    return json.dumps({"value": value})

