import smtplib

smt_server="smtp.gmail.com"
port=557

user="wassimtatari@gmail.com"
password='#######'

from_user='wassimtaatri@gmail.com'
to_user="duexmers@gmail.com"


subject="important email"
body="lists of last month sales"

message=f'From:{from_user}\nTo:{to_user}\nSubject:{subject}\nBody:{body}'

try:
    server=smtplib.SMTP(smt_server,port)
    server.starttls()
    server.login(user,password)
    server.sendmail(from_user,to_user,message)
    print('Message sent')
except Exception as e:
    print(e)
finally:
    server.quit()