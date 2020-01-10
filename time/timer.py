import time
import logging
import functools
from dataclasses import dataclass, field
from typing import Callable, Dict, ClassVar, Optional
from reader import feed


class TimeError(Exception):
    """Exception of the Timer class"""
    
@dataclass    
class Timer:
    timers: ClassVar[Dict[str, float]] = dict()
    name: Optional[str] = None
    text: str = "Elapsed time {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
    # By using dataclasses.field() you say that ._start_time should be removed
    # from .__init__() and the representation of Timer.
    
    def __post_init__(self) -> None:
        if self.name is not None:
            self.timers.setdefault(self.name, 0)
        
    def start(self) -> None:
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._start_time = time.perf_counter()
        
    def stop(self) -> float:
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        
        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time
        
        return elapsed_time
    
    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self
    
    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        self.stop()
        
    def __call__(self, func):
        """Support using Timer as a decorator"""
        @functools.wraps(func)
        def wrapped_timer(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapped_timer
        
        
if __name__ == "__main__":        
    print("TEST 1")
    t = Timer(logger=logging.warning)
    t.start()
    time.sleep(3)
    t.stop()

    print("TEST 2")
    t = Timer(logger=None)
    t.start()
    time.sleep(3)
    value = t.stop()
    print(value)
    
    print("TEST 3")
    t = Timer("accumulate")
    t.start()
    time.sleep(2)
    t.stop()
    t.start()
    time.sleep(3)
    t.stop()
    print(f"Total time of execution: {(Timer.timers[t.name]):0.2f} seconds")
    
    print("TEST 4")
    with Timer():
        time.sleep(2.5)
