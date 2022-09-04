# string concatenation methods
# youtuber = "my channel"

# few methods include
# print("subscribe to " + youtuber)
# print("subscribe to", youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

""" Madlib is a phrasal template word game that involves one player prompting others 
for a list of words to substitute for blanks in a story before reading aloud.
"""
noun1 = input("noun: ")
noun2 = input("noun: ")
noun3 = input("noun3: ")
noun4 = input("noun4: ")

madlib = f"Madlib is a phrasal template {noun1} that involves {noun2} \
player prompting others fora list of {noun3} to substitute for blanks \
in a {noun4} before reading aloud"
print(madlib)
