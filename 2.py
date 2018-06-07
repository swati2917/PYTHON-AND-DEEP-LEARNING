def new(line,characters):
    f=open("output.txt","a")

    f.write(line+","+str(characters))
    f.write("\n")
    f.close()

fname = input("Enter the name of the file:")
with open(fname,'r') as infile:

    for line in infile:
        characters = 0

        wordslist = line.split()

        characters = sum(len(word) for word in wordslist)

        new(line,characters)

        print(line +"," +str(characters))