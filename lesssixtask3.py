l = ['a', 'b', 'c', 'd', 'e']
d = [0, 1, 2, 3, 4]

new_dict = {l: d for l, d in zip(d, l)}
print(new_dict)
