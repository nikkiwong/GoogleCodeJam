import argparse
import urllib.request
import numpy as np

def parse(buffer):

    line = buffer.split('\n')
    newfile = ()
    for x in line:
        values = x.strip().split()
        newfile += (values,)
    A = np.array(newfile)
    return A

def solution(file):
    # file = [(x,) for x in file]
    f = file[0]
    tot = int(f[0])
    print(tot)
    d = {}
    rows = []
    cols = []
    rowCount = 0
    colCount = 0
    a=1
    x=1
    F=0
    while x<tot+1:
        d["Case #{0}".format(x)] = 0
        if a<len(file):
            if F!=0:
                a+=F+1
            F = int(file[a][0])
            # frnds = F
            S = int(file[a][1])
            w = a
            print("F: ", F, "S: ", S)
            # for n in range(1, S):
            # print("n", n)
            print("w",w,"+1: ", w+1, (w+F))

            for n in range(1, S):

                for i in range(w+1, (w+F+1)):
                    print("are the numbers of line",i,":", file[i][0], "or ", file[i][1], "equal to ", n)
                    if int(file[i][0])== n or int(file[i][1]) == n:
                        rowCount+=1
                        print("rowcount", rowCount)
                    # if int(file[i][1]) == n:
                    #     colCount+=1
                    #     print("colCount", colCount)

            # x += 1
                rows.append(rowCount)
                cols.append(colCount)
                print("rows: ", rows,"cols:", cols)
                rowCount = 0
                # colCount = 0
            # for i in range(1, S):
            #     if rows[i]>rows[i+1]:
            #         rMax = rows[i]
            #     else:

            rMax = max(rows)
                # if cols[i] > cols[i+1]:
                #     cMax = cols[i]
                # else:
            cMax = max(cols)
            if cMax>rMax:
                d["Case #{0}".format(x)] = cMax
            else:
                d["Case #{0}".format(x)] = rMax



        x+=1
    return d



def main():
    '''This function executes the functions for parsing the file and executing the commands for the lights

    It returns the final count of lights turned on and the time it takes to execute this program'''

    f = open('ticketsample.txt').read()
    p = parse(f)
    s = solution(p)
    print(s)

main()