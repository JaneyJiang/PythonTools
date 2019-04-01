import unittest
from time import sleep
from MinuteHourCounter import MinuteHourCounter

class MinuteHourCounterTest(unittest.TestCase):
    def test_no_input_count(self):
        counter = MinuteHourCounter()
        self.assertEqual(counter.hour_count(), 0)
        self.assertEqual(counter.minute_count(), 0)

    def test_one_input_count(self):
        counter = MinuteHourCounter()
        counter.add(30)
        counter.add(30)
        sleep(60)
        counter.add(20)
        sleep(20)
        counter.add(20)
        self.assertEqual(counter.hour_count(), 100)
        self.assertEqual(counter.minute_count(), 40)

if __name__ == '__main__':
    unittest.main()