# The POC for the time management app

# Problem Description:
#
#   We need to fulfil some tasks
#   For each task, we need two kinds of resources:
#   - time
#   - energy/ intelligence

# Let's handle the simple case with the following assumption:
#   - The energy and time keep growing stably.
#   - For each task, it requires the energy and time to fulfil.


class DynamicScheduler:

    # tasks = [(deadline_timestamp_0, time_needed_0), (deadline_timestamp_1, time_needed_1), ...]
    def __init__(self, tasks: List[tuple]):
        self.tasks = sorted(tasks)

    def getAllValidSchedules(self):


    def _getAllValidSchedules(self, l_tm: int, r_rm: int):