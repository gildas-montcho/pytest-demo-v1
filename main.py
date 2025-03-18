from functions import add, sub, div, mult
from blue import greeting, helper
from green.counting import count
from blue.other.fourth import last_function

x, y = 5, 4
print(add(x, y))
print(sub(x, y))
print(mult(x, y))
print(div(x, y))
greeting.greet()
helper.help_me()
count(5)
last_function()
