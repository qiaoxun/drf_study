class Example:
    def __init__(self):
        print("Instance Created")

        # Defining __call__ method

    def __call__(self):
        print("Instance is called via special method")

    # Instance created


# e = Example()

# __call__ method will be called
# e()

import threading

def test_thread():
    websocket_key = '111'
    quit_keywords = '111'
    t1 = threading.Thread(target=thread_back, args=(websocket_key, quit_keywords))
    t1.start()

def thread_back(websocket_key, quit_keywords=None):
    print(websocket_key)
    print(quit_keywords)

test_thread()