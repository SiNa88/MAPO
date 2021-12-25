application= {}

#application_components:
#DetMentStat,DecomSaftConcern,GenMedRec,ViPatHist,Summ,MentHealthAct,FindenKlinik
#CPU:       200,500,200,1000,2000,200,200
#MEM:       100,200,200,100,300,500,200
#STOR:      256,256,256,512,512,256,256
#Data_i:    125,125,125,65,125,500,125
application['DetMentStat']={
            'CPU':'200',
            'MEM':'100',
            'STOR':'256',
            'Data_i':'125'}

application['DecomSaftConcern']={
            'CPU':'500',
            'MEM':'200',
            'STOR':'256',
            'Data_i':'125'}

application['GenMedRec']={
            'CPU':'200',
            'MEM':'200',
            'STOR':'256',
            'Data_i':'125'}

application['ViPatHist']={
            'CPU':'1000',
            'MEM':'100',
            'STOR':'512',
            'Data_i':'65'}

application['Summ']={
            'CPU':'2000',
            'MEM':'300',
            'STOR':'512',
            'Data_i':'125'}

application['MentHealthAct']={
            'CPU':'200',
            'MEM':'500',
            'STOR':'256',
            'Data_i':'500'}

application['FindenKlinik']={
            'CPU':'200',
            'MEM':'200',
            'STOR':'256',
            'Data_i':'125'}

print (application)
print (type(application))

import json

s= json.dumps(application)

print (s)
print (type(s))


with open("C:\\Users\\ASUS\\Desktop\\json\\InputToMultiObjectiveAlgorithm\\application_requirement_MHC.json","w") as outfile:
        outfile.write(s)
