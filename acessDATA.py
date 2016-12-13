"""
Author: Juan Emmanuel Tenorio Arzola
Date: 10/11/2016
Assignment: 6, REST Server

File: Data Retriever

"""
import sqlite3



conn = sqlite3.connect('measures.sqlite')
conn.row_factory = sqlite3.Row
print ("opened database")
c = conn.cursor()


#Function to get a dictionary from the SQL execution
def get_dict(sql):
	return (c.execute(sql).fetchall())

#Get ALL of the areas
def api_get_area(json_str = True):
	rows =  get_dict("select * from area")
	if json_str: #If false the retured values will not be in JSON format
	
	
		#Structuring the dictionary from 'get_dict' with sub-dictionaries
		# This way we can then 'jsonify' it.
		return [dict((x)) for x in rows] 
	
	
#Gets all the locations with the given 'id'
def api_get_all_locations(id, json_str = True):
	rows =  get_dict("select name,altitude from location where location_area ="+str(id))
	if json_str:#If false the retured values will not be in JSON format
	
	
		#Structuring the dictionary from 'get_dict' with sub-dictionaries
		# This way we can then 'jsonify' it.
		return [dict((x)) for x in rows]
	
	
#gets all the measurements with the given 'location_id'
def api_get_all_measurements(location_id, json_str = True):
	rows =  get_dict("select * from measurement where measurement_id ="+str(location_id))
	if json_str:#If false the retured values will not be in JSON format
	
	
		#Structuring the dictionary from 'get_dict' with sub-dictionaries
		# This way we can then 'jsonify' it.
		return [dict((x)) for x in rows]
	

def api_get_all_categories(area, json_str = True):
	rows = get_dict("select * from category_area where area_id ="+str(area))
	
	#Before we run the SQL statement we need to structure 'rows' with sub-directories
	rows = [dict((x)) for x in rows]
	
	#There are probably multiple categories, so we would need to run 1 SQL statement multiple times
	categories = [get_dict("select * from category where category_id="+str(id['category_id']))[0] for id in rows]
	if json_str:#If false the retured values will not be in JSON format
	
	
		#Structuring the dictionary from 'get_dict' with sub-dictionaries
		# This way we can then 'jsonify' it.
		return [dict(x) for x in categories]

def api_get_average(measurement_location,json_str = True):
	rows = get_dict("select * from measurement where measurement_location ="+str(measurement_location))
	#Before we can access the individual 'values' we need to structure the 'rows' dictionariy
	
	rows = [dict((x)) for x in rows]
	sum = 0
	for x in rows:
		sum += x['value']
		
	#Checking the case 'get_dict' does not find any measurements with the given 'measurement_location'.
	if(len(rows)>0):
		sum = sum/len(rows)
		
	if json_str:#If false the retured values will not be in JSON format
	
		return sum

def api_get_numberOfLocations(area, json_str = True):
	rows = get_dict("select * from location where location_area="+str(area))
	rows = [dict((x)) for x in rows]
	if json_str:#If false the retured values will not be in JSON format
	

		return len(rows)
