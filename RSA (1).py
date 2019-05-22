"""
NAME: Marcus Barnes
FSU ID: mbb11d
Python Assignment #2 (RSA.py)
"""
#all fuctions should be inside this RSA class
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

class RSA(object):

	def __init__(self):
		self.mylist = []
		self.e = 0
		self.d = 0
		print("inside constructor")

	def inputFunc(self):
		entries= 0
		entries = input("Enter the number of messages: ")
		entries = int(entries)
		print("Enter the messages: ")
		i = 0
		for i in range(0,entries):
			line = input()
			self.mylist.append(line)

	

	def primeGen(self, minVal):
		#yield next prime numbers
		unfound = 1
		num = minVal - 1
		while unfound == 1:		##code in this while loop is taken from slides
			num += 1
			if num%2 == 0:
				continue
			for i in range(3,num):
				if num%i == 0:
					break
			else:
				#print (num, 'is a prime number')
				return num
				break

	def keyGen(self):
		minVal = int(input("Enter the minimum value for the prime numbers:"))
		p = self.primeGen(minVal + 1)
		q = self.primeGen(p + 1)
		N = p * q
		lambN = (p-1)*(q-1)
		#print("p: ", p,"q: ", q, "N: ", N, "lambN:", lambN)
		counter = 0
		temp = lambN 
		cryptlist = []
		self.e = 286049
		#while loop to look at every number less than lamb N and 
		#if that number is relatively prime
		# while temp != 1:
		# 	gcd = RSA.getGcd(temp, lambN)
		# 	if( gcd == 1):	
		# 		#print("gcd of ", temp, lambN, 1 )
		# 		self.e = temp
		# 		if(temp <= lambN /2):
		# 			self.e = temp
		# 			break
		# 	temp -= 1
		#call to encrypt using self.d and the message

		print("N is " , N)
		print("e is " , self.e)
		i = 0
		while (i < len(self.mylist)):
			c = self.encrypt(self.mylist[i], N)#pass N and get back c as encrypted response
			#edec = self.e_decorate(self.printFunc)
			#print(edec(c))
			cryptlist.append(c)
			atPhone = RSA.e_decorate(RSA.printFunc)
			print(atPhone(cryptlist[i]))
			i +=1
		self.d = self.mulinv(self.e, lambN)

		#call decrypt
		i = 0
		while (i < len(cryptlist)):
			dm = self.decrypt(cryptlist[i], N)#pass N and get back c as encrypted response
			newPhone = RSA.d_decorate(RSA.printFunc)
			print(newPhone(dm))	
			i +=1
		



	def decrypt(self, c, N):
		return pow(c, self.d, N)

	@staticmethod
	def getGcd(x, y):
	    if x > y: 
        	small = y 
	    else: 
	        small = x 
	    for i in range(1, small+1): 
	        if((x % i == 0) and (y % i == 0)): 
	            gcd = i 
	              
	    return gcd 

	#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python
	
	def encrypt(self,m ,N):
		return pow(int(m),self.e, N)


		#pass in (e,lambN)
	# x = mulinv(b) mod n, (x * b) % n == 1
	@staticmethod
	def mulinv(b, n):
	    g, x, _ = RSA.egcd(b, n)
	    if g == 1:
	    	return x % n

	# return (g, x, y) a*x + b*y = gcd(x, y)
	@staticmethod
	def egcd(a, b):
	    if a == 0:
	        return (b, 0, 1)
	    else:
	        g, x, y = RSA.egcd(b % a, a)
	        return (g, y - (b // a) * x, x)

	@classmethod
	def printFunc(this, name):
		return "message is " + str(name)
	@classmethod
	def e_decorate(this, func):
		def func_wrap(name):
			return "The encrypted " + func(name)
		return func_wrap	
	@classmethod
	def d_decorate(this, func):
		def func_wrap(name):
			return "The decrypted " + func(name)
		return func_wrap	

	

#######END OF RSA class#####

####BEGINNING OF CALLS######
if __name__ == "__main__":
	obj1 = RSA()
	obj1.inputFunc()
	obj1.keyGen()


