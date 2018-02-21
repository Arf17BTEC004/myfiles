

import smtplib
 
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("arfath.17ec@cmr.edu.in", "arfath@cmru")
message = "heyyyyyyyy"
s.sendmail("arfath.17ec@cmr.edu.in", "arfathbaig355@gmail.com", message)
s.quit()
print("success")
