from queue import PriorityQueue

def check(n,e): # checks if n has already been explored in e
    arg = [0,0,0],[0,0,0],[0,0,0]
    pus = [0,0,0],[0,0,0],[0,0,0]

    for val in e:
        cnt = 0
        i=0
        while i<3:
            j=0
            while j<3:
                arg[i][j] = (n[1])[i][j]
                pus[i][j] = val[i][j]

                if arg[i][j]==pus[i][j]:
                    cnt = cnt +1
                    j=j+1
                else:
                    j = j+1
            i=i+1
        if cnt == 9:
            return 0
        return 1




def index(iarray, value): # checks which index the value 'value' is placed in iarray
    x = 0
    while x<3:
        y=0
        while y < 3:
            if iarray[x][y] == value:
                ab = [x , y]
                return ab
            else:
                y = y + 1
        x=x+1


def pathcost(cur):# calculates pathcost for each action
    summ = 0
    cece = 0
    while cece<=2:
        francis=0
        while francis<=2:
            l = [cece,francis]
            pctemp = cur[cece][francis]

            k = index(goal,pctemp)

            f=k[0]-l[0]
            s=k[1]-l[1]

            summ= summ + (abs(f)+abs(s))

            francis=francis+1
        cece=cece+1
    return summ


def A_SEARCH(start):
    currentnode = (0,start)
    frontier= PriorityQueue()
    frontier.put(currentnode)
    explored = []
    explored.append(start)

    fckoff = frontier.get()

    if currentnode[1] == goal:
        return ("initial state was the goal state")

    cnt=0
    while frontier.not_empty:
        array=[0,0,0],[0,0,0],[0,0,0]

        kknt = 0
        while kknt <= 2:
            kknt2 = 0
            while kknt2 <= 2:
                array[kknt][kknt2] = (currentnode[1])[kknt][kknt2]
                kknt2 = kknt2 + 1
            kknt = kknt + 1

        #print("\n\n\n\nnew array is: ",array)
        #print("explored ", explored)

        uarray = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        darray = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        rarray = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        larray = [0, 0, 0], [0, 0, 0], [0, 0, 0]

        knt=0
        while knt<=2:
            knt2 = 0
            while knt2<=2:
                uarray[knt][knt2]= array[knt][knt2]
                darray[knt][knt2] = array[knt][knt2]
                rarray[knt][knt2] = array[knt][knt2]
                larray[knt][knt2] = array[knt][knt2]
                knt2=knt2+1
            knt=knt+1

        h = index(array, 0)
        i = h[0]
        j = h[1]

        if i != 0:
                utemp = uarray[i - 1][j]
                uarray[i - 1][j] = 0
                uarray[i][j] = utemp

                upc = (pathcost(uarray)+cnt)
                unew = (upc, uarray)
                #print("after up ",unew)

                uval = check(unew, explored)
                if uval == 1:
                    frontier.put(unew)
                    #print("added")


        if i!=2:
                dtemp = darray[i + 1][j]
                darray[i + 1][j] = 0
                darray[i][j] = dtemp

                dpc = (pathcost(darray)+cnt)
                dnew = (dpc, darray)
                #print("after down ",dnew)

                dval = check(dnew, explored)
                if dval == 1:
                    frontier.put(dnew)
                    #print("added")


        if j != 2:
                rtemp = rarray[i][j + 1]
                rarray[i][j + 1] = 0
                rarray[i][j] = rtemp

                rpc = (pathcost(rarray)+cnt)
                rnew = (rpc, rarray)
                #print("after right ",rnew)

                rval = check(rnew, explored)
                if rval == 1:
                    frontier.put(rnew)
                    #print("added")


        if j != 0:
                ltemp = larray[i][j - 1]
                larray[i][j - 1] = 0
                larray[i][j] = ltemp

                lpc = (pathcost(larray)+cnt)
                lnew = (lpc, larray)
                #print("after left ",lnew)

                lval = check(lnew, explored)
                if lval == 1:
                    frontier.put(lnew)
                    #print("added")

        #print("new")
        #print("cn before: ",currentnode)

        currentnode = frontier.get()

        #print("cn after: ", currentnode)

        kknt = 0
        while kknt <= 2:
            kknt2 = 0
            while kknt2 <= 2:
                array[kknt][kknt2] = (currentnode[1])[kknt][kknt2]
                kknt2 = kknt2 + 1
            kknt = kknt + 1


        i=0
        while i<3:
            j=0
            while j<3:
                if array[i][j] != goal[i][j]:
                    j=20
                    i=20
                else: j = j+1
            i = i + 1

        #print(j)

        if j != 20:
            explored.append(currentnode[1])
            return (explored, cnt)
        else:
            explored.append(currentnode[1])






        cnt = cnt + 1

