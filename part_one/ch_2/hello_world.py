#variables are labels

message="Hello there, it's been a while, huh?"
print(message)
message="Yes it's been a while!"
print(message)


#let's include a misspelled word 'mesage'

print(mesage)
"""
{
	"name": "NameError",
	"message": "name 'mesage' is not defined",
	"stack": "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)\nFile \u001b[1;32mmparradop\\python_crash_course\\part_one\\ch_2\\hello_world.py:8\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[39mprint\u001b[39m(message)\n\u001b[0;32m      6\u001b[0m \u001b[39m#let's include a misspelled word 'mesage'\u001b[39;00m\n\u001b[1;32m----> 8\u001b[0m \u001b[39mprint\u001b[39m(mesage)\n\n\u001b[1;31mNameError\u001b[0m: name 'mesage' is not defined"
}
"""






