import threading
import time
import json  

with open('inventory.dat', 'r') as file:
    inventory = json.load(file)


cart = []
cart_lock = threading.Lock()

def bot_clerk(items):
    global cart
    robot_fetcher_lists = [[], [], []]

    for i, item in enumerate(items):
        robot_fetcher_lists[i % 3].append(item)

    threads = []

    for i in range(3):
        thread = threading.Thread(target=bot_fetcher, args=(robot_fetcher_lists[i], cart, cart_lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(items, cart, lock):
    for item in items:
        item_number = item
        item_description, seconds = inventory[item_number]

        time.sleep(seconds)

        with lock:
            cart.append([item_number, item_description])

