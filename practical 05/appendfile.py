with open('test.txt', 'a+') as file:
    file.write("Hello World")
    file.seek(0)
    print("full fill content")
    print(file.read())