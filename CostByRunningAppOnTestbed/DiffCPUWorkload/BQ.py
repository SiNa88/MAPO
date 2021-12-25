F65KB  = 0.125
F125KB = 0.25
F500KB = 0.5
F1MB   = 4


CommTimeToThreeRPi1MB = 0.102


CommTimeToRPi1MB   = 0.07 #sec



CommTimeToVM1MB   = 1.4  #sec


CompTime200VM = 0.00001        #sec
CompTime500VM = 0.00003      #sec
CompTime1000VM = 0.00007      #sec
CompTime2000VM = 0.0002      #sec
CompTime4000VM = 0.0004      #sec


CompTime200RPi = 0.0003
CompTime500RPi = 0.0008
CompTime1000RPi = 0.00195
CompTime2000RPi = 0.00514  #sec
CompTime4000RPi = 0.00914  #sec



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

Component4000RPi =    (CompTime4000RPi*Cost_Processing_RPi)     


Computation = Component200RPi + Component200RPi + Component200RPi + Component200RPi + Component200RPi + Component200RPi + Component200RPi 
Cost200MI =  Computation + (Cost_Storage_RPi*F1MB * 7) +   (CommTimeToThreeRPi1MB  * Cost_BW_RPi) 

Computation = Component500RPi + Component500RPi + Component500RPi + Component500RPi + Component500RPi + Component500RPi + Component500RPi 
Cost500MI = Computation + (Cost_Storage_RPi*F1MB * 7) +  (CommTimeToThreeRPi1MB * Cost_BW_RPi) 

Computation = Component1000RPi + Component1000RPi + Component1000RPi + Component1000RPi + Component1000RPi + Component1000RPi + Component1000RPi 
Cost1000MI = Computation + (Cost_Storage_RPi*F1MB * 7) +  (CommTimeToThreeRPi1MB * Cost_BW_RPi) 

Computation = Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi 
Cost2000MI =   Computation + (Cost_Storage_RPi*F1MB * 7) +    (CommTimeToThreeRPi1MB   * Cost_BW_RPi)

Computation = Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi + Component2000RPi 
Cost2000MI =   Computation + (Cost_Storage_RPi*F1MB * 7) +    (CommTimeToThreeRPi1MB   * Cost_BW_RPi)

Computation = Component4000RPi + Component4000RPi + Component4000RPi + Component4000RPi + Component4000RPi + Component4000RPi + Component4000RPi 
Cost4000MI =   Computation + (Cost_Storage_RPi*F1MB * 7) +    (CommTimeToThreeRPi1MB   * Cost_BW_RPi)

print  (Cost200MI, Cost500MI, Cost1000MI, Cost2000MI, Cost4000MI)
