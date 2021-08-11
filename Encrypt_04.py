import _thread, decimal, random, math, numpy
from multiprocessing.pool import ThreadPool
from Semiconductor1 import *

class Van:
	def Fisting(ass):
		a = ass % 2; b = ass % 3; c = ass % 5; d =ass % 7; e = ass % 13
		f = ass % 17; g = ass % 37; h = ass % 191; ret = 0.000007876
		cum = ((((a * b) / (d * c + ret)) + ((e * f) / (g * h + ret))) /
		(((a / (b + ret)) * (g / (h + ret))) - ((d / (c + ret)) * (e / (f + ret)) + ret)))
		if abs(cum) < 0.5:
			cum = cum / math.sqrt(abs((cum + cum) * cum))
		return cum
	def Cumming(FatCock, bondage):
		random.seed(FatCock); CumPuddle = 0
		semen = []; we_wee = []
		EjaculationPower = 2176384288
		while CumPuddle < 20:
			semen.append(random.randint(0,EjaculationPower)); CumPuddle += 1; we_wee.append(semen[CumPuddle])
		if bondage:
			print(we_wee)
		return semen
	def Fucking(slave, GatorLove):
		random.seed(GatorLove); semen = []
		for dick in slave:
			for cum in dick:
				semen.append(cum)
		random.shuffle(semen); return semen
	def Secutor(Cum, SemenFactor):
		length = len(Cum) / SemenFactor
		index0 = 0; index1 = 1
		kurwa0 = ""; kurwa1 = []
		length2 = 0; b = False
		while index0 < len(Cum):
				if index0 > length * index1:
						 kurwa1.append(kurwa0); index1 += 1
						 kurwa0 = ""
				kurwa0 += Cum[index0]
				index0 += 1
		kurwa1.append(kurwa0)
		return  kurwa1

class Billy:
	def FuckByGatorWithLove(Ass, SemenFactor):
		GatorAss = numpy.float64(SemenFactor)
		SemenHuffer = []
		for dick in Ass:
			GatorAss = GatorAss * Van.Fisting(GatorAss)
			CumCluster = int(abs(GatorAss))
			SemenHuffer.append(CumCluster)
		return SemenHuffer
	def SemenEmission(FaritOral, cum):
		SemenTank = []; i = 0
		CUM = Semiconductor(64, [
			"か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち"
			"つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ"
			"ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る"
			"れ", "ろ", "わ", "を", "ん", "が", "ぎ", "ぐ", "げ", "ご", "ざ", "じ"
			"ず", "ぜ", "ぞ", "だ", "ぢ", "づ", "で", "ど", "ば", "び", "ぶ", "べ"
			"ぼ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ", "ゃ", "ゅ", "ょ"])
		for semen in cum:
			SemenTank.append(CUM.Encode(ord(semen) + FaritOral[i])); i += 1
		return SemenTank

def Encrypt(text, keys, rand,  mode, threads):
	if mode == 0:
		KurwaArray = Van.Secutor(text, threads)
		print(KurwaArray)
		BrokenSlaves = []; Kurwawozka = []; q0 = 0
		slaves = []; AvailableSlaves = threads;
		while AvailableSlaves > 0:
			slaves.append(ThreadPool(processes=1))
			AvailableSlaves -= 1
		for dick in slaves:
			BrokenSlaves.append(dick.apply_async(Billy.FuckByGatorWithLove,(KurwaArray[q0], keys[q0]))); q0 += 1
		for LapisMother in BrokenSlaves:
			Kurwawozka.append(LapisMother.get())
		print(Kurwawozka)
		MainKurwa = Billy.SemenEmission(Van.Fucking(Kurwawozka, rand), text)
		print(MainKurwa)
