#===========================
#     round off function
#===========================
print(round(1.52))
print(round(1.56,1))
print(round(1.563255,3))
#===========================
#     sum
#===========================
print(sum([1,2,3,4,5]))
######################
ex = [1,2,3,4,5,6,7,8,9,10]
print(sum(ex))
print(max(ex))
print(min(ex))

#=====================
#           absolute value/function
#=====================
print(abs(-1))
print(abs(1))

#========================
#    enumarate function
#========================
ex = [3,7,5]
print(list(enumerate(ex)))

#=========================
#    zip function
#=========================
list1 = [2,3,4,5]
list2 = ['a','b','c','d']
print(list(zip(list1,list2)))

#=========================
#    find index function
#=========================
ex = [3,7,5]
print(ex.index(7))
####################
my_list = [10,20,30,40,50]
#print(my_list.index(30))
print("Index of element 30 :", my_list.index(30))
#################
my_string = "hello world"
print("index of 'world':", my_string.find('world'))

#==========================
#     get function
#==========================
my_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print("name :",my_dict.get('name'))
print("place :",my_dict.get('place'))