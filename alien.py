alien_0 = { 'color': 'green',
           'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
print(f"The alien is of {alien_0['color']} color.")


for key, value in alien_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value}")

favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name}'s favourite languages are: ")
    for l in languages:
        print(f"\t{l.title()}")