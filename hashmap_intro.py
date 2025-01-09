#hashmap is similar to the dictionary .
# dictionary works based on the hasmap technique in the backend
# storing username and password:hashing and storing..
# hashing:instead of that value we using the another one which maps to it..
# but for the password:encrypt and decrypt is used.

# print(hash("Name"))##each time running genearates dif value ineach session.
#
# we are accesing dictionary by using the index..
# in the backend ,what happens is:
#
# i want to store Name:Mukil
#
# what will happens is,
# for the Name ,if we consider its hash value is 100.we are having the 4 places in the list.
#     100%4=0##4 is nothing but the size of list.
# thn this mukil will go and occupy in the 0th index.
# Age:21
# Hash value of Age is 17 for ex.
#     17%4=1(remainder.)
#     storing the 21 in 1st index of list
#
#     hashing is nothing but the value of addition..
#     in case if both have the same value.
#     we are handling this as a collision and separately hanlding.

# class HashMap:
#     def __init__(self):
#         self.size=10##initializing the size of the list as 10 for storing value
#         self.hashList=[None]*self.size##here we are restricting the list to allow only 10 values.
#
# dictionary= HashMap()
# print(dictionary.hashList)##it will print the list woth 10 values of None.

class HashMap:
    def __init__(self,size=10):
        self.size=size##initializing the size of the list as 10 for storing value
        self.hashList=[None]*self.size##here we are restricting the list to allow only 10 values.

    def GetIndex(self,key):
        return hash(key)%self.size
    # def Add(self,key,value):#for adding key and value is needed..Also needed the hash for key
    #     index=self.GetIndex(key)
    #     # print(index)
    #     if self.hashList[index] is None:#if already list is not there creating a new one else appending to the list already present
    #         self.hashList[index]=[[key,value]]###handling the case of collision
    #     else:
    #         self.hashList[index].append([key,value])
##or to achieve the dictionary format ,we can use the __setitem__(builtin) instead of add
    def __setitem__(self, key, value):#for adding key and value is needed..Also needed the hash for key
        index=self.GetIndex(key)
        # print(index)
        if self.hashList[index] is None:#if already list is not there creating a new one else appending to the list already present
            self.hashList[index]=[[key,value]]###handling the case of collision
        else:
            self.hashList[index].append([key,value])

    def get(self,key):
        index = self.GetIndex(key)
        if self.hashList[index] is not None:
            sublist=self.hashList[index]

            print(sublist)


dictionary= HashMap()
print(dictionary.hashList)
# dictionary.Add("Name","Mukil")
# dictionary.Add("Age",25)
dictionary["Name"]="mukil"
dictionary["Age"]=25
dictionary.get("Name")
print(dictionary.hashList)
# print(dictionary.hashList)##it will print the list woth 10 values of None.


#Regarding the del operation...need to be included and quick recall to be done today.