from matplotlib import pyplot as plt
import numpy as np



serviceTime8 = open('serviceTimesMu8.txt', 'r')
serviceTime6 = open('serviceTimesMu6.txt', 'r')
serviceTime3 = open('serviceTimesMu3.txt', 'r')


def singleSrvSim(serviceTimes):
    intArrivalTimes = open('interArrivals.txt', 'r')

    #intArr = inter arrival time = ri
    intArr = []
    #srvTime = service time = si
    srvTime = []

    totPackets = 0

    for line in serviceTimes:
        srvTime.append(float(line.rstrip()))
        totPackets +=1


    #arrClockTime = the time at when the packet arrives = ai
    arrClockTime = []

    #delayExp = the delay experience in queue = di
    delayExp = []
    numDelayPackets = 0

    #deptClockTime = the time when the packet finishes being served = ci
    deptClockTime = []

    #totWaitTime = total time a packet waits to be completed = wi
    totWaitTime = []


    #For PACKET 1
    #Inter arrival time (r1) = 0
    #Arrive clock time (a1) = 0
    #Queuing Delay (d1) = 0
    #Total Wait (w1) = Service Time (si)
    #Departure time (c1) = Arrival time (a1) + serivce time (s1)
    delayExp.append(0)
    arrClockTime.append(0)
    intArr.append(0)
    totWaitTime.append(srvTime[0] + delayExp[0])
    deptClockTime.append(arrClockTime[0] + totWaitTime[0])


    cumsum = 0

    
    for line in intArrivalTimes:
        intArr.append(float(line.rstrip()))
        cumsum += float(line)
        arrClockTime.append(cumsum)

        
    for i in range(1, len(srvTime)):
        #If CURR Packet arrives after the PREV packet leaves, there will be no delay
        if(arrClockTime[i] >= deptClockTime[i-1]):
            delay = 0

        #Else, the CURR packet arrives before the PREV packet leaves, there will be delay
        else:
            #The delay for CURR packet is equal to the TOT WAIT of PREV packet - the interArrival time of CURR packet
            delay = delayExp[i-1] + srvTime[i-1] - intArr[i]
            numDelayPackets += 1
            
        #print("\nDELAY AMOUNT for Packet " + str(i + 1))
        #print(delay)
        delayExp.append(delay)
        totWaitTime.append(srvTime[i] + delayExp[i])
        deptClockTime.append(arrClockTime[i] + totWaitTime[i])

    # Sum of Delay experienced / Number of packets that experience delay
    print("\nAverage Queuing Delay (seconds / packet):")
    totDelay = sum(delayExp)
    print(totDelay / numDelayPackets)

    #Sum of time packets are in system / Number of packets that are in system
    print("\nAverage time a packet spends in the system:")
    waitTime = sum(totWaitTime)
    print(waitTime / len(totWaitTime))
            
    #Number of packets that experience delay / Number of packets in the system
    print("\nProbability a Packet will wait in the system:")
    print(numDelayPackets / totPackets)


    print("\nAverage number of packets in the system:")
    return delayExp


delay8 = singleSrvSim(serviceTime8)

delay6 = singleSrvSim(serviceTime6)

delay3 = singleSrvSim(serviceTime3)

plt.subplot(3,1,1)
plt.bar(np.arange(len(delay8)), delay8)
plt.xlabel("Packet #")
plt.ylabel("Delay in S")
plt.title("Delay Packets Experienced with a Service Time of 8p/s")


plt.subplot(3,1,2)
plt.bar(np.arange(len(delay6)), delay6)
plt.xlabel("Packet #")
plt.ylabel("Delay in S")
plt.title("Delay Packets Experienced with a Service Time of 6p/s")


plt.subplot(3,1,3)
plt.bar(np.arange(len(delay3)), delay3)
plt.xlabel("Packet #")
plt.ylabel("Delay in S")
plt.title("Delay Packets Experienced with a Service Time of 3p/s")


plt.show()




