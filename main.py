# main.py

from bots import bot_clerk

# Test Case 1
items_to_fetch = []
result_cart = bot_clerk(items_to_fetch)
print("Test Case 1:", result_cart)
assert result_cart == []

# Test Case 2
items_to_fetch = ['104']
result_cart = bot_clerk(items_to_fetch)
print("Test Case 2:", result_cart)
assert result_cart == [['104', 'Graph Paper']]

# Test Case 3
items_to_fetch = ['106', '109', '102']
result_cart = bot_clerk(items_to_fetch)
print("Test Case 3:", result_cart)
assert result_cart == [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']]

# Test Case 4
items_to_fetch = ['103', '108', '102', '110', '106']
result_cart = bot_clerk(items_to_fetch)
print("Test Case 4:", result_cart)
assert result_cart == [['108', '3 Ring Binder'], ['102', 'Pencils'], ['106', 'Staples'], ['103', 'Pens'], ['110', 'Notepad']]

# Test Case 5
items_to_fetch = ['106', '102', '108', '109', '103', '101', '110', '104', '107', '105']
result_cart = bot_clerk(items_to_fetch)
print("Test Case 5:", result_cart)
assert result_cart == [['108', '3 Ring Binder'], ['102', 'Pencils'], ['101', 'Notebook Paper'], ['106', 'Staples'], ['109', 'Printer Paper'], ['110', 'Notepad'], ['105', 'Paper Clips'], ['103', 'Pens'], ['104', 'Graph Paper'], ['107', 'Stapler']]

print("All test cases passed!")
