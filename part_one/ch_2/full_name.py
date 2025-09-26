first_name = " michael"
last_name = "jordan "
full_name = f"{first_name} {last_name}"
print(full_name.title())

#print(f"{full_name.title()}is the GOAT!")

message = f"{full_name.title()} is the GOAT!"

print(message)

#eliminate extra whites
print(message.strip()) #left and right
print(message.rstrip()) #right only
print(message.lstrip()) #left only
