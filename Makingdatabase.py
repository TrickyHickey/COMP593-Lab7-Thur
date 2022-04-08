from tempfile import tempdir


def main():

    me_info = {
        'name': 'Josiah', 
        'student_ID': 10243852,
        'pizza_toppings': ['mushrooms', 'pepperoni', 'bacon'],
        'movies': [
            {'movie': 'Game of Thrones',
            'genre': "drama",
            },
            {'movie': 'Dracula untold',
            'genre': 'fantasy',

            }
        ]
    }

    extra_movie = {'movie': 'aganst the ice', 'genre': 'adventure'}

    me_info['movies'].append(extra_movie)

    even_more_pizza_toppings = ('sausage', 'cheese', 'ketchup')
    add_new_toppings(me_info, even_more_pizza_toppings)

    print_about_me(me_info)
    pass

def add_new_toppings(me, toppings):
    for t in toppings:
        me['pizza_toppings'].append(t)

def print_about_me(me_data):

    #printing my name, student ID, and pizza toppings
    print("Hi Joe, my name is " + me_data['name'] + ", and my student ID is " + str(me_data['student_ID']))
    print('My ideal pizza has ', end='')
    for p in me_data['pizza_toppings']:
        print(p, end=', ')

    words = ('\nI like to watch ')
    for a,s in enumerate(me_data['movies']):
        words += s['genre']
        if a < len(me_data['movies']) - 1:
            words += ', '
        else: 
            words += '. '
    print(words)

    #printing movies I like to watch
    sentence = ('Some of my favourites are ')
    for i,m in enumerate(me_data['movies']):
        sentence += m['movie']
        if i < len(me_data['movies']) - 1:
            sentence += ', '
        else: 
            sentence += '. '
    print(sentence)
 
    

main()