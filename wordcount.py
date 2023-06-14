"""Count words in file."""

with open("test.txt") as file:

    repetitions = {}

    for line in file:
        line = line.rstrip().split(" ")

        for word in line:
            repetitions[word] = repetitions.get(word, 0) + 1

    for keys, values in repetitions.items():
        print(keys, values)