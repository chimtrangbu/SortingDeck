#!/usr/bin/env python3

import pyglet
from pyglet.window import key
from classes import ListBox

window = pyglet.window.Window(1024, 600, fullscreen=False)  # create window
stats = []  # statuses of listN every time having change
i_pos, j_pos = 0, 0  # current possitions of i, j while swapping
i_des, j_des = 0, 0  # destination where i, j move to
done_swap = True  # if i, j are swapping, return False that do not update listn
space_flag = False  # True if press SPACE

# back ground
ahri = pyglet.image.load('Ahri.jpg')
ahri.texture.width = window.width
ahri.texture.height = window.height
background = pyglet.sprite.Sprite(ahri)

list_n = []
sort_key = ''
listbox = ListBox(list_n, window)


def main():
    pyglet.clock.schedule_interval(update, 1/12000.)
    pyglet.app.run()


def swap(list_n, i, j):
    list_n[i], list_n[j] = list_n[j], list_n[i]


def show_list(list_n):
    for e in list_n[:-1]:
        print(e, end=' ')
    print(list_n[-1])
    return


def bubble_sort(list_n):
    stats = []
    n = len(list_n)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if list_n[j] > list_n[j + 1]:
                stats.append((list_n.copy(), j, j+1, i + 1))
                swap(list_n, j, j + 1)
                show_list(list_n)
            else:
                stats.append((list_n.copy(), j, j, i + 1))
    return stats


def insertion_sort(list_n):
    stats = []
    n = len(list_n)
    for index in range(1, n):
        flag = 0
        current = list_n[index]
        pos = index
        while pos > 0 and list_n[pos - 1] > current:
            stats.append((list_n.copy(), pos - 1, pos, pos))
            list_n[pos] = list_n[pos - 1]
            list_n[pos - 1] = current
            pos = pos - 1
            flag = 1
        else:
            stats.append((list_n.copy(), pos - 1, pos - 1, pos))
        list_n[pos] = current
        if flag:
            show_list(list_n)
    return stats


def partition(list_n, first, last):
    global stats
    mid = (first + last)//2
    pivot = list_n[mid]
    print('P:', pivot)
    stats.append((list_n.copy(), first, mid, first))
    swap(list_n, first, mid)
    i = first + 1
    j = last
    while True:
        while i <= j and list_n[i] <= pivot:
            i += 1
        while i <= j and list_n[j] >= pivot:
            j -= 1
        if i > j:
            break
        else:
            stats.append((list_n.copy(), i, j, first))
            swap(list_n, i, j)
            list_n = list_n
    stats.append((list_n.copy(), first, j, mid))
    swap(list_n, first, j)
    show_list(list_n)
    return j


def quick_sort(list_n, first, last):
    global stats
    if first < last:
        p = partition(list_n, first, last)
        quick_sort(list_n, first, p - 1)
        quick_sort(list_n, p + 1, last)
    return stats


def get_stats():
    if sort_key == 'insert':
        stats = insertion_sort(list_n)
    elif sort_key == 'quick':
        stats = quick_sort(list_n, 0, len(list_n) - 1)

    else:
        stats = bubble_sort(list_n)
    return stats


def swap_in_list():
    # swap Boxes in listbox
    global listbox, i_pos, j_pos, i_des, j_des

    listbox.list_box[i_pos].light_flag = True
    listbox.list_box[j_pos].light_flag = True

    if i_des == j_des:
        return True

    i_done = False
    j_done = False

    if listbox.list_box[i_pos].x < i_des:
        listbox.list_box[i_pos].move_right()
    else:
        i_done = True
    if listbox.list_box[j_pos].x > j_des:
        listbox.list_box[j_pos].move_left()
    else:
        j_done = True

    if i_done and j_done:
        return True
    return False


@window.event
def on_draw():
    window.clear()
    background.draw()
    listbox.show_list()


@window.event
def on_key_press(symbol, _):
    global space_flag
    if symbol == key.SPACE:
        space_flag = True


def update(dt):
    global listbox, stats, done_swap, i_pos, j_pos, i_des, j_des, space_flag
    done_swap = swap_in_list()
    if done_swap and stats != []:
        if space_flag:
            listbox.list_box[i_pos].light_flag = False
            listbox.list_box[j_pos].light_flag = False
            st = stats.pop(0)
            listbox = ListBox(st[0], window)
            i_pos = st[1]
            j_pos = st[2]
            if st[3] < len(listbox.list_box):
                listbox.list_box[st[3]].light_flag = True
            listbox.list_box[i_pos].light_flag = True
            i_des = listbox.list_box[j_pos].x
            j_des = listbox.list_box[i_pos].x
            space_flag = False
    if stats == []:
        listbox = ListBox(list_n, window, True)
        if space_flag:
            window.close()
