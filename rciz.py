# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 16:53:36 2018

@author: Emalron
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 14:00:13 2018

@author: 9010553
"""
import matplotlib.pyplot as plt
import valves
import random as rnd

popHis = [[1], [0], [0]]
popDis = [[0], [0], [0]]
totHis = [0]
ciHis = [0]
emHis = [0]
laHis = [0]
valHis = [[0], [0], [0]]
vOut = []
vOutHis = [[0], [0], [0]]
time = [0]
tax = [0]
avgLandValue = 80.0
employ = [0]
zoneLvUp = -1

for i in range(600):
    # calculating valves
#    print(str(popHis[0][i]) + ' ' + str(popHis[1][i]) + ' ' + str(popHis[2][i]))
    valves.calculate(popHis[0], popHis[1], popHis[2])
    vOut = valves.update()
    
    resValve = valHis[0][i] + vOut[0]
    comValve = valHis[1][i] + vOut[1]
    indValve = valHis[2][i] + vOut[2]
    for n in range(3):
        vOutHis[n].append(vOut[n])
    emHis.append(vOut[3])
    laHis.append(vOut[4])
    
    resValve = max(resValve, -2000)
    resValve = min(resValve, 2000)
    valHis[0].append(resValve)
    
    comValve = max(comValve, -1500)
    comValve = min(comValve, 1500)
    valHis[1].append(comValve)
    
    indValve = max(indValve, -1500)
    indValve = min(indValve, 1500)
    valHis[2].append(indValve)
        
    # find zone to be upgraded
#    velocities = [0, 0, 0]
#    velocities[0] = (0.0211 + (.1737-.0211)/(5000.0 + 5000.0) * (valHis[0][i+1] + 5000))
#    velocities[1] = (0.0736 + (.1213-.0736)/(1500.0 + 1500.0) * (valHis[1][i+1] + 1500))
#    velocities[2] = (0.0746 + (.1204-.0611)/(1500.0 + 1500.0) * (valHis[2][i+1] + 1500))
#    
#    for k in range(3):
#        popDis[k].append(popDis[k][i]+velocities[k])
#        popHis[k].append(int(popHis[k][0] + popDis[k][i+1]))


    curVal = [valHis[0][i+1], valHis[1][i+1], valHis[2][i+1]]
#    curVal = [vOut[0], vOut[1], vOut[2]]
#    zoneLvUp = curVal.index(max(curVal))
#    zoneLvDw = curVal.index(min(curVal))

#    zoneLvUp = -1
    
#    if curVal[0] >= 2000:
#        zoneLvUp = 0
#    elif curVal[1] >= 1500:
#        zoneLvUp = 1
#    elif curVal[2] >= 1500:
#        zoneLvUp = 2

    
    popHis[0].append(popHis[0][i])
    popHis[1].append(popHis[1][i])
    popHis[2].append(popHis[2][i])
    

    if curVal[0] > -350 and curVal[0] > curVal[1] and curVal[0] > curVal[2]:
        popHis[0][i+1] = popHis[0][i+1]+1
    else:
        if curVal[0] < 350 and curVal[0] < curVal[1] and curVal[0] < curVal[2] and popHis[0][i+1] > 0:
            popHis[0][i+1] = popHis[0][i+1]-1
                  
    if curVal[1] > -350 and curVal[1] > curVal[0] and curVal[1] >= curVal[2]:
        popHis[1][i+1] = popHis[1][i+1]+1
    else:
        if curVal[1] < 350 and curVal[1] < curVal[0] and curVal[1] < curVal[2] and popHis[1][i+1] > 0:
            popHis[1][i+1] = popHis[1][i+1]-1
                  
    if curVal[2] > -350 and curVal[2] >= curVal[1] and curVal[2] > curVal[0]:
        popHis[2][i+1] = popHis[2][i+1]+1
    else:
        if curVal[2] < 350 and curVal[2] < curVal[1] and curVal[2] < curVal[0] and popHis[2][i+1] > 0:
            popHis[2][i+1] = popHis[2][i+1]-1

#    if i%2 == 0:
#        if zoneLvUp == 0 and curVal[0] >= 2000:
#            popHis[0][i+1] = popHis[0][i+1]+1
#        elif zoneLvUp == 1 and curVal[1] >= 1500:
#            popHis[1][i+1] = popHis[1][i+1]+1
#        elif zoneLvUp == 2 and curVal[2] >= 1500:
#            popHis[2][i+1] = popHis[2][i+1]+1
            
#    if zoneLvUp > -1:
#        for k in range(3):
#            if k == zoneLvUp:
#                popHis[k].append(popHis[k][i]+1)
#            else:
#                popHis[k].append(popHis[k][i])
#        zoneLvUp = -1
#    else:
#        zoneLvUp = -1
#        for k in range(3):
#            popHis[k].append(popHis[k][i])
                
    time.append(i+1)
    totHis.append(popHis[0][i]+popHis[1][i]+popHis[2][i])
    ciHis.append(popHis[1][i+1]+popHis[2][i+1])
    tax.append(totHis[i+1]*avgLandValue*7/120.0)
        
#plt.step(time,normResHis, label='R-Zone')
plt.step(time,popHis[0], label='R-Zone')
plt.step(time,popHis[1], label='C-Zone')
plt.step(time,popHis[2], label='I-Zone')
#plt.step(time,ciHis, label='CI-Zone')
#plt.step(time,totHis)
plt.legend(ncol=1, loc='upper left')
plt.show()

#plt.step(time,employ)
#plt.show()

plt.plot(valHis[0], label='R-Zone')
plt.plot(valHis[1], label='C-Zone')
plt.plot(valHis[2], label='I-Zone')
plt.legend(ncol=1, loc='lower right')
plt.show()

plt.plot(vOutHis[0], label='R-Zone')
plt.plot(vOutHis[1], label='C-Zone')
plt.plot(vOutHis[2], label='I-Zone')
plt.legend(ncol=1, loc='lower right')
plt.show()

plt.plot(emHis, label='Employment')
plt.plot(laHis, label='LaborBase')
plt.legend(ncol=1, loc='lower right')
plt.show()