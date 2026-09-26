"""
K-way Merge of Sorted Transaction Lists
----------------------------------------
Compares two approaches to merging k sorted lists:
  a) Min-Heap based k-way merge
  b) Pairwise (sequential) merging
"""

import heapq


def k_way_merge_heap(lists, verbose=True):
    heap = []
    result = []
    heap_pushes = 0
    heap_pops = 0

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
            heap_pushes += 1

    if verbose:
        print("Initial heap:", heap)

    while heap:
        value, list_idx, elem_idx = heapq.heappop(heap)
        heap_pops += 1
        result.append(value)

        if verbose:
            print(f"Popped {value} from L{list_idx+1} | "
                  f"Heap now: {heap} | Result so far: {result}")

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            next_val = lists[list_idx][next_idx]
            heapq.heappush(heap, (next_val, list_idx, next_idx))
            heap_pushes += 1

    stats = {
        "heap_pushes": heap_pushes,
        "heap_pops": heap_pops,
        "max_heap_size": len(lists),
        "approx_comparisons": heap_pushes + heap_pops,
    }
    return result, stats


def merge_two_lists(a, b, counter):
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        counter["comparisons"] += 1
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


def pairwise_merge(lists, verbose=True):
    counter = {"comparisons": 0}
    result = lists[0]

    for idx in range(1, len(lists)):
        result = merge_two_lists(result, lists[idx], counter)
        if verbose:
            print(f"After merging with L{idx+1}: {result}")

    stats = {
        "comparisons": counter["comparisons"],
        "max_temp_array_size": len(result),
    }
    return result, stats


if __name__ == "__main__":
    L1 = [10, 30, 50, 70]
    L2 = [20, 40, 60, 80]
    L3 = [15, 35, 55, 75]
    lists = [L1, L2, L3]

    print("=" * 50)
    print("K-WAY MERGE USING MIN HEAP")
    print("=" * 50)
    heap_result, heap_stats = k_way_merge_heap(lists)
    print("\nFinal merged result:", heap_result)
    print("Stats:", heap_stats)

    print("\n" + "=" * 50)
    print("PAIRWISE MERGING")
    print("=" * 50)
    pair_result, pair_stats = pairwise_merge(lists)
    print("\nFinal merged result:", pair_result)
    print("Stats:", pair_stats)

    print("\n" + "=" * 50)
    print("COMPARISON SUMMARY")
    print("=" * 50)
    print(f"{'Metric':<25}{'Heap Approach':<20}{'Pairwise Approach'}")
    print(f"{'Max heap/temp size':<25}{heap_stats['max_heap_size']:<20}"
          f"{pair_stats['max_temp_array_size']}")
    print(f"{'Time complexity':<25}{'O(n log k)':<20}{'O(nk)'}")
    print(f"{'Space complexity':<25}{'O(k)':<20}{'O(n)'}")
