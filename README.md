# TimedTask
A python wrapper for an object to run a function at a set interval. This is set-up to not be a true wrapper so that it is compatible with third-party objects.

class TimedTask(object):


The constructor for the TimedTask is 
```python
def __init__(self, 
             object_to_wrap,
             calling_function,
             sampling_rate=0.1,
             calling_func_args=None,
             forwarding_function=None):
```

```object_to_wrap``` is an instance of an object that is associated with the repetitive task. References to this object can be obtained from two member methods of TimedTask under the name ```wrapped_object``` and the name of the type of the object that is passed (i.e. if an object of type "Sensor" is passed, then the reference would be "myTimedTask.Sensor"). This can be set as None if you do not want this feature or are not using an object.

```calling_function``` is the function that will be called at the set interval.

```sampling_rate``` is the period in seconds of task loop.

```calling_func_args``` any arguments that need to be passed to the calling_function when it is called.

```forwarding_function``` an additional optional function that can be specified to be called every loop.

For an example of how to use this, see the examples folder.
