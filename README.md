# k-way-merge-transaction-system
K-way merge using min heap vs pairwise merging
Nanditha P Nambiar
## Problem
A financial system receives three sorted transaction lists:
- L1 = 10, 30, 50, 70
- L2 = 20, 40, 60, 80
- L3 = 15, 35, 55, 75

## Solution
See `kway_merge.py` for both implementations:
- Part a) K-way merge using Min Heap
- Part b) Pairwise merging approach

## Analysis (Part c)

| Metric | Min-Heap | Pairwise |
|---|---|---|
| Heap/temp size | O(k) | O(n) |
| Comparisons | O(n log k) | O(nk) |
| Time complexity | O(n log k) | O(nk) |
| Space complexity | O(k) | O(n) |

**Conclusion:** As the number of sorted files (k) increases, the Min-Heap approach becomes more suitable since it scales better — each insertion/extraction costs only O(log k), while pairwise merging repeats an O(n) merge step k−1 times, making its cost grow linearly with k.
