# Prim's Algorithm: Minimum Spanning Tree Generator

This Python project generates a **Minimum Spanning Tree (MST)** from a graph represented as an adjacency matrix in CSV format, using **Prim's Algorithm**. It logs each selected edge and the total weight of the MST in an output text file.

## 📌 Features

- Reads input graph from a CSV file (adjacency matrix format)
- Implements Prim's algorithm from scratch
- Writes step-by-step edge selection and final MST weight to a `.txt` file

## How It Works

1. The CSV contains the number of vertices followed by a flattened adjacency matrix.
2. The script reads the matrix and constructs a list of all edges with their weights.
3. Prim's algorithm is applied:
   - Starts from vertex `0`
   - Iteratively selects the minimum-weight edge connecting to a new vertex
4. The selected edges and total weight are saved to an output file.

## Files

| File | Description |
|------|-------------|
| `prims.py` | Main script that runs Prim's algorithm |
| `deliverablefile1.csv`, `deliverablefile2.csv`, etc. | Input CSVs with graph data (provided by professor) |
| `deliverablefile1.txt`, `deliverablefile2.txt` | Output files showing selected MST edges and weights |

## Getting Started

1. Clone the repo and navigate to the directory
2. Run:
   ```bash
   python prims.py
