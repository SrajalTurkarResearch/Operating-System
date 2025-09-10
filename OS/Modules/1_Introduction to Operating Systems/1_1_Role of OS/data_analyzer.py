import psutil
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_memory_limit(max_memory_mb: float) -> bool:
    """
    Checks if system memory usage exceeds a simulated VM limit.

    Args:
        max_memory_mb (float): Maximum allowed memory in MB.

    Returns:
        bool: True if within limit, False otherwise.
    """
    try:
        mem = psutil.virtual_memory()
        used_mb = mem.used / 1024**2
        if used_mb > max_memory_mb:
            logging.warning(
                f"Memory usage ({used_mb:.2f} MB) exceeds VM limit ({max_memory_mb} MB)"
            )
            return False
        logging.info(f"Memory usage ({used_mb:.2f} MB) within limit")
        return True
    except Exception as e:
        logging.error(f"Error checking memory limit: {e}")
        return False


def analyze_iris_dataset() -> pd.DataFrame:
    """
    Loads and analyzes the Iris dataset, simulating a virtualized environment.

    Returns:
        pd.DataFrame: Statistical summary of the dataset.
    """
    try:
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        stats = df.describe()
        logging.info("Iris dataset analysis completed")

        # Visualize
        plt.figure(figsize=(8, 6))
        plt.scatter(
            df["sepal length (cm)"],
            df["sepal width (cm)"],
            c=iris.target,
            cmap="viridis",
        )
        plt.title("Iris Sepal Dimensions")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Sepal Width (cm)")
        plt.tight_layout()
        plt.show()

        return stats
    except Exception as e:
        logging.error(f"Error analyzing Iris dataset: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # Example usage
    if check_memory_limit(100):
        stats = analyze_iris_dataset()
        print("Iris Dataset Statistics:\n", stats)
