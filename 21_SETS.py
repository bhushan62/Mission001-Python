services = {
    "Dry Cleaning",
    "Wash & Iron",
    "Steam Iron"
}

print(services)

services.add("Shoe Cleaning")

print(services)

services.remove("Steam Iron")

print(services)

services.discard("Carpet Cleaning")

for service in services:                                              #This we already did before
    print(service)                 


store_one = {"Dry Cleaning", "Wash & Iron"}
store_two = {"Steam Iron", "Wash & Iron"}

all_services = store_one.union(store_two)                      #    union() combines both sets and removes duplicate values.

print(all_services)

common_services = store_one.intersection(store_two)

print(common_services)


difference = store_one.difference(store_two)

print(difference)