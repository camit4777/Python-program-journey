def merge(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:  # overlap
            merged[-1][1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Merged intervals:", merge(intervals))