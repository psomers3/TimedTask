import threading
import time


class TimedTask(object):
    def __init__(self,
                 calling_function,
                 object_to_wrap=None,
                 sampling_rate=10,
                 calling_func_args=None,
                 forwarding_function=None):
        """
        Creates an object that maintains a reference (if desired) to another object and runs a function at a given fixed
        update rate.

        :param calling_function: The function that will be called at the set interval.
        :type calling_function: function

        :param object_to_wrap: An instance of an object that is associated with the repetitive task. References to
               this object can be obtained from two member methods of TimedTask under the name "wrapped_object" and the
               name of the type of the object that is passed (i.e. if an object of type "Sensor" is passed, then the
               reference would be "myTimedTask.Sensor"). This can be set as None if you do not want this feature or are
               not using an object.
        :type object_to_wrap: object

        :param sampling_rate: The frequency in Hz of task loop.
        :type sampling_rate: float

        :param calling_func_args: A list of any arguments that need to be passed to the calling_function when it is
               called.
        :type calling_func_args: list

        :param forwarding_function: An additional optional function that can be specified to be called every loop.
        :type forwarding_function: function
        """

        type_name = type(object_to_wrap).__name__
        self.__setattr__(type_name, object_to_wrap)
        self.wrapped_object = object_to_wrap
        """A reference to the object_to_wrap passed in constructor"""

        self.calling_function = calling_function
        """The function that is called periodically"""
        self.calling_func_args = calling_func_args
        """Arguments to pass to the calling_function"""

        if forwarding_function is None:
            def pass_func(args):
                pass
            self.forwarding_function = pass_func
        else:
            self.forwarding_function = forwarding_function
            """Bonus function that may be called every loop"""

        self.sampling_rate = sampling_rate
        """Sampling rate of the Task in Hz"""
        self.sampling_period = 1 / sampling_rate
        """period in seconds of the task loop. Derived from sampling_rate"""

        self.timer_thread = threading.Thread(target=self._sample_loop)
        """The thread that runs the task loop"""
        self.stop_flag = threading.Event()
        """A flag that when set will stop the timer_thread"""

    def _sample_loop(self):
        current_time = time.time()

        while not self.stop_flag.is_set():
            while time.time() - current_time < self.sampling_period:
                time.sleep(0.00001)
            current_time = time.time()
            self.output = self.calling_function()
            self.forwarding_function(self.output)

    def start(self):
        """
        This initiates the loop and will begin calling the set function at the desired interval until stop() is called.
        """
        self.timer_thread.start()

    def stop(self):
        """
        This stops the task from running.
        """
        self.stop_flag.set()
        self.timer_thread.join()



