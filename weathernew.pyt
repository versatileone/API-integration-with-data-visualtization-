import requests , json
import matplotlib.pyplot as plt 
import numpy as np

api_key="61e20fe99f0d5b172e27e4ae9c8baa42"
print("HERE YOU CAN FIND TEMPRATURE COMPARISOIN BETWEEN MULTIPLE CITIES\n")
city_no=int(input("enter the no. of cities >> \n"))
list=[]
list2=[]
for i in range(0,city_no):
    city_name=input(f"enter the name of city {i+1} >>")
    list.append(city_name)
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    get_info=requests.get(api_url)
    get_info=get_info.json()
    pretty_info=json.dumps(get_info,indent=4)
    temp=get_info["main"]["temp"]
    list2.append(temp)
print(list)
print(list2)

x=np.array(list)
y=np.array(list2)
plt.xlabel("NAME OF CITIES")
plt.ylabel("LIVE TEMPRATURE")
plt.title(f"graph comparision between {city_no} cities")
plt.bar(x,y,color="pink")
plt.show()