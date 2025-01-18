classes_dict = {'Mo': [12,"Patna","PHY"],
                'Sa': [22,"Kolkata","GEO"]
               }
print(classes_dict['Mo'])
print(list(classes_dict.keys()))
print(list(classes_dict.values()))
print(list(classes_dict.items()))
print(len(classes_dict))



birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("enter a name:(blank to quit)")
    name = input()
    if name == ' ':
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of "+ name)
    else:
        print("I do not have birthday information of "+ name)
        print("What is their birthday?")
        birthdays[name] = input()
        print("Birthdays is updated.")

print(birthdays)
