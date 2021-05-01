import requests

#We got the base URL from the server that we ran
BASE="http://127.0.0.1:5000/"

#Our response is a get request to the base URL + our endpoint
#Additional parameters such as name and age have been added
response=requests.get(BASE+"helloworld/joe/23")
print(response.json())
