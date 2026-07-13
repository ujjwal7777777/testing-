#dictionary
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],'abc':{1:2,3:4}}
print(marvel_dict)
#############
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(marvel_dict['place'])
############
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(type(marvel_dict))
###############
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(marvel_dict['alibies'])
print(marvel_dict['alibies'][0])
###############
#values in dict
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(marvel_dict.values())
################
#item in dict
marvel_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(marvel_dict.items()) 
################
#dictionary is mutable
customer ={'id':1234,'name':'ujjwal deshwal','email':'ujjwal@5625472'}
customer['email'] = 'ujjwal@deshwal762316418'
customer ['phone'] = '65361876398'
del customer['id']
print(customer)
################
