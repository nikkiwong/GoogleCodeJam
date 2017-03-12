import operator

def parse(buffer):

    line = buffer.split('\n')
    #putting all the data into a list of lists
    newfile = []
    for x in line:
        values = x.strip().split()
        newfile += (values,)
    return newfile

def solution(file):

    f = file[0]
    tot = int(f[0])
    d = {}
    rows = []
    result = []
    rowCount = 0
    sameCount = 0
    a=1
    x=1
    F=0
    while x<tot+1:
        d["Case #{0}".format(x)] = 0
        #this condition is because you don't want to change the value of a in the very first run
        if a<len(file):
            if F!=0:
                a+=F+1
            F = int(file[a][0])
            S = int(file[a][1])
            print("F: ", F, "S: ", S)
            print("w",a,"+1: ", a+1, (a+F))

            for n in range(1, S+1):
            #from the number 1 --> max grid size. Iterates through all the numbers that could possibly be on the ticket
            #splitting the section that containing the number of relevant tickets
                section = file[a + 1: a + F + 1]
                print("section: ", section)
                #because the section is a list in a list I used this way to remove duplicates in 'section'. Removing duplicates because if there are duplicates
                #it means that there is no chance that the friends will sit in the same row.
                b_set = set(tuple(x) for x in section)
                b = [list(x) for x in b_set]
                print("section: ", b)

                for i in b:
                # for every ticket that each friend has in this section
                    print("are the numbers of line",i,":", "equal to ", n)
                    #there is a max number of rows/columns so that would be the max number on the ticket (x, y), therefore I'm iterating through
                    #each ticket to see if x or y is equal to the numbers from 1 --> max number one by one.. if the number appears it gets appended to
                    #the list 'rows'.
                    if int(i[0])== n or int(i[1]) == n:
                        rowCount+=1
                        print("rowcount", rowCount)
                rows.append(rowCount)
                print("rows: ", rows,"tots:", result)
                rowCount = 0
                # the counter is reset every time we check for a new number to match with the ticket.
            result.append(max(rows))
            #we take the max number from the list rows that's from this section and put it into a new list called 'tots'.
            rows = []
            #reset the list for the next section

            d["Case #{0}".format(x)] = result[x-1]
        x+=1

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    return sorted_d



def main():
    '''This function executes the functions for parsing the file and executing the commands for the lights

    It returns the final count of lights turned on and the time it takes to execute this program'''

    f = open('ticketsample.txt').read()
    p = parse(f)
    s = solution(p)
    print(s)

main()