import threading
import time


class TimedTask(object):
    def __init__(self,
                 object_to_wrap,
                 calling_function,
                 sampling_rate=0.1,
                 calling_func_args=None,
                 forwarding_function=None):

        type_name = type(object_to_wrap).__name__
        self.__setattr__(type_name, object_to_wrap)
        self.wrapped_object = object_to_wrap

        self.calling_function = calling_function
        self.calling_func_args = calling_func_args

        if forwarding_function is None:
            def pass_func(args):
                pass
            self.forwarding_function = pass_func
        else:
            self.forwarding_function = forwarding_function

        self.sampling_rate = sampling_rate
        self.sampling_period = 1 / sampling_rate

        self.output = None
        self.timer_thread = threading.Thread(target=self._sample_loop)
        self.stop_flag = threading.Event()

    def _sample_loop(self):
        current_time = time.time()

        while not self.stop_flag.is_set():
            while time.time() - current_time < self.sampling_period:
                time.sleep(0.00001)
            current_time = time.time()
            self.output = self.calling_function()
            self.forwarding_function(self.output)

    def start(self):
        self.timer_thread.start()

    def stop(self):
        self.stop_flag.set()
        self.timer_thread.join()



