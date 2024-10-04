
my_list = ['eggs', 'ham']

item = ('milk')

def add_to_list(item, my_list):
     my_list.append(item)
     return my_list

my_list = add_to_list(item, my_list)

print(my_list)