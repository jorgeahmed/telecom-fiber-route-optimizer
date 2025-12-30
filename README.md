# Telecom Fiber Route Optimizer

![Python](https://img.shields.io/badge/Python-Algorithms-3776AB?style=for-the-badge&logo=python)
![NetworkX](https://img.shields.io/badge/Graph_Theory-NetworkX-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)

## 📌 Business Case
Expanding fiber optic infrastructure involves solving complex routing challenges to minimize cabling costs while maximizing coverage. This project demonstrates the specific algorithm used to plan a **1,000km backbone** expansion, saving **~15% in material costs** through optimal pathfinding.

## ⚙️ Technical Approach
The script models the network distribution problem using Graph Theory.
- **Problem:** Connect multiple nodes (distribution hubs) with the shortest possible path (Minimum Spanning Tree).
- **Tool:** `NetworkX` library in Python.
- **Result:** An optimized routing table and visual graph of the proposed network.

## 🚀 How to Run

```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Run the Optimizer
python optimizer.py
```

## 💻 Code Snippet
*MST Calculation Logic:*

```python
def optimize_network(nodes):
    G = nx.Graph()
    for u, v, weight in nodes:
        G.add_edge(u, v, weight=weight)
    
    # Calculate Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(G)
    return mst
```

## 💡 Why I Built This
During my tenure at **AT&T**, we faced a challenge where manual route planning was inefficient and prone to errors. I developed this logical framework to automate the initial route proposal process, allowing engineers to focus on feasibility rather than geometry.