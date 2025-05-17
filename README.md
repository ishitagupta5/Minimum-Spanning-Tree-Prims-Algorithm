# Prim's Algorithm: Minimum Spanning Tree Generator

This Python project generates a **Minimum Spanning Tree (MST)** from a graph represented as an adjacency matrix in CSV format, using **Prim's Algorithm**. It logs each selected edge and the total weight of the MST in an output text file.

## Features

- Reads input graph from a CSV file (adjacency matrix format)
- Implements Prim's algorithm from scratch
- Logs every selected edge and the total MST weight
- Efficient for sparse and dense graphs

---

## What is Prim's Algorithm?

Prim’s Algorithm is a **greedy algorithm** that finds a **Minimum Spanning Tree (MST)** for a connected weighted undirected graph. The MST connects all the vertices in the graph with the **minimum total edge weight** and **no cycles**.

**How it works**:
- Start with any node (in this case, vertex `0`)
- Repeatedly add the **lowest-weight edge** that connects a node **in** the MST to a node **not yet included**
- Stop when all vertices are part of the MST

This ensures a minimum-cost network connecting all nodes.

---

## How the Script Works

1. The input CSV file contains:
   - The first element: number of vertices `n`
   - The rest: a flattened `n x n` adjacency matrix
2. The script:
   - Parses the CSV
   - Extracts edges and their weights
   - Sorts the edges
   - Applies Prim’s algorithm to grow the MST
   - Writes the selected edges and the final MST weight to a `.txt` file

---

## Files

| File | Description |
|------|-------------|
| `prims.py` | Main script that runs Prim's algorithm |
| `deliverablefile1.csv`, `deliverablefile2.csv`, etc. | Input CSVs with graph data (provided by professor) |
| `deliverablefile1.txt`, `deliverablefile2.txt` | Output files showing selected MST edges and total weight |

---

## Getting Started

1. Clone the repo and navigate to the project directory.
2. Ensure your CSV file is named appropriately.
3. Run:
   ```bash
   python prims.py
