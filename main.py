AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

print("********************************")
print("AutoCountry Vehicle Finder v0.3")
print("********************************")
print("Please Enter the following number below from the following menu:")
print("")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. ADD Authorized Vehicle")
print("4. Exit")
print("********************************")

while True:
  number = input(int)
  if number == "1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for truck in AllowedVehiclesList:
      print(truck)

  elif number == "2":
    response = input("Please enter the full Vehicle name: ")
    if response in AllowedVehiclesList:
      print(response + " is an authorized vehicle")
    else:
      print(response + " is not an authorized vehicle, if you received this in error please check the spelling and try again")

  elif number == "3":
    with open("AllowedVehiclesList.txt", "a") as db:
      response = input("Please enter the full Vehicle name you would like to add: ")
      AllowedVehiclesList.append(response)
      db.write(response + "\n")
      print("You have added " + response + " as an authorized vehicle" )

  elif number == "4":
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    break