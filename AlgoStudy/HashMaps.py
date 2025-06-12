# ✅ 1. Initialize a HashMap (empty)
my_map = {}

# ✅ 2. Initialize with values
person = {"name": "Alice", "age": 30, "city": "Toronto"}

# ✅ 3. Add / Update an item
my_map["key1"] = "value1"
my_map["key2"] = 42

# ✅ 4. Access a value by key
print(my_map["key1"])       # → "value1"

# ✅ 5. Check if key exists
if "key1" in my_map:
    print("Found!")


# ✅ 6. Use .get() to safely access (avoids crash if key missing)
print(my_map.get("key3"))            # → None
print(my_map.get("key3", "default")) # → "default"

# ✅ 7. Remove an item
del my_map["key2"]

# ✅ 8. Loop through items
for key, value in my_map.items():
    print(f"{key}: {value}")

# ✅ 9. Get all keys / values
keys = list(my_map.keys())     # → ["key1"]
values = list(my_map.values()) # → ["value1"]

# ✅ 10. Default values using defaultdict
from collections import defaultdict

anagrams = defaultdict(list)
word = "tea"
key = ''.join(sorted(word))  # "aet"
anagrams[key].append(word)   # anagrams["aet"] = ["tea"]

# ✅ 11. Count characters using Counter
from collections import Counter

count = Counter("banana")  # → {'b':1, 'a':3, 'n':2}
print(count["a"])          # → 3

# ✅ 12. Dictionary comprehension (quick build)
squares = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# ✅ 13. Clear all items
my_map.clear()

# ✅ 14. Length of map
print(len(my_map))

# ✅ 15. Merge two dicts (Python 3.9+)
a = {"x": 1}
b = {"y": 2}
merged = a | b   # → {'x': 1, 'y': 2}
