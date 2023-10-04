from matplotlib import pyplot as plt

intArrivalTimes = open('interArrivals.txt', 'r')
serviceTime8 = open('serviceTimesMu8.txt', 'r')

#intArr = inter arrival time = ri
#THis is GIVEN from txt file
intArr = []

#srvTime = service time = si
#This is GIVEN from txt file
srvTime = []

for line in serviceTime8:
    srvTime.append(float(line.rstrip()))


#arrClockTime = the time at when the packet arrives = ai
# ai = ri + ai-1
# a2 = r2 + a1
# a1 = 0
arrClockTime = []

#delayExp = the delay experience in queue = di
# d1 = 0
# no delay on first packet because there are no previous packets 
# if (ai > ci-1) di = 0
# else( di = di-1 + si-1 - ri)
delayExp = []

#deptClockTime = the time when the packet finishes being served = ci
# ci = ai + wi
deptClockTime = []

#totWaitTime = total time a packet waits to be completed = wi
# wi = si + di
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
    if(arrClockTime[i] >= deptClockTime[i-1]):
        #print("\nPacket " + str(i-1) + " departs at " + str(deptClockTime[i-1]))
        #print("Packet " + str(i) + " arrives at " + str(arrClockTime[i]))
        delay = 0

    else:
        #print("\nPacket " + str(i-1) + " departs at " + str(deptClockTime[i-1]))
        #print("Packet " + str(i) + " arrives at " + str(arrClockTime[i]))
        delay = delayExp[i-1] + srvTime[i-1] - intArr[i]
        #print("Packet " + str(i-1) + " DELAYED " + str(delayExp[i-1]) +  " + SERVED " + str(srvTime[i-1]) + " - ARRIVAL of next " +str(intArr[i]))
        
    
    #print("\nDELAY AMOUNT for Packet " + str(i + 1))
    #print(delay)
    delayExp.append(delay)
    totWaitTime.append(srvTime[i] + delayExp[i])
    deptClockTime.append(arrClockTime[i] + totWaitTime[i])

    
'''
print("Packets 1 - 5 Ai \n")
print(arrClockTime[:10])

print("\nPackets 1 - 5 Si \n")
print(srvTime[:10])

print("\nPackets 1 - 5 Di \n")
print(delayExp[:10])

print("\n Packets 1 - 5 Wi \n")
print(totWaitTime[:10])

print("\nPackets 1 - 5 Ci \n")
print(deptClockTime[:10])

'''


for i in range(len(delayExp)):
    plt.bar(i, delayExp[i])

plt.xlabel("Packet #")
plt.ylabel("Delay in S")
plt.show()

print("GRAPHS")

