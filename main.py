import pandas as pd
import itertools

# DATA being used: 5000-out1.csv 
# goods.id    receipt.id 
# 1, 4, 5, 6, 10
# 2, 1, 12, 19, 46, 47
# 3, 16, 32
# 4, 18, 24, 35


# Following the Apirori Algorithm in : https://www.geeksforgeeks.org/apriori-algorithm/

from csv import reader
# open file in read mode



def main(): 
    data = unpack_data_set("SHORT_receipts_&_goods.csv")
    goods = unpack_goods("SHORT_goods.csv")
    good_ids = goods.keys()

    full_implementation(good_ids, data, 2)
    
def unpack_data_set(filename):
    original_data = []
    with open(filename, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            int_ = []
            for item in row: 
                int_.append(int(item))
            
            original_data.append(int_)

    print(original_data)
    return original_data

def unpack_goods(filename):
    goods = {}
    with open(filename, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        i = 0 
        for row in csv_reader:
            if i > 1: 
            # row variable is a list that represents a row in csv
                goods[int(row[0])] = row[1]
            i+=1

    return goods 

def list_of_pairs_helper(stuff, length): 
    pair_ret = []
    for i in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, i):
            if len(subset) == length or length == 0:
                pair_ret.append(list(subset))
    return pair_ret


def find_support_count(data, t):  # t = tuple to find support count of 
    support_count = 0
  
    for receipt_list in data:  
        receipt_set = set(receipt_list[1:])
        # print(set(receipt_list[1:]))
        # print(set(t))
        # print(set(t).issubset(receipt_set))
        if set(t).issubset(receipt_set): 
            support_count += 1

    return support_count
    

def delete_instance_from_tree(list_of_sets, delete): 
    overall_list = list_of_sets.copy()
    for i in list_of_sets:
        if set(delete).issubset(i):
           overall_list.remove(i)
    return overall_list

def find_skylines(overall_set):
    final = overall_set.copy()
    for i in overall_set:
        for comp in final:
            if set(i).issubset(comp) and i != comp:
                final.remove(i)
                break
    return final 

def full_implementation(good_ids, data, minSup): 

    list_of_sets = list_of_pairs_helper(good_ids, 0) # edit this so its all the sizes 
    overall_set = list_of_sets.copy()

    for set_ in list_of_sets:   # organized in order of size smallest to large (2,3)  (3,4,2) 
        if set_ in overall_set:
            print("set: ", set_)
            x = find_support_count(data, set_)
            #print("\nfor ", set_)
            if x < minSup: 
                overall_set = delete_instance_from_tree(overall_set, set_)

        print(overall_set)

    final = find_skylines(overall_set[1:])
    print("Final Skyline  ", final)


    # delete possible set values 









# def remove_less_than_support_counts(data, min_support): 
#     for key, value in list(data.items()):
#         if value <= min_support: 
#             del data[key]

#     print(data)



# def make_pairs(support_counts, data): 

#     # data 
#     # list of lists of all data 
#     #  [[ 1, 4, 5, 6, 10] 
#     #  [2, 1, 12, 19, 46, 47]
#     #  [3, 16, 32]
#     #  [4, 18, 24, 35]] 

#     list_of_item_ids = support_counts.keys() # 1 2 3 4 
#     print("item_ids ", list(list_of_item_ids))
#     list_of_pairs = list_of_pairs_helper(list(list_of_item_ids), 2)#  (1,2)  (1,3) (3,4)
#     print("list of pairs ", list_of_pairs)
#     dict_of_pairs = {}

# # JOSH LOOK AT MY TEXT I THINK IT WORKS NOW 
#     # dict of pairs:
#     #    pair    support count  
#     #  { (1,2) :  4 }

#     for item_lists in data: 
#         for pair_set in list_of_pairs: #1,4
#             if check_if_tuple_in_list(pair_set, item_lists):  #1, 4, 5, 6, 10
#                 if pair_set in dict_of_pairs: 
#                     dict_of_pairs[pair_set] += 1
#                 else: 
#                     dict_of_pairs[pair_set] = 1

#     print(dict_of_pairs)







# def full_implementation(): 

#     list_of_sets = list_of_pairs_helper() # edit this so its all the sizes 

#     for set in list_of_sets:   # organized in order of size smallest to large (2,3)  (3,4,2) 
#         if support < minSup 
#             helper()        # (1,2)  sup = 3       



#   support counts    A   B     C    D    E  
                    # deletions rest of tree 

#  support counts     AB    BC     DE    







# def check_if_tuple_in_list(tuple_, list_): 
#     # returns true if tuple is in list (1-end)
#     list_minus_first = list_[1:]
#     print("\n")
#     print("list_minus_first ", list_minus_first)
#     print("tuple check", (tuple_[0] in list_minus_first) and (tuple_[1] in list_minus_first))
#     print("tuple & list ", tuple_, list_minus_first )
#     return (tuple_[0] in list_minus_first) and (tuple_[1] in list_minus_first)


       


                
            
#[ 1, 4, 5, 6, 10
# 2, 1, 12, 19, 46, 47
# 3, 16, 32
# 4, 18, 24, 35]





    











# step one : Frequent items 
# def apriori(T, I, min_support): 
#     """
#     def: finds the frequent items sets 
#     PARAM: 
#         min_support: (float) between 0.0-0.999
#         T: market basket data set 
#         I: List of items 

#     """
#     pass 


# def canidate_gen(): 
#     """
#     helper function frequent items 
#     """
#     pass 

# # step two 
# def association_rules(): 
#     pass 


if __name__ == "__main__": 
    main()




# receipt id      goods 
# 2,          1, 5, 7, 4, 10, 1 

#             1   5   7   4   10  1

#              1 5     7 4     10 1 


#              1 5 7        4 10 1 

#                 1, 5, 7, 4, 10, 1 



# 1, 4, 5, 6, 10
# 2, 1, 5, 7, 4, 10, 1 
# 3, 16, 10
# 6, 6, 5


# minSup 3 

# for all of the cases of receipts 
#       1 and 5 show up together = 1 

# go through entire dict 
#      if 1 and 5 in dict delete 






# support number 
#           5 2 3 4  6 1 2 3 4          
# item:     1  2 3 4 5 6 7 8 
# bucket    0 1 0 1 


#           1 2     3 4   5 6   78 
           

#           1 2 3 4        5 6 7 8 


#           1234 

# support count 


