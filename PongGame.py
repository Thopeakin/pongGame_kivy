from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
import time

Pad = ''
Score = ''
class Frame(Widget):

    def on_touch_down(self, *args):
        gett = self.ids['paddlee']
        global Pad, Score
        Pad = gett
        scor = self.ids['score']
        Score  = scor

class Ball(Widget):
    xVelocity = 6
    yVelocity = 6

    def on_touch_up(self, *args):
        Clock.unschedule(self.bUpdate)
        Clock.schedule_interval(self.bUpdate, 1/40)

    def rebound(self, paddle):
        if self.collide_widget(paddle):
            self.xVelocity *= -1
            global Score
            the = Score.text
            thhh = int(the)
            thhh += 1
            Score.text = '{}'.format(thhh)
            self.xVelocity *= 1.15
            self.yVelocity*= 1.15


    def bUpdate(self, *args):
        global Pad
        f = Frame()
        paddle = Pad
        self.rebound(paddle)
        self.pos[0] += self.xVelocity
        self.pos[1] += self.yVelocity
        if (self.pos[0] + 40) >= Window.width:
            self.xVelocity *= -1

        if(self.pos[0]) <= 0:
            Clock.unschedule(self.bUpdate)
            global Score
            Score.text = '0'
            self.pos = Window.width/2 - self.width /2, 250
            self.xVelocity = 6
            self.yVelocity = 6


        if (self.pos[1] + 40) >= Window.height or (self.pos[1]) <= 0:
            self.yVelocity *= -1

class Paddle(Widget):
    def on_touch_down(self, touch):
        self.center_y = touch.pos[1]
        if self.pos[1] <= 0:
            self.pos[1] = 0
        if (self.pos[1] + self.height) >= Window.height:
            self.pos[1] = Window.height - self.height

    def on_touch_move(self, touch):
        self.center_y = touch.pos[1]
        if self.pos[1] <= 0:
            self.pos[1] = 0
        if (self.pos[1] + (self.height)) >= Window.height:
            self.pos[1] = Window.height - self.height

Builder.load_file('PongGame.kv')

class Main(App):
    def build(self):
        return Frame()

if __name__ == '__main__':
    Main().run()
