# first = input("Your first name")
#
# last = input("Your last name")
#
# temp=last
# last=first
#
# print(temp,last)


def reverseWords(input,output):
    inputWords=input.split(" ")
    inputWords = inputWords[-1::-1]

    outputWords = output.split(" ")
    outputWords = outputWords[-1::-1]

    solution=' '.join(inputWords)
    solution1=' '.join(outputWords)

    print(solution,solution1)

if __name__ == "__main__":

    print (reverseWords('a b c z','d e f'))
