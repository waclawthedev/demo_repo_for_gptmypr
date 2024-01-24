import json
import requests


def fetch_random_user():
    response = requests.get("https://randomuser.me/api/")
    return response.json()


def save_user_to_file(user_data, filename):
    with open(filename, "w") as file:
        json.dump(user_data, file, indent=4)


def read_user_from_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


def print_user(user):
    name = user["results"][0]["name"]
    print(f"Name: {name['title']} {name['first']} {name['last']}")
    email = user["results"][0]["email"]
    print(f"Email: {email}")


def main():
    user_data = fetch_random_user()
    file_name = "random_user.json"

    save_user_to_file(user_data, file_name)
    print(f"User data has been saved to {file_name}")

    saved_user_data = read_user_from_file(file_name)

    print("Here is the fetched user data:")
    print_user(saved_user_data)


if __name__ == "__main__":
    main()
