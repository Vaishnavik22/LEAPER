import json
import os
import sys
from collections import OrderedDict

file_obj = open("blocks.txt","w");
dict_data = {}
rootdir = "/home/vinitha/Leaper/Data/Level2Vaish.txt";

with open(rootdir) as f:
    content = f.readlines()
content = [x.strip() for x in content]

order_blocks = {};
for line in content:
    list_line = line.split(" ");
    timestamp = list_line[0]
    if timestamp in dict_data:
      
        for value in dict_data[timestamp]:
            found = 0;
            #if it is a child

           
            if(list_line[1] == value[4]):
                index = dict_data[timestamp].index(value);
                dict_data[timestamp].insert(index+1, list(list_line[1:]));
                #order_blocks[timestamp].append(list_line[2]);
                order_blocks[timestamp].append(list_line[2]);
                found = 1;
                break;
            elif(list_line[1] in value[2]):
                value.append(list(list_line[1:]))
                order_blocks[timestamp].append(list_line[2]);
                found = 1;
                break;
            else:
                for val in value:
                    if(type(val)==type([])):
                        if(list_line[1] in val[2]):
                            value.append(list(list_line[1:]));
                            order_blocks[timestamp].append(list_line[2]);
                            found = 1;
                            break;
                    if(found == 1):
                        break;

        if(found == 0):
            dict_data[timestamp].append(list(list_line[1:]));
            order_blocks[timestamp].append(list_line[2]);
    else:	 
        dict_data[timestamp] = [];
        order_blocks[timestamp] = [];
        dict_data[timestamp].append(list(list_line[1:]));
        order_blocks[timestamp].append(list_line[2]);


dict_data = OrderedDict(sorted(dict_data.items()));
order_blocks = OrderedDict(sorted(order_blocks.items()));


for key,values in dict_data.items():
	time = "Timestamp: " + str(key) + "\n";
	file_obj.write(time);
	blocks = [];
	for value in values:
		if(len(value) == 8):
			
			blocks.append(value[1:4]);
			
		else:
			blocks.append(value[1:4]);
			for i in range(8,len(value)):
				blocks.append(value[i][1:4]);
	file_obj.write(str(blocks));
	file_obj.write("\n\n\n");




'''
for key,values in order_blocks.items():
    time = "Timestamp: " + str(key) + "\n";
    file_obj.write(time);   
    for value in values:
        file_obj.write(str(value))  ;
        file_obj.write("\n");
    file_obj.write("\n\n\n");
''' 




	

