def parse(buffer):
    #parses the data file to make it accessible for execution
    line = buffer.split('\n')
    #putting all the data into a list of lists
    newfile = []
    for x in line:
        #taking every line and putting it into a list
        values = x.strip().split()
        newfile += (values,)
    return newfile

def solution(file):
    #this method provides the main solution to the question.
    #it returns the largest possible number of the friends that could actually be seated all in the same-numbered row of seats
    #it also returns the number of test cases
    f = file[0]
    tot = int(f[0])
    rows = []
    result = []
    rowCount = 0
    sameCount = 0
    a=1
    x=1
    F=0
    while x<tot+1:
        #this condition is because you don't want to change the value of a in the very first run
        if a<len(file):
            if F!=0:
                a+=F+1
            F = int(file[a][0])
            S = int(file[a][1])
            for n in range(1, S+1):
            #from the number 1 --> max grid size. Iterates through all the numbers that could possibly be on the ticket
            #splitting the section that containing the number of relevant tickets
                section = file[a + 1: a + F + 1]
                #because the section is a list in a list I used this way to remove duplicates in 'section'. Removing duplicates because if there are duplicates
                #it means that there is no chance that the friends will sit in the same row.
                b_set = set(tuple(x) for x in section)
                b = [list(x) for x in b_set]
                for i in b:
                # for every ticket that each friend has in this section
                    #there is a max number of rows/columns so that would be the max number on the ticket (x, y), therefore I'm iterating through
                    #each ticket to see if x or y is equal to the numbers from 1 --> max number one by one.. if the number appears it gets appended to
                    #the list 'rows'.
                    if int(i[0])== n or int(i[1]) == n:
                        rowCount+=1
                rows.append(rowCount)
                rowCount = 0
                # the counter is reset every time we check for a new number to match with the ticket.
            result.append(max(rows))
            #we take the max number from the list rows that's from this section and put it into a new list called 'tots'.
            rows = []
            #reset the list for the next section
        x+=1
        #increase the counter to move onto the next case.

    return result, tot

def main():
    f = open('TTlarge.in').read()
    p = parse(f)
    s = solution(p)
    i=1
    #sending the information to a txt file.
    with open('TTlarge_result.txt', 'w') as f:
        while i < s[1]+1:
            #because write() only takes one string argument, you need to concatenate the strings, instead of using commas.
            f.write("Case #" + str(i) + ": " + str(s[0][i - 1]) + "\n")
            i+=1
    f.close()

main()

