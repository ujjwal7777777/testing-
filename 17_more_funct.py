#===========================
#    append function
#===========================
my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)

#===========================
#   update function
#===========================
my_dict ={'name':'thor','age':'13'}
my_dict.update({'age':'14'})
print(my_dict)

#===========================
#     insert function
#===========================
ex = [1,2,3,4,5]
ex.insert(2,6)
print(ex)

#===========================
#     string join function
#===========================
string ="alma better"
print("original string:",string)
print("string afte rupper case:", string.upper())
print("string after lower case:", string.lower())
print("string after title case:", string.title())
print("string after split:", string.split("l"))
print("string after join:", string.join("123"))
new_string = "-".join(string)
print("joined string:", new_string)