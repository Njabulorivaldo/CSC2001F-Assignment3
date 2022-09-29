import os

#found =1 if the best combinations are found and equals 0 while not found. 
found = 0 


def generate_files():

    count = 0
    file_no = 1


    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        for f in range(5):
                            for g in range(5):
                                for h in range(5):
                                    for i in range(5):
                                        file = open("data/Combinations_"+str(file_no)+".txt", "a")
                                        file.write(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)+" "+str(i)+"\n")
                                        count += 1
                                    
                                    
                                        file.close()    
                                        if count == 200000:
                                            file_no +=1
                                            count = 0
 

def Checking():
	
	#Interchange the file number by changing it to the file no you want to check. or else use the for loop and comment out the other
	#part for testing
	file_no = 1
	
	
	#for file_no in range(11):
		#file = open("data/Combinations_"+str(file_no+1)+".txt", "r")
		#with open("data/Combinations_"+str(file_no)+".txt", "r") as f:
		
			#lines = f.readlines()
			#for i in lines:
				#arr = []
				#a = i.split(" ")
				#print(a)
				#for j in a:
					#arr.append(j)
			
				#arr[-1] = arr[-1][0] #Cutting off the new line tag on the last element
				#if found == 1:
					#break
				#else:
					#os.system(f"java TestHashTable {0} {arr[0]} {arr[1]} {arr[2]} {arr[3]} {arr[4]} {arr[5]} {arr[6]} {arr[7]} {arr[8]} | awk \'NR % 2 == 0\' >results.txt")
					#checkCollisions(arr)
		#if found == 1:
			#break
	
		#file = open("data/Combinations_"+str(file_no)+".txt", "r")
	with open("data/Combinations_"+str(file_no)+".txt", "r") as f:
		
		lines = f.readlines()
		for i in lines:
			arr = []
			a = i.split(" ")
			#print(a)
			for j in a:
				arr.append(j)
			
			arr[-1] = arr[-1][0] #Cutting off the new line tag on the last element
			if found == 1:
				break
			else:
				os.system(f"java TestHashTable {0} {arr[0]} {arr[1]} {arr[2]} {arr[3]} {arr[4]} {arr[5]} {arr[6]} {arr[7]} {arr[8]} | awk \'NR % 2 == 0\' >results.txt")
				checkCollisions(arr)
						


def checkCollisions(arr):
	
	with open("results.txt", "r") as results:
		line = results.readline()
		res = line.split(" ")
		collisions = res[-1][:-1]
		print(arr, "Coll: ", collisions)
		print(collisions)
		
		#if 
		if collisions == "Met!":
			global found
			found = 1
			with open("Final_weights.txt", "w") as f:
				f.write("Array: "+str(arr))
				f.close() 
		print(found)
		
def main():
	generate_files()
	Checking()

if __name__ == "__main__":
	try:
		main()
	except:
		pass


