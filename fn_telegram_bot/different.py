class Filter_patterns:
    def __init__(self, start_date, desired_date_from, desired_date_until, start_time, desired_start_time, rate, desired_rate, send_to_bot, filter_pattern):
        self.start_date = start_date
        self.desired_date_from = desired_date_from
        self.desired_date_until = desired_date_until
        self.start_time = start_time
        self.desired_start_time = desired_start_time
        self.rate = rate
        self.desired_rate = desired_rate
        self.send_to_bot = send_to_bot
        self.filter_pattern = filter_pattern

    def filter_pattern_func(self):
        if self.filter_pattern == 1 and self.desired_date_from <= self.start_date <= self.desired_date_until and self.start_time >= self.desired_start_time and self.rate >= self.desired_rate and self.send_to_bot == 1:
            return True
        elif self.filter_pattern == 2 and self.desired_date_from <= self.start_date <= self.desired_date_until or self.start_time >= self.desired_start_time and self.rate >= self.desired_rate and self.send_to_bot == 1:
            return True

def filter_pattern_func(send_to_bot, filter_pattern, start_date, desired_date_from, desired_date_until, start_time, desired_start_time, rate, desired_rate):
    if filter_pattern == 1 and send_to_bot == 1 and desired_date_from <= start_date <= desired_date_until and start_time >= desired_start_time and rate >= desired_rate:
        return 1
    elif filter_pattern == 2 and send_to_bot == 1 and (desired_date_from <= start_date <= desired_date_until or start_time >= desired_start_time) and rate >= desired_rate:
        return 2
    else:
        return 0    

print(filter_pattern_func(7,5,9,10,9,6,5,1,2)) 
