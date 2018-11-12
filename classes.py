#!/usr/bin/env python3

import pyglet

class Box(object):
    def __init__(self, value, x, y, size, light_flag=False):
        self.value = value
        self.x = x
        self.y = y
        self.size = size
        self.light_flag = light_flag

        self.label = pyglet.text.Label(str(self.value),
                                       font_name='Times New Roman',
                                       color=(0, 0, 102, 240),
                                       font_size=self.size*0.5,
                                       x=self.x+size//2, y=self.y+size//2,
                                       anchor_x='center', anchor_y='center')

        ball = pyglet.image.load('Crys.png')
        ball.anchor_x = ball.width // 2
        ball.anchor_y = ball.height // 2
        texture = ball.get_texture()
        texture.width = size
        texture.height = size
        self.image = pyglet.sprite.Sprite(ball, self.x + ball.height//2,
                                          self.y + ball.height//2)

        light = pyglet.image.load('light3.png')
        light.anchor_x = light.width // 2
        light.anchor_y = light.height // 2
        light.get_texture().width = self.size * 1.4
        light.get_texture().height = self.size * 1.4
        self.light_on = pyglet.sprite.Sprite(light,
                                             self.x + 100*light.height//203,
                                             self.y + 100*light.height//203)

    def draw(self):
        self.image.draw()
        if self.light_flag:
            self.light_on.draw()
        self.label.draw()

    def update_box(self):
        ball = pyglet.image.load('Crys.png')
        ball.anchor_x = ball.width // 2
        ball.anchor_y = ball.height // 2
        texture = ball.get_texture()
        texture.width = self.size
        texture.height = self.size
        self.image = pyglet.sprite.Sprite(ball, self.x + ball.height//2,
                                          self.y + ball.height//2)

        light = pyglet.image.load('light3.png')
        light.anchor_x = light.width // 2
        light.anchor_y = light.height // 2
        light.get_texture().width = self.size * 1.4
        light.get_texture().height = self.size * 1.4
        self.light_on = pyglet.sprite.Sprite(light,
                                             self.x + 100*light.height//203,
                                             self.y + 100*light.height//203)

        self.label = pyglet.text.Label(str(self.value),
                                       font_name='Times New Roman',
                                       color=(0, 0, 102, 240),
                                       font_size=self.size*0.5,
                                       x=self.x+self.size//2,
                                       y=self.y+self.size//2,
                                       anchor_x='center', anchor_y='center')

    def move_up(self):
        self.y += 10
        self.update_box()

    def move_down(self):
        self.y -= 10
        self.update_box()

    def move_left(self):
        self.x -= 20
        self.update_box()

    def move_right(self):
        self.x += 20
        self.update_box()

    def move(self, des_x, des_y):
        if self.x - des_x > 10:
            self.move_left()
        elif self.x - des_x < -10:
            self.move_right()
        if self.y - des_y > 10:
            self.move_down()
        elif self.y - des_y < -10:
            self.move_up()


class ListBox(object):
    def __init__(self, list_n, window, done=False):
        self.n = len(list_n)
        dist = window.width//(self.n+1)
        self.box_size = window.width//(self.n+3)
        self.list_box = []
        for i in range(self.n):
            if done:
                self.list_box.append(Box(list_n[i], i * dist + 50, 120,
                                         self.box_size, True))
            else:
                self.list_box.append(Box(list_n[i], i * dist + 50, 120,
                                         self.box_size))

    def show_list(self):
        for i in self.list_box:
            i.draw()
