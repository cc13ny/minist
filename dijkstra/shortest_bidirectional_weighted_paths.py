"""
bi-directional, weighted
"""

import collections
import heapq
from typing import List


class WeightedPathsAlgorithms:

    def __init__(self, weights: List[tuple]):
        self.weights = weights
        self.min_dists = []
        self.prevs = []

    def _build_adj_list(self):
        adj_list = collections.defaultdict(list)
        for v1, v2, w in self.weights:
            adj_list[v1].append((w, v2))
            adj_list[v2].append((w, v1))
        return adj_list

    # Dijkstra's algorithm
    # Note: O((V+E) log (V+E)) instead of O((V+E) log (V)) because the lack of 'sift down'
    def build_shortest_weighted_pathes(self, start: int) -> None:
        adj_list = self._build_adj_list()
        self.start = start  # ToDO: fix 'instance attribute start defined outside __init__'

        if start not in adj_list:
            return []

        min_dists = {}
        prevs = collections.defaultdict(list)

        dist_hp = [(0, start, None)]  # distance, vertex, prevous_vertex
        while dist_hp:
            d, v1, prev = heapq.heappop(dist_hp)

            # with the characteristic of min heap/ priority queue,
            # the 1st occurrence of any vertex will set the short distance from start to that vertex.
            if v1 not in min_dists:  # TODO: with 'sift down', we don't need it
                prevs[v1].append(prev)
                min_dists[v1] = d
                for w, v2 in adj_list[v1]:
                    if v2 not in min_dists:  # TODO: with 'sift down', we don't need it
                        # since we cannot decrease priority in the heap directly in python,
                        # which is called 'sift down', we add the new priority/distance to
                        # the queue instead. However, by doing so, it increases the time complexity
                        # because of the increasing size of the heap.
                        heapq.heappush(dist_hp, (w + d, v2, v1))
            elif min_dists[v1] == d:
                prevs[v1].append(prev)

        self.min_dists = min_dists  # ToDO: fix 'instance attribute start defined outside __init__'
        self.prevs = prevs  # ToDO: fix 'instance attribute start defined outside __init__'

    def get_mini_dists(self):
        return self.min_dists

    def get_prevs(self):
        return self.prevs

    def _get_shortest_paths_recursive(self, start, end):
        if end not in self.min_dists:
            return []

        if start == end:
            return [[start]]

        paths = []
        for prev in self.prevs[end]:
            prev_paths = self._get_shortest_paths_recursive(start, prev)
            for prev_path in prev_paths:
                paths.append(prev_path + [end])

        return paths  # e.g [[1, 3, 5], [1, 5]]

    def get_shortest_paths_recursive(self, end):
        return self._get_shortest_paths_recursive(self.start, end)

    def get_shortest_paths_iterative(self, end):
        if end not in self.min_dists:
            return []

        paths = [[end]]
        q = [(end, 0)]
        while q:
            v, pid = q.pop(0)
            path = paths[pid]
            new_path_cnt = 0
            for prev in self.prevs[v]:
                if prev:
                    # here is the trick to ensure the 'pid's in the queue
                    # are fixed when new paths are added.
                    new_path_cnt += 1
                    if new_path_cnt == 1:
                        paths[pid] = [prev] + path
                        q.append((prev, pid))
                    else:
                        paths.append([prev] + path)
                        q.append((prev, len(paths)-1))
        return paths

    def check_route_if_passed_for_min_dist(self, end):
        yes, no = 'Yes', 'No'
        routes_passed = [no] * len(self.weights)

        # Step 1: map each route to the idx.
        edge2idx = {}
        for i, weight in enumerate(self.weights):
            v1, v2, w = weight
            edge2idx[(v1, v2)] = i
            edge2idx[(v2, v1)] = i

        # Step 2: DFS from end through prev where
        #         it includes the shortest paths from start to end.
        q = [end]
        while q:
            v = q.pop(0)
            for prev in self.prevs[v]:
                if prev:
                    if (prev, v) in edge2idx:
                        idx = edge2idx[(prev, v)]
                        routes_passed[idx] = yes
                    if (v, prev) in edge2idx:
                        idx = edge2idx[(v, prev)]
                        routes_passed[idx] = yes

                    q.append(prev)
        return routes_passed


if __name__ == '__main__':
    break_line = "=" * 40

    weights1 = [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1), (5, 1, 3), (1, 3, 2), (5, 3, 1)]

    algs1 = WeightedPathsAlgorithms(weights1)
    start1, end1 = 1, 5
    algs1.build_shortest_weighted_pathes(start1)
    print("Shortest Paths:")
    print(algs1.get_mini_dists())
    print("Previous Vertex in the shortest paths:")
    print(algs1.get_prevs())
    print("Expected result: [[1, 5], [1, 3, 5], [1, 2, 3, 5]]\n")
    print("By recursion:")
    print(sorted(algs1.get_shortest_paths_recursive(end1)))
    print()
    print("By iteration:")
    print(sorted(algs1.get_shortest_paths_iterative(end1)))
    print()
    print("If the routes are belonged to the shortest paths:")
    print(weights1)
    print(algs1.check_route_if_passed_for_min_dist(end1))
    print(break_line)
    print()

    weights2 = [(1, 2, 1), (2, 6, 1), (1, 7, 1), (6, 7, 1), (4, 6, 1), (4, 7, 2), (2, 4, 5)]

    algs2 = WeightedPathsAlgorithms(weights2)
    start2, end2 = 1, 4
    algs2.build_shortest_weighted_pathes(start2)
    print("Shortest Paths:")
    print(algs2.get_mini_dists())
    print("Previous Vertex in the shortest paths:")
    print(algs2.get_prevs())
    print("Expected result: [[1, 2, 6, 4], [1, 7, 6, 4], [1, 7, 4]]\n")
    print("By recursion:")
    print(sorted(algs2.get_shortest_paths_recursive(end2)))
    print()
    print("By iteration:")
    print(sorted(algs2.get_shortest_paths_iterative(end2)))
    print()
    print("If the routes are belonged to the shortest paths:")
    print(weights2)
    print(algs2.check_route_if_passed_for_min_dist(end2))
