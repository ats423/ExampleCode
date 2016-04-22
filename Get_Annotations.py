#Code: Get mapped sequences that have protein coding gene annotations 
#!/usr/bin/python   

import re 
import sys 
import os   

#Open the protein coding gene annotation file for reading 

input_file = open( "/sonashs/gingeras/nlsas_norepl/user/ascavell/STAR_Work/STAR_output/ANN_PROTEIN.txt", "rU" ) 

#Open the SAM file containing the mapped sequences 
#from the CIGAR string for reading 

sec_input_file = open ("/sonashs/gingeras/nlsas_norepl/user/ascavell/STAR_Work/STAR_output/PARSED_MATCH_255_SA M_DATA.sam", "rU") 

#Open a file for writing 

writing_file = open ("/sonashs/gingeras/nlsas_norepl/user/ascavell/STAR_Work/STAR_output/MATCHED_PROTEIN_2.tx t", "w")    

#Define the function get_word 
#and pass the two reading files 
#to it  

def get_word (myFile, mySecFile): 
   
    #create an empty list 
    sec_list = [] 
    
    #use the for loop to read the 
    #SAM file line by line 
    
    for secRow in mySecFile: 
        
        #remove the newlines 
        new_line = secRow.rstrip("\n") 
        
        #split on the tab delimiter 
        column = new_line.split('\t') 
       
        #assign the read position to 
        #the variable start_num 
        
        start_num = column[1] 
         
        #use a second for loop to read the 
        #annotation file line by line 
        
        for aRow in myFile: 
            
            #remove newlines 
            new_line_2 = aRow.rstrip("\n") 
           
            #split on the tab delimiter 
            column_pos = new_line_2.split('\t') 
            
            #assign the gene start position 
            #to start_col variable 
            
            start_col = column_pos[1] 
            
            #assign the gene end position 
            #to the end_col variable 
            
            end_col = column_pos[2] 
            
            #use the if statement to check 
            #if the read position is inbetween 
            #the gene start and end positions 
            
            if int(start_col) <= int(start_num) <= int( end_col): 
                
                #if the read position is  
                #inbetween the gene  
                #start and end positions 
                #then assign the mapped sequence 
                #to the variable seq 
               
                seq = column[4] + "\n" 
               
               #add the mapped sequence 
                #to the list  
               
                sec_list.append(seq)  
      
    #return the list containing the mapped 
    #sequences with protein coding gene annotations         
    
    return sec_list 
