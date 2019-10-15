# Dictionaries
# dict

my_dictionary = {
    "key":"value",
    "key_two": 78,
}

product ={
    "id"            : 98294,
    "description"   : "A yellow submarine",
    "price"         : 9.99,
    "weight"        : 9001,
    "department"    : 'grocery',
    "aisle"         : 2,
    "shelf"         : "B"
}

print(product["price"])
location = (product["aisle"], product["shelf"])
print(location)

print(product.get("quantity")) # to find out if key exists

product['aisle'] = 4 # changes to another aisle
product["department"] = 'guy\'s grocery games'

for key in product:
    print(product[key])

# A list of values
print(product.values())
print(product.keys())

# add a key, value pair
product.update({"whatever": "the value"})
#OR, by individual
product["random"] = 56

# add empty dictionary to another
you = {}
data = [("name", "your name"), ("age", 90), ("class", "Python")]
you.update(data)
print(you)

# #other solution
# for dat in data:
#     you.update({dat[0]:dat[1]})

# #other solution still
# for k,v in data:
#     you[k] = v

#                   Collections
# Type          Mutable     Ordered     Denotation
# ------------------------------------------------
# List          Yes         Yes         [,]
# Set           Yes         No          {,}
# Tuple         No          Yes         (,)
# Dictionary    Yes         No          { KEY : VALUE, }

