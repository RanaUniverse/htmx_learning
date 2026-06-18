from datetime import datetime
from time import time


def get_now_time_in_str() -> str:
    now_time = datetime.fromtimestamp(timestamp=time())
    now_time_str = now_time.strftime(format="%H:%M:%S")
    return now_time_str
