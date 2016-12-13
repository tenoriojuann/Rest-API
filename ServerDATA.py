"""
Author: Juan Emmanuel Tenorio Arzola
Date: 10/11/2016
Assignment: 6, REST Server

File: REST Server

"""

#importing the necessary modules
import acessDATA
from flask import Flask, jsonify

app = Flask(__name__)


#Entry point for the server
@app.route('/', methods = ['GET'])
def welcome():	
	return ("Welcome!")

#Grabbing the table 'area' from the database
@app.route('/area', methods = ['GET'])
def api_get_area():
	d = acessDATA.api_get_area()
	return jsonify(d)
	
	
#Serving locations based on the area provided
@app.route('/area/<int:area_id>/location', methods = ['GET'])
def get_locations(area_id):
	d = acessDATA.api_get_all_locations(area_id)
	
	if(bool(d)): #Checking if the returned locations dictionary is empty
		return jsonify(d)
	else:
		return "No location was found with that ID"
		
		
#Serving measuraments based on the location provided
@app.route('/location/<int:location_id>/measurement', methods = ['GET'])
def get_all_measurements(location_id):
	d = acessDATA.api_get_all_measurements(location_id)
	
	if(bool(d)): #Checking if the returned measuraments dictionary is empty
		return jsonify(d)
	else:
		return "No measuraments were found with that ID"

		
#Serving categories based on the area provided
@app.route('/area/<int:area>/category', methods = ['GET'])
def get_categories(area):
	d = acessDATA.api_get_all_categories(area)
	
	if(bool(d)):#Checking if the returned categories dictionary is empty
		return jsonify(d)
	else:
		return "No category was found with that area_id"
		
		
#Serving the average of all of the values that are in the given location
@app.route('/area/<int:measurement_location>/average_measurement', methods = ['GET'])
def get_average(measurement_location):
	d = acessDATA.api_get_average(measurement_location)
	
	if(bool(d)):#Checking if the returned average is empty
		return jsonify(d)
	else:
		return "No locations were found"

		
		
#Serving the number of locations based on the given area
@app.route('/area/<int:area>/number_locations', methods = ['GET'])
def get_numberOfLocations(area):
	d = acessDATA.api_get_numberOfLocations(area)
	
	if(bool(d)):#Checking if the returned number of locations is empty
		return jsonify(d)
	else:
		return "No locations were found"

		
if __name__ == '__main__':
	app.run(host = "localhost" ,port = "5000")