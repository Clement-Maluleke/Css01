# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:45:23 2024

@author: CLEMENT H MALULEKE
"""

#list 

age= [25,32,54,44,18,62,48,55,66,41,55,2,1,14]

print(age)
names= ["clem","ben","pen","malulek","lucky","josef","talan","mitchel","rifumu","mhan","christina","thuli","bali","tebogo"]
print(names)

#printing elements of the list

print(names[5])

print(max(age))
print(min(age))
print(len(age))

#to print an average we use

avg= sum(age)/len(age)

gender = ["F","M","F","M","F","M","F","F","F","M","F","M","M","M"]
print(gender)

#to remove a colum use .drop dunction. i.e df.drop

#dictionary


mammals = {"cat": "a cute animal", "lion": "king of the jungle", "elephant": " a gigantic herbivor"}

import pandas as pd
#We make use of dictionaries but this dictionary actually contains a list as its entries. that is why when combined with DataFrame it forms a data frame
datas= {'Age': age,
        'Names' : names,
        'Gender': gender}


df = pd.DataFrame(datas)




 
#check the way he decleared the dataframe