import time
from TimedTask import TimedTask


class MySensor(object):
    def __init__(self):
        self.value = 1

    def get_value(self):
        return [2 * self.value, 4*self.value, 6*self.value]

    def set_value(self, new_value):
        self.value = new_value


if __name__ == '__main__':
    new_sensor = MySensor()

    start = time.time()
    count = [0, start]

    def print_time(values):
        count[0] += 1
        print("values:", values, "time elapsed: ", (time.time() - count[1])/count[0])


    timed_sensor = TimedTask(new_sensor,
                             calling_function=new_sensor.get_value,
                             forwarding_function=print_time,
                             sampling_rate=50)
    timed_sensor.start()
    try:
        while 1:
            time.sleep(2)
            timed_sensor.wrapped_object.value = timed_sensor.MySensor.value * 2
    except:
        timed_sensor.stop()
