from typing import List


class Solution(object):
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def _get_num_range_str(self, curr_num, prev_num):
        return str(curr_num) if curr_num == prev_num else str(prev_num) + "->" + str(curr_num)

    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums += [upper + 1]

        prev = lower - 1
        for num in nums:
            if num < lower:
                continue

            num = min(num, upper + 1)

            if num - prev > 1:
                res.append(self._get_num_range_str(prev, num))

            if num > upper:
                break

            prev = num

        return res


if __name__ == '__main__':
    solution = Solution()

    tests = []

    for test_nums, test_lower, test_upper in tests:
        solution.find_missing_ranges(test_nums, test_lower, test_upper)
