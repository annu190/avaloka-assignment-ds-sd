import unittest

from lru_cache import LRUCache
from event_scheduler import can_attend_all, min_rooms_required


class TestLRUCache(unittest.TestCase):

    def test_get_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 100)

        self.assertEqual(cache.get(1), 100)

    def test_get_missing_key(self):
        cache = LRUCache(2)

        self.assertEqual(cache.get(99), -1)

    def test_evict_least_recently_used(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)

        cache.get(1)       # Key 1 becomes most recently used.
        cache.put(3, 30)   # Key 2 should be evicted.

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 30)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(1, 50)

        self.assertEqual(cache.get(1), 50)
        self.assertEqual(len(cache.cache), 1)

    def test_zero_capacity(self):
        cache = LRUCache(0)
        cache.put(1, 10)

        self.assertEqual(cache.get(1), -1)

    def test_negative_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)


class TestEventScheduler(unittest.TestCase):

    def test_can_attend_all_adjacent_events(self):
        events = [(9, 10), (10, 11), (11, 12)]

        self.assertTrue(can_attend_all(events))

    def test_cannot_attend_overlapping_events(self):
        events = [(9, 11), (10, 12)]

        self.assertFalse(can_attend_all(events))

    def test_empty_events_can_be_attended(self):
        self.assertTrue(can_attend_all([]))

    def test_one_room_required(self):
        events = [(9, 10), (10, 11), (11, 12)]

        self.assertEqual(min_rooms_required(events), 1)

    def test_two_rooms_required(self):
        events = [(9, 11), (10, 12), (11, 13)]

        self.assertEqual(min_rooms_required(events), 2)

    def test_multiple_simultaneous_events(self):
        events = [
            (9, 12),
            (9, 11),
            (10, 13),
            (11, 14),
        ]

        self.assertEqual(min_rooms_required(events), 3)

    def test_empty_schedule_requires_no_rooms(self):
        self.assertEqual(min_rooms_required([]), 0)


if __name__ == "__main__":
    unittest.main()
