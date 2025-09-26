name = 'hector'
last_name= 'lavoe'
full_name = f"{name} {last_name}"

lowercase_msg = full_name.lower()
uppercase_msg = full_name.upper()
title_case_msg= full_name.title()

msgs_list= [lowercase_msg,uppercase_msg,title_case_msg]

counter= 0
for msg in msgs_list:
    print(f"{counter}. {msg}")
    counter = counter+1
print(f"Original full name: {full_name}")