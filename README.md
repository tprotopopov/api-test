# API-Tests

## Overview


- This script is a testing suite for a Random Image API service, specifically targeting the https://dog.ceo/api/breeds/image/random endpoint. It uses the requests library to make HTTP requests to the API service.
- The script produces logs upon test execution in ```tests/test.log```.
- The script also produces XML test reports as ```test-reports/*.xml ```, providing detailed insights into each executed test.

## Python Setup Summary
Before running the tests make sure all required dependencies are installed:
   - To install python dependencies run: "python3 setup.py"
   - To execute tests run: "python3 test_dog_breed_random_image_api.py"
