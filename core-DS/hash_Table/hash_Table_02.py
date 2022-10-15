# In python hashmaps are implemented thought dictinaries . So you can directly use python dictionaries for your
# hashmaps opoerations, if you wanna create your own hashmaps with custom features then following code should do the job
# Added collision handeling



class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range(self.MAX)]

    
    # A custom hash function to generate different key for different characters
    def get_hash(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX


    def __setitem__(self,key,value):
        temp_hash = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[temp_hash]):
            # IF the key already existed 
            if len(element)==2 and element[0]==key:
                self.arr[temp_hash][idx] = (key,value)
                found = True
                break
        # If it did not existed 
        if not found:
            self.arr[temp_hash].append((key,value))

    def __getitem__(self,key):
        temp_hash  = self.get_hash(key)
        for element in self.arr[temp_hash]:
            if element[0] == key:
                return element[1]
        
        
    
    def __str__(self):
        vals = ""
        for elem in self.arr:
            if elem != None:
                vals = vals +   f"{elem}" 
        return vals

    def __len__(self):
        count = 0
        for i in self.arr:
            if i != None:
                count +=1
        return count

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]



if __name__ == "__main__":
    table = HashTable( )


    table["Suman"] = "Pokhrel 1"
    table["Suman"] = "Pokhrel 2"
    table["Binod"] = "Pokhrel 3"

    # print(table.arr)
    print(len(table))
    print(table["Suman"])
    del table["Suman"]
    print(table["Suman"])





