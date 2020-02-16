with open('example-mp.txt', 'r') as t:
    frames = int(t.readline())
    data = []
    for line in t.readlines():
        data.append(int(line))


def FIFO(f, d):

    curList = []
    removeIndex = 0
    missingPages = 0

    for i in d:
        
        if i not in curList:
            if len(curList) < f:
                curList.append(i)
            
            else:
                curList[removeIndex] = i
                removeIndex += 1

                if removeIndex == f:
                    removeIndex = 0

            missingPages += 1
        else:
            pass
    
    return footer(missingPages, "FIFO")


def LRU(f, d):

    curList = []
    missingPages = 0
    dictMax = {}

    for i in range(0, len(d), 1):
        
        if d[i] not in curList:
            if len(curList) < f:
                curList.append(d[i])
            
            else:
                for item in range(0, i, 1):

                    if d[item] in curList:

                        dictMax[d[item]] = i - item

                max_val = max(dictMax.values())
                max_key = getKey(max_val, dictMax)
                                
                oldIndex = curList.index(max_key)
                curList[oldIndex] = d[i]
                
            missingPages += 1
            dictMax.clear()

        else:
            pass

    return footer(missingPages, "LRU")


def OTM(f, d):
    
    curList = []
    missingPages = 0
    dictMax = {}

    for i in range(0, len(d), 1):
        
        if d[i] not in curList:
            if len(curList) < f:
                curList.append(d[i])
            
            else:
                itemsForward = d[i:len(d)]
                
                for forwardInd in range(0, len(itemsForward), 1):

                    if itemsForward[forwardInd] in curList:

                        dictMax[forwardInd] = i + forwardInd

                if len(dictMax) < f:

                    for e in curList:
                        if e not in dictMax:
                            oldIndex = curList.index(e)
                            break
                
                else:
                    max_val = max(dictMax.values())
                    max_key = getKey(max_val, dictMax)
                    oldIndex = curList.index(max_key)

                curList[oldIndex] = d[i]
                
            missingPages += 1
            dictMax.clear()

        else:
            pass

    return footer(missingPages, "OTM")


def getKey(val, dicto):
     
    for k, v in dicto.items(): 
        if v == val: 
            return k 
        

def footer(missingPages, functionType):

    return "{} {}".format(functionType, missingPages)


print(FIFO(frames, data[:]))
print(OTM(frames, data[:]))
print(LRU(frames, data[:]))
