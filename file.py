'''
file = open('python.txt','r')

inside the paranthesis specifies the location and the there is a file mode specified
 there are read,append,write,read and write

read=file.read()
reads=file.readline()
readss=file.readlines()
print(read)
print(reads)
print(readss)
file.close()


file = open('python.txt','a')
write=file.write("how is ur life")
print(write)
file = open('python.txt','r')
read=file.read()
print(read)
file.close()

'''
file = open('python.txt','r+')
write=file.write("how is ur life")
print(write)
read=file.read()
print(read)
file.close()