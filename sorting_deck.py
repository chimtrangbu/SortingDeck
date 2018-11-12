#!/usr/bin/env python3

import argparse
import sys
from classes import ListBox


def parse_input():
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('N', nargs='+', type=int,
                        help='an integer for the list to sort')
    parser.add_argument('--algo', action='store', default='bubble', type=str,
                        help='specify which algorithm to use for sorting among'
                             ' [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true', default=False,
                        help='visualise the algorithm in GUI mode')
    return parser.parse_args()


def swap(list_n, i, j):
    list_n[i], list_n[j] = list_n[j], list_n[i]


def show_list(list_n):
    for e in list_n[:-1]:
        print(e, end=' ')
    print(list_n[-1])
    return


def bubble_sort(list_n):
    n = len(list_n)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if list_n[j] > list_n[j + 1]:
                swap(list_n, j, j + 1)
                show_list(list_n)
    return list_n


def insertion_sort(list_n):
    n = len(list_n)
    for index in range(1, n):
        flag = 0
        current = list_n[index]
        pos = index
        while pos > 0 and list_n[pos - 1] > current:
            list_n[pos] = list_n[pos - 1]
            pos = pos - 1
            flag = 1
        list_n[pos] = current
        if flag:
            show_list(list_n)
    return list_n


def partition(list_n, first, last):
    mid = (first + last)//2
    pivot = list_n[mid]
    print('P:', pivot)
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
            swap(list_n, i, j)
    swap(list_n, first, j)
    show_list(list_n)
    return j


def quick_sort(list_n, first, last):
    if first < last:
        p = partition(list_n, first, last)
        quick_sort(list_n, first, p - 1)
        quick_sort(list_n, p + 1, last)
    return list_n


def merge_sort(list_n):
    n = len(list_n)
    if n > 1:
        mid = n//2
        left_half = merge_sort(list_n[:mid])
        right_half = merge_sort(list_n[mid:])
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_n[k] = left_half[i]
                i = i + 1
            else:
                list_n[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            list_n[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            list_n[k] = right_half[j]
            j = j + 1
            k = k + 1
        show_list(list_n)
    return list_n


def main():
    args = parse_input()
    list_n = args.N
    sort_key = args.algo
    gui_flag = args.gui
    if gui_flag and len(list_n) > 15:
        sys.exit('Input too large')
    if not gui_flag:
        if sort_key == 'insert':
            insertion_sort(list_n)
        elif sort_key == 'quick':
            quick_sort(list_n, 0, len(list_n) - 1)
        elif sort_key == 'merge':
            merge_sort(list_n)
        else:
            bubble_sort(list_n)
    else:
        import graphic
        graphic.list_n = list_n
        graphic.sort_key = sort_key
        graphic.listbox = ListBox(graphic.list_n, graphic.window)
        graphic.stats = graphic.get_stats()
        graphic.main()


if __name__ == '__main__':
    main()
