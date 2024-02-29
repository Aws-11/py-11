band = {"vocals": "john", "guitar": "sara", "drums": "buzz" }
print(band)

search_word = input("type here: ")
search_word = search_word.lower()

if search_word in band:
    print("we found", band[search_word])

else:
    search_word = input("type here: ")
    print("we found", band[search_word])
    


