# Password Hasher and Verification

This program is a simple password management tool written in Python that allows a user to create a secure password, stores it as a hashed value, and verifies user login attempts. Failed login attempts are logged with a timestamp, and the program includes a lockout period after multiple failed attempts.

## Features

- **Password Hashing**: Utilizes SHA-256 hashing to securely store passwords.
- **Password Verification**: Checks user-provided passwords against the stored hash.
- **Failed Attempt Logging**: Records the date and time of failed login attempts in a log file.
- **Lockout Mechanism**: Locks out users for 30 seconds after 3 failed attempts.

## How to Use

1. **First-Time Setup**: When run for the first time, the program will prompt the user to create a new password. This password will be hashed and saved in `password_hash.txt`.
2. **Login**: On subsequent runs, the user will be prompted to enter the password for verification.
3. **Logging**: Failed login attempts are recorded in `attempt_log.txt` with a timestamp.
4. **Lockout**: After 3 failed attempts, the user will be locked out for 30 seconds.

## Files

- `password_hash.txt`: Stores the hashed version of the user's password.
- `attempt_log.txt`: Logs failed login attempts with timestamps.

## Example Usage

1. Run the program.
2. If it's your first time, create a new password.
3. Enter your password for verification.
4. If the password is incorrect, the attempt is logged. After 3 incorrect attempts, the user is locked out for 30 seconds.

## Requirements

- Python 3.x

## License

This project is open-source and free to use.
