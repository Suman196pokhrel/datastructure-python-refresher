# In python hashmaps are implemented thought dictinaries . So you can directly use python dictionaries for your
# hashmaps opoerations, if you wanna create your own hashmaps with custom features then following code should do the job



class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]

    
    # A custom hash function to generate different key for different characters
    def get_hash(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX


    def __setitem__(self,key,value):
        temp_hash = self.get_hash(key)
        self.arr[temp_hash] = value

    def __getitem__(self,key):
        temp_hash  = self.get_hash(key)
        return self.arr[temp_hash]
    
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
        self.arr[h] = None



if __name__ == "__main__":
    table = HashTable( )


    table["Suman"] = "Pokhrel 1"
    table["Sumina"] = "Pokhrel 2"
    table["Binod"] = "Pokhrel 3"

    # print(table.arr)
    print(len(table))
    print(table)





