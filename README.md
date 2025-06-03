# LSEG-Tech-challenge
# User Creation Script - Support Engineer Coding Challenge

## Overview
Automates user account creation from CSV via HTTP POST. Includes error handling and field validation.

## Features
- Skips rows with missing `name`, `email`, or `role`
- Logs failures to `error_log.txt`
- Uses modular, readable code

## Files
- `create_users.py`: Main script
- `users.csv`: Sample input
- `error_log.txt`: Error log

## How It Works
1. Reads `users.csv`
2. Validates each row
3. Sends POST request
4. Logs errors

## Sample Input
```csv
name,email,role
Alice,alice@example.com,admin
Bob,,user
Charlie,charlie@example.com,moderator
