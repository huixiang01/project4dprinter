import matplotlib as matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App

import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy
# ignore the above warning... it is stated in the libary that this would happen... kivy...
                     
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

import matplotlib.pyplot as plt


def press(event):
    print('press released from test', event.x, event.y, event.button)

def release(event):
    print('release released from test', event.x, event.y, event.button)

def keypress(event):
    print('key down', event.key)

def keyup(event):
    print('key up', event.key)

def motionnotify(event):
    print('mouse move to ', event.x, event.y)

def resize(event):
    print('resize from mpl ', event.width, event.height)

def scroll(event):
    print('scroll event from mpl ', event.x, event.y, event.step)

def figure_enter(event):
    print('figure enter mpl')

def figure_leave(event):
    print('figure leaving mpl')

def close(event):
    print('closing figure')

N = 5
means1 = (20, 35, 30, 35, 27)
std1 = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
rects1 = ax.bar(ind, means1, width, color='#add8e6', yerr=std1)

Means2 = (25, 32, 34, 20, 25)
std2 = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, Means2, width, color='b', yerr=std2)

# add some text for labels, title and axes ticks
ax.set_ylabel('Index')
ax.set_title('Average ccupancy in the Day')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
ax.legend((rects1[0], rects2[0]), ('Legend1', 'Legend2'))

rects2 = ax2.bar(ind + width, Means2, width, color='b', yerr=std2)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height), ha='center', va='bottom')

fig.canvas.mpl_connect('button_press_event', press)
fig.canvas.mpl_connect('button_release_event', release)
fig.canvas.mpl_connect('key_press_event', keypress)
fig.canvas.mpl_connect('key_release_event', keyup)
fig.canvas.mpl_connect('motion_notify_event', motionnotify)
fig.canvas.mpl_connect('resize_event', resize)
fig.canvas.mpl_connect('scroll_event', scroll)
fig.canvas.mpl_connect('figure_enter_event', figure_enter)
fig.canvas.mpl_connect('figure_leave_event', figure_leave)
fig.canvas.mpl_connect('close_event', close)

fig2.canvas.mpl_connect('button_press_event', press)
fig2.canvas.mpl_connect('button_release_event', release)
fig2.canvas.mpl_connect('key_press_event', keypress)
fig2.canvas.mpl_connect('key_release_event', keyup)
fig2.canvas.mpl_connect('motion_notify_event', motionnotify)
fig2.canvas.mpl_connect('resize_event', resize)
fig2.canvas.mpl_connect('scroll_event', scroll)
fig2.canvas.mpl_connect('figure_enter_event', figure_enter)
fig2.canvas.mpl_connect('figure_leave_event', figure_leave)
fig2.canvas.mpl_connect('close_event', close)

canvas = fig.canvas
canvas2 = fig2.canvas

# def callback(instance):
#     autolabel(rects1)
#     autolabel(rects2)
#     canvas.draw()

