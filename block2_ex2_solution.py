fails = 0
password= 'password'
attempt = ' '
while fails < 3:
   print("Please input your password user.")
   attempt = input()
   if attempt != password:
       fails += 1
       print("Wrong password! You have tried and attempted " + str(fails) + " times")
   else:
       print("Welcome User!")
       break
else:
   print("You have failed too many times. Goodbye.")
