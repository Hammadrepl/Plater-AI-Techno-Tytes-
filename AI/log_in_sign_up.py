import json

def log_in():
    while True:
     username = input("Please enter your username:")
     password = input("\nPlease enter your password:")
     try:
      with open("users.json","r") as file:
        users =   json.load(file)
        if username in users and users[username]["password"] == password:
           print("\nLog in succesful!")
           print("\nWelcome back %s!" % username)
           break
        elif users == {}:
          print("\nNo account found!\nPlease create an account.")
          y_n = input("\nWould you like to create an account(y/n):").lower()
          if y_n == "y":
            sign_in()
          elif y_n == "n":
            break
          else:
            print("\nInvalid input !")
            break
        elif username not in users:
          print("\nNo account found!\nPlease create an account.")
          y_n = input("\nWould you like to create an account(y/n):").lower()
          if y_n == "y":
            sign_in()
          elif y_n == "n":
            break
          else:
            print("\nInvalid input !")
            break
        else:
          print("Username or password incorrect!")
     except Exception as error:
       print(f"An error occured!\nError : {error}")
       break


def remove_user():
  while True:
   username = input("Please enter your username:")
   password = input("\nPlease enter your password:")
   with open("users.json","r") as file:
     users = json.load(file)
 
     if username in users and users[username]["password"] == password:
       with open("users.json","w") as file:
         users = dict(users)
         users.pop(username)
         json.dump(users,file,indent=1)
         print("User Removed !")
         break
     elif users == {}:
         print("\nAccount not found!")
         y_n = input("\nWould you like to create an account(y/n):").lower()
         if y_n == "y":
           sign_in()
         elif y_n == "n":
           break
     else:
          print("Invalid input !")
          y_n = input("\nWould you like to continue(y/n):").lower()
          if y_n == "y":
             continue
          elif y_n == "n":
             break
          else:
             print("\nInvalid input !")
             break
        


def sign_in():
  while True:
   username = input("Please enter your username:")
   password = input("\nPlease enter your password:")
   try:
    with open("users.json","r") as file:
      users = json.load(file)
      if username in users:
        print("\nSorry username already taken.\nPlease choose a different one.\n")
        y_n = input("Would you like to continue(y/n):").lower()
        if y_n == "y":
             continue
        elif y_n == "n":
             break
        else:
             print("Invalid input !")
             break

      else:
        if len(password) < 6:
          print("The length of the password \nshould be atleast of 6 characters.")
          y_n = input("\nWould you like to continue(y/n):").lower()
          if y_n == "y":
             pass
          elif y_n == "n":
             break
          else:
             print("\nInvalid input !")
             break
        else:
          users[username] = {"password":password}
          with open("users.json","w") as file:
            json.dump(users,file,indent=1)
          print("\nSign up successful!\n\nPlease log in to continue.\n")
          log_in()
          break
   except Exception as error:
     print(f"Oh! An error occured!\nerror : {error}")
     break


def change_password():
 while True:
   username = input("Please enter your username:")
   password = input("\nPlease enter your password:")
   try:
    with open("users.json","r") as file:
      users = json.load(file)
      if users == {}:
          print("\nNo account found!\nPlease create an account.")
          y_n = input("\nWould you like to create an account(y/n):").lower()
          if y_n == "y":
            sign_in()
          elif y_n == "n":
            break
          else:
            print("\nInvalid input !")
            break

      if username in users and users[username]["password"] == password:
        new_pwd = input("Please enter your new password:")
        with open("users.json","w") as file:
          users = dict(users)
          users.pop(username)
          users[username] = {"password":new_pwd}
          json.dump(users,file,indent=1)
          print("Password changed !")
          break
      
      elif username not in users:
        print("\nAccount not found!")
        y_n = input("\nWould you like to create an account(y/n):").lower()
        if y_n == "y":
          sign_in()
        elif y_n == "n":
          break
        else:
            print("Invalid input !")
            break
      
      else:
        print("Invalid Input")
        y_n = input("\nWould you like to contine(y/n):\n").lower()
        if y_n == "y":
          continue
        elif y_n == "n":
          break
        else:
            print("\nInvalid input !\n")
            break

   except Exception as error:
     print(f"\nOh! An error occured!\nerror : {error}")
     break
   
remove_user()