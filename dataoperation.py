#coding: utf-8
import sys
import pickle
import datatree
import dataextract
Data=['uno','due','tre',['x','y','z'],'charlie','delta']
Cache=[]
def Showhelp():
	Helptext='''
1.	Pattern of basic commands: 
	<keysign> [<index0> <index1> <index..>]
	Available keysigns: d-display, i-insert from cache, r-remove.
2.	Remaining commands:
	- Copy to cache: c <content>
		content separated by '##' will be arranged in a list
	- Dump datatree to a file: d <filename>
	- Load to datatree from a file: l <filename>
'''
	print(Helptext)
def FileSave(Data,Wejscie):
	if len(Wejscie)==1:
		print("\nYou didn't give the filename")
	else:
		print("datatree to be saved:")
		datatree.Showdata(Data,0)
		File=open(Wejscie[1],'wb')	#write in binary mode
		pickle.dump(Data,File)
		print("datatree has been saved to {}".format(Wejscie[1]))
def FileLoad(data,wejscie):
	if len(wejscie)==1:
		print("\nYou didn't give the filename")
	else:
		try:
			File=open(wejscie[1],'rb')	#read in binary mode
			data[:]=pickle.load(File)
			#data[:]=[]
			#data[:]=datalocal[:]
		except FileNotFoundError:
			print('File {} has not been found'.format(Wejscie[1]))
			return None
		print("datatree has been loaded from {}".format(Wejscie[1]))
print('\n----------------------------DataOperation----------------------------------\n')
while 1:
	Wejscietekst=input("\nType command, h-help, q-quit: ")
	Wejscie=Wejscietekst.split()
	if Wejscie[0] == 'q': break
	elif Wejscie[0] == 'h':  #help
		Showhelp()
	elif Wejscie[0] == 'c':  #assigning to cache
		if len(Wejscie)==1:
			print("\nYou didn't give content")
		else:
			Gapsign=' '
			InText = Gapsign.join(Wejscie[1:])
			if InText.find('##')>=1:		#there are separator signs, we need to make a list
				InList=InText.split('##')
				Cache=InList
			else:
				Cache=InText
	elif Wejscie[0] == 's':   #save to file
		FileSave(Data,Wejscie)
	elif Wejscie[0] == 'l':   #load from file
		FileLoad(Data,Wejscie)
	else:
		if len(Wejscie) == 1:    #only command sign - whole tree
			if Wejscie[0] == 'd':		#display
				print('')
				datatree.Showdata(Data,0)
			elif Wejscie[0] == 'r':		#remove
				Data=[]
			elif Wejscie[0] == 'i':		#insert, no index given so on the end of Data
				Data.append(Cache)
		else:		# command sign and at least one index
			try:
				Arg = [int(elem) for elem in Wejscie[1:]]  #all items of list of indexes
				Dat=dataextract.Extract(Data,Arg,Wejscie[0],Cache)
			except IndexError:
				print("\nError: wrong index")
				continue
			print('')
			if Wejscie[0] == 'r':
				print('Item has been removed:')
			elif Wejscie[0] == 'i':
				print('Item has been added:')
			datatree.Showdata(Dat,0)
		