a=[[0,0,0],[0,0,0],[0,0,0]]
b=[["first","second","third"],["fourth", "fifth","sixth"],["seventh", "eight", "ninth"]]
goal=[[0,0,0],[0,0,0],[0,0,0]]

print("PUZZLE CONFIGUARION\n")
print("  1st  2nd  3rd    \n")
print("  4th  5th  6th    \n")
print("  7th  8th  9th    \n")

print("input values can only be 0-8, 0 denotes blank space, input a letter to close the program\n")

print("START STATE:\n")


x=0
while x<3:
    y=0
    while y<3:

        num=input("\nplease enter your " + b[x][y] +" data value:")

        (a[x][y]) = int(num)

        if a[x][y] == 0 or a[x][y] == 1 or a[x][y] == 2 or a[x][y] == 3 or a[x][y] == 4 or a[x][y] == 5 or a[x][y] == 6 or a[x][y] == 7 or a[x][y] == 8:
            i=0
            while i<=x:
                j=0
                while j<y:
                    if x==0 and y==0: rand = 5
                    else:
                        if a[x][y] == a[i][j]:
                            print("number is already taken in puzzle at the " + b[i][j] + " entry")
                            y = y - 1
                    j=j+1
                i=i+1
            y = y + 1
        else:
            print("invalid input, enter a data between 0 - 8")
    x=x+1

print("\n\n\nTHIS IS YOUR START STATE")

x=0
while x<3:
    print("    ",a[x])
    x=x+1



print("\n\n\n\n\nGOAL STATE:\n")

x=0
while x<3:
    y=0
    while y<3:

        num=input("\nplease enter your " + b[x][y] +" goal value:")
        (goal[x][y]) = int(num)

        if goal[x][y] == 0 or goal[x][y] == 1 or goal[x][y] == 2 or goal[x][y] == 3 or goal[x][y] == 4 or goal[x][y] == 5 or goal[x][y] == 6 or goal[x][y] == 7 or goal[x][y] == 8:
            i=0
            while i<=x:
                j=0
                while j<y:
                    if x==0 and y==0: rand = 5
                    else:
                        if goal[x][y] == goal[i][j]:
                            print("number is already taken in puzzle at the " + b[i][j] + " entry")
                            y = y - 1
                    j=j+1
                i=i+1
            y = y + 1
        else:
            print("invalid input, enter a data between 0 - 8")
    x=x+1

print("THIS IS YOUR GOAL STATE")

x=0
while x<3:
    print("     ",goal[x])
    x=x+1

print("\n\n\n")
print("            ", a[0], "           ",goal[0])
print("START STATE:", a[1], "GOAL STATE:",goal[1])
print("            ", a[2], "           ",goal[2])

l = input("enter any key to search: ")

result= A_SEARCH(a)
nodesvisited = result[0]
steps= result[1]+1

i =0
while i<len(nodesvisited):
    print("STEP : ", (i+1))
    j = 0
    while j<3:
        print(nodesvisited[i][j])
        j=j+1
    print("\n")
    i=i+1

print("STEPS TAKEN : ",i )

l = input("enter any key to close prorgam")