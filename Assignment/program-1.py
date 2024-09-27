# 1.WRITE A PROGRAM TO CREATE ONE TEXT FILE "PYTHON.TXT". 2.WRITE 15 LINES FROM USER IN IT. 3.TAKE USER INPUT WORD WHICH YOU WANT TO FIND,AND REPLACE IT WITH APPROPRIATE REPLACEMENT WORD.
f=open("D:\\pythontextfile\\python.txt","w")
line=[]
while True:
    l=input()
    if l:
        line.append(l+"\n")
    else:
        break
text="\n".join(line)
f.writelines(line)
f.close()
# TAKE USER INPUT WORD WHICH YOU WANT TO FIND, AND REPLACE IT WITH APPROPRIATE REPLACEMENT WORD.

f=open("D:\\pythontextfile\\python.txt","r")
l=f.read()
word_to_find=input("Enter the word you want to find:")
replacement_word=input(f"Enter the word to replace '{word_to_find}' with:")

#REPLACE THE WORD IN THE CONTENT.

update_contend=l.replace(word_to_find,replacement_word) #replace() is a in-built function
f.close()

#WRITE THE UPDATED CONTEND BACK TO THE FILE.
f=open("D:\\pythontextfile\\python.txt","w")
f.write(update_contend)
f.close()
f=open("D:\\pythontextfile\\python.txt","r")
w=f.read()
print(w)
f.close()
