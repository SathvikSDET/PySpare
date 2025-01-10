import logging

class Log:
    def __init__(self, log_file="app.log"):
        # Create a logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG (you can change it to INFO, WARNING, etc.)
        
        # Create a file handler to log messages to a file
        file_handler = logging.FileHandler(log_file)
        
        # Create a formatter and set it for the handler
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        
        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def log_message(self, level, message):
        """
        Logs the message at a specified level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        """
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.info(message)  # Default to info if the level is not recognized

# Example usage:
if __name__ == "__main__":
    log = Log("app.log")  # Create the Log object and specify log file name
    log.log_message("info", "This is an info message")
    log.log_message("warning", "This is a warning message")
    log.log_message("error", "This is an error message")
