F65KB  = 0.125
F125KB = 0.25
F500KB = 0.5
F1MB   = 1


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

######## VM

Component200VM =    (CompTime200VM*Cost_Processing_VM)   

Component500VM =    (CompTime500VM*Cost_Processing_VM)    

Component1000VM =    (CompTime1000VM*Cost_Processing_VM)  

Component2000VM =    (CompTime2000VM*Cost_Processing_VM)

Component4000VM =    (CompTime4000VM*Cost_Processing_VM)


Computation = Component200RPi + Component200VM + Component200VM + Component200VM + Component200RPi +  (CompTime200RPi*Cost_Processing_GWRPi) +  (CompTime200RPi*Cost_Processing_GWRPi) 
Cost200MI =  Computation + (Cost_Storage_RPi*F1MB ) + (Cost_Storage_GWRPi*F1MB*2) +  (Cost_Storage_VM*F1MB  * 4) +   (CommTimeToVM1MB  * Cost_BW_VM) 

Computation = Component500RPi + Component500VM + Component500VM + Component500VM + Component500RPi +  (CompTime500RPi*Cost_Processing_GWRPi)  +  (CompTime500RPi*Cost_Processing_GWRPi)  
Cost500MI = Computation + (Cost_Storage_RPi*F1MB ) + (Cost_Storage_GWRPi*F1MB *2)+  (Cost_Storage_VM*F1MB * 4) +   (CommTimeToVM1MB * Cost_BW_VM) 

Computation = Component1000RPi + Component1000VM + Component1000VM + Component1000VM + Component1000RPi +  (CompTime1000RPi*Cost_Processing_GWRPi)  +  (CompTime1000RPi*Cost_Processing_GWRPi) 
Cost1000MI = Computation + (Cost_Storage_RPi*F1MB ) + (Cost_Storage_GWRPi*F1MB *2)+  (Cost_Storage_VM*F1MB * 4) +   (CommTimeToVM1MB * Cost_BW_VM) 

Computation = Component2000RPi + Component2000VM + Component2000VM + Component2000VM + Component2000RPi +  (CompTime2000RPi*Cost_Processing_GWRPi)  +  (CompTime2000RPi*Cost_Processing_GWRPi) 
Cost2000MI =   Computation + (Cost_Storage_RPi*F1MB ) + (Cost_Storage_GWRPi*F1MB *2)  +  (Cost_Storage_VM*F1MB   * 4) +   (CommTimeToVM1MB   * Cost_BW_VM)

Computation = Component4000RPi + Component4000VM + Component4000VM + Component4000VM + Component4000RPi +  (CompTime4000RPi*Cost_Processing_GWRPi)  +  (CompTime4000RPi*Cost_Processing_GWRPi) 
Cost4000MI =   Computation + (Cost_Storage_RPi*F1MB ) + (Cost_Storage_GWRPi*F1MB *2)  +  (Cost_Storage_VM*F1MB   * 4) +   (CommTimeToVM1MB   * Cost_BW_VM)

print  (Cost200MI, Cost500MI, Cost1000MI, Cost2000MI, Cost4000MI)
