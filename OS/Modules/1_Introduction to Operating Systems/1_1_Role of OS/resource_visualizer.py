import matplotlib.pyplot as plt
import psutil
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def plot_cpu_usage(samples: int = 10, interval: float = 1.0) -> None:
    """
    Plots CPU usage over time.

    Args:
        samples (int): Number of samples to collect.
        interval (float): Seconds between samples.

    Logic: Visualizes OS scheduling dynamics.
    """
    try:
        cpu_data: List[float] = []
        for _ in range(samples):
            cpu_data.append(psutil.cpu_percent(interval=interval))

        plt.figure(figsize=(8, 4))
        plt.plot(cpu_data, marker="o", color="blue")
        plt.title("CPU Usage Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("CPU Usage (%)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        logging.info("CPU usage plot generated")
    except Exception as e:
        logging.error(f"Error plotting CPU usage: {e}")


def plot_vm_allocation(allocations: dict, total_cpu: float = 100.0) -> None:
    """
    Plots a pie chart of virtual machine CPU allocations.

    Args:
        allocations (dict): VM names and their CPU percentages.
        total_cpu (float): Total CPU percentage available.

    Logic: Demonstrates virtualization resource slicing.
    """
    try:
        used = sum(allocations.values())
        labels = list(allocations.keys()) + ["Free"]
        sizes = list(allocations.values()) + [total_cpu - used]

        plt.figure(figsize=(6, 6))
        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            colors=["lightblue", "lightgreen", "lightcoral", "lightgray"],
        )
        plt.title("CPU Allocation in Virtualization")
        plt.tight_layout()
        plt.show()
        logging.info("VM allocation pie chart generated")
    except Exception as e:
        logging.error(f"Error plotting VM allocation: {e}")


if __name__ == "__main__":
    # Example usage
    plot_cpu_usage(samples=5)
    plot_vm_allocation({"VM1": 30, "VM2": 40, "Hypervisor": 10})
