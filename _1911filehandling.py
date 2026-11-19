# file1 = open("hello.txt","r") # No file created
# print(file1.read())
# file1.close()

# # Overwrite 
# file2 = open("demo.txt","w") # Create file if not exist
# file2.write("hakfdkbi")
# file2.close()

# Append
# file3 = open("xd.txt","a")  # Create file if not exist 
# for i in range(1,1001):
#     file3.write(f"Hello {i}\n")

# file3.close()



# pat = "C:\\Users\\HP\\Desktop\\Python\\xd.txt"
# # pat = r"C:\Users\HP\Desktop\Python\xd.txt"
# with open(pat,"r") as f:
#     print(f.read())




# import os

# os.mkdir("hello") # Make directory

# os.rename("demo.txt","dem.txt")
# os.remove("dem.txt")


# pat = "C:\\Users\\HP\\Desktop\\Python"
# if os.path.exists(pat):
#     if os.path.isfile(pat):
#         print("File")
#     elif os.path.isdir(pat):
#         print("Directory")