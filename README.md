## If/Elif/Else conditional Statements
Used for decision-making operations with conditions

Conditional statements always start with an 
'if' header
'elif' opitional, but we can have as many as we want
' else' opitional, but only 1 for every 'if'

### Condition:
An expression that evaluates to produce a result which is a Boolean value. (AKA. Boolean expression)

### Indentation
Python relies in indentation to define scope in the code

### Formula:
if (condition):
>Body Statement

elif (condition):
>Body Statement

else
>Body Statement

*Ex. *
'''

a = 2
if(a == 0): # False
  print ("hi")
else:
  print ("bye")
  '''

>bye

## Nested Conditional Statement

A conditional statement inside another Conditional statement

### Indentation
The header/clause of a nested conditional statement must be from an outer header
## Formula

```
if(Conditional):
  if(Conditional): <---Starting a nested statement
    Body Statement
  elif(Conditional):
  Body Statement
else:
    body statement <-- End of nested statement
elif(Conditional):
  Body Statement
else:
  Body Statement
```

```
X = 10
y = 10
if (x < y):
  print("x is less than y")
else:
  if(x > y):
    print("x is greater than y")
  else:
    print("x and y must be equal")
'''
  >x and y must be equal