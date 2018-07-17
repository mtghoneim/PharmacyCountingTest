# The first part of my program parses the input and organizes it in manageable data structure for further processing.
# This format is a list of entries where each entry is a dictionary of all key fields and their values.
# Based on the desired output, it is apparent that the unique field should be the drug name. This program organizes the output structure in dictionary format.
# Each key is a unique drug, and each value is composed of a list of integer and a double/float. Integer for number of prescribers and float for total cost.


def main():
    input_file = open('./input/itcont.txt') #opens the input file
    
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
        paired_struct={}
        itemized=line.strip().split(',')
        
        #print(itemized)
        fields_counter = 0
        
        for key in field_keys:
            paired_struct[key]=itemized[fields_counter]
            fields_counter +=1
        #print (id(paired_struct))
        #print(paired_struct)
        parsed_file.append(paired_struct)
    outputlist=output(parsed_file,total_data_lines)
    sortedlist=sortlist (outputlist, len(outputlist))
    proper_print (sortedlist, len(sortedlist))
#####################################################################################
#this module is for preparing a list of the requested file
def output(list,totalLines):
    summary={'drug_name':'','num_prescriber': 0,'total_cost': 0}
    summaryList=[{}]
    i=0
    summaryList[i]['drug_name']=list[i]['drug_name']
    summaryList[i]['num_prescriber']= 1
    summaryList[i]['total_cost']=list[i]['drug_cost']
    values=[list[i]['drug_name']]
    #print(values)
    i=1
    while i< totalLines:
        summary={}
        if list[i]['drug_name'] in values:
            summaryList[findindex(summaryList,'drug_name',list[i]['drug_name'])]['num_prescriber']+=1
            summaryList[findindex(summaryList,'drug_name',list[i]['drug_name'])]['total_cost']=int(summaryList[findindex(summaryList,'drug_name',list[i]['drug_name'])]['total_cost'])+int(list[i]['drug_cost'])
        else:
            summary['drug_name']=list[i]['drug_name']
            summary['num_prescriber']=1
            summary['total_cost']=list[i]['drug_cost']
            summaryList.append(summary)
            values.append(list[i]['drug_name'])
        i+=1
    return summaryList

def findindex (list,key,value):
    i=0
    index=0
    while i < len(list):
        if list[i][key] == value:
            index=i
        i+=1
    return index


    ################################################################################################        
#This module is for sorting the summary list according to the test specs (by total cost....and name in case of a tie)
def sortlist(list,totalLines): # this function takes the summary list and total number of lines
    i=0
    j=0
    while j <totalLines:
        while i <totalLines-1:
            if int(list[i]['total_cost']) <= int(list[i+1]['total_cost']):
                if int(list[i]['total_cost']) == int(list[i+1]['total_cost']):
                    if str(list[i]['drug_name']) > str(list[i+1]['drug_name']):
                        list[i], list[i+1] = list[i+1], list[i]                                  
                else: list[i], list[i+1] = list[i+1], list[i]
            i+=1
        j+=1
        i=0
    return list
########################################################
#This module prints the output file as required
def proper_print (list,totalLines):
    f=open('./output/top_cost_drug.txt','w')
    f.write('drug_name,num_prescriber,total_cost\n')
    i=0
    while i < totalLines:
        f.write("{},{},{}\n".format(list[i]['drug_name'],list[i]['num_prescriber'],list[i]['total_cost']))
        i+=1
       
if __name__ == '__main__': main()
