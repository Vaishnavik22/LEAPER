import json
import os
import sys
import re
import ast
from collections import OrderedDict

file_obj = open("blocks.txt","r");
file_obj1 = open("blocks_output.txt","w");


prevStr = "";
newStr = "";
start = 0;
count = 0;
for line in file_obj.readlines():
	
	


	if(re.search("Timestamp:",line)):
		if(count == 0):
			startTime = (line.split("Timestamp: ")[1]).split("\n")[0];
			count = 1;
			#print(startTime);
		if(newStr != "" and start == 0):
			file_obj1.write(newStr);
			file_obj1.write("\n")
			start = 1;
		else:
		#file_obj1.write(line);
			if(prevStr != newStr):
				file_obj1.write(newStr);
				file_obj1.write("\n");
			else:
				file_obj1.write("\n");
		
		prevStr = newStr;
		newStr = "";
		file_obj1.write(line);
		percentageTime = str((int((line.split("Timestamp: ")[1]).split("\n")[0])-int(startTime)) / 1000 ) + "th Second\n";
		file_obj1.write(percentageTime);

	elif(line == "\n"):
		pass

	else:
		lines = ast.literal_eval(line);
		for line in lines:

			if("event_whenbackdropswitchesto" in line):
				val = {};
				#print("when backdrop switches to []");
				#file_obj1.write("when backdrop switches to []\n");
				val = line[2];
				val = eval(val);
				value = val["BACKDROP"]["value"];

				newStr = newStr + "when backdrop switches to [" +  value + "]\n";


			if("motion_gotoxy" in line):
				valX = {};
				valY = {};
				index = lines.index(line);
				X = index + 1;
				Y = index + 2;
				valX = lines[X][2];
				valX = eval(valX);
				valueX = valX["NUM"]["value"];

				valY = lines[Y][2];
				valY = eval(valY);
				valueY = valY["NUM"]["value"];


				#print("go to x() y()");
				#file_obj1.write("go to x() y()\n");
				newStr = newStr + "go to x(" + str(valueX) + ") y(" + str(valueY) +")\n";

			if("math_number"in line):
				pass

			if("event_whenflagclicked"in line):
				#print("when green flag clicked");
				#file_obj1.write("when green flag clicked\n");
				newStr = newStr + "when green flag clicked\n";
			

			if("looks_show"in line):
				#print("show");
				#file_obj1.write("show\n");
				newStr = newStr + "show\n";

			if("motion_pointindirection"in line):
				val  = {};
				index = lines.index(line);
				valueAngle = lines[index+1][2];
				valueAngle = eval(valueAngle);
				angle = valueAngle["NUM"]["value"];
				#print("point in direction ()");
				#file_obj1.write("point in direction ()\n");
				newStr = newStr + "point in direction ("+ str(angle)+")\n";
				

			if("control_if"in line):
				val  = {};
				index = lines.index(line);
				valuetouching = lines[index+2][2];
				valuetouching = eval(valuetouching);
				touching = valuetouching["TOUCHINGOBJECTMENU"]["value"];
				#print("if <> then");
				#file_obj1.write("if <> then\n");
				newStr = newStr + "if < touching ["+ touching +"]> then\n";

			if("control_forever"in line):
				#print("forever");
				#file_obj1.write("forever\n");
				newStr = newStr + "forever\n";

			if("sensing_keypressed"in line):
				#print("key [] pressed?");
				#file_obj1.write("key [] pressed?\n");
				newStr = newStr + "key [] pressed?\n";
			"""
			if("sensing_touchingobject"in line):
				#print("touching []");
				#file_obj1.write("touching []\n");
				newStr = newStr + "touching []\n";

			if("sensing_touchingobjectmenu" in line):
				#print("touching_menu []");
				#file_obj1.write("touching_menu []\n");
				newStr = newStr + "touching_menu []\n";
			"""
			if("motion_movesteps"in line):
				val  = {};
				index = lines.index(line);
				valueSteps = lines[index+1][2];
				valueSteps = eval(valueSteps);
				steps = valueSteps["NUM"]["value"];
				#print("move () steps");
				#file_obj1.write("move () steps\n");
				newStr = newStr + "move ("+ str(steps) +") steps\n";

			if("looks_switchbackdropto"in line):
				val = {};
				index = lines.index(line);
				valuebackdrop = lines[index+1][2];
				valuebackdrop = eval(valuebackdrop);
				backdrop = valuebackdrop["BACKDROP"]["value"];

				#print("switch backdrop to []");
				#file_obj1.write("switch backdrop to []\n");
				newStr = newStr + "switch backdrop to ["+backdrop+"]\n";

'''
	if(line == "\n"):
		print("\n");
		file_obj1.write("\n");
'''