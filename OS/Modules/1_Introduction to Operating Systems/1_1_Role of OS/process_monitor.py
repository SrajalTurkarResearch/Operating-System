import psutil
import pandas as pd
import logging
from typing import List, Dict

# Configure logging for debugging and research traceability
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_process_data(top_n: int = 5) -> pd.DataFrame:
    """
    Collects data on running processes, focusing on CPU and memory usage.

    Args:
        top_n (int): Number of top processes to return (default: 5).

    Returns:
        pd.DataFrame: DataFrame with process name, CPU usage, and memory usage.

    Logic: Uses psutil to iterate over processes, abstracting system calls.
    """
    try:
        processes: List[Dict] = []
        for proc in psutil.process_iter(["name", "cpu_percent", "memory_info"]):
            try:
                processes.append(
                    {
                        "Name": proc.info["name"],
                        "CPU": proc.info["cpu_percent"],
                        "Memory_MB": proc.info["memory_info"].rss / 1024**2,
                    }
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                logging.warning(f"Skipping process {proc.pid} due to access issues.")
        df = pd.DataFrame(processes)
        return df.sort_values("CPU", ascending=False).head(top_n)
    except Exception as e:
        logging.error(f"Error collecting process data: {e}")
        return pd.DataFrame()


def save_process_data(df: pd.DataFrame, filename: str = "processes.csv") -> None:
    """
    Saves process data to a CSV file.

    Args:
        df (pd.DataFrame): Process data.
        filename (str): Output CSV file name.
    """
    try:
        df.to_csv(filename, index=False)
        logging.info(f"Process data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving process data: {e}")


if __name__ == "__main__":
    # Example usage
    df = get_process_data()
    print(df)
    save_process_data(df)
