from csv import reader # this imports the csv module with the reader method

def main(): # this is the main program
   
    input_file = open('./input/itcont.txt') # opens the input file
    output_content=[] # this initializes the output_content list
    drug_names=[] # this would store the list of all drug names processed so far
    Top_line=input_file.readline().strip().split(',') # stores the first line in input file for reference
    
    for line in reader(input_file): # this loops as long as there are new data lines in input file
        current_drug_name=line[3] # this holds the drug name of the data line currently being processed
       
        if current_drug_name in drug_names: # checks if the drug name is already processed
            found_index=drug_names.index(current_drug_name) # finds the index of the drug name which corresponds to list index in output content
            output_content[found_index]['num_prescriber']+=1 # updates number of subscribers by adding one new subscriber
            output_content[found_index]['total_cost']+=float(line[4]) # updates the total cost by adding the new cost
        
        else: # if the drug name has not been processed before
            output_content.append({'drug_name':current_drug_name,'num_prescriber':1,'total_cost':float(line[4])}) # adds new output line for the new drug entry
            drug_names.append(current_drug_name) # adds the drug name to the list of processed drugs
     
    input_file.close() # closes the input file
            
    sorted_output=sorted(output_content, key= lambda value: (-value['total_cost'],value['drug_name'])) # sorts the output content by total cost (high to low) as primary key and drug name (alphabetically) as secondary key
    
    output_file= open ('./output/top_cost_drug.txt', 'w') # opens output file
   
    output_file.write("drug_name,num_prescriber,total_cost\n") # writes first line in output file (key fields)
   
    for line in sorted_output: # moves sorted data from sorted contents to output file
        output_file.write("{},{},{}\n".format(line['drug_name'],line['num_prescriber'],line['total_cost']))

    output_file.close() # closes output file to free up resources

if __name__ == '__main__': main() # end of code
