# Created on 21 oct 2016
# Created by: Matthew Lourenco
# this is a program that creates 10 random numbers then gibes the option to average them.

import ui
from numpy import random

my_numbers = []

def randomize_touch_up_inside(sender):
    global my_numbers
    view['random_number_textview'].text = ''
    my_numbers = []
    for index1 in range(0, 10):
        my_numbers.append(float(random.randint(1, 100)))
        view['random_number_textview'].text = (view['random_number_textview'].text + str(my_numbers[index1]) + '\n')

def average_touch_up_inside(sender):
    average = 0
    global my_numbers
    for index2 in my_numbers:
        average = average + index2
    average = average / len(my_numbers)
    view['average_label'].text = 'The average is: ' + str(average)

view = ui.load_view()
view.present('fullscreen')
