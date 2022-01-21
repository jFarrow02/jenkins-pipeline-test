def validate_and_execute():
    try:
        return 1/0
    except ZeroDivisionError: # Specify a specific error type, or omit type to catch all errors
        print("Division by 0 is undefined. Exiting.")


validate_and_execute()