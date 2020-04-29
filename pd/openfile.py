import os

ls = os.listdir("samples")

with open("s.txt", "w") as text_file:
    for i in range(len(ls)):
        print(ls[i], file=text_file)
