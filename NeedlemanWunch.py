gap=int(input("Enter gap penalty:"))
match=int(input("Enter match score:"))
mismatch=int(input("Enter mismatch score:"))
seq1=input("Enter first sequence:")
seq2=input("Enter second sequence:")

m = len(seq1)+1 #rows
n = len(seq2)+1 #columns
gapIndicator = '-'
optAlignmentList = [] #Optimum alignment list

A = [[[[None] for i in range(2)] for i in range(n)] for i in range(m)] # Score Matrix
    
def identifyPaths(mat_xPos,mat_yPos,path=''): 
    global optAlignmentList 
    i = mat_xPos 
    j = mat_yPos 
    if i == 0 and j==0: 
        optAlignmentList.append(path) 
        return 2 
    movement = len(A[i][j][1]) 
    while movement<=1: 
        if (i != 0 and j != 0):
            getMovement = A[i][j][1][0]
        else:
            if i == 0:
                getMovement =1
            else:
                if j==0:
                    getMovement =3
                else:
                    getMovement =0
                        
        path = path + str(getMovement) 
        if getMovement == 1: 
            j=j-1
        elif getMovement == 2:
            i=i-1
            j=j-1
        elif getMovement == 3:
            i=i-1
        movement = len(A[i][j][1])
        if i == 0 and j==0:
            optAlignmentList.append(path)
            return 3
    if movement>1:
        for x in range(movement):

            if (i != 0 and j != 0):
                getMovement = A[i][j][1][x]
            else:
                if i == 0:
                    getMovement =1
                else:
                    if j==0:
                        getMovement =3
                    else:
                        getMovement =0
            tmp_path = path + str(getMovement)
            if getMovement == 1:
                x_index = i
                y_index=j-1
            elif getMovement == 2:
                x_index=i-1
                y_index=j-1
            elif getMovement == 3:
                x_index=i-1
                y_index = j
            identifyPaths(x_index,y_index,tmp_path)
    return len(optAlignmentList)

for i in range(m):
    A[i][0] = [gap*i,[]]
for j in range(n):
     A[0][j] = [gap*j,[]]
for i in range(1,m):
    for j in range(1,n):
        if seq1[i-1] == seq2[j-1]:
            matchMismatchScore=match
        else:
            matchMismatchScore=mismatch
        calc = [(A[i][j-1][0] + gap),(A[i-1][j-1][0] + matchMismatchScore),(A[i-1][j][0] + gap)]
        A[i][j] = [max(calc), [i+1 for i,v in enumerate(calc) if v==max(calc)]] 

totalScore = A[i][j][0]
score = totalScore

ind1 = i
ind2 = j
optList = []
identifyPaths(i,j)

for algn in optAlignmentList:

    i = ind1-1
    j = ind2-1
    verticalAlignment = ''
    horizontalAlignment = ''
    
    for x in range(len(algn)):
        getMovement = algn[x]

        if getMovement == '2':
            verticalAlignment = verticalAlignment + seq1[i]
            horizontalAlignment = horizontalAlignment + seq2[j]
            i=i-1
            j=j-1
        elif getMovement == '1':
            verticalAlignment = verticalAlignment + gapIndicator
            horizontalAlignment = horizontalAlignment + seq2[j]
            j=j-1
        elif getMovement == '3':
            verticalAlignment = verticalAlignment + seq1[i]
            horizontalAlignment = horizontalAlignment + gapIndicator
            i=i-1
    
    optList.append([horizontalAlignment[::-1],verticalAlignment[::-1]])

print('Optimum alignments are: \n')
for seq in optList:
    print(seq[0]+'\n'+seq[1]+'\n')