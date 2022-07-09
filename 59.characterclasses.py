import re
#A-178
pattern = r"[A-Z][-][0-9][0-9][0-9]"
if re.search(pattern,"A-178"):
    print("Match found")