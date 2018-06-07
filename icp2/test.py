
fname = input("Enter File name:")

num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        print(line)
print("Number of words:")
print(num_words)