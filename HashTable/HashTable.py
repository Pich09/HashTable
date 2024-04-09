from HashKey import Hash

hash = Hash.HashTable()

#create the hashtable by giving three elements
hash.add_to_table("Hey", 13)
hash.add_to_table("Hello", 15)
hash.add_to_table("Stree", 19)
hash.add_to_table("Monday", 54)
hash.add_to_table("Tuesday", 46)
hash.add_to_table("Dog", 8)
hash.add_to_table("Cat", 56)
hash.add_to_table("Monkey", 23)
hash.add_to_table("Thursday 4", 435)
hash.add_to_table("Why", 16)

print("HashTable: ", hash.arr)
print("Key: ", hash.get_by_key("Hey"))

#hash.delete_item("Hello")
#print("HashTable: ", hash.arr)
