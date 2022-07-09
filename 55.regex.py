import re
pattern = r'eggs'
if re.match(pattern, "baconeggs"):
    print ('Match found')
else:
    print('No match found')
# search will search the entire string while match search only the start
if re.search(pattern,"eggseggseggsbacon"):
    print ('Match found')
else:
    print('No match found')
    
print(re.findall(pattern,"eggseggseggsbacon"))
#findall will count the number of occurences of the string
x = (re.findall(pattern,"eggseggseggsbacon"))
print(x.count(pattern))


