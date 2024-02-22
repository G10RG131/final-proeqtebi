import random

while True:
    print("თამაში სათამაშოდ ჩაწერეთ მისი სახელი \"guess\"  ან \"hangman\".\nთამაშის შესაწვეტად \"end\".")
    game = input().upper()
    if game == "GUESS":
        chapiqrebuli_ricxvi = random.randrange(1001)
        count = 0
        print("გამოიცანით ჩაფიქრებული რიცხვი 0-დან 1000-მდე")

        while True:
            guess_str = input()
            if guess_str.upper() == "END":
                break
            try:
                guess_int = int(guess_str)
            except ValueError:
                print("მხოლოდ ნატურალური რიცხვები")
                continue
            count += 1
            if guess_int < 1 or guess_int > 1000:
                print("ჩაფიქრებული რიცხვი არის 0-დან 1000-მდე")
            elif guess_int > chapiqrebuli_ricxvi:
                print("საძიებო რიცხვი ნაკლებია გადმოცემულ რიცხვზე")
            elif guess_int < chapiqrebuli_ricxvi:
                print("საძიებო რიცხვი მეტია გადმოცემულ რიცხვზე")
            else:
                print("გამოსაცნობად დაგჭირდა", count, "მცდელობა", "\n")
                break
        print("ჩაფიქრებული რიცხცვი იყო", chapiqrebuli_ricxvi, "\n")

    elif game == "HANGMAN":
        words_list = ["python", "Java", "Ruby"]
        tries = 0
        used_letters = []
        word = str(random.choice(words_list)).upper()
        letters_to_guess = list(word)
        secret_word = []
        i = 0
        while i < len(word):
            secret_word.append("_")
            i += 1

        while True:
            if letters_to_guess == secret_word:
                print("გილოცავ შენ სწორად გამოიცანი ჩაფიქრებული სიტყვა:", word, "\n")
                break
            if tries >= 8:
                print("სამწუხაროდ მცდელობების რაოდენობა ამოგეწურათ, ჩაფიქრებული სიტყვა იყო", word, "\n")
                break

            print("ჩაფიქრებული სიტყვა", *secret_word, sep=" ", end="\n")
            print("მცდელობების რაოდენობა", 8-tries)
            guess = input("").strip().upper()

            if guess == word:
                print("გილოცავ შენ სწორად გამოიცანი ჩაფიქრებული სიტყვა:", word, "\n")
                break
            elif guess == "!END":
                print("ჩაფიქრებული სიტყვა იყო", word, "\n")
                break
            elif len(guess) == 1 and guess.isalpha():
                if guess in used_letters:
                    print("ეს ასო უკვე ცადე")
                elif guess in letters_to_guess:
                    for i in range(0, len(letters_to_guess)):
                        if guess == letters_to_guess[i]:
                            secret_word[i] = guess
                else:
                    tries += 1
                    print("ასო არ არის ჩაფიქრებულ სიტყვაში")
                used_letters.append(guess)
            elif len(guess) > 1 and guess != word:
                tries += 1
                print(guess, "არ არის ჩაფიქრებული სიტყვა")
    elif game == "END":
        break
    else:
        print("ეს თამაში ჯერ არ დამატებული \n")
