class StrExtension:

    @staticmethod
    def remove_vowels(string):
        removed_chars = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
        return ''.join(filter(lambda x: x not in removed_chars, string))

    @staticmethod
    def leave_alpha(string):
        return ''.join(x for x in list(string) if x.isalpha())
        pass

    @staticmethod
    def replace_all(string, chars, char):
    
        for letter in chars:
            string = string.replace(letter, char)
        return string

   



# INPUT DATA:

# TEST_1:
print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))

# # TEST_2:
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

# # TEST_3:
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))

# # TEST_4:
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'))
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'.upper()))

# # TEST_5:
# print(StrExtension.leave_alpha('beegeek!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~BEEGEEK'))
# print(StrExtension.leave_alpha('beegeek0123456789BEEGEEK'))

# # TEST_6:
# from string import ascii_lowercase

# text = '''I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
# My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.'''

# print(StrExtension.remove_vowels(text))
# print(StrExtension.leave_alpha(text))
# print(StrExtension.replace_all(text, ascii_lowercase, ''))