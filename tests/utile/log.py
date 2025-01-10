import logging
import os
from datetime import datetime

class Log:
    def __init__(self, class_name):

         # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create a dynamic log directory
        log_dir = os.path.join(os.getcwd(),"PySpare", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"{class_name}_{timestamp}.log")

        self.logger = logging.getLogger(class_name)
        self.logger.setLevel(logging.DEBUG)  
      
        file_handler = logging.FileHandler(log_file)
        
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        
        
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
            self.logger.info(message)  


if __name__ == "__main__":
    log = Log(__name__) 
     #
    log.log_message("info", "This is an info message")
    log.log_message("warning", "This is a warning message")
    log.log_message("error", "This is an error message")
