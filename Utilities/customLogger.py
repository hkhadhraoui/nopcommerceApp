import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_dir = ".\\Logs"
        os.makedirs(log_dir, exist_ok=True)  # ✅ create folder if missing
        log_file = os.path.join(log_dir, "automation.log")

        # Remove existing handlers (so logs don’t get blocked by pytest or duplicate)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=log_file,
                           format='%(asctime)s %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger