from time import sleep
import webbrowser
import wikipedia
import pyjokes
from log_in_sign_up import sign_in,log_in,remove_user,change_password

def text_recongnition():
        text = input(":").lower()
        print("  ")
        return text
    
def wikipedia_search():
        search = input("Please enter the name of the person:").lower()
        try:
         result = wikipedia.summary(search,3)
         print("  ")
         print(result)
        except Exception as error:
            print("An Error occured !\n\nError %s" % error)



          


def website_open():
        web = input("Please enter the url of the website:")
        webbrowser.open(web)
        print("Website Opened !")
    
def jokes():
       joke =  pyjokes.get_joke()
       print(joke)

def responding():
           sleep(1)
           print("Responding.")
           sleep(1)
           print("Responding..")
           sleep(1)
           print("  ")

def TaskExe():
             sleep(2)
             print("\nHello ,\n\nI am Plater 1.1")
             sleep(2)
             print("\nNow you can delete your account and change your password\n")
             sleep(2)
             print('''Search on web, search on youtube, 
                   tell jokes, check weather 
                   - even search on wikipedia for you.
                    ''')
             sleep(2)
             while True:
              print("\nPlater : How may I help you ?")
              query = text_recongnition()
              responding()
         
              if "hello" in query:
                  print("Hello ,\nI am Plater 1.1")
              elif "how are you" in query:
                  print("Thank you for asking! As an AI model, I don't have\nfeelings, but I'm here and ready to assist you.")
              elif "how are you ?" in query:
                  print("Thank you for asking! As an AI model, I don't have\nfeelings, but I'm here and ready to assist you.")
              elif "open youtube" in query:
                  webbrowser.open("youtube.com")
                  print("Youtube Opened !")
              elif "wikipedia" in query:
                  wikipedia_search()
              elif "open google" in query:
                  webbrowser.open("google.com")
                  print("Google Opened !")
              elif "stop" in query:
                  print("Absolutely! If you have any more questions or need assistance in the future, feel free to \nreach out. I'm here to help.")
                  break
              elif "bye" in query:
                  print("Goodbye! If you ever have more questions or need assistance in the future, feel free \nto return. Take care!")
                  break
              elif "facebook" in query:
                  webbrowser.open("facebook.com")
              elif "website" in query:
                  website_open()
              elif "joke" in query:
                  jokes()
              elif "temperature outside" in query:
                  webbrowser.open("https://www.google.com/search?q=temperature&rlz=1C1PRUI_enAE1063AE1063&oq=tempera&gs_lcrp=EgZjaHJvbWUqCggAEAAYsQMYgAQyCggAEAAYsQMYgAQyCggBEAAYsQMYgAQyBggCEEUYOTINCAMQABixAxjJAxiABDIKCAQQABiSAxiABDIHCAUQABiABDINCAYQABiDARixAxiABDIHCAcQABiABDINCAgQABiDARixAxiABDINCAkQABiDARixAxiABNIBCDIyODZqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8")
              elif "instagram" in query:
                  webbrowser.open("instagram.com")
                  sleep(2)
                  print("Instagram Opened !")
              elif "youtube search" in query:
                  search = input("Please enter what you want to search:")
                  print(f"Youtube results for {search}")
                  sleep(2)
                  webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
              elif "change password" in query:
                   change_password()
              elif "change my password" in query:
                   change_password()
              elif "delete my account" in query:
                   remove_user()
                   break
              elif "delete account" in query:
                   remove_user()
                   break
              else:
                  print("Sorry couldn't get you !")
             
                 
def sign_in_log_in():
    while True:
      print("\nWelcome to Plater 1.1!")
      sleep(2)
      s_l = input("\nWould like to sign in or log in:").lower()
      if s_l == "sign in":
           sign_in()
           TaskExe()
           break
      elif s_l == "log in":
           log_in()
           TaskExe()
           break
      else:
           print("Invalid input!")
           y_n = input("Would you like to continue(y/n):").lower()
           if y_n == "y":
             continue
           elif y_n == "n":
             break
           else:
             print("Invalid input !")
             break
          


sign_in_log_in()
