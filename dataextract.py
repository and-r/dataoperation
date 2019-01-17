#coding: utf-8
def Extract(Data,Arg,Mode,Cache='-null-'):
	if len(Arg) > 1 and (type(Data[Arg[0]]) is list or type(Data[Arg[0]]) is tuple):
		#going deeper
		return Extract(Data[Arg[0]],Arg[1:],Mode,Cache)
	else:
		#action on current level
		if Mode == 'r':
			return Data.pop(Arg[0])	#data removal
		elif Mode == 'i':
			if len(Data) <= Arg[0]:
				for i in range(0,Arg[0]-len(Data)):
					Data.append('-null-')
				Data.append(Cache)
			else:
				Data.insert(Arg[0],Cache)
			return Data[Arg[0]]
		else:
			return Data[Arg[0]]


