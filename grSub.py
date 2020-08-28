#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:16:52 2020

@author: yushi
"""

from PIL import ImageTk

class CanvasOval:
    canvas = None
    def __init__(self, x0, y0, x1, y1, **key):
        self.id = self.canvas.create_oval(x0, y0, x1, y1, **key)
        self.canvas.tag_bind(self.id, '<1>', self.drag_start)
        self.canvas.tag_bind(self.id, '<Button1-Motion>', self.dragging)
    def drag_start(self, event):
        self.x = event.x ; self.y = event.y
    def dragging(self, event):
        self.canvas.move(self.id, event.x - self.x, event.y - self.y)
        self.x = event.x ; self.y = event.y

class Rectangle:
    canvas = None
    def __init__(self, x0, y0, x1, y1, **key):
        self.id = self.canvas.create_rectangle(x0, y0, x1, y1, **key)
        self.canvas.tag_bind(self.id, '<1>', self.drag_start)
        self.canvas.tag_bind(self.id, '<Button1-Motion>', self.dragging)
    def drag_start(self, event):
        self.x = event.x ; self.y = event.y
    def dragging(self, event):
        self.canvas.move(self.id, event.x - self.x, event.y - self.y)
        self.x = event.x ; self.y = event.y

class PhotoMove1:
    canvas = None
    def __init__(self):
        self.guru_1 = ImageTk.PhotoImage(file = 'image/logo_photo/guru_2.png')
        self.id_1 = self.canvas.create_image(800, 420, image = self.guru_1) ; self.id_1
        self.canvas.tag_bind(self.id_1, '<1>', self.drag_start)
        self.canvas.tag_bind(self.id_1, '<Button1-Motion>', self.dragging)
    def drag_start(self, event):
        self.x = event.x ; self.y = event.y
    def dragging(self, event):
        self.canvas.move(self.id_1, event.x - self.x, event.y - self.y)
        self.x = event.x ; self.y = event.y

class PhotoMove2:
    canvas = None
    def __init__(self):
        self.guru_2 = ImageTk.PhotoImage(file = 'image/logo_photo/guru_1.png')
        self.id_2 = self.canvas.create_image(800, 420, image = self.guru_2) ; self.id_2
        self.canvas.tag_bind(self.id_2, '<1>', self.drag_start)
        self.canvas.tag_bind(self.id_2, '<Button1-Motion>', self.dragging)
    def drag_start(self, event):
        self.x = event.x ; self.y = event.y
    def dragging(self, event):
        self.canvas.move(self.id_2, event.x - self.x, event.y - self.y)
        self.x = event.x ; self.y = event.y

"""
# Free Draw(practice 3)
def freeDraw(self):
    self.after_Dr()
    self.FtoDr_btn = tk.Button(self.cvs, text = 'Return', command = self.FtoDr)
    self.FtoDr_btn.place(x = 850, y = 600)
    self.num = 1
    self.gridSystem()
    self.drawing()  
def FtoDr(self):
    self.cvs.delete('all') ; self.Fbtn_dlt() ; self.design_rule() ; self.cvs.bind('<B1-Motion>', self.reset)
def Fbtn_dlt(self):
    self.FtoDr_btn.destroy() ; self.write_radio.destroy() ; self.erase_radio.destroy() ; self.clear_btn.destroy()
    self.save_btn.destroy() ; self.gridW_btn.destroy() ; self.gridH_btn.destroy() ; self.gridD_btn.destroy()
def gridSystem(self):
    self.gridW = ImageTk.PhotoImage(file = 'image/practice/gridW.png')
    self.gridW_btn = tk.Button(self.cvs, text = 'gridW', command = self.gridSW)
    self.gridW_btn.place(x = 280, y = 600)
    self.gridH = ImageTk.PhotoImage(file = 'image/practice/gridH.png')
    self.gridH_btn = tk.Button(self.cvs, text = 'gridH', command = self.gridSH)
    self.gridH_btn.place(x = 360, y = 600)
    self.gridD_btn = tk.Button(self.cvs, text = 'gridDelete', command = self.gridD)
    self.gridD_btn.place(x = 440, y = 600)
def gridSW(self):
    self.gridD()
    self.cvs.create_image(325, 325, ancho='c', image = self.gridW, tag = 'sw')
def gridSH(self):
    self.gridD()
    self.cvs.create_image(325, 325, ancho='c', image = self.gridH, tag = 'sh')
def gridD(self):
    self.cvs.delete('sw', 'sh')

def drawing(self):
    self.vr = tk.IntVar()
    self.vr.set(1)
    self.write_radio = tk.Radiobutton(text='write', variable=self.vr, value=1, command=self.change_radio)
    self.write_radio.place(x = 850, y = 200)
    self.erase_radio = tk.Radiobutton(text='erase', variable=self.vr, value=2, command=self.change_radio)
    self.erase_radio.place(x = 850, y = 250)
    self.clear_btn = tk.Button(text='clear all', command=self.clear_canvas)
    self.clear_btn.place(x = 850, y = 300)
    self.save_btn = tk.Button(text='save', command=self.save_canvas)
    self.save_btn.place(x = 850, y = 350)
    self.cvs.bind('<B1-Motion>', self.paint) ; self.cvs.bind('<ButtonRelease-1>', self.reset)
    self.old_x = None ; self.old_y = None ; self.color = 'black' ; self.eraser_on = False
    self.im = Image.new('RGB', (1050, 650), 'white')
    self.draw = ImageDraw.Draw(self.im)
def change_radio(self):
    if self.vr.get() == 1 : self.eraser_on = False
    else : self.eraser_on = True
def clear_canvas(self):
    self.cvs.delete('all')
def save_canvas(self):
    self.num += 1 ; self.cvs.postscript(file='saveimg/practice3_' + str(self.num) + '.ps', colormode='color')
def paint(self, event):
    if self.eraser_on : paint_color = 'white'
    else : paint_color = '#5f5f5f'
    if self.old_x and self.old_y:
        self.cvs.create_line(self.old_x, self.old_y, event.x, event.y, width=4.0, fill=paint_color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=paint_color, width=4)
    self.old_x = event.x ; self.old_y = event.y
def reset(self, event):
    self.old_x, self.old_y = None, None
"""
