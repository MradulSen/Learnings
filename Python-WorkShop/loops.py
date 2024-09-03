#list --> data structure which can hold multiple values of multiple type
#array --> data structure which can hold multiple values of same type
list_of_cloud = ["aws","azure","gcp","utho"]
cloud = "gcp" #variable

print(list_of_cloud)

#add a new Cloud Salesforce

list_of_cloud.append("Salesforce")
print(list_of_cloud)
list_of_cloud.append("IBM")
print(list_of_cloud)
list_of_cloud.insert(2,"Heroku")
print(list_of_cloud)

print(len(list_of_cloud))

# insert Hello Cloud at zeroth index

list_of_cloud.insert(0,"Hello Clould")
print(list_of_cloud)

# Iteration of list
for clould in list_of_cloud:
    print("")
    print(cloud)

# For loop
for i in range(0,10):
    print(i)