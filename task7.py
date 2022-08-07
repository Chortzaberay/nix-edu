users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]


def greeting(args):
    name, country = args[0], args[1]
    lang_dict = {"us": "Hello", "uk": "Hello", "ua": "Привіт", \
                 "ru": "Привет", "es": "Hola"}
    
    if country not in lang_dict.keys():
        return f"Hello, {name}, but I do not know where are you from!"
    else:
        return f"{lang_dict[country.lower()]}, {name}!\n"


if __name__ == '__main__':
        res = map(greeting, users_list)
        print(*res)
