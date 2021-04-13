#List of market items 
rice=5,500
beans= 2000
yam=1,200
garri=1,100

#total cost of items listed
total_cost=(rice +beans+yam+garri)
print("The total cost of listed items using conventional addition method is: " total_cost)

#Creating Array
def fooditem_array(arr):
    return sum(arr)

#  Test input
print(fooditem_array([rice,beans,yam,garri]))
