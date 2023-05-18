import pickle

with open('my_array.pickle', 'rb') as f:
    arr = pickle.load(f)

print(arr)