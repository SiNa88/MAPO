resources= {}


#Node ID,1,2,3,4,5
#Nodes Name,My PC (Lenovo PC) as a CDC,Raspberry Pi as a Gateway,Raspberry Pi,Raspberry Pi,Raspberry Pi,,,,,,,,,,,,,,,,
#MIPS,29491,1400,1400,1400,1400
#RAM (MB),16384,1024,1024,1024,1024
#Storage (MB),256000,65536,65536,65536,65536
#uplink bandwidth (MB),1024,1024,1024,1024,1024
#level hierarchy,0,1,2,2,2
#p_Pj and p_Mj in Equations 4 and 5 (watt),220,6,6,6,6
#cost of Proc,0.002,0.002,0.003,0.003,0.003
#cost of Mem,0.0002,0.03,0.03,0.03,0.03
#cost of BW(Comm),0.00002,0.03,0.04,0.04,0.04

resources['cloud']={
            'CPU':'29491',
            'MEM':'1024',
            'STOR':'256',
            'BW':'1024'}

resources['proxy']={
            'CPU':'1400',
            'MEM':'1024',
            'STOR':'256',
            'BW':'1024'}

resources['m-0-0']={
            'CPU':'1400',
            'MEM':'1024',
            'STOR':'512',
            'BW':'1024'}

resources['m-0-1']={
            'CPU':'1400',
            'MEM':'1024',
            'STOR':'512',
            'BW':'1024'}

resources['m-0-2']={
            'CPU':'1400',
            'MEM':'1024',
            'STOR':'256',
            'BW':'1024'}


print (resources)
print (type(resources))

import json

s= json.dumps(resources)

print (s)
print (type(s))



with open("C:\\Users\\ASUS\\Desktop\\json\\InputToMultiObjectiveAlgorithm\\resources.json","w") as outfile:
        outfile.write(s)

