import collections

def jobScheduling(startTime, endTime, profit):
    times = sorted(set(startTime + endTime))

    dp = collections.defaultdict(int)

    end2start = collections.defaultdict(list)
    for i, t in enumerate(endTime):
        end2start[t].append((startTime[i], profit[i]))

    # dp represents the max profit until that time (not necessary
    # to include a time slot that ends with that time
    prev_e = None
    for e in times:
        for s, p in end2start[e]:
            dp[e] = max(dp[e], dp[s] + p)
        if prev_e is not None:
            dp[e] = max(dp[e], dp[prev_e])

        prev_e = e

    return dp[times[-1]]