import hashlib

def signUp():
  #sign up with email and password
  email = input("Enter your email address: ")
  pwd = input("Create a password: ")
  conf_pwd = input("Confirm password: ")

  #if password matches confirmed password
  #logged the email and password to the database

  if conf_pwd == pwd:
    #encode password
    enc = conf_pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest();

    #create file and write to it
    with open("Credentials.txt", "w") as f:
      f.write(email + '\n')
      f.write(hash1)
    f.close()
    print("You have registered successfully!")

  else:
    print("Password is not same as above!")

def login():
  #user login page
  email = input("Enter email address: ")
  pwd = input("Enter your password: ")

  #encript password
  auth = pwd.encode()
  auth_hash = hashlib.md5(auth).hexdigest()
  #fetch email and password from database
  with open("Credentials.txt" , "r") as f:
    stored_email, stored_pwd = f.read().split("\n")
  f.close()

  #check to see if data from database matches login data
  if email == stored_email and auth_hash == stored_pwd:
    print("Logged in Successfully!")
  else:
    print("Email or password does not match existing data")

choice = "0"
while choice != "3":
  print("******* Login System *******")
  print("1. signup")
  print("2. login")
  print("3. exit")
  choice = input("Please select an option: ")
  if choice == "1":
    signUp()
  elif choice == "2":
    login()
  elif choice == "3":
    break;
  else:
    print("Invalid option")
