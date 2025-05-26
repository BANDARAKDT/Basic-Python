with open("test.txt","w+") as file:
    file.write("hellow")
    file.seek(0)

    content= file.read()
    print("content after write")
    print(content)
