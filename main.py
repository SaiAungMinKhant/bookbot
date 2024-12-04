def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    arr = file_contents.split()
    # # print(arr)
    # print(len(arr))

    lower_book = file_contents.lower()

    letter_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    for x in lower_book:
        if x in letter_dict:
            letter_dict[x] += 1
    # print(letter_dict)

    print(sorted)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{len(arr)} words found in the document")
    
    sort_letters_by_count = sorted(letter_dict.items(), key=lambda x:x[1], reverse=True)
    convert_sorted_letters_dict = dict(sort_letters_by_count)
    for x in convert_sorted_letters_dict:
        print(f"The {x[0]} character was found {convert_sorted_letters_dict[x]} times")

main()