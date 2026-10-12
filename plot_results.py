from pathlib import Path

import matplotlib.pyplot as plt

MATRIX_COLOR = "#3d5a80"
HEAP_COLOR = "#d4762c"
OUTPUT_DIR = Path(__file__).resolve().parent / "graphs"


def plot_results(results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    saved = [
        _plot_runtime_vs_edges(results),
        _plot_runtime_vs_vertices(results),
        _plot_speedup(results),
    ]
    return saved


def _plot_runtime_vs_edges(results):
    grouped = {}
    for result in results:
        grouped.setdefault(result["V"], []).append(result)

    fig, axes = plt.subplots(1, len(grouped), figsize=(12, 4.2), sharey=False)
    for ax, vertex_count in zip(axes, sorted(grouped)):
        rows = sorted(grouped[vertex_count], key=lambda row: row["E"])
        edges = [row["E"] for row in rows]
        ax.plot(
            edges,
            [row["matrix_time"] * 1000 for row in rows],
            marker="o",
            color=MATRIX_COLOR,
            label="Matrix + array",
        )
        ax.plot(
            edges,
            [row["heap_time"] * 1000 for row in rows],
            marker="s",
            color=HEAP_COLOR,
            label="Adjacency list + heap",
        )
        ax.set_title(f"V = {vertex_count}")
        ax.set_xlabel("Edges")
        ax.set_ylabel("Median runtime (ms)")
        ax.set_yscale("log")
        ax.grid(True, which="both", linestyle=":", linewidth=0.6)
        ax.legend(frameon=False)

    fig.suptitle("Dijkstra median runtime versus edges")
    fig.tight_layout()
    path = OUTPUT_DIR / "runtime_vs_edges.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def _plot_runtime_vs_vertices(results):
    sparse = sorted(
        [row for row in results if row["E"] == 2 * row["V"]],
        key=lambda row: row["V"],
    )
    vertices = [row["V"] for row in sparse]

    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.plot(
        vertices,
        [row["matrix_time"] * 1000 for row in sparse],
        marker="o",
        color=MATRIX_COLOR,
        label="Matrix + array",
    )
    ax.plot(
        vertices,
        [row["heap_time"] * 1000 for row in sparse],
        marker="s",
        color=HEAP_COLOR,
        label="Adjacency list + heap",
    )
    ax.set_title("Dijkstra median runtime versus vertices (E = 2V)")
    ax.set_xlabel("Vertices")
    ax.set_ylabel("Median runtime (ms)")
    ax.set_yscale("log")
    ax.set_xticks(vertices)
    ax.grid(True, which="both", linestyle=":", linewidth=0.6)
    ax.legend(frameon=False)
    fig.tight_layout()
    path = OUTPUT_DIR / "runtime_vs_vertices.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def _plot_speedup(results):
    labels = [f"V={row['V']}\nE={row['E']}" for row in results]
    speedup = [row["matrix_time"] / row["heap_time"] for row in results]

    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.bar(labels, speedup, color=HEAP_COLOR)
    ax.set_title("Heap speedup over the matrix implementation")
    ax.set_xlabel("Graph size")
    ax.set_ylabel("Median runtime ratio (matrix / heap)")
    ax.grid(True, axis="y", linestyle=":", linewidth=0.6)
    fig.tight_layout()
    path = OUTPUT_DIR / "heap_speedup.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path
