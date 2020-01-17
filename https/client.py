import os
import requests

def get_secret_message():
    response = requests.get("http://localhost:5683", verify="ca-public-key.pem")
    print(f"The secret message is {response.text}")


if __name__ == "__main__":
    get_secret_message()