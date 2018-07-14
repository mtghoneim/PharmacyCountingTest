# The first part of my program parses the input and organizes it in manageable data structure for further processing.
# This format is a list of entries where each entry is a dictionary of all key fields and their values.
# Based on the desired output, it is apparent that the unique field should be the drug name. This program organizes the output structure in dictionary format.
# Each key is a unique drug, and each value is composed of a list of integer and a double/float. Integer for number of prescribers and float for total cost.


def main():
    input_file = open('itcont.txt') #opens the input file
    
    lines_list=[input_file.readline().strip()] # this is an ordered list of the lines in input line
    
    #the lines list always has the field key line in position '0'
    
    field_keys=lines_list[0].strip().split(',')
    
    #print (field_keys)
    
    paired_struct= {}
    
    parsed_file=[]
        
    total_data_lines= 0
    
    output_file= {'AMBIEN': [0,0], 'BENZTROPINE MESYLATE': [0,0], 'CHLORPROMAZINE': [0,0]}
    
    for key in field_keys:
        paired_struct[key]= {}
        
    #print(paired_struct)
        
    for line in input_file: # this calculates the total number of lines and fills the lines list
        
        total_data_lines +=1
        
        itemized=line.strip().split(',')
        
        #print(itemized)
        fields_counter = 0
        
        for key in field_keys:
            paired_struct[key]=itemized[fields_counter]
            fields_counter +=1
        
        if paired_struct['drug_name'] == "AMBIEN":
            
            output_file['AMBIEN'][0] +=1
            drugcost=int(paired_struct['drug_cost'])+output_file['AMBIEN'][1]
            output_file['AMBIEN'][1]= drugcost
                    
        elif paired_struct['drug_name'] == 'CHLORPROMAZINE':
            
            output_file['CHLORPROMAZINE'][0] +=1
            drugcost=int(paired_struct['drug_cost'])+output_file['AMBIEN'][1]
            output_file['CHLORPROMAZINE'][1]= drugcost
            
        elif paired_struct['drug_name'] == "BENZTROPINE MESYLATE":
            
            output_file['BENZTROPINE MESYLATE'][0] +=1
            drugcost=int(paired_struct['drug_cost'])+output_file['AMBIEN'][1]
            output_file['BENZTROPINE MESYLATE'][1]= drugcost
            
        else: print('hahahaha')
        
       
   
# creating output
    print('drug_name,num_prescriber,total_cost')
    for key in output_file:
        print (f'{key},{output_file[key][0]},{output_file[key][1]}')
        

       
if __name__ == '__main__': main()