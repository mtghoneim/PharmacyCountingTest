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
        print(paired_struct)
        parsed_file.append(paired_struct)
        print (parsed_file)
        

       
if __name__ == '__main__': main()