# Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.

data =  {'a': 10, 'b': 15, 'c': 7}

max_key = max(data, key=data.get)
print(f"The key with the maximum value is: '{max_key}'")