from functools import wraps
import time
from utils.custom_exceptions import raise_rate_limiter_exceeded_exception

# https://www.youtube.com/watch?v=49oC1uHxJ-o&ab_channel=Monkhaus
def rate_limited(max_calls: int, time_frame:int):
    """Custom Rate Limiter.

    Args:
        max_calls (int): Maximum number of calls allowed in the specified time frame.
        time_frame (int): Time frame in seconds.
    
    Return:
        Function: The applied function.
    """

    def decorator(func):
        calls = []

        @wraps(func)
        async def wrapper( *args, **kwargs):
            now = time.time()
            class_in_time_frame = [call for call in calls if call > now - time_frame]
            if len(class_in_time_frame) >= max_calls:
                raise raise_rate_limiter_exceeded_exception(class_in_time_frame[0],time_frame)
            calls.append(now)
            return await func(*args, **kwargs)
        return wrapper
    return decorator