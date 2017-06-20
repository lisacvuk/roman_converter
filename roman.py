import hexchat

__module_name__ = "roman_converter"
__module_version__ = "1.0"
__module_description__ = "Converts whatever you type in /say_w to actual latin"



def say_cb(word, word_eol, userdata):
	finalstring = ""
	message = ""
	if len(word) < 2:
		print("Second arg must be the message!")
	else:
		for w in word[1:]:
			message = message + str(w) + " "
		for char in message:
			if char == 'r':
				char = 'w'
			if char == 'R':
				char = 'W'
			finalstring = finalstring + char
	hexchat.command("say " + finalstring)
hexchat.hook_command("SAY_W", say_cb, help="/say_w <message> Convert message to latin and send it to current channel")
