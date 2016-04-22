#Code: Access Biomart 
#!/usr/bin/python  
#import BiomartServer from the  
#biomart module 

from biomart import BiomartServer 

#connect to the biomart server 

server = BiomartServer("http://www.biomart.org/biomart") 

#show all the server databases on the console 

server.show_databases()  

#show all the  server datasets on the console 

server.show_datasets() 

#use the 'uniprot' dataset 

uniprot = server.datasets['uniprot'] 

#run a search with custom filters and attributes 
#such as searching for results with the  
#protein name "Dystrophin"  
#the UniProt accession number, 
#the protein name and the  
#gene name are give for  
#each search result 

response = uniprot.search({ 
  'filters': { 
      'protein_name': ['Dystrophin'] 
  }, 
  'attributes': [ 
      'accession', 'protein_name', 'gene_name' 
  ] 
  
}) 

#print each search result 
#with each attribute separated 
#by a tab delimeter 

for line in response.iter_lines(): 
        print line.split("\t")   
