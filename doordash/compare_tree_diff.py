from typing import List


class TreeNode(object):
    def __init__(self, key: str, val: str, children: List =[]):
        self.key = key
        self.val = val
        self.children = children


def compute_diff(tree_node1: TreeNode, tree_node2: TreeNode) -> int:
    if tree_node1 is None or tree_node2 is None or tree_node1.key != tree_node2.key:
        return count_nodes(tree_node1) + count_nodes(tree_node2)

    diff_count = 0 if tree_node1.val == tree_node2.val else 2

    key_node_map1 = {}
    for node in tree_node1.children:
        if node:
            key_node_map1[node.key] = node

    key_node_map2 = {}
    for node in tree_node2.children:
        if node:
            key_node_map2[node.key] = node

    same_key_sets = key_node_map1.keys() & key_node_map2.keys()
    diff_key_sets = (key_node_map1.keys() | key_node_map2.keys()) - same_key_sets

    for key in same_key_sets:
        diff_count += compute_diff(key_node_map1[key], key_node_map2[key])

    for key in diff_key_sets:
        diff_count += count_nodes(key_node_map1.get(key, None) or key_node_map2.get(key, None))

    return diff_count


def count_nodes(tree_node: TreeNode) -> int:
    if tree_node is None:
        return 0

    cnt = 1
    for child in tree_node.children:
        cnt += count_nodes(child)

    return cnt


a = TreeNode('key1', 'val1')
b = TreeNode('key1', 'val1')

a.children = [TreeNode('key2', 'val1'), TreeNode('key3', 'val1')]
b.children = [TreeNode('key2', 'val2'), TreeNode('key4', 'val1')]

print(compute_diff(a, b))