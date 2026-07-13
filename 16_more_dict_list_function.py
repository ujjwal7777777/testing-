#******more dict function
my_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america']}
my_list = list(my_dict.keys())
print(my_list)
##############
my_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america']}
my_list = list(my_dict.values())
print(my_list)
##################
my_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america']}
my_list = list(my_dict.items())
print(my_list)

#========================
#     sort the list
#========================
my_list = [30,10,20,50,40]
my_list.sort()
print(my_list)
########################
my_list = [30,10,20,50,40]
sorted_list = sorted(my_list)
print("original list :", my_list)
print("sorted list :", sorted_list)