value=150
new_value=int(value/2) if value<100 else -value
print(new_value)

value=10
new_value=1 if value<100 else 0
print(new_value)


value=10
new_value=True if value<100 else False
print(new_value)

my_str='qwerty'
my_str=2*str(my_str) if len(my_str)>5 else my_str
print(my_str)

my_str='qwer'
my_str=(my_str+my_str[::-1]) if len(my_str)<5 else my_str
print(my_str)
