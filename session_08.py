#write a function to swamp coma and dot in a string.
#Sample string: "32.054,23"
#Expected Outpout: "32,054.23"

def dotcomma():
    string = "32.054,23"
    result = ""
    index = 0

    while index < len(string):
        if string[index] == ",":
            result += "."
        elif string[index] == ".":
            result += ","
        else:
            result += string[index]
        
        index += 1
    print(result)

dotcomma()


#2. Write a function to return a list by concatenating elements of a given list and elements of range from 1 to n.
#Sample list : ['p', 'q'], #n = 5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4','p5', 'q5']

def concatenating():
    sample_list = ['p', 'q']
    sample_output = []
    n = 5

    for i in range(1, n + 1):
        for element in sample_list:
            sample_output.append(element + str(i))
    return sample_output
    print(sample_output)

concatenating()
