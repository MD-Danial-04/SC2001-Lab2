import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from benchmarks import run_experiments
from plot_results import plot_results


def main():
    results = run_experiments()
    for path in plot_results(results):
        print(f"Saved {path}")


if __name__ == "__main__":
    main()
