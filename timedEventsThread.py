import threading
import time


def timer_function(func, interval_minutes, flag):
    def run_func():
        while flag():
            func()
            time.sleep(interval_minutes * 60)

    t = threading.Thread(target=run_func)
    t.start()


# Example usage:
def example_function():
    print("Example function is running...")


def flag():
    return True  # Modify this function to return False when you want to stop the timer


# Run example_function every 2 minutes while the flag is True
timer_function(example_function, 1, flag)
