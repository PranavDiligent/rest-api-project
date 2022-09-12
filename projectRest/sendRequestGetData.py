import requests

# api_url = "http://127.0.0.1:8000/api/students/9"

api_url = "http://127.0.0.1:8000/api/users"
data = {"name":"jack","age":61,"gender":"M"}
response = requests.get(api_url,auth=requests.auth.HTTPBasicAuth('root','root')
    
)
# response = requests.post(api_url,data=data,auth=requests.auth.HTTPBasicAuth('root','root'))
print(response.status_code)
print(response.json())
data = response.json()



def printOnlyUsername(dataJson):
    
    for data in dataJson:
        print(f"The username is {data['username']}")
        q+=1

printOnlyUsername(data)
