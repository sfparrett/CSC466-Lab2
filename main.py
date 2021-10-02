import pandas as pd

# DATA being used 
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
    support_counts = find_support_counts(data)
    remove_less_than_support_counts(support_counts, 1)

def unpack_data_set(filename):
    original_data = []
    with open(filename, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            original_data.append(row)
    return original_data


def find_support_counts(data): 
    support_counts = {}
    
    for item_list in data: 
        i = 1 # ignore the first one because its the receipt 
        for i in range(len(item_list)):
            if item_list[i] in support_counts:
                support_counts[item_list[i]] += 1
            else: 
                support_counts[item_list[i]] = 1

    print(support_counts)
    return support_counts



def remove_less_than_support_counts(data, min_support): 
    for key, value in list(data.items()):
        if value <= min_support: 
            del data[key]

    print(data)





    











# step one : Frequent items 
def apriori(T, I, min_support): 
    """
    def: finds the frequent items sets 
    PARAM: 
        min_support: (float) between 0.0-0.999
        T: market basket data set 
        I: List of items 

    """
    pass 


def canidate_gen(): 
    """
    helper function frequent items 
    """
    pass 

# step two 
def association_rules(): 
    pass 


if __name__ == "__main__": 
    main()
