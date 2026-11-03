import poplib


user_email="wassimtatari@gmail.com"
password='#########'


pop3_server="pop.gmail.com"
mail_box=poplib.POP3_SSL(pop3_server,995)


mail_box.user(user_email)
mail_box.pass_(password)

num_message=len(mail_box.list()[0])
print(f"Number messages{num_message}")


if num_message>0:
    response,lines,octets=mail_box.retr(num_message)
    message='\n'.join(line.decode('utf-8')for line in lines)
    print("message content:")
    print(message)
mail_box.quit()


