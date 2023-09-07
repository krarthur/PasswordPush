import requests
import json

def generate_pwpush_link():
    # Get password input from the user
    password = input("Enter the user's password you want to share: ")

    # Define the API endpoint
    url = "https://pwpush.com/p.json"

    # Define the payload with password details
    payload = {
        "password": {
            "payload": password,
            "expire_after_days": 7,  # The link will expire after 7 days
            "expire_after_views": 5  # The link will expire after 5 views
        }
    }

    # Send a POST request to the pwpush API
    response = requests.post(url, json=payload)


# Check if the request was successful
    if response.status_code == 201:
        data = response.json()
        link = f"https://pwpush.com/p/{data['url_token']}"
        print(f"Here's your secure link: {link}")
    else:
        print("Failed to generate the link. Please try again.")


if __name__ == "__main__":
    generate_pwpush_link()
