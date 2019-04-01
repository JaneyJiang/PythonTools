from collections import deque
import time
class ConveyorQueue:
    def __init__(self, num_buckets):
        self.queue = deque()
        self.max_items = num_buckets
        self.totalsum = 0

    def shift(self, num_shifted):
        if num_shifted >= self.max_items:
            self.queue = deque()
            self.totalsum = 0
            return 

        while num_shifted:
            self.queue.append(0)
            num_shifted-=1

        while len(self.queue) > self.max_items:
            self.totalsum -= self.queue.popleft()

    def addToBack(self,num):
        if not self.queue:
            self.queue.append(0)
        self.queue[-1] += num
        self.totalsum += num
         

class TrailingBucketCounter:
    def __init__(self, num_buckets, secs_per_bucket):
        self.secs_per_bucket = secs_per_bucket
        self.buckets = ConveyorQueue(num_buckets)
        self.last_update_time = int(time.time())
    
    def update(self, now):
        cur_bucket =  now // self.secs_per_bucket
        last_update_bucket = self.last_update_time // self.secs_per_bucket
        self.buckets.shift(cur_bucket-last_update_bucket)
        self.last_update_time = now

    def add(self,count,now):
        self.update(now)
        self.buckets.addToBack(count)

    def trailing_count(self, now):
        self.update(now)
        return self.buckets.totalsum
    

         
    

class MinuteHourCounter:
    def __init__(self):
        self.minute_counts = TrailingBucketCounter(60,1)
        self.hour_counts = TrailingBucketCounter(60,60)
    
    def add(self, count):
        now = int(time.time())
        self.minute_counts.add(count,now)
        self.hour_counts.add(count,now)
    
    def minute_count(self):
        now = int(time.time())
        return self.minute_counts.trailing_count(now)

    def hour_count(self):
        now = int(time.time())
        return self.hour_counts.trailing_count(now)



counter = MinuteHourCounter()
counter.add(30)
print(counter.hour_count())
print(counter.minute_count())
