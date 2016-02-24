#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
sys.path.append("../tools/")
import pickle
import feature_format

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print enron_data.keys()
#
# Keys: enron_data[i].keys()
#salary
#to_messages
#deferral_payments
#total_payments
#exercised_stock_options
#bonus
#restricted_stock
#shared_receipt_with_poi
#restricted_stock_deferred
#total_stock_value
#expenses
#loan_advances
#from_messages
#other
#from_this_person_to_poi
#poi
#director_fees
#deferred_income
#long_term_incentive
#email_address
#from_poi_to_this_person


print enron_data["LAY KENNETH L"]['total_payments']
print enron_data["SKILLING JEFFREY K"]['total_payments']
print enron_data["FASTOW ANDREW S"]['total_payments']

poi=0
p=0

for i in enron_data:
    if enron_data[i]['poi'] == True:
        poi+=1
        if enron_data[i]['total_payments'] == 'NaN':
            p+=1
   
poi+=10
p+=10
print "poi",poi,"p",p
print "percent", p/float(len(enron_data)) *100



#EOF