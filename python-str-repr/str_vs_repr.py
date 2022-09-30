import datetime
today = datetime.date.today()

print(str(today))
print(repr(today))

# __str__ should be easy to read, for human consumption. 
# __repr__ unambiguous should be for developer use.