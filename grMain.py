#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:51:13 2020

@author: yushi
"""

import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image, ImageDraw
import math

from grSub import CanvasOval
from grSub import Rectangle
from grSub import PhotoMove1
from grSub import PhotoMove2


class Frame(tk.Frame):
    
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.cvs = tk.Canvas(self, width = '1050', height = '650', bg = 'white')
        self.cvs.grid(row = 0, column = 0)
        self.master.title('golden ratio')
        self.font1 = font.Font(family = 'Helvetica', size = 50, weight = 'bold')
        self.font2 = font.Font(family = 'Helvetica', size = 30)
        self.font3 = font.Font(family = 'Helvetica', size = 20)
        self.label_title = tk.Label(text = 'Golden Ratio in Logo Design',font = self.font1, fg = 'black', bg = 'white')
        self.label_title.place(x = 180, y = 250)
        self.start_btn = tk.Button(self.cvs, text = 'Start Practice', font = self.font2, command = self.design_rule)
        self.start_btn.place(x = 420, y = 350)

    def design_rule(self):
        self.label_title.destroy() ; self.start_btn.destroy()
        self.label_wGr = tk.Label(text = '黄金比についての説明', font = self.font2, fg = 'black', bg = 'white')
        self.label_exLg = tk.Label(text = 'ロゴデザインにおける黄金比の実用例', font = self.font2, fg = 'black', bg = 'white')
        self.label_prDe = tk.Label(text = '黄金比によるロゴデザインの練習', font = self.font2, fg = 'black', bg = 'white')
        self.label_logo = tk.Label(text = 'デザインルールの一覧・使用したロゴの一覧・引用元', font = self.font3, fg = 'black', bg = 'white')
        self.label_wGr.place(x=120, y=50) , self.label_exLg.place(x=120, y=150) , self.label_prDe.place(x=120, y=400), self.label_logo.place(x=120, y=500)
        self.gr1_btn = tk.Button(self.cvs, text = 'about Golden Ratio 1', command = self.gr1)
        self.gr2_btn = tk.Button(self.cvs, text = 'about Golden Ratio 2', command = self.gr2)
        self.gr3_btn = tk.Button(self.cvs, text = 'about Golden Ratio 3', command = self.gr3)
        self.gr4_btn = tk.Button(self.cvs, text = 'about Golden Ratio 4', command = self.gr4)
        self.rule1_btn = tk.Button(self.cvs, text = 'Design Rule 1', command = self.rule1)
        self.rule2_btn = tk.Button(self.cvs, text = 'Design Rule 2', command = self.rule2)
        self.rule3_btn = tk.Button(self.cvs, text = 'Design Rule 3', command = self.rule3)
        self.rule4_btn = tk.Button(self.cvs, text = 'Design Rule 4', command = self.rule4)
        self.rule5_btn = tk.Button(self.cvs, text = 'Design Rule 5', command = self.rule5)
        self.rule6_btn = tk.Button(self.cvs, text = 'Design Rule 6', command = self.rule6)
        self.rule7_btn = tk.Button(self.cvs, text = 'Design Rule 7', command = self.rule7)
        self.rule8_btn = tk.Button(self.cvs, text = 'Design Rule 8', command = self.rule8)
        self.rule9_btn = tk.Button(self.cvs, text = 'Design Rule 9', command = self.rule9)
        self.rule10_btn = tk.Button(self.cvs, text = 'Design Rule 10', command = self.rule10)
        self.rule11_btn = tk.Button(self.cvs, text = 'Design Rule 11', command = self.rule11)
        self.rule12_btn = tk.Button(self.cvs, text = 'Design Rule 12', command = self.rule12)
        self.rule13_btn = tk.Button(self.cvs, text = 'Design Rule 13', command = self.rule13)
        self.rule14_btn = tk.Button(self.cvs, text = 'Design Rule 14', command = self.rule14)
        self.rule15_btn = tk.Button(self.cvs, text = 'Design Rule 15', command = self.rule15)
        self.practice1_btn = tk.Button(self.cvs, text = 'Practice 1', command = self.Shape)
        self.practice2_btn = tk.Button(self.cvs, text = 'Practice 2', command = self.createZone)
        self.Ruleall_btn = tk.Button(self.cvs, text = 'Rule all', command = self.RuleAll)
        self.logoall_btn = tk.Button(self.cvs, text = 'logo all', command = self.logoAll)
        self.logourl_btn = tk.Button(self.cvs, text = 'logo URL', command = self.logoURL)
        self.gr1_btn.place(x=125, y=100), self.gr2_btn.place(x=325, y=100), self.gr3_btn.place(x=525, y=100), self.gr4_btn.place(x=725, y=100)
        self.rule1_btn.place(x=125, y=200), self.rule2_btn.place(x=125, y=250), self.rule3_btn.place(x=125, y=300), self.rule4_btn.place(x=125, y=350)
        self.rule5_btn.place(x=325, y=200), self.rule6_btn.place(x=325, y=250), self.rule7_btn.place(x=325, y=300), self.rule8_btn.place(x=325, y=350)
        self.rule9_btn.place(x=525, y=200), self.rule10_btn.place(x=525, y=250), self.rule11_btn.place(x=525, y=300), self.rule12_btn.place(x=525, y=350)
        self.rule13_btn.place(x=725, y=200), self.rule14_btn.place(x=725, y=250), self.rule15_btn.place(x=725, y=300)
        self.practice1_btn.place(x=125, y=450), self.practice2_btn.place(x=325, y=450)
        self.Ruleall_btn.place(x=125, y=550), self.logoall_btn.place(x=325, y=550), self.logourl_btn.place(x=525, y=550)

# after design_rule (button delete)
    def after_Dr(self):# after design_rule
        self.label_wGr.destroy() ; self.label_exLg.destroy() ; self.label_prDe.destroy() ; self.label_logo.destroy()
        self.gr_num = [self.gr1_btn, self.gr2_btn, self.gr3_btn, self.gr4_btn]
        for i in range(4):self.gr_num[i].destroy()
        self.rule_num = [self.rule1_btn, self.rule2_btn, self.rule3_btn, self.rule4_btn, self.rule5_btn,
                         self.rule6_btn, self.rule7_btn, self.rule8_btn, self.rule9_btn, self.rule10_btn,
                         self.rule11_btn, self.rule12_btn, self.rule13_btn, self.rule14_btn, self.rule15_btn,
                         self.practice1_btn, self.practice2_btn, self.Ruleall_btn, self.logoall_btn, self.logourl_btn]
        for j in range(20):self.rule_num[j].destroy()

# gr
    def to_Dr(self):# To re_Dr
        self.reDr_btn = tk.Button(self.cvs, text = 'Return', command = self.re_Dr)
        self.reDr_btn.place(x = 800, y = 600)
    def re_Dr(self):# return design_rule
        self.cvs.delete('all') ; self.reDr_btn.destroy() ; self.design_rule()
    def gr(self,i):
        self.after_Dr() ; self.to_Dr()
        self.gr_img = ImageTk.PhotoImage(file = 'image/what_gr/gr_' + str(i) + '.png')
        self.cvs.create_image(525, 300, anchor = 'c', image = self.gr_img)
    def gr1(self):self.gr(1)
    def gr2(self):self.gr(2)
    def gr3(self):self.gr(3)
    def gr4(self):self.gr(4)

# before DRA
    def beforeDRA(self):
        self.a1_btn = tk.Button(self.cvs, text = 'go', command = self.a1) ; self.a2_btn = tk.Button(self.cvs, text = 'go', command = self.a2)
        self.a3_btn = tk.Button(self.cvs, text = 'go', command = self.a3) ; self.a4_btn = tk.Button(self.cvs, text = 'go', command = self.a4)
        self.a5_btn = tk.Button(self.cvs, text = 'go', command = self.a5) ; self.a6_btn = tk.Button(self.cvs, text = 'go', command = self.a6)
        self.a7_btn = tk.Button(self.cvs, text = 'go', command = self.a7) ; self.a8_btn = tk.Button(self.cvs, text = 'go', command = self.a8)
        self.a9_btn = tk.Button(self.cvs, text = 'go', command = self.a9) ; self.a10_btn = tk.Button(self.cvs, text = 'go', command = self.a10)
        self.a11_btn = tk.Button(self.cvs, text = 'go', command = self.a11) ; self.a12_btn = tk.Button(self.cvs, text = 'go', command = self.a12)
        self.a13_btn = tk.Button(self.cvs, text = 'go', command = self.a13) ; self.a14_btn = tk.Button(self.cvs, text = 'go', command = self.a14)
        self.a15_btn = tk.Button(self.cvs, text = 'go', command = self.a15)
# DesignRuleAll
    def RuleAll(self):
        self.after_Dr() ; self.beforeDRA() ; self.DRtoDr()
        self.RuleAll_img = ImageTk.PhotoImage(file = 'image/what_gr/RuleAll.png')
        self.cvs.create_image(525, 325, anchor = 'c', image = self.RuleAll_img)
        rx1=220 ; rx2=680 ; ry=64.5 ; ry1=108 ; ry2=ry+ry1 ; ry3=ry+ry2 ; ry4=ry+ry3 ; ry5=ry+ry4 ; ry6=ry+ry5 ; ry7=ry+ry6 ; ry8=ry+ry7
        self.a1_btn.place(x=rx1, y=ry1), self.a2_btn.place(x=rx1, y=ry2), self.a3_btn.place(x=rx1, y=ry3), self.a4_btn.place(x=rx1, y=ry4)
        self.a5_btn.place(x=rx1, y=ry5), self.a6_btn.place(x=rx1, y=ry6), self.a7_btn.place(x=rx1, y=ry7), self.a8_btn.place(x=rx1, y=ry8)
        self.a9_btn.place(x=rx2, y=ry1), self.a10_btn.place(x=rx2, y=ry2), self.a11_btn.place(x=rx2, y=ry3), self.a12_btn.place(x=rx2, y=ry4)
        self.a13_btn.place(x=rx2, y=ry5), self.a14_btn.place(x=rx2, y=ry6), self.a15_btn.place(x=rx2, y=ry7)
# after DRA
    def DRtoDr(self):
        self.dtd_btn = tk.Button(self.cvs, text = 'Return', command = self.DrfromDR)
        self.dtd_btn.place(x = 800, y = 600)
    def DrfromDR(self):
        self.drAll_num = [self.a1_btn, self.a2_btn, self.a3_btn, self.a4_btn, self.a5_btn, self.a6_btn, self.a7_btn, self.a8_btn,
                          self.a9_btn, self.a10_btn, self.a11_btn, self.a12_btn, self.a13_btn, self.a14_btn, self.a15_btn, self.dtd_btn]
        for i in range(16):self.drAll_num[i].destroy()
        self.cvs.delete('all') ; self.design_rule()
# to Rule from All
    def a1(self) : self.DrfromDR() ; self.rule1()
    def a2(self) : self.DrfromDR() ; self.rule2()
    def a3(self) : self.DrfromDR() ; self.rule3()
    def a4(self) : self.DrfromDR() ; self.rule4()
    def a5(self) : self.DrfromDR() ; self.rule5()
    def a6(self) : self.DrfromDR() ; self.rule6()
    def a7(self) : self.DrfromDR() ; self.rule7()
    def a8(self) : self.DrfromDR() ; self.rule8()
    def a9(self) : self.DrfromDR() ; self.rule9()
    def a10(self) : self.DrfromDR() ; self.rule10()
    def a11(self) : self.DrfromDR() ; self.rule11()
    def a12(self) : self.DrfromDR() ; self.rule12()
    def a13(self) : self.DrfromDR() ; self.rule13()
    def a14(self) : self.DrfromDR() ; self.rule14()
    def a15(self) : self.DrfromDR() ; self.rule15()

# logoAll
    def logoAll(self):
        self.after_Dr()
        self.logoall_img = ImageTk.PhotoImage(file = 'image/what_gr/logoall.png')
        self.cvs.create_image(525, 325, anchor = 'c', image = self.logoall_img)
        self.to_Dr()

# logoURL
    def logoURL(self):
        self.after_Dr()
        self.logourl_img = ImageTk.PhotoImage(file = 'image/what_gr/logoURL.png')
        self.cvs.create_image(525, 325, anchor = 'c', image = self.logourl_img)
        self.to_Dr()

# before after
    def BeAf(self):
        self.before_btn.place(x = 600, y = 600) ; self.after_btn.place(x = 650, y = 600)
    def before(self, i, j):
        self.cvs.delete('all')
        self.before_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j)  + '.png')
        self.cvs.create_image(525, 300, anchor = 'c', image = self.before_img)
    def after(self, i, j):
        self.cvs.delete('all')
        self.after_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '_s' + '.png')
        self.cvs.create_image(525, 300, anchor = 'c', image = self.after_img)
    def ba_dlt(self):
        self.cvs.delete('all') ; self.before_btn.destroy() ; self.after_btn.destroy()

# rule1
    def rule1(self):
        self.after_Dr()
        self.rule1_1btn = tk.Button(self.cvs, text = '1. MGV', command = self.rule1_1)
        self.rule1_2btn = tk.Button(self.cvs, text = '2. Conservation International', command = self.rule1_2)
        self.rule1_3btn = tk.Button(self.cvs, text = '3. CRAFTMAN UNION', command = self.rule1_3)
        self.rule1_4btn = tk.Button(self.cvs, text = '4. 中央大学', command = self.rule1_4)
        self.rule1_5btn = tk.Button(self.cvs, text = '5. Azure Spa Hotel', command = self.rule1_5)
        self.rule1_6btn = tk.Button(self.cvs, text = '6. Ontic', command = self.rule1_6)
        self.rule1_7btn = tk.Button(self.cvs, text = '7. 東京都美術館', command = self.rule1_7)
        self.rule1_1btn.place(x = 100, y = 200), self.rule1_2btn.place(x = 100, y = 300)
        self.rule1_3btn.place(x = 100, y = 400), self.rule1_4btn.place(x = 100, y = 500)
        self.rule1_5btn.place(x = 350, y = 200), self.rule1_6btn.place(x = 350, y = 300)
        self.rule1_7btn.place(x = 350, y = 400)
        self.label1 = tk.Label(text = 'シンボルマークに黄金比率', font = self.font2, fg = 'black', bg = 'white')
        self.label1.place(x = 100, y = 50)
        self.R1toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R1toDr)
        self.R1toDr_btn.place(x = 800, y = 600)      
    def R1btn_dlt(self):
        self.label1.destroy()
        self.rule1_num = [self.rule1_1btn, self.rule1_2btn, self.rule1_3btn, self.rule1_4btn,
                          self.rule1_5btn, self.rule1_6btn, self.rule1_7btn]
        for i in range(7):self.rule1_num[i].destroy()
    def R1toDr(self):
        self.R1toDr_btn.destroy() ; self.R1btn_dlt() ; self.design_rule()
    def to_R1(self):
        self.reR1_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R1)
        self.reR1_btn.place(x = 800, y =600)
    def re_R1(self):
        self.ba_dlt() ; self.reR1_btn.destroy() ; self.rule1()
    def rule1_pack(self):
        self.R1toDr_btn.destroy() ; self.R1btn_dlt() ; self.BeAf() ; self.to_R1()
# rule1_1
    def rule1_1(self):
        self.before(1, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_1)
        self.rule1_pack()
    def before1_1(self):
        self.before(1, 1)
    def after1_1(self):
        self.after(1, 1)
# rule1_2
    def rule1_2(self):
        self.before(1, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_2)
        self.rule1_pack()
    def before1_2(self):
        self.before(1, 2)
    def after1_2(self):
        self.after(1, 2)
# rule1_3
    def rule1_3(self):
        self.before(1, 3)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_3)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_3)
        self.rule1_pack()
    def before1_3(self):
        self.before(1, 3)
    def after1_3(self):
        self.after(1, 3)
# rule1_4
    def rule1_4(self):
        self.before(1, 4)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_4)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_4)
        self.rule1_pack()
    def before1_4(self):
        self.before(1, 4)
    def after1_4(self):
        self.after(1, 4)
# rule1_5
    def rule1_5(self):
        self.before(1, 5)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_5)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_5)
        self.rule1_pack()
    def before1_5(self):
        self.before(1, 5)
    def after1_5(self):
        self.after(1, 5)
# rule1_6
    def rule1_6(self):
        self.before(1, 6)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_6)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_6)
        self.rule1_pack()
    def before1_6(self):
        self.before(1, 6)
    def after1_6(self):
        self.after(1, 6)
# rule1_7
    def rule1_7(self):
        self.before(1, 7)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before1_7)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after1_7)
        self.rule1_pack()
    def before1_7(self):
        self.before(1, 7)
    def after1_7(self):
        self.after(1, 7)

# rule2
    def rule2(self):
        self.after_Dr()
        self.rule2_1btn = tk.Button(self.cvs, text = '1. National Geographic', command = self.rule2_1)
        self.rule2_2btn = tk.Button(self.cvs, text = '2. Towson University', command = self.rule2_2)
        self.rule2_3btn = tk.Button(self.cvs, text = '3. Hiway', command = self.rule2_3)
        self.rule2_1btn.place(x = 100, y = 200), self.rule2_2btn.place(x = 100, y = 300), self.rule2_3btn.place(x = 100, y = 400)
        self.label2 = tk.Label(text = 'シンボルマーク、ロゴタイプのアスペクト比に黄金比率', font = self.font2, fg = 'black', bg = 'white')
        self.label2.place(x = 100, y = 50)
        self.R2toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R2toDr)
        self.R2toDr_btn.place(x = 800, y = 600)        
    def R2btn_dlt(self):
        self.label2.destroy()
        self.rule2_num = [self.rule2_1btn, self.rule2_2btn, self.rule2_3btn]
        for i in range(3):self.rule2_num[i].destroy()
    def R2toDr(self):
        self.R2toDr_btn.destroy() ; self.R2btn_dlt() ; self.design_rule()
    def to_R2(self):
        self.reR2_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R2)
        self.reR2_btn.place(x = 800, y =600)
    def re_R2(self):
        self.ba_dlt() ; self.reR2_btn.destroy() ; self.rule2()
    def rule2_pack(self):
        self.R2toDr_btn.destroy() ; self.R2btn_dlt() ; self.BeAf() ; self.to_R2()
# rule2_1
    def rule2_1(self):
        self.before(2, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before2_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after2_1)
        self.rule2_pack()
    def before2_1(self):
        self.before(2, 1)
    def after2_1(self):
        self.after(2, 1)
# rule2_2
    def rule2_2(self):
        self.before(2, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before2_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after2_2)
        self.rule2_pack()
    def before2_2(self):
        self.before(2, 2)
    def after2_2(self):
        self.after(2, 2)
# rule2_3
    def rule2_3(self):
        self.before(2, 3)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before2_3)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after2_3)
        self.rule2_pack()
    def before2_3(self):
        self.before(2, 3)
    def after2_3(self):
        self.after(2, 3)

# rule3
    def rule3(self):
        self.after_Dr()
        self.rule3_1btn = tk.Button(self.cvs, text = '1. EQ Office', command = self.rule3_1)
        self.rule3_2btn = tk.Button(self.cvs, text = '2. Qwant', command = self.rule3_2)
        self.rule3_3btn = tk.Button(self.cvs, text = '3. Medscan', command = self.rule3_3)
        self.rule3_4btn = tk.Button(self.cvs, text = '4. Midco', command = self.rule3_4)
        self.rule3_1btn.place(x = 100, y = 200), self.rule3_2btn.place(x = 100, y = 300), 
        self.rule3_3btn.place(x = 100, y = 400), self.rule3_4btn.place(x = 100, y = 500)
        self.label3 = tk.Label(text = 'シンボルマークとロゴタイプが黄金比率の関係', font = self.font2, fg = 'black', bg = 'white')
        self.label3.place(x = 100, y = 50)
        self.R3toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R3toDr)
        self.R3toDr_btn.place(x = 800, y = 600)
    def R3btn_dlt(self):
        self.label3.destroy()
        self.rule3_num = [self.rule3_1btn, self.rule3_2btn, self.rule3_3btn, self.rule3_4btn]
        for i in range(4):self.rule3_num[i].destroy()
    def R3toDr(self):
        self.R3toDr_btn.destroy() ; self.R3btn_dlt() ; self.design_rule()
    def to_R3(self):
        self.reR3_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R3)
        self.reR3_btn.place(x = 800, y =600)
    def re_R3(self):
        self.ba_dlt() ; self.reR3_btn.destroy() ; self.rule3()
    def rule3_pack(self):
        self.R3toDr_btn.destroy() ; self.R3btn_dlt() ; self.BeAf() ; self.to_R3()
# rule3_1
    def rule3_1(self):
        self.before(3, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before3_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after3_1)
        self.rule3_pack()
    def before3_1(self):
        self.before(3, 1)
    def after3_1(self):
        self.after(3, 1)
# rule3_2
    def rule3_2(self):
        self.before(3, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before3_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after3_2)
        self.rule3_pack()
    def before3_2(self):
        self.before(3, 2)
    def after3_2(self):
        self.after(3, 2)
# rule3_3
    def rule3_3(self):
        self.before(3, 3)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before3_3)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after3_3)
        self.rule3_pack()
    def before3_3(self):
        self.before(3, 3)
    def after3_3(self):
        self.after(3, 3)
# rule3_4
    def rule3_4(self):
        self.before(3, 4)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before3_4)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after3_4)
        self.rule3_pack()
    def before3_4(self):
        self.before(3, 4)
    def after3_4(self):
        self.after(3, 4)

# rule4
    def rule4(self):
        self.after_Dr()
        self.rule4_1btn = tk.Button(self.cvs, text = '1. Mike Kelley', command = self.rule4_1)
        self.rule4_2btn = tk.Button(self.cvs, text = '2. 台南市美術館', command = self.rule4_2)
        self.rule4_3btn = tk.Button(self.cvs, text = '3. 長浜クリニック', command = self.rule4_3)
        self.rule4_4btn = tk.Button(self.cvs, text = '4. Matterfund', command = self.rule4_4)
        self.rule4_5btn = tk.Button(self.cvs, text = '5. MasterCard', command = self.rule4_5)
        self.rule4_1btn.place(x = 100, y = 200), self.rule4_2btn.place(x = 100, y = 300), 
        self.rule4_3btn.place(x = 100, y = 400), self.rule4_4btn.place(x = 100, y = 500), self.rule4_5btn.place(x = 350, y = 200)
        self.label4 = tk.Label(text = '黄金長方形による要素の位置決定', font = self.font2, fg = 'black', bg = 'white')
        self.label4.place(x = 100, y = 50)
        self.R4toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R4toDr)
        self.R4toDr_btn.place(x = 800, y = 600)
    def R4btn_dlt(self):
        self.label4.destroy()
        self.rule4_num = [self.rule4_1btn, self.rule4_2btn, self.rule4_3btn, self.rule4_4btn, self.rule4_5btn]
        for i in range(5):self.rule4_num[i].destroy()
    def R4toDr(self):
        self.R4toDr_btn.destroy() ; self.R4btn_dlt() ; self.design_rule()
    def to_R4(self):
        self.reR4_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R4)
        self.reR4_btn.place(x = 800, y =600)
    def re_R4(self):
        self.ba_dlt() ; self.reR4_btn.destroy() ; self.rule4()
    def rule4_pack(self):
        self.R4toDr_btn.destroy() ; self.R4btn_dlt() ; self.BeAf() ; self.to_R4()
# rule4_1
    def rule4_1(self):
        self.before(4, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before4_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after4_1)
        self.rule4_pack()
    def before4_1(self):
        self.before(4, 1)
    def after4_1(self):
        self.after(4, 1)
# rule4_2
    def rule4_2(self):
        self.before(4, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before4_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after4_2)
        self.rule4_pack()
    def before4_2(self):
        self.before(4, 2)
    def after4_2(self):
        self.after(4, 2)
# rule4_3
    def rule4_3(self):
        self.before(4, 3)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before4_3)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after4_3)
        self.rule4_pack()
    def before4_3(self):
        self.before(4, 3)
    def after4_3(self):
        self.after(4, 3)
# rule4_4
    def rule4_4(self):
        self.before(4, 4)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before4_4)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after4_4)
        self.rule4_pack()
    def before4_4(self):
        self.before(4, 4)
    def after4_4(self):
        self.after(4, 4)
# rule4_5
    def rule4_5(self):
        self.before(4, 5)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before4_5)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after4_5)
        self.rule4_pack()
    def before4_5(self):
        self.before(4, 5)
    def after4_5(self):
        self.after(4, 5)

# rule5
    def rule5(self):
        self.after_Dr()
        self.rule5_1btn = tk.Button(self.cvs, text = '1. Yoga Id', command = self.rule5_1)
        self.rule5_2btn = tk.Button(self.cvs, text = '2. Old Chatham Sheepherding Company', command = self.rule5_2)
        self.rule5_3btn = tk.Button(self.cvs, text = '3. Cactus @ Alhambra', command = self.rule5_3)
        self.rule5_4btn = tk.Button(self.cvs, text = '4. Vitali Bosch', command = self.rule5_4)
        self.rule5_1btn.place(x = 100, y = 200), self.rule5_2btn.place(x = 100, y = 300), 
        self.rule5_3btn.place(x = 100, y = 400), self.rule5_4btn.place(x = 100, y = 500)
        self.label5 = tk.Label(text = '黄金長方形による要素の量の決定', font = self.font2, fg = 'black', bg = 'white')
        self.label5.place(x = 100, y = 50)
        self.R5toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R5toDr)
        self.R5toDr_btn.place(x = 800, y = 600)
    def R5btn_dlt(self):
        self.label5.destroy()
        self.rule5_num = [self.rule5_1btn, self.rule5_2btn, self.rule5_3btn, self.rule5_4btn]
        for i in range(4):self.rule5_num[i].destroy()
    def R5toDr(self):
        self.R5toDr_btn.destroy() ; self.R5btn_dlt() ; self.design_rule()
    def to_R5(self):
        self.reR5_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R5)
        self.reR5_btn.place(x = 800, y =600)
    def re_R5(self):
        self.ba_dlt() ; self.reR5_btn.destroy() ; self.rule5()
    def rule5_pack(self):
        self.R5toDr_btn.destroy() ; self.R5btn_dlt() ; self.BeAf() ; self.to_R5()
# rule5_1
    def rule5_1(self):
        self.before(5, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before5_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after5_1)
        self.rule5_pack()
    def before5_1(self):
        self.before(5, 1)
    def after5_1(self):
        self.after(5, 1)
# rule5_2
    def rule5_2(self):
        self.before(5, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before5_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after5_2)
        self.rule5_pack()
    def before5_2(self):
        self.before(5, 2)
    def after5_2(self):
        self.after(5, 2)
# rule5_3
    def rule5_3(self):
        self.before(5, 3)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before5_3)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after5_3)
        self.rule5_pack()
    def before5_3(self):
        self.before(5, 3)
    def after5_3(self):
        self.after(5, 3)
# rule5_4
    def rule5_4(self):
        self.before(5, 4)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before5_4)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after5_4)
        self.rule5_pack()
    def before5_4(self):
        self.before(5, 4)
    def after5_4(self):
        self.after(5, 4)

# rule6
    def rule6(self):
        self.after_Dr()
        self.rule6_1btn = tk.Button(self.cvs, text = '1. Ipek Koray Design', command = self.rule6_1)
        self.rule6_1btn.place(x = 100, y = 200)
        self.label6 = tk.Label(text = '黄金螺旋によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label6.place(x = 100, y = 50)
        self.R6toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R6toDr)
        self.R6toDr_btn.place(x = 800, y = 600)
    def R6btn_dlt(self):
        self.label6.destroy() ; self.rule6_1btn.destroy()
    def R6toDr(self):
        self.R6toDr_btn.destroy() ; self.R6btn_dlt() ; self.design_rule()
    def to_R6(self):
        self.reR6_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R6)
        self.reR6_btn.place(x = 800, y =600)
    def re_R6(self):
        self.ba_dlt() ; self.reR6_btn.destroy() ; self.rule6()
    def rule6_pack(self):
        self.R6toDr_btn.destroy() ; self.R6btn_dlt() ; self.BeAf() ; self.to_R6()
# rule6_1
    def rule6_1(self):
        self.before(6, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before6_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after6_1)
        self.rule6_pack()
    def before6_1(self):
        self.before(6, 1)
    def after6_1(self):
        self.after(6, 1)

# rule7
    def rule7(self):
        self.after_Dr()
        self.rule7_1btn = tk.Button(self.cvs, text = '1. Sail', command = self.rule7_1)
        self.rule7_1btn.place(x = 100, y = 200)
        self.label7 = tk.Label(text = '黄金円によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label7.place(x = 100, y = 50)
        self.R7toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R7toDr)
        self.R7toDr_btn.place(x = 800, y = 600)
    def R7btn_dlt(self):
        self.label7.destroy() ; self.rule7_1btn.destroy()
    def R7toDr(self):
        self.R7toDr_btn.destroy() ; self.R7btn_dlt() ; self.design_rule()
    def to_R7(self):
        self.reR7_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R7)
        self.reR7_btn.place(x = 800, y =600)
    def re_R7(self):
        self.ba_dlt() ; self.reR7_btn.destroy() ; self.rule7()
    def rule7_pack(self):
        self.R7toDr_btn.destroy() ; self.R7btn_dlt() ; self.BeAf() ; self.to_R7()
# rule7_1
    def rule7_1(self):
        self.before(7, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before7_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after7_1)
        self.rule7_pack()
    def before7_1(self):
        self.before(7, 1)
    def after7_1(self):
        self.after(7, 1)

# rule8
    def rule8(self):
        self.after_Dr()
        self.rule8_1btn = tk.Button(self.cvs, text = '1. Arthur Gall', command = self.rule8_1)
        self.rule8_1btn.place(x = 100, y = 200)
        self.label8 = tk.Label(text = '黄金正方形によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label8.place(x = 100, y = 50)
        self.R8toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R8toDr)
        self.R8toDr_btn.place(x = 800, y = 600)
    def R8btn_dlt(self):
        self.label8.destroy() ; self.rule8_1btn.destroy()
    def R8toDr(self):
        self.R8toDr_btn.destroy() ; self.R8btn_dlt() ; self.design_rule()
    def to_R8(self):
        self.reR8_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R8)
        self.reR8_btn.place(x = 800, y =600)
    def re_R8(self):
        self.ba_dlt() ; self.reR8_btn.destroy() ; self.rule8()
    def rule8_pack(self):
        self.R8toDr_btn.destroy() ; self.R8btn_dlt() ; self.BeAf() ; self.to_R8()
# rule8_1
    def rule8_1(self):
        self.before(8, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before8_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after8_1)
        self.rule8_pack()
    def before8_1(self):
        self.before(8, 1)
    def after8_1(self):
        self.after(8, 1)

# rule9
    def rule9(self):
        self.after_Dr()
        self.rule9_1btn = tk.Button(self.cvs, text = '1. Muram', command = self.rule9_1)
        self.rule9_1btn.place(x = 100, y = 200)
        self.label9 = tk.Label(text = '黄金長方形の応用によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label9.place(x = 100, y = 50)
        self.R9toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R9toDr)
        self.R9toDr_btn.place(x = 800, y = 600)
    def R9btn_dlt(self):
        self.label9.destroy() ; self.rule9_1btn.destroy()
    def R9toDr(self):
        self.R9toDr_btn.destroy() ; self.R9btn_dlt() ; self.design_rule()
    def to_R9(self):
        self.reR9_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R9)
        self.reR9_btn.place(x = 800, y =600)
    def re_R9(self):
        self.ba_dlt() ; self.reR9_btn.destroy() ; self.rule9()
    def rule9_pack(self):
        self.R9toDr_btn.destroy() ; self.R9btn_dlt() ; self.BeAf() ; self.to_R9()
# rule9_1
    def rule9_1(self):
        self.before(9, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before9_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after9_1)
        self.rule9_pack()
    def before9_1(self):
        self.before(9, 1)
    def after9_1(self):
        self.after(9, 1)

# rule10
    def rule10(self):
        self.after_Dr()
        self.rule10_1btn = tk.Button(self.cvs, text = '1. Artland', command = self.rule10_1)
        self.rule10_2btn = tk.Button(self.cvs, text = '2. Dovetail Custom Nurseries', command = self.rule10_2)
        self.rule10_1btn.place(x = 100, y = 200), self.rule10_2btn.place(x = 100, y = 300)
        self.label10 = tk.Label(text = '黄金長方形と黄金螺旋の組み合わせ', font = self.font2, fg = 'black', bg = 'white')
        self.label10.place(x = 100, y = 50)
        self.R10toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R10toDr)
        self.R10toDr_btn.place(x = 800, y = 600)
    def R10btn_dlt(self):
        self.label10.destroy()
        self.rule10_num = [self.rule10_1btn, self.rule10_2btn]
        for i in range(2):self.rule10_num[i].destroy()
    def R10toDr(self):
        self.R10toDr_btn.destroy() ; self.R10btn_dlt() ; self.design_rule()
    def to_R10(self):
        self.reR10_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R10)
        self.reR10_btn.place(x = 800, y =600)
    def re_R10(self):
        self.ba_dlt() ; self.reR10_btn.destroy() ; self.rule10()
    def rule10_pack(self):
        self.R10toDr_btn.destroy() ; self.R10btn_dlt() ; self.BeAf() ; self.to_R10()
# rule10_1
    def rule10_1(self):
        self.before(10, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before10_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after10_1)
        self.rule10_pack()
    def before10_1(self):
        self.before(10, 1)
    def after10_1(self):
        self.after(10, 1)
# rule10_2
    def rule10_2(self):
        self.before(10, 2)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before10_2)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after10_2)
        self.rule10_pack()
    def before10_2(self):
        self.before(10, 2)
    def after10_2(self):
        self.after(10, 2)

# rule11
    def rule11(self):
        self.after_Dr()
        self.rule11_1btn = tk.Button(self.cvs, text = '1. Andrea Pedretti', command = self.rule11_1)
        self.rule11_1btn.place(x = 100, y = 200)
        self.label11 = tk.Label(text = '黄金長方形と黄金円の組み合わせ', font = self.font2, fg = 'black', bg = 'white')
        self.label11.place(x = 100, y = 50)
        self.R11toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R11toDr)
        self.R11toDr_btn.place(x = 800, y = 600)
    def R11btn_dlt(self):
        self.label11.destroy() ; self.rule11_1btn.destroy()
    def R11toDr(self):
        self.R11toDr_btn.destroy() ; self.R11btn_dlt() ; self.design_rule()
    def to_R11(self):
        self.reR11_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R11)
        self.reR11_btn.place(x = 800, y =600)
    def re_R11(self):
        self.ba_dlt() ; self.reR11_btn.destroy() ; self.rule11()
    def rule11_pack(self):
        self.R11toDr_btn.destroy() ; self.R11btn_dlt() ; self.BeAf() ; self.to_R11()
# rule11_1
    def rule11_1(self):
        self.before(11, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before11_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after11_1)
        self.rule11_pack()
    def before11_1(self):
        self.before(11, 1)
    def after11_1(self):
        self.after(11, 1)

# rule12
    def rule12(self):
        self.after_Dr()
        self.rule12_1btn = tk.Button(self.cvs, text = '1. Motherbird', command = self.rule12_1)
        self.rule12_1btn.place(x = 100, y = 200)
        self.label12 = tk.Label(text = '黄金円の応用によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label12.place(x = 100, y = 50)
        self.R12toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R12toDr)
        self.R12toDr_btn.place(x = 800, y = 600)
    def R12btn_dlt(self):
        self.label12.destroy() ; self.rule12_1btn.destroy()
    def R12toDr(self):
        self.R12toDr_btn.destroy() ; self.R12btn_dlt() ; self.design_rule()
    def to_R12(self):
        self.reR12_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R12)
        self.reR12_btn.place(x = 800, y =600)
    def re_R12(self):
        self.ba_dlt() ; self.reR12_btn.destroy() ; self.rule12()
    def rule12_pack(self):
        self.R12toDr_btn.destroy() ; self.R12btn_dlt() ; self.BeAf() ; self.to_R12()
# rule12_1
    def rule12_1(self):
        self.before(12, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before12_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after12_1)
        self.rule12_pack()
    def before12_1(self):
        self.before(12, 1)
    def after12_1(self):
        self.after(12, 1)

# rule13
    def rule13(self):
        self.after_Dr()
        self.rule13_1btn = tk.Button(self.cvs, text = '1. GHEU', command = self.rule13_1)
        self.rule13_1btn.place(x = 100, y = 200)
        self.label13 = tk.Label(text = '黄金三角形によるロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label13.place(x = 100, y = 50)
        self.R13toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R13toDr)
        self.R13toDr_btn.place(x = 800, y = 600)
    def R13btn_dlt(self):
        self.label13.destroy() ; self.rule13_1btn.destroy()
    def R13toDr(self):
        self.R13toDr_btn.destroy() ; self.R13btn_dlt() ; self.design_rule()
    def to_R13(self):
        self.reR13_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R13)
        self.reR13_btn.place(x = 800, y =600)
    def re_R13(self):
        self.ba_dlt() ; self.reR13_btn.destroy() ; self.rule13()
    def rule13_pack(self):
        self.R13toDr_btn.destroy() ; self.R13btn_dlt() ; self.BeAf() ; self.to_R13()
# rule13_1
    def rule13_1(self):
        self.before(13, 1)
        self.before_btn = tk.Button(self.cvs, text = 'Origin', command = self.before13_1)
        self.after_btn = tk.Button(self.cvs, text = 'Analyze', command = self.after13_1)
        self.rule13_pack()
    def before13_1(self):
        self.before(13, 1)
    def after13_1(self):
        self.after(13, 1)
#-----------------------------------------------------------------------------
# origin create
    def OrCr(self):
        self.create_dlt_btn.place(x = 250, y = 600)
        self.create_btn.place(x = 250, y = 600)
    def origin(self, i, j):
        self.origin_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '.png')
        self.cvs.create_image(300, 300, anchor = 'c', image = self.origin_img)
    def create(self, i, j):
        self.create_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '_s' + '.png')
        self.cvs.create_image(300, 300, anchor = 'c', image = self.create_img, tag = 'cr')
    def create_dlt(self):
        self.cvs.delete('cr') ; self.create_dlt_btn.lower()
    def oc_dlt(self):
        self.cvs.delete('all') ; self.create_dlt_btn.destroy() ; self.create_btn.destroy()
#-----------------------------------------------------------------------------
    def NBpack(self):
        self.count = 0
        self.hideB_label = tk.Label(text = 'xxxx', fg='white', bg='white') ; self.hideB_label.place(x=680, y=600)
        self.hideN_label = tk.Label(text = 'xxxx', fg='white', bg='white') ; self.hideN_label.place(x=730, y=600)
        self.Next() ; self.Back()  
    def Next(self):
        self.hideN_label.lower()
        self.next_btn = tk.Button(self.cvs, text = 'next', command = self.NextImage)
        self.next_btn.place(x=730, y=600)
    def Back(self):
        self.back_btn = tk.Button(self.cvs, text = 'back', command = self.BackImage)
        self.back_btn.place(x=680, y=600)
    def NextImage(self):
        self.count += 1
        i = self.count
        self.cvs.delete('imgs'+str(i-1))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[i], tag ='imgs'+str(i))
        if self.count != 0 : self.hideB_label.lower()
        if self.num == 14 and self.count == 14 : self.hideN_label.lift()
        if self.num == 7 and self.count == 7 : self.hideN_label.lift()
        if self.num == 24 and self.count == 24 : self.hideN_label.lift()
    def BackImage(self):
        if self.num == 14 and self.count == 14 : self.hideN_label.lower()
        if self.num == 7 and self.count == 7 : self.hideN_label.lower()
        if self.num == 24 and self.count == 24 : self.hideN_label.lower()
        self.count -= 1
        j = self.count
        self.cvs.delete('imgs'+str(j+1))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[j], tag ='imgs'+str(j))
        if self.count == 0 : self.hideB_label.lift()
#-----------------------------------------------------------------------------
    def Twitter(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(15):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/twEx/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 14 ; self.NBpack()
    def Fire(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7]
        for i in range(8):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/fiEx/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 7 ; self.NBpack()
    def Free(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        for i in range(25):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/frEx/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 24 ; self.NBpack()
    def Apple(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(15):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/apEx/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 300, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 14 ; self.NBpack()
#-----------------------------------------------------------------------------
# rule14
    def rule14(self):
        self.after_Dr()
        self.rule14_1btn = tk.Button(self.cvs, text = '1. Twitter', command = self.rule14_1)
        self.rule14_2btn = tk.Button(self.cvs, text = '2. UPC', command = self.rule14_2)
        self.rule14_3btn = tk.Button(self.cvs, text = '3. Free Creative Studio', command = self.rule14_3)
        self.rule14_1btn.place(x = 100, y = 200), self.rule14_2btn.place(x = 100, y = 300), self.rule14_3btn.place(x = 100, y = 400)
        self.label14 = tk.Label(text = '黄金円によってシェイプを形成したロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label14.place(x = 100, y = 50)
        self.R14toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R14toDr)
        self.R14toDr_btn.place(x = 800, y = 600)
    def R14btn_dlt(self):
        self.label14.destroy()
        self.rule14_num = [self.rule14_1btn, self.rule14_2btn, self.rule14_3btn]
        for i in range(3):self.rule14_num[i].destroy()
    def R14toDr(self):
        self.R14toDr_btn.destroy() ; self.R14btn_dlt() ; self.design_rule()
    def to_R14(self):
        self.reR14_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R14)
        self.reR14_btn.place(x = 800, y =600)
    def re_R14(self):
        self.oc_dlt() ; self.reR14_btn.destroy() ; self.rule14() ; self.labelRe14.destroy()
        self.hideB_label.destroy() ; self.hideN_label.destroy() ; self.next_btn.destroy() ; self.back_btn.destroy()
    def rule14_pack(self):
        self.R14toDr_btn.destroy() ; self.R14btn_dlt() ; self.OrCr() ; self.to_R14() ; self.create_btn.lift()
        self.labelRe14 = tk.Label(text = '黄金円によってシェイプを形成したロゴデザイン', font = self.font3, fg = 'black', bg = 'white')
        self.labelRe14.place(x =100, y = 30)
# rule14_1
    def rule14_1(self):
        self.origin(14, 1)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.create14_1)
        self.rule14_pack()
        self.Twitter()
    def create14_1(self):
        self.create(14, 1) ; self.create_btn.lower()
# rule14_2
    def rule14_2(self):
        self.origin(14, 2)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.create14_2)
        self.rule14_pack()
        self.Fire()
    def create14_2(self):
        self.create(14, 2) ; self.create_btn.lower()
# rule14_3
    def rule14_3(self):
        self.origin(14, 3)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.create14_3)
        self.rule14_pack()
        self.Free()
    def create14_3(self):
        self.create(14, 3) ; self.create_btn.lower()

# rule15
    def rule15(self):
        self.after_Dr()
        self.rule15_1btn = tk.Button(self.cvs, text = '1. Apple', command = self.rule15_1)
        self.rule15_1btn.place(x = 100, y = 200)
        self.label15 = tk.Label(text = '黄金円と黄金螺旋によってシェイプを形成したロゴデザイン', font = self.font2, fg = 'black', bg = 'white')
        self.label15.place(x = 100, y = 50)
        self.R15toDr_btn = tk.Button(self.cvs, text = 'Return', command = self.R15toDr)
        self.R15toDr_btn.place(x = 800, y = 600)
    def R15btn_dlt(self):
        self.label15.destroy()
        self.rule15_1btn.destroy()
    def R15toDr(self):
        self.R15toDr_btn.destroy() ; self.R15btn_dlt() ; self.design_rule()
    def to_R15(self):
        self.reR15_btn = tk.Button(self.cvs, text = 'Return', command = self.re_R15)
        self.reR15_btn.place(x = 800, y =600)
    def re_R15(self):
        self.oc_dlt() ; self.reR15_btn.destroy() ; self.rule15() ; self.labelRe15.destroy()
        self.hideB_label.destroy() ; self.hideN_label.destroy() ; self.next_btn.destroy() ; self.back_btn.destroy()
    def rule15_pack(self):
        self.R15toDr_btn.destroy() ; self.R15btn_dlt() ; self.OrCr() ; self.to_R15() ; self.create_btn.lift()
        self.labelRe15 = tk.Label(text = '黄金円と黄金螺旋によってシェイプを形成したロゴデザイン', font = self.font3, fg = 'black', bg = 'white')
        self.labelRe15.place(x =100, y = 30)
# rule15_1
    def rule15_1(self):
        self.origin(15, 1)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.create15_1)
        self.rule15_pack()
        self.Apple()
    def create15_1(self):
        self.create(15, 1) ; self.create_btn.lower()
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    def ReNBpack(self):
        self.count = 0
        self.hideB_label = tk.Label(text = 'xxxx', fg='white', bg='white') ; self.hideB_label.place(x=850, y=200)
        self.hideN_label = tk.Label(text = 'xxxx', fg='white', bg='white') ; self.hideN_label.place(x=900, y=200)
        self.ReNext() ; self.ReBack()  
    def ReNext(self):
        self.hideN_label.lower()
        self.next_btn = tk.Button(self.cvs, text = 'next', command = self.ReNextImage)
        self.next_btn.place(x=900, y=200)
    def ReBack(self):
        self.back_btn = tk.Button(self.cvs, text = 'back', command = self.ReBackImage)
        self.back_btn.place(x=850, y=200)
    def ReNextImage(self):
        self.count += 1
        i = self.count
        self.cvs.delete('imgs'+str(i-1))
        self.cvs.create_image(725, 130, anchor = 'c', image = self.imgs[i], tag ='imgs'+str(i))
        if self.count != 0 : self.hideB_label.lower()
        if self.num == 14 and self.count == 14 : self.hideN_label.lift()
        if self.num == 7 and self.count == 7 : self.hideN_label.lift()
        if self.num == 24 and self.count == 24 : self.hideN_label.lift()
    def ReBackImage(self):
        if self.num == 14 and self.count == 14 : self.hideN_label.lower()
        if self.num == 7 and self.count == 7 : self.hideN_label.lower()
        if self.num == 24 and self.count == 24 : self.hideN_label.lower()
        self.count -= 1
        j = self.count
        self.cvs.delete('imgs'+str(j+1))
        self.cvs.create_image(725,130, anchor = 'c', image = self.imgs[j], tag ='imgs'+str(j))
        if self.count == 0 : self.hideB_label.lift()
#-----------------------------------------------------------------------------
    def ReTwitter(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(15):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/twPr/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 130, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 14 ; self.ReNBpack()
    def ReFire(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7]
        for i in range(8):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/fiPr/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 130, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 7 ; self.ReNBpack()
    def ReFree(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        for i in range(25):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/frPr/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 130, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 24 ; self.ReNBpack()
    def ReApple(self):
        self.imgs = []
        self.order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(15):
            self.imgs.append(ImageTk.PhotoImage(file = 'image/apPr/'+str(self.order[i])+'.png'))
        self.cvs.create_image(725, 130, anchor = 'c', image = self.imgs[0], tag ='imgs'+str(0))
        self.num = 14 ; self.ReNBpack()
#-----------------------------------------------------------------------------
# practice1      
    def Shape(self):
        self.after_Dr()
        self.shape_1btn = tk.Button(self.cvs, text = '1. Twitter', command = self.shape_1)
        self.shape_2btn = tk.Button(self.cvs, text = '2. UPC', command = self.shape_2)
        self.shape_3btn = tk.Button(self.cvs, text = '3. Free Creative Studio', command = self.shape_3)
        self.shape_4btn = tk.Button(self.cvs, text = '4. Apple', command = self.shape_4)
        self.shape_1btn.place(x = 100, y = 200), self.shape_2btn.place(x = 100, y = 300)
        self.shape_3btn.place(x = 100, y = 400), self.shape_4btn.place(x = 100, y = 500)
        self.labelS = tk.Label(text = 'ロゴデザインにおけるシェイプ形成の練習', font = self.font2, fg = 'black', bg = 'white')
        self.labelS.place(x = 100, y = 50)
        self.StoDr_btn = tk.Button(self.cvs, text = 'Return', command = self.StoDr)
        self.StoDr_btn.place(x = 800, y = 600)
    def StoDr(self):
        self.StoDr_btn.destroy() ; self.Sbtn_dlt() ; self.design_rule()
    def Sbtn_dlt(self):
        self.labelS.destroy()
        self.shape_num = [self.shape_1btn, self.shape_2btn, self.shape_3btn, self.shape_4btn]
        for i in range(4):self.shape_num[i].destroy()
    def to_S(self):
        self.reS_btn = tk.Button(self.cvs, text = 'Return', command = self.re_S)
        self.reS_btn.place(x = 800, y =600)
    def re_S(self):
        self.oc_dlt() ; self.reS_btn.destroy() ; self.Shape()
        self.hideB_label.destroy() ; self.hideN_label.destroy() ; self.next_btn.destroy() ; self.back_btn.destroy()
    def S_pack(self):
        self.StoDr_btn.destroy() ; self.Sbtn_dlt() ; self.OrCr() ; self.to_S() ; self.create_btn.lift()
# shape_1
    def shape_1(self):
        self.origin(14, 1)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.createS_1)
        self.S_pack()
        x = 750 ; y = 300 ; a = 104.772 ; b = a*((1+math.sqrt(5))/2) ; c = b*((1+math.sqrt(5))/2)
        CanvasOval.canvas = self.cvs
        for l in range(2):
            l = CanvasOval(x-c/2, y, x+c/2, y+c, outline='#c30d23', width=2.0) ; l
        for m in range(5):
            m = CanvasOval(x-b/2, y+c/2-b/2, x+b/2, y+b/2+c/2, outline='#036eb7', width=2.0) ; m
        for n in range(6):
            n = CanvasOval(x-a/2, y+c/2-a/2, x+a/2, y+a/2+c/2, outline='#e95513', width=2.0) ; n
        self.ReTwitter()
    def createS_1(self):
        self.create(14, 1) ; self.create_btn.lower()
# shape_2
    def shape_2(self):
        self.origin(14, 2)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.createS_2)
        self.S_pack()
        x = 750 ; y = 300 ; a = 89.167 ; b = a*((1+math.sqrt(5))/2) ; c = b*((1+math.sqrt(5))/2) ; p = 184.725
        CanvasOval.canvas = self.cvs
        l = CanvasOval(x-c/2, y, x+c/2, y+c, outline='#fbb03b', width=2.0) ; l
        q = CanvasOval(x-p/2, y+c/2-p/2, x+p/2, y+p/2+c/2, outline='#000000', width=2.0) ; q
        for m in range(2):
            m = CanvasOval(x-b/2, y+c/2-b/2, x+b/2, y+b/2+c/2, outline='#29abe2', width=2.0) ; m
        for n in range(2):
            n = CanvasOval(x-a/2, y+c/2-a/2, x+a/2, y+a/2+c/2, outline='#00a199', width=2.0) ; n
        self.ReFire()
    def createS_2(self):
        self.create(14, 2) ; self.create_btn.lower()
# shape_3
    def shape_3(self):
        self.origin(14, 3)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.createS_3)
        self.S_pack()
        x = 750 ; y = 300 ; a = 56.547 ; b = a*((1+math.sqrt(5))/2) ; c = b*((1+math.sqrt(5))/2) ; d = c*((1+math.sqrt(5))/2)
        CanvasOval.canvas = self.cvs
        for l in range(9):
            l = CanvasOval(x-d/2, y, x+d/2, y+d, outline='#c30d23', width=2.0) ; l
        for m in range(5):
            m = CanvasOval(x-c/2, y+d/2-c/2, x+c/2, y+c/2+d/2, outline='#036eb7', width=2.0) ; m
        for n in range(4):
            n = CanvasOval(x-b/2, y+d/2-b/2, x+b/2, y+b/2+d/2, outline='#e95513', width=2.0) ; n
        for o in range(5):
            o = CanvasOval(x-a/2, y+d/2-a/2, x+a/2, y+a/2+d/2, outline='#2ca6e0', width=2.0) ; o
        self.ReFree()
    def createS_3(self):
        self.create(14, 3) ; self.create_btn.lower()
# shape_4
    def shape_4(self):
        self.origin(15, 1)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', command = self.createS_4)
        self.S_pack()
        PhotoMove1.canvas = self.cvs ; PhotoMove1()
        PhotoMove2.canvas = self.cvs ; PhotoMove2()
        x = 580 ; y = 350
        a = 13.637 ; b = a*((1+math.sqrt(5))/2) ; c = b*((1+math.sqrt(5))/2) ; d = c*((1+math.sqrt(5))/2)
        e = d*((1+math.sqrt(5))/2) ; f = e*((1+math.sqrt(5))/2)
        CanvasOval.canvas = self.cvs
        l = CanvasOval(x-f/2, y, x+f/2, y+f, outline='#c30d23', width=2.0) ; l
        for m in range(7):
            m = CanvasOval(x-e/2, y+f/2-e/2, x+e/2, y+e/2+f/2, outline='#036eb7', width=2.0) ; m
        for n in range(2):
            n = CanvasOval(x-d/2, y+f/2-d/2, x+d/2, y+d/2+f/2, outline='#e95513', width=2.0) ; n
        o = CanvasOval(x-a/2, y+f/2-a/2, x+a/2, y+a/2+f/2, outline='#2ca6e0', width=2.0) ; o
        self.ReApple()
    def createS_4(self):
        self.create(15, 1) ; self.create_btn.lower()
#-----------------------------------------------------------------------------
# createZone(practice 2)
    def createZone(self):
        self.after_Dr()
        self.coordinate() ; self.num = 0 ; self.calNum = 0 ; self.drawing2()
        self.label_scale = tk.Label(text = 'グリッドの1マス = 10×10(pixel)    黄金長方形の１番大きい正方形 = 300×300(pixel)') ; self.label_scale.place(x = 50, y = 20)
        self.label_d = tk.Label(text = 'diameter') ; self.label_d.place(x = 670, y = 422)
        self.txt1 = tk.Entry(width = 10) ; self.txt1.place(x = 740, y = 420)
        self.cc_btn = tk.Button(text = 'circle', command = self.circle) ;  self.cc_btn.place(x = 850, y = 425)
        self.deCir_btn = tk.Button(text = 'delete', command = self.deleteCir) ; self.deCir_btn.place(x = 950, y = 425)
        self.label_w = tk.Label(text = 'width') ; self.label_w.place(x = 670, y = 472)
        self.txt2 = tk.Entry(width = 10) ; self.txt2.place(x = 740, y = 470)
        self.label_h = tk.Label(text = 'height') ; self.label_h.place(x = 670, y = 502)
        self.txt3 = tk.Entry(width = 10) ; self.txt3.place(x = 740, y = 500)
        self.rt_btn = tk.Button(text = 'rectangle', command = self.rectangle) ; self.rt_btn.place(x = 850, y = 505)
        self.deRec_btn = tk.Button(text = 'delete', command = self.deleteRec) ; self.deRec_btn.place(x = 950, y = 505)
        self.crGRh_btn = tk.Button(text = 'GRh On', command = self.gridGRh) ; self.crGRh_btn.place(x = 260, y = 600)
        self.crGRw_btn = tk.Button(text = 'GRw On', command = self.gridGRw) ; self.crGRw_btn.place(x = 340, y = 600)
        self.crCoo_btn = tk.Button(text = 'gridOn', command = self.gridLine) ; self.crCoo_btn.place(x = 420, y = 600)
        self.deCoo_btn = tk.Button(text = 'gridOff', command = self.deleteCoo) ; self.deCoo_btn.place(x = 500, y = 600)
        self.deFig_btn = tk.Button(text = 'delete All', command = self.deleteFigure) ; self.deFig_btn.place(x = 950, y = 570)
        self.label_Cal = tk.Label(text = '黄金比計算') ; self.label_Cal.place(x = 665, y = 302)
        self.txt4 = tk.Entry(width = 10) ; self.txt4.place(x = 740, y = 300)
        self.label_Mul = tk.Label(text = '× 1.618 =') ; self.label_Mul.place(x = 850, y = 300)
        self.label_Div = tk.Label(text = '÷ 1.618 =') ; self.label_Div.place(x = 850, y = 330)
        self.Cal_btn = tk.Button(text = '計算する', command = self.calGR) ; self.Cal_btn.place(x = 740, y = 330)
        self.save_btn = tk.Button(text = 'save', command = self.save_canvas2)
        self.save_btn.place(x = 850, y = 570)
        self.deAll_btn = tk.Button(text = 'Return', command = self.deleteAll)
        self.deAll_btn.place(x =950, y = 600)
    def coordinate(self):
        k = 50 ; l = 550 ; s = 0 ; t = 0
        for i in range(51):
            self.cvs.create_line(k, k+s, l, k+s, fill = '#aabbcc', tag='coo') ; s += 10
            self.cvs.create_line(k+t, k, k+t, l, fill = '#aabbcc', tag='coo') ; t += 10
    def gridLine(self):
        self.cvs.delete('GRw', 'GRh') ; self.coordinate()
    def gridGRw(self):
        self.cvs.delete('coo', 'GRh')
        f = (1+math.sqrt(5))/2 ; f2 = pow(f,2) ; f3 = pow(f,3) ; f4 = pow(f,4) ; f5 = pow(f,5)
        wx01 = 50 ; wy01 = 150 ; wx11 = wx01+300 ; wy11 = wy01+300 ; ww = wx11-wx01 ; wh = wy11-wy01
        wx02 = wx11 ; wy02 = wy01 ; wx22 = wx02+ww/f ; wy22 = wy02+wh/f
        wx03 = wx22 ; wy03 = wy22 ; wx33 = wx03-ww/f2 ; wy33 = wy03+wh/f2
        wx04 = wx33 ; wy04 = wy33 ; wx44 = wx04-ww/f3 ; wy44 = wy04-wh/f3
        wx05 = wx44 ; wy05 = wy44 ; wx55 = wx05+ww/f4 ; wy55 = wy05-wh/f4
        wx06 = wx55 ; wy06 = wy55 ; wx66 = wx06+ww/f5 ; wy66 = wy06+wh/f5
        self.cvs.create_rectangle(wx01, wy01, wx11, wy11, outline = '#aabbcc', tag = 'GRw')
        self.cvs.create_rectangle(wx02, wy02, wx22, wy22, outline = '#aabbcc', tag = 'GRw')
        self.cvs.create_rectangle(wx03, wy03, wx33, wy33, outline = '#aabbcc', tag = 'GRw')
        self.cvs.create_rectangle(wx04, wy04, wx44, wy44, outline = '#aabbcc', tag = 'GRw')
        self.cvs.create_rectangle(wx05, wy05, wx55, wy55, outline = '#aabbcc', tag = 'GRw')
        self.cvs.create_rectangle(wx06, wy06, wx66, wy66, outline = '#aabbcc', tag = 'GRw')
    def gridGRh(self):
        self.cvs.delete('coo', 'GRw')
        f = (1+math.sqrt(5))/2 ; f2 = pow(f,2) ; f3 = pow(f,3) ; f4 = pow(f,4) ; f5 = pow(f,5)
        wx01 = 150 ; wy01 = 70 ; wx11 = wx01+300 ; wy11 = wy01+300 ; ww = wx11-wx01 ; wh = wy11-wy01
        wx02 = wx01 ; wy02 = wy11 ; wx22 = wx02+ww/f ; wy22 = wy02+wh/f
        wx03 = wx22 ; wy03 = wy22 ; wx33 = wx03+ww/f2 ; wy33 = wy03-wh/f2
        wx04 = wx33 ; wy04 = wy33 ; wx44 = wx04-ww/f3 ; wy44 = wy04-wh/f3
        wx05 = wx44 ; wy05 = wy44 ; wx55 = wx05-ww/f4 ; wy55 = wy05+wh/f4
        wx06 = wx55 ; wy06 = wy55 ; wx66 = wx06+ww/f5 ; wy66 = wy06+wh/f5
        self.cvs.create_rectangle(wx01, wy01, wx11, wy11, outline = '#aabbcc', tag = 'GRh')
        self.cvs.create_rectangle(wx02, wy02, wx22, wy22, outline = '#aabbcc', tag = 'GRh')
        self.cvs.create_rectangle(wx03, wy03, wx33, wy33, outline = '#aabbcc', tag = 'GRh')
        self.cvs.create_rectangle(wx04, wy04, wx44, wy44, outline = '#aabbcc', tag = 'GRh')
        self.cvs.create_rectangle(wx05, wy05, wx55, wy55, outline = '#aabbcc', tag = 'GRh')
        self.cvs.create_rectangle(wx06, wy06, wx66, wy66, outline = '#aabbcc', tag = 'GRh')
    def circle(self):
        a = float(self.txt1.get()) ; m = 250
        CanvasOval.canvas = self.cvs
        cc = CanvasOval(m, m, m+a, m+a, outline='#6699ff', width=2.0, tag='crC') ; cc
    def rectangle(self):
        b = float(self.txt2.get()) ; c = float(self.txt3.get()) ; m = 250
        Rectangle.canvas = self.cvs
        rt = Rectangle(m, m, m+b, m+c, outline='#6699ff', width=2.0, tag='crR') ; rt
    def calGR(self):
        if self.calNum != 0:
            self.label_dMul.destroy() ; self.label_dDiv.destroy()
        d = float(self.txt4.get())
        dMul = round(d * ((1+math.sqrt(5))/2), 3) ; dDiv = round(d / ((1+math.sqrt(5))/2), 3)
        self.label_dMul = tk.Label(text = dMul) ; self.label_dMul.place(x = 920, y = 300)
        self.label_dDiv = tk.Label(text = dDiv) ; self.label_dDiv.place(x = 920, y = 330)
        self.calNum += 1
    def deleteCoo(self):self.cvs.delete('coo', 'GRw', 'GRh')
    def deleteCir(self):self.cvs.delete('crC')
    def deleteRec(self):self.cvs.delete('crR')
    def deleteLine(self):self.cvs.delete('line')
    def deleteFigure(self):self.cvs.delete('crC','crR','line')
    def save_canvas2(self):
        self.num += 1 ; self.cvs.postscript(file = 'saveimg/self' + str(self.num) + '.ps', colormode='color')
    def drawing2(self):
        self.vr = tk.IntVar()
        self.vr.set(0)
        self.point_radio = tk.Radiobutton(text='point', variable=self.vr, value=0, command=self.change_radio2)
        self.point_radio.place(x = 670, y = 370)
        self.write_radio = tk.Radiobutton(text='write', variable=self.vr, value=1, command=self.change_radio2)
        self.write_radio.place(x = 760, y = 370)
        self.erase_radio = tk.Radiobutton(text='erase', variable=self.vr, value=2, command=self.change_radio2)
        self.erase_radio.place(x = 850, y = 370)
        self.deLine_btn = tk.Button(text = 'delete', command = self.deleteLine)
        self.deLine_btn.place(x = 950, y = 370)
        self.cvs.bind('<B1-Motion>', self.paint2) ; self.cvs.bind('<ButtonRelease-1>', self.reset2)
        self.old_x = None ; self.old_y = None ; self.color = 'black' ; self.eraser_on = None
        self.im = Image.new('RGB', (1050, 650), 'white')
        self.draw = ImageDraw.Draw(self.im)
    def change_radio2(self):
        if self.vr.get() == 0 : self.eraser_on = None
        elif self.vr.get() == 1 : self.eraser_on = False
        elif self.vr.get() == 2 : self.eraser_on = True
    def paint2(self, event):
        if self.eraser_on == None:
            self.old_x = None ; self.old_y = None
        if self.eraser_on : paint_color = 'white'
        else : paint_color = '#6699ff'
        if self.old_x and self.old_y:
            self.cvs.create_line(self.old_x, self.old_y, event.x, event.y, width=5.0, fill=paint_color,
                                 capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36, tag = 'line')
            self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=paint_color, width=4)
        self.old_x = event.x ; self.old_y = event.y
    def reset2(self, event):
        self.old_x, self.old_y = None, None
    def deleteAll(self):
        self.cvs.delete('all')
        self.zone_num = [self.cc_btn, self.deCir_btn, self.rt_btn, self.deRec_btn, self.crCoo_btn, 
                         self.deCoo_btn, self.deFig_btn, self.save_btn, self.deAll_btn, self.Cal_btn,
                         self.label_d, self.txt1, self.label_w, self.txt2, self.label_h, self.txt3,
                         self.point_radio, self.write_radio, self.erase_radio, self.deLine_btn, self.label_scale,
                         self.crGRw_btn, self.crGRh_btn, self.label_Cal, self.txt4, self.label_Mul, self.label_Div]
        for i in range(27):self.zone_num[i].destroy()
        if self.calNum != 0:
            self.label_dMul.destroy() ; self.label_dDiv.destroy()
        self.design_rule() ; self.cvs.bind('<B1-Motion>', self.reset2)

#=============================================================================
if __name__=='__main__':
    win = tk.Tk()
    win.geometry('1050x650')
    win.resizable(width = False, height = False)
    f = Frame()
    f.pack()
    f.mainloop()
