import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from dataset_gen import edges_to_list, edges_to_matrix, generate_graph
from djikstra_matrix import djikstra as dijkstra_matrix
from djikstra_heap import djikstra as dijkstra_heap


def benchmark(V, E, trials=5):

    # Generate ONE graph
    edges = generate_graph(V, E)

    # Convert same graph into both representations
    matrix = edges_to_matrix(V, edges)
    adj_list = edges_to_list(V, edges)

    matrix_times = []
    heap_times = []

    for _ in range(trials):

        # Matrix + Array PQ
        start = time.perf_counter()
        result_matrix = dijkstra_matrix(matrix, 0)
        end = time.perf_counter()

        matrix_times.append(end - start)

        # Adjacency List + Min Heap
        start = time.perf_counter()
        result_heap = dijkstra_heap(adj_list, 0)
        end = time.perf_counter()

        heap_times.append(end - start)

    # Make sure both algorithms produced the same result
    assert result_matrix == result_heap

    return {
        "V": V,
        "E": E,
        "matrix_time": statistics.median(matrix_times),
        "heap_time": statistics.median(heap_times)
    }


# ============================================================
# 7. Run experiments
# ============================================================

datasets = [
    (100, 200),
    (100, 500),
    (100, 1000),

    (500, 1000),
    (500, 5000),
    (500, 20000),

    (1000, 2000),
    (1000, 10000),
    (1000, 50000),
]

def run_experiments():
    results = []

    for V, E in datasets:

        print(f"Testing V={V}, E={E}...")

        result = benchmark(V, E)

        results.append(result)

        print(
            f"Matrix: {result['matrix_time']:.6f}s | "
            f"Heap: {result['heap_time']:.6f}s"
        )

    print("\nFinal Results")
    print("-" * 60)

    for result in results:

        print(
            f"V={result['V']:5} "
            f"E={result['E']:7} | "
            f"Matrix={result['matrix_time']:.6f}s | "
            f"Heap={result['heap_time']:.6f}s"
        )

    return results


if __name__ == "__main__":
    run_experiments()
