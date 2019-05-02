	
import hashlib

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

def getHash(my_str):

	hash_object = hashlib.sha256(my_str.encode())
	#print("Hash produced: " , hash_object.hexdigest())
	return hash_object.hexdigest()

def matchHash(my_str , my_hash):
	if getHash(my_str) == my_hash:
		return True

	return False


