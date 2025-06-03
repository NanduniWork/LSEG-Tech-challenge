import csv
import requests

ERROR_LOG_FILE = "error_log.txt"
API_URL = "https://example.com/api/create_user"

def log_error(message):
    """Log error messages to a file."""
    with open(ERROR_LOG_FILE, "a") as error_file:
        error_file.write(message + "\n")

def is_valid_user(row):
    """Check if required fields are present and valid."""
    return row.get("email") and row.get("name") and row.get("role")

def create_user(user_data):
    """Send POST request to create a single user."""
    try:
        response = requests.post(API_URL, json=user_data)
        if response.status_code != 201:
            error_message = f"Error creating user {user_data.get('email')}: Status {response.status_code} - {response.text}"
            print(error_message)
            log_error(error_message)
    except requests.RequestException as e:
        error_message = f"Exception creating user {user_data.get('email')}: {e}"
        print(error_message)
        log_error(error_message)

def create_users(file_path):
    """Main function to read CSV and process user creation."""
    with open(file_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not is_valid_user(row):
                print(f"Skipping invalid row: {row}")
                log_error(f"Skipped row due to missing fields: {row}")
                continue
            create_user(row)

if __name__ == "__main__":
    create_users("users.csv")
