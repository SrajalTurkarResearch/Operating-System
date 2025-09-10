import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Saves a DataFrame to a CSV file with error handling.

    Args:
        df (pd.DataFrame): DataFrame to save.
        filename (str): Output file name.
    """
    try:
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {e}")


def log_message(message: str, level: str = "info") -> None:
    """
    Logs a message at the specified level.

    Args:
        message (str): Message to log.
        level (str): Logging level ('info', 'warning', 'error').
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.error(f"Invalid log level: {level}")
