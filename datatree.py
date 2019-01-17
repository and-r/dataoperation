#coding: utf-8
def Showdata(Data,Depth):
	if type(Data) is not list and type(Data) is not tuple:	#then Data can be shown in a single line
		print('|'+Data)
	else:
		for i in range(0,len(Data)):
			# if Data[i] is list or tuple, either one bigger than 1-element
			if type(Data[i]) is list or type(Data[i]) is tuple:
				print(' '*Depth*3+'-'*3)
				Showdata(Data[i],Depth+1)
				print(' '*Depth*3+'-'*3)
			else:
				print("{}|{}".format(" "*Depth*3,str(Data[i])))

			
#Data=['a',8,12,16,20,'bcde',(0.15,0.30,0.45,["efg","hij","xyz"],0.6,0.75),24,28,32]

