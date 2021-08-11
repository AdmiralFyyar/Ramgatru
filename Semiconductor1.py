import math
class Semiconductor:
	def __init__(self, base, dictionary):
		self.__base = int(base)
		self.__dictionary = dictionary
	def Encode(self, value):
		PreferValue = value; CharIndex = []
		RankIndex = 0;  Value1 = []; Value1.append(value)
		while PreferValue > self.__base:
			PreferValue /= self.__base
			CharIndex.append(0); RankIndex += 1
			Value1.append(0)
		resoult = ""; CharIndex.append(0); index = 0
		while RankIndex > 0:
			CharIndex[index] = int(Value1[index] // math.pow(self.__base, RankIndex))
			index += 1
			Value1[index] = int(Value1[index - 1] % math.pow(self.__base, RankIndex))
			RankIndex -= 1
			if RankIndex == 0:
				CharIndex[index] = Value1[index]
		for CurrentChat in CharIndex:
			resoult += self.__dictionary[CurrentChat]
		return resoult
	def Decode(self, string):
		FixicTank = []
		for fixic in string:
			FixicTank.append(fixic)
		FixicTank.reverse(); index = 0; RankIndex = 0
		valueIndex = 0; resoult = 0
		for CurrentChat in FixicTank:
			for CurrentItem in self.__dictionary:
				if CurrentChat == CurrentItem:
					valueIndex = index
				index += 1
			resoult += valueIndex * math.pow(self.__base, RankIndex)
			RankIndex += 1; index = 0; valueIndex = 0
		return resoult
