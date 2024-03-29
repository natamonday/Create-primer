from Bio import SeqIO                                   #import module to read sequence
from Bio.Seq import Seq                                 #import module to analys sequence
import os

list5 = list()
dataTm5 = list()
dataGC5 = list()
alldata5 = list()
ana_data5 = list()
list3 = list()
dataTm3 = list()
dataGC3 = list()
alldata3 = list()
ana_data3 = list()                                      #crete blank list to keep data

	
os.chdir('D:\Resume\Create Primer')
filename = input('Input file name here :')              #input filename "test2.fasta"
for record in SeqIO.parse(filename, "fasta"):           #for any sequence in file .fasta
    seq_5 = str(record.seq)                             #assign seq_5 to be sequence of 5'-3'
    seq_3 = str(record.seq.reverse_complement())        #assign seq_3 to be sequence of 3'-5'

#######################################################################################################################################

class primer_5:                                         #create class of analysis of sequence 5'-3'
    def pri():                                          #create function to find pre-primer 
        pos = 0                                         #first position equal 0
        for i in range(0,len(seq_5)+1):                 #for initial position in range 0 to length of sequence 
            pre_prim = seq_5[pos:pos+20]                #pre-primer create from position to position+20
            if len(pre_prim)!= 20 or pre_prim.count('AAAA')>1 or pre_prim.count('AAAAA')>1 or pre_prim.count('TTTT')>1:
                break                                   #if pre-primer contain 'AAAAA' or 'TTTT' , it will go to next position
            list5.append(pre_prim)                      #if pre-primer didn't contain 'AAAAA' or 'TTTT', assign it in list5
            pos += 1                                    #position move forward +1
                
    def Tm():                                           #create function to calculate Tm 
        for i in list5:                                 #for any pre-primer in list5 
                A = i.count('A')
                T = i.count('T')
                C = i.count('C')
                G = i.count('G')                        #calculate base and assing to character or any base
                Tm = (2*(A+T))+(4*(C+G))                #calculate Tm of this pre-primer
                dataTm5.append(Tm)                      #append Tm value into dataTm5   

    def GC():                                           #create function to calculate GC%
        for primer in list5:                            #for any pre-primer in list5
            G_count = primer.count('G')                 #count G base in pre-primer
            C_count = primer.count('C')                 #count C base in pre-primer
            total = len(primer)                         #count total base in pre-primer
            CG_content = ((G_count+C_count)/total)*100  
            dataGC5.append(CG_content)                  #append CG% into dataGC5

    def createdata():                                   #create function to group data into 1 key
        for i in range(0,len(list5)):
            D0 = list5[i]
            D1 = dataGC5[i]
            D2 = dataTm5[i]
            alldata5.append({D0:[D1,D2]})

    def analyze_pri():                                  #create function to analysis data
        for items in alldata5:                          #for any data in alldata
            for key,item in items.items():              #for any key and item in data dictionary
                if item[0] > 50 and item[0] < 65:       #if CG% more that 50 but less than 65
                    if item[1] > 55 and item[1] < 66:   #if Tm more that 55 but less than 66
                        firstlocation = seq_5.find(key)+1 #assign position that have first pattern key to be first location
                        endlocation = seq_5.find(key)+20 #assign position plus to 20 to be end location
                        ana_data5.append({key:[int(item[0]),item[1],firstlocation,endlocation]}) #append allposition into new data

    def main_5():                                       #create function to call of function in sequence 5'-3'
        primer_5.pri()
        primer_5.Tm()
        primer_5.GC()
        primer_5.createdata()
        primer_5.analyze_pri()

###############################################################################################

class primer_3:
    def pri():
        pos = 0
        for i in range(0,len(seq_3)+1):
            pre_prim = seq_3[pos:pos+20]
            if len(pre_prim)!= 20 or pre_prim.count('AAAA')>1 or pre_prim.count('AAAAA')>1 or pre_prim.count('TTTT')>1:
                break
            list3.append(pre_prim)
            pos += 1
                
    def Tm():
        for i in list3:
                A = i.count('A')
                T = i.count('T')
                C = i.count('C')
                G = i.count('G')
                Tm = (2*(A+T))+(4*(C+G))
                anelling = Tm-5
                dataTm3.append(Tm)    

    def GC():
        for primer in list3:
            G_count = primer.count('G')
            C_count = primer.count('C')
            total = len(primer)
            CG_content = ((G_count+C_count)/total)*100
            dataGC3.append(CG_content)

    def createdata():
        for i in range(0,len(list3)):
            D0 = list3[i]
            D1 = dataGC3[i]
            D2 = dataTm3[i]
            alldata3.append({D0:[D1,D2]})

    def analyze_pri():
        for items in alldata3:
            for key,item in items.items():
                if item[0] > 50 and item[0] < 65:
                    if item[1] > 55 and item[1] < 66:
                        endlocation = seq_3[::-1].find(key[::-1])+1           #change sequence to be reverse sequence to find in term of 3'-5' and save position
                        firstlocation = seq_3[::-1].find(key[::-1])+20
                        ana_data3.append({key:[int(item[0]),item[1],firstlocation,endlocation]})

    def main_3():
        primer_3.pri()
        primer_3.Tm()
        primer_3.GC()
        primer_3.createdata()
        primer_3.analyze_pri()

##########################################################################################################

def main():                                                                    #create function to call all of class to run program
    primer_5.main_5()
    primer_3.main_3()

    """"Show the prediction that it can be real primer"""
    
    print('Forward Primer| Have',len(ana_data5),'primer')
    print('{Primer: [GC content , Tm , start position , stop position]}')
    for i in ana_data5:
        print(i)
    print('====================')
    print('Reverse Primer | Have',len(ana_data3),'primer')
    print('{Primer: [GC content , Tm , stop position , start position]}')
    for i in ana_data3:
        print(i)
    print('====================')
                
main()


