from numpy import prod


def parse(buffer):
    #parses the data file to make it accessible for execution
    line = buffer.split('\n')
    #putting all the data into a list of lists
    newfile = []
    for x in line:
        #taking every line and putting it into a list
        values = x.strip().split()
        #converting the strings to integers/floats accordingly
        if values==[]:
            continue
        elif values[0].find(".") == -1:
            values = [int(x) for x in values]
        else:
            values = [float(x) for x in values]
        newfile.append(values)
    return newfile

def solution(file):
    tot_prob_success = []
    prob_unavail = file[2::2]
    num_roles = file[1::2]
    for x in range(0, len(prob_unavail)):
        prob_success = []
        count = 0
        A = sorted(prob_unavail[x])
        B = A[:len(A)//2]
        C = A[len(A) // 2:]
        for i in range(0,len(B)):
            # print(num_roles[i][0])
            if B[i] == 0 and num_roles[x][0]>0:
                num_roles[x][0] = num_roles[x][0] - 1
                count = count + 1
                prob_success.append(1)
            elif num_roles[x][0]>0:
                unavail = B[i]*C[i-count]
                prob_success.append(1 - unavail)
        # print(prob_success)
        tot_prob_success.append(prod(prob_success))
    return tot_prob_success

def main():
    f = open('B-large-practice.in').read()
    p = parse(f)
    s = solution(p)
    i=1
    #sending the information to a txt file.
    with open('UnderStudieslarge_result.txt', 'w') as f:
        while i < p[0][0]-1:
            for x in s:
                x = '{:6f}'.format(x)
            #because write() only takes one string argument, you need to concatenate the strings, instead of using commas.
                f.write("Case #" + str(i) + ": " + x + "\n")
                i+=1
    f.close()

main()
