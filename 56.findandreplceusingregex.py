# find and replace a string with another
import re

string = 'My name is Sourav'
pattern = r'Sourav'
            #  re.sub(deletevariable,replaceword,stringinwhichwewanttoreplace)
newstring  = re.sub(pattern,"Kabir",string)
print(newstring)
