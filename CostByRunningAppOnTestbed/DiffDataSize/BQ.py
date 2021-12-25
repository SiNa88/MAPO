F65KB  = 0.125
F125KB = 0.25
F500KB = 0.5
F1MB   = 1

CommTimeToThreeRPi65KB = 0.015
CommTimeToThreeRPi125KB = 0.017
CommTimeToThreeRPi500KB = 0.042
CommTimeToThreeRPi1MB = 0.102

CommTimeToRPi65KB  = 0.051#sec
CommTimeToRPi125KB = 0.053#sec
CommTimeToRPi500KB = 0.065#sec
CommTimeToRPi1MB   = 0.07 #sec


CommTimeToLenovo65KB  = 0.57 #sec
CommTimeToLenovo125KB = 0.763#sec
CommTimeToLenovo500KB = 1.01 #sec
CommTimeToLenovo1MB   = 1.4  #sec


CompTime200Lenovo = 0.00001        #sec
CompTime500Lenovo = 0.00003      #sec
CompTime1000Lenovo = 0.00007      #sec
CompTime2000Lenovo = 0.0002      #sec


CompTime200RPi = 0.0003
CompTime500RPi = 0.0008
CompTime1000RPi = 0.00195
CompTime2000RPi = 0.00514  #sec


Cost_Processing_Lenovo = 0.00035  	  #MB
Cost_Storage_Lenovo = 0.00000015	  #MB
Cost_BW_Lenovo = 0.000000035	  	  #MB


Cost_Processing_GWRPi = 0.00045        #MB
Cost_Storage_GWRPi = 0.00000018        #MB
Cost_BW_GWRPi = 0.00000004             #MB


Cost_Processing_RPi = 0.0004        #MB
Cost_Storage_RPi = 0.0000002        #MB
Cost_BW_RPi = 0.00000004             #MB


######## RPi

Component200RPi =    (CompTime200RPi*Cost_Processing_GWRPi)    

Component500RPi =    (CompTime500RPi*Cost_Processing_GWRPi)  

Component1000RPi =    (CompTime1000RPi*Cost_Processing_GWRPi)    

Component2000RPi =    (CompTime2000RPi*Cost_Processing_GWRPi)    


Computation = Component200RPi + Component500RPi + Component200RPi + Component1000RPi + Component2000RPi + Component200RPi + Component200RPi 
Cost65KB =  Computation + (Cost_Storage_GWRPi*F65KB * 7) +   (CommTimeToThreeRPi65KB  * Cost_BW_GWRPi) 
Cost125KB = Computation + (Cost_Storage_GWRPi*F125KB * 7) +  (CommTimeToThreeRPi125KB * Cost_BW_GWRPi) 
Cost500KB = Computation + (Cost_Storage_GWRPi*F500KB * 7) +  (CommTimeToThreeRPi500KB * Cost_BW_GWRPi) 
Cost1MB =   Computation + (Cost_Storage_GWRPi*F1MB * 7) +    (CommTimeToThreeRPi1MB   * Cost_BW_GWRPi)

print  (Cost65KB, Cost125KB, Cost500KB, Cost1MB)
