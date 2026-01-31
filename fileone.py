# file handling
# storing the keystroke into a text file
# file handling hoe to read write and append to a file
# r = reading
# w = writing
#
#f = open("log.txt","a")
#filedata = f.read()
#print(filedata)
#f.write(' \n i am God! ')
#f.write('i am freeky aweasom  ')
#f.close()

# listeners  = listerns to keysstroke
# it requires memory alloction and memory is relese after it
# has done it job

with open("log.txt", 'a') as f:
    f.write("\n Hello : again!")