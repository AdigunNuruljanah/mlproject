import sys  # Provides access to Python's system-specific functions and exception information


def error_message_detail(error, error_detail):
    """
    Creates a detailed error message containing:
    - The Python file where the error occurred
    - The line number where the error occurred
    - The actual error message
    """

    # Get the exception information:
    # _  = exception type
    # _  = exception value
    # exc_tb = traceback object containing information about where the error occurred
    _, _, exc_tb = error_detail.exc_info()

    # Get the name/path of the Python file where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed error message
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(
        file_name,           # {0} → file name
        exc_tb.tb_lineno,    # {1} → line number
        str(error)           # {2} → actual error message
    )

    # Return the formatted error message
    return error_message


class CustomException(Exception):
    """
    Custom exception class.
    This allows us to create more informative error messages.
    """

    def __init__(self, error_message, error_detail):

        # Initialize the parent Exception class
        super().__init__(error_message)

        # Generate our detailed error message
        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.error_message