# Data Structures and Algorithms in Python

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Alexandria University](https://img.shields.io/badge/Coursework-Data%20Structures-green)](https://eng.alexu.edu.eg/)

Comprehensive implementations, empirical benchmarking, and problem sets covering fundamental Data Structures and Algorithms (DSA) in Python, completed as part of the Computer and Communication Engineering coursework at Alexandria University.

---

## Repository Structure

```text
DataStructure-2/
├── Assignment-1/
│ └── SortingAlgorithmsP1/
│ ├── SortingAlgorithms.py # Bubble Sort, Selection Sort, Insertion Sort
│ └── TestImplementation.ipynb # Empirical benchmarking & runtime analysis
├── Assignment-2/
│ └── Sorting_algo_p2.py # Divide-and-conquer sorting (Merge Sort)
├── lab1.py # Binary Search implementation
├── sheet1.py # Array problem set: second largest element
├── sheet1.2.py # Recursive maximum finding algorithm
└── README.md # Repository documentation
```

---

## Implemented Algorithms and Complexity

| Algorithm | Category | Best Time | Average Time | Worst Time | Space Complexity | Implementation File |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | Comparison Sorting | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | `Assignment-1/.../SortingAlgorithms.py` |
| **Selection Sort** | Comparison Sorting | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | `Assignment-1/.../SortingAlgorithms.py` |
| **Insertion Sort** | Comparison Sorting | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | `Assignment-1/.../SortingAlgorithms.py` |
| **Merge Sort** | Divide & Conquer | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | `Assignment-2/Sorting_algo_p2.py` |
| **Binary Search** | Searching | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | `lab1.py` |
| **Recursive Max** | Recursion | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ (Call stack) | `sheet1.2.py` |

---

## How to Run

### Run Python Scripts
```bash
python lab1.py
python sheet1.py
python sheet1.2.py
```

### Run Sorting Benchmark Notebook
```bash
pip install jupyter matplotlib
jupyter notebook Assignment-1/SortingAlgorithmsP1/TestImplementation.ipynb
```
