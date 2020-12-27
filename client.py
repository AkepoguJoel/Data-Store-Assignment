#This code is used by the clients to interact with the data store
#Clients import the core file that has the main code
# these are the commands that I used to demonstrate how to access and perform operations on a core file


#Execute the MODULE of CORE FILE and import corefile as a library

import back_end_code as c
#importing the main file("back_end_code" is the name of the file I have used) as a library


c.create("John",25)
#to create a key with key_name,value given and with no time-to-live property


c.create("Lisa",23,3600)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


c.read("John")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


c.read("Lisa")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


c.create("John",40)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error
#either use modify operation to change the value of a key
#or use delete operation and recreate it


c.modify("John",35)
#it replaces the initial value of the respective key with new value


c.delete("John")
#it deletes the respective key and its value from the database(memory is also freed)

c.delete("Lisa")

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

#The code also returns other errors like
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
