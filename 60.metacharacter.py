# meta character in python
import re
# *star here means that we can have the bacon repeated as many times as possible
pattern = r'eggs(bacon)*'
if re.search(pattern,"eggsbaconbacon"):
    print("match found")
  