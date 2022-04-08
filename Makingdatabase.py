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

    print("Hi Joe, my name is", me_data['name'], 'and my student ID is', me_data['student_ID'], end='\n') 

    for m in me_data['movies']:
        print(m['movie'], end=', ')


main()