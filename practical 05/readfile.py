with open('test.txt', 'r+') as file:
    print("original content")
    print(file.read())

    file.seek(0,2)
    file.write("\n this is new content")
