

email_txt = "templates/email.txt"

content = ""

with open(email_txt, "r") as f:
    content = f.read()
    
print(content.format(name="Adam"))