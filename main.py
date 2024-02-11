import string



def main():
    file_name = "frankenstein.txt"
    with open(f'./books/{file_name}') as f:
        file_contents = f.read()
        num_of_words = count_words(file_contents)
        # print(num_of_words)
        characters_dict = count_letters(file_contents)
        # print(characters_dict)
        print_report(file_name, num_of_words, characters_dict)

def count_words(book_content):
    words = book_content.split()
    return len(words)

def count_letters(file_contents):
    ascii_lower = string.ascii_lowercase
    character_count = {}
    for character in file_contents:
        if character.lower() in ascii_lower: 
            if character.lower() in character_count:
                character_count[character.lower()] += 1
            else:
                character_count[character.lower()] = 1
    return character_count

def sort_on(letter_dict):
    return letter_dict["num"]
    
def convert_dict_to_list(letter_dict):
    letter_list = []
    for key, value in letter_dict.items():
        letter_list.append({"letter":key, "num":value})

    return letter_list

    
def print_report(file_name, word_count, letter_count):
    print(f"--- Begin report of books/{file_name} ---")
    print(f"{word_count} words found in the document")
    print("\n")


    letter_list = convert_dict_to_list(letter_count)
    letter_list.sort(reverse=True, key=sort_on)
    
    for item in letter_list:
        letter = item["letter"]
        num = item["num"]
        print(f"The '{letter}' character was found {num} times")

    print("--- End report ---")

main()