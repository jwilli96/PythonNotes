import re

txt = "The rain is pouring down"
x = re.search("^The.*down$", txt)
print(x)