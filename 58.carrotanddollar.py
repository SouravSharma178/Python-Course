# ^ - this signifies start of the string
# $ - this is for end of the string
import re

pattern = r'^gr.y$'

if re.search(pattern,"Gray"):
    print("found")
else:
    print("Not found")
 