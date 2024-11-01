import hashlib
import time

def hash_password(password):
    # FILL_CODE: Hash a password for storing, use SHA-256
    # Create a sha256 hash
    hash_object = hashlib.sha256(password.encode())
    # Return 
    return hash_object.hexdigest()

def verify_password(stored_password_hash, input_password):
    # FILL_CODE: Verify a stored password against one provided by the user
    # Hash the input password
    input_password_hash = hash_password(input_password)
    # Compare
    return stored_password_hash == input_password_hash

def log_failed_attempt(attempt_log_file):
     # Open the log file in append mode
    with open(attempt_log_file, 'a') as file:
         # Generate a timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
         # Write the failed attempt and timestamp to the file
        file.write(f"Failed login attempt at {timestamp}\n")
        
def main():
    password_file = 'password_hash.txt'
    attempt_log_file = 'attempt_log.txt'
    
    # FILL_CODE: Check if password_file exists and read the hashed password
    # If it doesn't exist, prompt the user to create a new password and write the hash to the file
    try:
          # Try to open the password file to read the stored password hash
        with open(password_file, 'r') as file:
            password_hash = file.read()
    except FileNotFoundError:
        while True:
            new_password = input("Create a new password: ")
            if len(new_password) >= 5:
                 # Hash the new password and write it to the password file
                password_hash = hash_password(new_password)
                with open(password_file, 'w') as file:
                    file.write(password_hash)
                break
            else:
                print("Password must be at least 5 characters.")

    attempts = 0
    # Allow up to 3 password attempts
    while attempts < 3:
        password_attempt = input("Enter your password: ")
        if verify_password(password_hash, password_attempt):
            # If password is correct, welcome the user
            print("Welcome back!")
            break
        else:
              # Log failed attempt and increment the attempt counter
            print("Password incorrect.")
            log_failed_attempt(attempt_log_file)
            attempts += 1
            if attempts == 3:
                 # After 3 failed attempts, lock out for 30 seconds
                print("Too many failed attempts. Please wait 30 seconds.")
                time.sleep(30)  # Pause the program for 30 seconds
                attempts = 0

if __name__ == "__main__":
    main()