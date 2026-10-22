# Data Structures & Systems Design Assignment

Solutions to the LRU Cache and Event Scheduler problems for the AI / Multi-Agent Systems Intern recruitment assignment at Avaloka (Guruvai Sciences).

## Problem 1: LRU Cache

Implemented an LRU cache using a dictionary and a doubly linked list.

**Approach**
- The dictionary provides direct access to cache entries.
- The doubly linked list maintains usage order.
- Recently accessed or updated entries move to the front.
- When capacity is exceeded, the least recently used entry is evicted.

**Complexity**
- `get()` — average O(1)
- `put()` — average O(1)
- Space — O(C), where C is the cache capacity.

## Problem 2: Event Scheduler

Implemented two functions:

- `can_attend_all(events)`: Sorts events by start time and checks consecutive intervals for overlaps.
- `min_rooms_required(events)`: Uses a min-heap to track meeting end times and calculate the minimum number of rooms required.

**Complexity**
- Both functions — O(n log n) time.
- Auxiliary space — O(n).

Adjacent events are allowed; a meeting ending at the same time another begins does not count as an overlap.

## Running the Code

Requires Python 3. No external packages are needed.

Run the individual files:

```bash
python lru_cache.py
python event_scheduler.py
```

Run tests:

```bash
python -m unittest test_assignment.py
```

## Design Discussion

The assignment also covers data structure trade-offs, extending the scheduler to assign room identifiers, and making the LRU cache thread-safe.
