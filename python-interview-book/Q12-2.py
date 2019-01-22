def is_letter_constructible_from_magazine(letter_text, magazine_text):
    #this below code automatically sets up the counter hash table
    # ready for the letters
    char_freq_for_letter = collections.Counter(letter_text)
    #now pass thru magazine
    for c in magazine_text:
        if c in char_freq_for_letter:
            char_freq_for_letter[c] -=1
            if char_freq_for_letter[c] == 0:
                del char_freq_for_letter[c]
                if not char_freq_for_letter:
                    return True
    return not char_fre_for_letter
