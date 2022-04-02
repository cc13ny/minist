"""
# Definition for an Interval.

"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


# Sweep Line
# Or you can also look at the last end until there's no intersection
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        import heapq
        heap, result = [], []
        for employee in schedule:
            for i in range(len(employee)):
                heapq.heappush(heap, (employee[i].start, 0)) # start should be first to be counted
                heapq.heappush(heap, (employee[i].end, 1))

        # Free time means
        # when an interval starts, the count plus 1
        # when an interval starts, the count minus 1
        # when the count is equal to 0, it reaches the start of the free time
        count, n = 0, len(heap)
        while n > 1:
            left = heapq.heappop(heap)
            right = heap[0]
            count += 1 if left[1] == 0 else -1

            if count == 0:
                result.append(Interval(left[0], right[0]))

            n -= 1

        return result


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# import heapq

# Easier to understand
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        import heapq
        if schedule is None or len(schedule) == 0:
            return []

        hq = []
        for employee_schedules in schedule:
            for time_slot in employee_schedules:
                heapq.heappush(hq, (time_slot.start, time_slot.end))

        n = len(hq)
        if n == 0:
            return []

        res = []
        current_time_slot = heapq.heappop(hq)
        for i in range(1, n):
            next_time_slot = heapq.heappop(hq)
            if current_time_slot[1] < next_time_slot[0]:
                res.append(Interval(current_time_slot[1], next_time_slot[0]))
            if current_time_slot[1] < next_time_slot[1]:
                current_time_slot = next_time_slot

        return res