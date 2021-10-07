import pandas as pd
import itertools

# DATA being used: 5000-out1.csv 
# goods.id    receipt.id 
# 1, 4, 5, 6, 10
# 2, 1, 12, 19, 46, 47
# 3, 16, 32
# 4, 18, 24, 35

# "5000-out1.csv"
# "goods.csv"


# Following the Apirori Algorithm in : https://www.geeksforgeeks.org/apriori-algorithm/

from csv import reader
# open file in read mode



def main(): 
    data = unpack_data_set("5000-out1.csv")
    goods = unpack_goods("goods.csv")
    good_ids = goods.keys()

    full_implementation(good_ids, data, 8)
    
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

    # print(original_data)
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

def candidate_generator(stuff, length): 
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
        # if(t == (41, 47)):
        #     print(data)
        #     break
        #     print("rec_set ", receipt_set)
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

# def full_implementation(good_ids, data, minSup): 
#     list_of_sets = candidate_generator(good_ids, 0) # edit this so its all the sizes 
#     overall_set = list_of_sets.copy()

#     for set_ in list_of_sets:   # organized in order of size smallest to large (2,3)  (3,4,2) 
#         if set_ in overall_set:
#             if find_support_count(data, set_) <= minSup: 
#                 overall_set = delete_instance_from_tree(overall_set, set_)
            
#         print(overall_set)
#     final = find_skylines(overall_set[1:])
#     print("Final Skyline  ", final)


    # delete possible set values 


def full_implementation(good_ids, data, minSup): 
    ones = list(good_ids)
    final_list = []
    for id in ones: # pandas df.table - will give counts on df
        sup = find_support_count(data, [id])
        if sup <= minSup: 
            ones.remove(id)
    
    list_of_sets  = find_2s(ones)

    i = 0
    x = len(ones) - 2
    y = 0
    while x > i: #what condition do we do it on? 

        # pandas df.table - will give counts on df of lists of lists
    
        for set_ in list_of_sets:   # organized in order of size smallest to large (2,3)  (3,4,2) 
            print("\nlist of sets ",list_of_sets)
            print("set ", set_)
            # print(type(set_))
            print("support count ", find_support_count(data, set_))
            if find_support_count(data, set_) <= minSup: 
                list_of_sets = delete_instance_from_tree(list_of_sets, set_) #delete function 
            else: 
                final_list.append(list(set_))
        #     if(set_ == (41, 49)):
        #         y = 1
        #         break

        # if(y == 1):
        #     break    
        #print("List of Set1 ", list_of_sets)
        list_of_sets = find_next_layer(list_of_sets)
        #print("List of Set2 ", list_of_sets)
        if list_of_sets == False: 
            break 
        i = i + 1


    skyline = find_skylines(final_list)
    print("Skyline ", skyline)


        


    # print(ones)
    # twos = find_2s(ones)
    # print(twos)
    # next_layer = find_next_layer(twos)
    # print(next_layer)
    # next_next_layer = find_next_layer(next_layer)
    # print(next_next_layer)





def find_next_layer(past_layer): 
    if past_layer == []: 
        return False 
    else: 
        length_of_layer = len(past_layer[0])
        next_layer = []

        for i in range(len(past_layer)): 
            A = set(past_layer[i])
            for j in range(len(past_layer)):
                B = set(past_layer[j])
                union = A.union(B)
                if (len(union) == length_of_layer + 1) and (union not in next_layer):
                    next_layer.append(union)
                j+=1 
            i+=1 

        return next_layer






def find_2s(list_): 
    length = len(list_)
    return [(list_[i],list_[j]) for i in range(length) for j in range(i+1, length)]
 

if __name__ == '__main__': 
    main()




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