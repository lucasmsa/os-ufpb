with open('example.txt', 'r') as f:
    data = f.readlines()
    counter = 0
    jobs = [[0] * 2 for i in range(len(data))]    

    for lines in data:
        jobs[counter][0] = int(lines.split()[0])
        jobs[counter][1] = int(lines.split()[1])
        counter += 1


def FCFS(t):

    t = sorted(t, key=lambda col: col[0])
    waitingTime, returnTime, answerTime, endTime = float(t[0][0]), float(t[0][1] - t[0][0]), float(t[0][0]), float(t[0][1])

    for e in range(1, len(t), 1):

        waitingTime += endTime - t[e][0]
        returnTime += endTime - t[e][0] + t[e][1]
        answerTime += endTime - t[e][0]
        endTime += t[e][1]

    return footer(returnTime, answerTime, waitingTime, t, 'FCFS')


def RR(t, quantum):

    returnTime, answerTime = 0.0, {}
    cpuTime, process, processQueue = 0.0, [], []
    startingTime, quantumTimer = [], 0.0
    processStartTime, waitingTime, deadProcesses = {}, {}, {}
    count = 0

    for e in t:
        size = e[1]
        processNumber = "P" + str(count)
        process.append([e, size, processNumber])
        startingTime.append(e[0])
        count += 1

    processQueue.append(process[0])

    while len(processQueue):

        key = processQueue[0][2]

        if key in processStartTime:
            pass
        else:
            if cpuTime > 0:
                processStartTime[processQueue[0][2]] = cpuTime-1 
                answerTime[processQueue[0][2]] = (cpuTime-1) - processQueue[0][0][0]
            else:
                processStartTime[processQueue[0][2]] = 0
                answerTime[processQueue[0][2]] = 0

        for key in answerTime:
            
            if key == processQueue[0][2]:
                continue
            
            else: 
                if key in waitingTime:
                    
                    if key in deadProcesses:
                        waitingTime[key]
                    else:
                        waitingTime[key] += 1

                else:
                    waitingTime[key] = answerTime[key] + 1                

        if cpuTime in startingTime:

            currentProcess = processQueue[0]
            processQueue.pop(0)
            p = elementsInList(startingTime, cpuTime)
            
            while len(p):
                processQueue.append(process[p[0]])
                p.pop(0)

            processQueue.insert(0, currentProcess)

        if quantumTimer == quantum or processQueue[0][1] == 0:
            if processQueue[0][1] == 0:
                returnTime += cpuTime - processQueue[0][0][0]
                deadProcesses[processQueue[0][2]] = 1
                processQueue.pop(0)

            else:
                currentProcess = processQueue[0]
                processQueue.pop(0)
                processQueue.append(currentProcess)

            quantumTimer = 0
        
        cpuTime += 1
        quantumTimer += 1
        if len(processQueue):
            processQueue[0][1] -= 1

    return footer(returnTime, sum(answerTime.values()), sum(waitingTime.values()), t, 'RR')
        

def SJF(t):
    
    t.sort()

    process, waitingTime, returnTime  = [], float(t[0][0]), float(t[0][0]) 
    answerTime, processQueue, cpuTime = float(t[0][0]), [], 0
    startingTime, lastProcessTime = [], 0

    for p in t:
        data = p
        process.append(data)
        startingTime.append(p[0])

    processQueue.append(process[0])

    while len(processQueue):

        if processQueue[0][1] - lastProcessTime == 0:

            waitingTime += cpuTime - processQueue[0][1] - processQueue[0][0]
            answerTime += cpuTime - processQueue[0][1] - processQueue[0][0]
            returnTime += cpuTime - processQueue[0][0]

            processQueue.pop(0)
            lastProcessTime = 0
        
        if cpuTime in startingTime:

            currentProcess = processQueue[0]
            processQueue.pop(0)
            p = elementsInList(startingTime, cpuTime)

            while len(p):
                
                processQueue.append(process[p[0]])
                p.pop(0)
                processQueue = sorted(processQueue, key=lambda col: col[1])
            
            processQueue.insert(0, currentProcess)

        cpuTime += 1
        lastProcessTime += 1

    return footer(returnTime, answerTime, waitingTime, t, 'SJF')


def elementsInList(arr, item):
    data = []
    for e in range(1, len(arr), 1):
        if arr[e] == item:
            data.append(e)
    return data


def footer(returnTime, answerTime, waitingTime, t, funcType):
    mRT, mAT, mWT = returnTime/len(t), answerTime/len(t), waitingTime/len(t)
    ans = "{} {} {} {}".format(funcType, mRT, mAT, mWT)
    return ans


print(FCFS(jobs[:]))
print(SJF(jobs[:]))
print(RR(jobs[:], 2))