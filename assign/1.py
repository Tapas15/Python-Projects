#JSON Validator function
import json

#Made json as str data 
#jsonData = """ ((A=2 && B=3 || (C=4 && D=5)) """ #checking for if valid or not json
jsonData = """{
	"query": {
		"or": [{
				"and": {
					"A": 2,
					"B": 3
				}
			},
			{
				"and": {
					"C": 4,
					"D": 5
				}
			}
		]
	}
}"""

#checking if jsondata is valid or not 


# checking for string using loads function
try:
	print("printing string ",jsonData)
	print(type(jsonData))  # class string data 
	json_object = json.loads(jsonData) # converted into json type 
	print("____Convetted json_____")
	print ("Valid json string ",type(json_object)) # converted json dict type 
	print ("a valid json ",json_object)  
except: 
	print ("not a valid json") 
	print ("initial string",jsonData) 
	