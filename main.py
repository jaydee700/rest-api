#This Python script runs the server using Flask and intializes the REST API.
#Once the server is running, a GET request can be made by running test.py 

from flask import Flask
from flask_restful import Api, Resource

#Initialize Flask
app=Flask(__name__)
#Initialize REST API
api=Api(app)

#Create a class that inherits methods and properties frmo Resource
#Define the get request 
class HelloWorld(Resource):
	def get(self, name, age):
		return{"name":name, "age":age}

#Add your class HelloWorld and choose the endpoint
api.add_resource(HelloWorld, "/helloworld/<name>/<age>")


#Initialize your server in debug mode
if __name__=="__main__":
	app.run(debug=True)
