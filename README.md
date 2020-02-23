<!-- TimedTask documentation master file, created by
sphinx-quickstart on Sun Feb 23 12:20:30 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# TimedTask

An thread-based module to create timed execution of a function. See examples folder for how to use.


### class TimedTask.TimedTask(calling_function, object_to_wrap=None, sampling_rate=10, calling_func_args=None, forwarding_function=None)
Creates an object that maintains a reference (if desired) to another object and runs a function at a given fixed
update rate.


* **Parameters**

    
    * **calling_function** (*function*) – The function that will be called at the set interval.


    * **object_to_wrap** (*object*) – An instance of an object that is associated with the repetitive task. References to
    this object can be obtained from two member methods of TimedTask under the name “wrapped_object” and the
    name of the type of the object that is passed (i.e. if an object of type “Sensor” is passed, then the
    reference would be “myTimedTask.Sensor”). This can be set as None if you do not want this feature or are
    not using an object.


    * **sampling_rate** (*float*) – The frequency in Hz of task loop.


    * **calling_func_args** (*list*) – A list of any arguments that need to be passed to the calling_function when it is
    called.


    * **forwarding_function** (*function*) – An additional optional function that can be specified to be called every loop.



#### start()
This initiates the loop and will begin calling the set function at the desired interval until stop() is called.


#### stop()
This stops the task from running.
