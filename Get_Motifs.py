#Code: Get most frequently occurring motifs 
#!/usr/bin/python  
#open the file for reading  

input_file = open( "/sonashs/gingeras/nlsas_norepl/user/ascavell/STAR_Work/STAR_output/MATCHED_PROTEIN_2.tx t", "rU" ) 

#open the file for writing 

writing_file = open ("/sonashs/gingeras/nlsas_norepl/user/ascavell/STAR_Work/STAR_output/PROTEIN_MOTIF_OUTPU T_4B.txt", "w")  

#define the function get_motif 
#and pass the reading file to it 

def get_motif(myFile): 

    #create empty dictionaries 

    Motif={}; 
    Num={}; 

    #create empty list 
    list = [] 

    #assign variable to a minimum and maximum nucleotide 
    #number that will be used in the motif search 
    # 
    #this can be changed depending on the length of the motif desired 

    minimum=4; #the minimum length of a motif will be 3 nucleotides 
    maximum=5; #the maximum length of a motif will be 4 nucleotides (up to but not including 5) 

    #use for loop to go through 
    #the reading file with 
    #the protein coding mapped 
  
    #sequences line by line 

    for aRow in myFile: 

        #remove newlines 

        no_new = aRow.rstrip("\n") 

        #assign seq variable to mapped 
        #sequences in the reading file 

        seq = no_new 

        #use for loop to go through seq  
        #based on the range of nucleotides 

        for length_motif in range(minimum , maximum):  

                #use the for loop to go through each  
                #nucleotide in seq based how many nucleotides 
                #the motif will contain  

                for i in range(len(seq)-length_motif-1):  

                        #assign each motif to motif_str 

                        motif_str = seq[i:i+length_motif];  

                        #use if-else function to see if the  
                        #same motif is already present in the 
                        #hash and to count the number of times  
                        #the same motif occurs 

                        if motif_str in Motif.keys():  

                                #if the motif is already present in 
                                #the Motif hash, add 1 to the count    

                                Motif[motif_str] += 1;  
                        else: 
                                #else keep the count the same 

                                Motif[motif_str] = 1;  

                        #use if-else function to count the number  
                        #of 4-nucleotide motifs and 
                        #add to the Num hash                 
                        
                        if len(motif_str) in Num.keys():  
                        
                                #if a motif of the same size exists, add to the count 
                        
                                Num[len(motif_str)] +=1; 
                        else: 
                        
                                #else, do not add to the count 
                        
                                Num[len(motif_str)] = 1;   
          
        #use the for loop go through each key and value  
        #in the Motif hash using the iteritems() method  
        
        for key, value in Motif.iteritems():  
        
                #assign the motifs to my_keys 
        
                my_keys = key 
        
                #divide the number of times the same motif occurs by the 
                #total number of motifs for that nucleotide range 
        
                my_values = float(value)/float(Num[len(key)]) 
        
                #concatenate the motif frequencies with the motif strings 
        
                my_string = str(my_values) + "\t" + str(my_keys) + "\n" 
        
                #add motifs and their frequencies to the list 
        
                list.append(my_string) 
        
                #sort the frequencies in descending order 
        
                list.sort(reverse=True) 
    
    #return the sorted list 
    #with motif frequencies              
    
    return list        
  
#assign the return listed with motif 
#frequencies to the motif_test variable      

motif_test = get_motif(input_file) 

#write the motif frequencies in motif_test 
#to the writing file 

writing_file.writelines(motif_test) 

#close the input and output files 

input_file.close() 
writing_file.close()   
