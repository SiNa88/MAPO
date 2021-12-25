F65KB  = 0.125
F125KB = 0.25
F500KB = 0.5
F1MB   = 1

CommTimeToRPi65KB  = 0.051#sec
CommTimeToRPi125KB = 0.053#sec
CommTimeToRPi500KB = 0.065#sec
CommTimeToRPi1MB   = 0.07 #sec


CommTimeToVM65KB  = 0.57 #sec
CommTimeToVM125KB = 0.763#sec
CommTimeToVM500KB = 1.01 #sec
CommTimeToVM1MB   = 1.4  #sec

CompTime200VM = 0.00001        #sec
CompTime500VM = 0.00003      #sec
CompTime1000VM = 0.00007      #sec
CompTime2000VM = 0.0002      #sec


CompTime200RPi = 0.0003
CompTime500RPi = 0.0008
CompTime1000RPi = 0.00195
CompTime2000RPi = 0.00514  #sec


Cost_Processing_VM = 0.00035  	  #sec
Cost_Storage_VM = 0.00000015	  #MB
Cost_BW_VM = 0.000000035	  	  #sec


Cost_Processing_GWRPi = 0.00045        #sec
Cost_Storage_GWRPi = 0.00000018        #MB
Cost_BW_GWRPi = 0.00000004             #sec


Cost_Processing_RPi = 0.0004        #sec
Cost_Storage_RPi = 0.0000002        #MB
Cost_BW_RPi = 0.00000004             #sec


######## RPi

Component200RPi =    (CompTime200RPi*Cost_Processing_RPi)        

Component500RPi =    (CompTime500RPi*Cost_Processing_RPi)     

Component1000RPi =    (CompTime1000RPi*Cost_Processing_RPi)       

Component2000RPi =    (CompTime2000RPi*Cost_Processing_RPi)      


######## VM

Component200VM =    (CompTime200VM*Cost_Processing_VM)  

Component500VM =    (CompTime500VM*Cost_Processing_VM)  

Component1000VM =    (CompTime1000VM*Cost_Processing_VM)

Component2000VM =    (CompTime2000VM*Cost_Processing_VM)

Computation = Component200RPi + Component500RPi + Component200RPi + (CompTime1000RPi*Cost_Processing_GWRPi) + Component2000VM + Component200VM + Component200VM 
Cost65KB =  Computation + (Cost_Storage_RPi*F65KB * 3)  + (Cost_Storage_GWRPi*F65KB) +  (Cost_Storage_VM*F65KB * 3) + (CommTimeToVM65KB  * Cost_BW_VM) 
Cost125KB = Computation + (Cost_Storage_RPi*F125KB * 3) + (Cost_Storage_GWRPi*F125KB) + (Cost_Storage_VM*F125KB * 3) + (CommTimeToVM125KB * Cost_BW_VM) 
Cost500KB = Computation + (Cost_Storage_RPi*F500KB * 3) + (Cost_Storage_GWRPi*F500KB) + (Cost_Storage_VM*F500KB * 3) + (CommTimeToVM500KB * Cost_BW_VM) 
Cost1MB =   Computation + (Cost_Storage_RPi*F1MB * 3)   + (Cost_Storage_GWRPi*F1MB) + (Cost_Storage_VM*F1MB * 3) + (CommTimeToVM1MB   * Cost_BW_VM)

print  (Cost65KB, Cost125KB, Cost500KB, Cost1MB)
