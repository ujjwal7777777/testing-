#                   P  Y  T  H  O  N
#POSTIVE INDEXING   0  1  2  3  4  5
#NEGATIVE INDEXING -6 -5 -4 -3 -2 -1

my_string = "hello world"
print(my_string[0])
print(my_string[-1])
############
my_tuple =(1,2,3,4,5)
print(my_tuple[0])
print(my_tuple[-1])
#################
#set is not suitable indexing
# dict we can indexing
my_dict ={'name':'thor','place':'asgard','weapon':'hammer',1:2,3:'power','alibies':['ironman','caption america'],}
print(my_dict['name'])
#################
marvel_words =['avenger','x-men','spider-man','ironman','hulk','black widow','captain america','wolverline','doctor strange','namor']
team1 = [marvel_words[0],marvel_words[2],marvel_words[4],marvel_words[6],marvel_words[8]]
team2 = [marvel_words[1],marvel_words[3],marvel_words[5],marvel_words[7],marvel_words[9]]
print(team1)
print(team2)

#====================================
#    slicing
#====================================
my_string = "hello, world"
print(my_string[0:5])
print(my_string[7:])
print(my_string[::2])
print(my_string[::-1])
print(my_string[::-2])
print(my_string[-1:-5:-1])
######################
#slicing doesn't support on dict becoz of no indexing
my_dict ={'a':1, 'b':2, 'c':3}
print(my_dict['a'])
print(my_dict['b'])