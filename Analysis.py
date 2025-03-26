#core concepts 
#1. file streams
   #its an abstraction reping a sequence of bytes flowing btwn program and a file.
   #types of streams input(reading data) streams, output(writing data) streams and error streams
#2. file pointers
    #indicates the current position in file where reading and writing will occur.
    #allows programs to keep track of their position within the file.
#3. file modes
    #diff modes for opening files eg r -( for reading), w- (for writing), A - (for appending) and r+ -(for both reading and writing, if file doesnt exist it will raise an error)
#Reading Data from files to Python
#opening files - done using the open () function
   #-Takes the file name and mode as arguments
#Reading methods - read() reads the entire content of a file as as ingle string
#Readline () - reads a single line from a file.
#Readlines() - reads all lines from a file and returns a list of strings
#FILE CONTEXT MANAGERS
#using with statements ensures files are properly closed after operations
with open("file.txt","r") as f:
    data=f.readlines()
print(data)

#WRITING DATA FROM PYTHN INTO FILES
#opening files - done using the open () function
#writing methods - writes() writes a single string to the file
#  Writelines() - writes lits of strings to the file
# appending methods - use the a- mode
with open("file.txt", "a") as f:
 f.writelines("Moringa wewe \n")

#FILE TYPES
#1. Text files - contain plain texts
#2. CSV Files - store tarbular data in plan text(each row reps a line)
#3. JSON Files - Stores JSON data (JavaScript object Notation. transfer data from WEB )
#4. Binary Files - Raw data, not human readable 

#KAGGLE
