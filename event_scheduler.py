import heapq

def can_attend_all(events):
    if not events:
        return True

    ordered_events = sorted(events, key=lambda event: event[0])

    for i in range(1, len(ordered_events)):
        previous_end = ordered_events[i - 1][1]
        current_start = ordered_events[i][0]

        # Equal end and start times are allowed.
        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    ordered_events = sorted(events, key=lambda event: event[0])
    room_end_times = []
    max_rooms = 0

    for start, end in ordered_events:
        # Release all rooms available by this meeting's start.
        while room_end_times and room_end_times[0] <= start:
            heapq.heappop(room_end_times)

        # The current meeting occupies a room.
        heapq.heappush(room_end_times, end)

        max_rooms = max(max_rooms, len(room_end_times))

    return max_rooms


if __name__ == "__main__":
    events = [(9, 10), (10, 11), (11, 12)]
    print(can_attend_all(events))      # True
    print(min_rooms_required(events))  # 1

    events = [(9, 11), (10, 12), (11, 13)]
    print(can_attend_all(events))      # False
    print(min_rooms_required(events))  # 2
