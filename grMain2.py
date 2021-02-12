from pathlib import Path
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image, ImageDraw
import math
from grSub2 import CanvasOval ; from grSub2 import Rectangle ; from grSub2 import LINE ; from grSub2 import PhotoMove1 ; from grSub2 import PhotoMove2

# 出力フォルダを作成
output_folder = Path("./saveimg")
output_folder.mkdir(exist_ok=True)

class Main(tk.Frame):
    
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.cvs = tk.Canvas(self, width = "1050", height = "750", bg = "white")
        self.cvs.grid(row = 0, column = 0)
        self.master.title('Golden Ratio')
        self.fA = font.Font(family = 'Helvetica', size = 55, weight = 'bold') ; self.fa = font.Font(family = 'Helvetica', size = 50)
        self.fB = font.Font(family = 'Helvetica', size = 40, weight = 'bold') ; self.fb = font.Font(family = 'Helvetica', size = 40)
        self.fC = font.Font(family = 'Helvetica', size = 30, weight = 'bold') ; self.fc = font.Font(family = 'Helvetica', size = 30)
        self.fD = font.Font(family = 'Helvetica', size = 20, weight = 'bold') ; self.fd = font.Font(family = 'Helvetica', size = 20)
        self.fe = font.Font(family = 'Helvetica', size = 15) ; self.ff = font.Font(family = 'Helvetica', size = 14)
        self.number = 0
        self.reNum = 0
        self.signal = 0
        self.NOreprg_btn = 0
        self.num = 0
        self.save_num = 0 #セーブ回数(保存psのナンバリング)
        self.Start()

# Start ===============================================================================================================
    def Start(self):
        self.reNum = 0 ; self.NOreprg_btn = 0
        self.ttl_l = tk.Label(text = 'Golden Ratio in Logo Design',font = self.fA, fg = 'black', bg = 'white')
        self.exg_l = tk.Label(text='1. 黄金比についての説明', font=self.fc, fg='black', bg='white')
        self.prg_l = tk.Label(text='2. ロゴデザインにおける黄金比の実用例', font=self.fc, fg='black', bg='white')
        self.prd_l = tk.Label(text='3. 黄金比によるロゴデザインの練習', font=self.fc, fg='black', bg='white')
        self.url_l = tk.Label(text='4. 使用したロゴの一覧・引用元', font=self.fc, fg='black', bg='white')
        self.ttl_l.place(x=130, y=70)
        self.exg_l.place(x=130, y=200) ; self.prg_l.place(x=130, y=320)
        self.prd_l.place(x=130, y=440) ; self.url_l.place(x=130, y=560)
        self.exg1_btn = tk.Button(self.cvs, text = 'about Golden Ratio 1', highlightbackground='white', command = self.exg1)
        self.exg2_btn = tk.Button(self.cvs, text = 'about Golden Ratio 2', highlightbackground='white', command = self.exg2)
        self.exg3_btn = tk.Button(self.cvs, text = 'about Golden Ratio 3', highlightbackground='white', command = self.exg3)
        self.exg4_btn = tk.Button(self.cvs, text = 'about Golden Ratio 4', highlightbackground='white', command = self.exg4)
        self.exg1_btn.place(x=130, y=250) ; self.exg2_btn.place(x=330, y=250)
        self.exg3_btn.place(x=530, y=250) ; self.exg4_btn.place(x=730, y=250)
        self.prg_btn = tk.Button(self.cvs, text='Design Rule', highlightbackground='white', command = self.prg)
        self.prg_btn.place(x=130, y=370)
        self.prd_btn = tk.Button(self.cvs, text='Practice', highlightbackground='white', command = self.Practice)
        self.prd_btn.place(x=130, y=490)
        self.url1_btn = tk.Button(self.cvs, text='Logo All', highlightbackground='white', command = self.LogoAll)
        self.url2_btn = tk.Button(self.cvs, text='Logo URL', highlightbackground='white', command = self.LogoURL)
        self.url1_btn.place(x=130, y=610) ; self.url2_btn.place(x=330, y=610)

    def start_delete(self):
        self.start_l = [self.ttl_l, self.exg_l, self.prg_l, self.prd_l, self.url_l]
        for i in range(5):self.start_l[i].destroy()
        self.start_b = [self.exg1_btn, self.exg2_btn, self.exg3_btn, self.exg4_btn, self.prg_btn, self.prd_btn, self.url1_btn, self.url2_btn]
        for i in range(8):self.start_b[i].destroy()


# exg(Explain about the Golden Ratio)==================================================================================
    def exg2St(self):
        self.cvs.delete('all') ; self.reSt_btn.destroy() ; self.Start()
    def exg(self,i):
        self.start_delete()
        self.reSt_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.exg2St)
        self.reSt_btn.place(x = 900, y = 680)
        self.exg_img = ImageTk.PhotoImage(file = 'image/what_gr/gr_' + str(i) + '.png')
        self.cvs.create_image(1050/2, 750/2, anchor = 'c', image = self.exg_img)
    def exg1(self):self.exg(1)
    def exg2(self):self.exg(2)
    def exg3(self):self.exg(3)
    def exg4(self):self.exg(4)


# prg(Practical example about the Golden Ratio)========================================================================
    def prg_delete(self):
        self.prg_l = [self.prg_l, self.dr1_l, self.dr2_l, self.dr3_l, self.dr4_l, self.dr5_l, self.dr6_l, self.dr7_l, self.dr8_l,
                      self.dr9_l, self.dr10_l, self.dr11_l, self.dr12_l, self.dr13_l, self.dr14_l, self.dr15_l]
        for i in range(16):self.prg_l[i].destroy()
        self.prg_b = [self.dr1_btn, self.dr2_btn, self.dr3_btn, self.dr4_btn, self.dr5_btn, self.dr6_btn, self.dr7_btn, self.dr8_btn,
                      self.dr9_btn, self.dr10_btn, self.dr11_btn, self.dr12_btn, self.dr13_btn, self.dr14_btn, self.dr15_btn]
        for i in range(15):self.prg_b[i].destroy()
    def prg2St(self):
        self.cvs.delete('all') ; self.prg_delete() ; self.reSt_btn.destroy() ; self.Start()
    def prg(self):
        if self.reNum == 0:
            self.start_delete()
        self.reNum = 0
        self.reSt_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.prg2St)
        self.reSt_btn.place(x = 900, y = 680)
        self.prg_l = tk.Label(text='ロゴデザインにおける黄金比の実用例', font=self.fB, fg='black', bg='white')
        self.dr1_l = tk.Label(text='1. シンボルマークに黄金比率', font=self.ff, fg='black', bg='white')
        self.dr2_l = tk.Label(text='2. シンボルマーク，ロゴタイプのアスペクト比に黄金比率', font=self.ff, fg='black', bg='white')
        self.dr3_l = tk.Label(text='3. シンボルマークとロゴタイプが黄金比の関係', font=self.ff, fg='black', bg='white')
        self.dr4_l = tk.Label(text='4. 黄金長方形による要素の位置決定', font=self.ff, fg='black', bg='white')
        self.dr5_l = tk.Label(text='5. 黄金長方形による要素の量の決定', font=self.ff, fg='black', bg='white')
        self.dr6_l = tk.Label(text='6. 黄金螺旋によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr7_l = tk.Label(text='7. 黄金円によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr8_l = tk.Label(text='8. 黄金正方形によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr9_l = tk.Label(text='9. 黄金長方形の応用によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr10_l = tk.Label(text='10. 黄金長方形と黄金螺旋の組み合わせ', font=self.ff, fg='black', bg='white')
        self.dr11_l = tk.Label(text='11. 黄金長方形と黄金円の組み合わせ', font=self.ff, fg='black', bg='white')
        self.dr12_l = tk.Label(text='12. 黄金円の応用によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr13_l = tk.Label(text='13. 黄金三角形によるロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr14_l = tk.Label(text='14. 黄金円によってシェイプを形成したロゴデザイン', font=self.ff, fg='black', bg='white')
        self.dr15_l = tk.Label(text='15. 黄金円と黄金螺旋によってシェイプを形成したロゴデザイン', font=self.ff, fg='black', bg='white')
        self.prg_l.place(x=135, y=30)
        lx = 300 ; ly =100 ; p = 40
        self.dr1_l.place(x=lx, y=ly+3) ; self.dr6_l.place(x=lx, y=ly+p*5+3)  ; self.dr11_l.place(x=lx, y=ly+p*10+3)
        self.dr2_l.place(x=lx, y=ly+p+3) ; self.dr7_l.place(x=lx, y=ly+p*6+3)  ; self.dr12_l.place(x=lx, y=ly+p*11+3)
        self.dr3_l.place(x=lx, y=ly+p*2+3) ; self.dr8_l.place(x=lx, y=ly+p*7+3)  ; self.dr13_l.place(x=lx, y=ly+p*12+3)
        self.dr4_l.place(x=lx, y=ly+p*3+3) ; self.dr9_l.place(x=lx, y=ly+p*8+3)  ; self.dr14_l.place(x=lx, y=ly+p*13+3)
        self.dr5_l.place(x=lx, y=ly+p*4+3) ; self.dr10_l.place(x=lx, y=ly+p*9+3) ; self.dr15_l.place(x=lx, y=ly+p*14+3)
        
        self.dr1_btn = tk.Button(self.cvs, text='Design Rule 1', highlightbackground='white', command=self.rule1)
        self.dr2_btn = tk.Button(self.cvs, text='Design Rule 2', highlightbackground='white', command=self.rule2)
        self.dr3_btn = tk.Button(self.cvs, text='Design Rule 3', highlightbackground='white', command=self.rule3)
        self.dr4_btn = tk.Button(self.cvs, text='Design Rule 4', highlightbackground='white', command=self.rule4)
        self.dr5_btn = tk.Button(self.cvs, text='Design Rule 5', highlightbackground='white', command=self.rule5)
        self.dr6_btn = tk.Button(self.cvs, text='Design Rule 6', highlightbackground='white', command=self.rule6)
        self.dr7_btn = tk.Button(self.cvs, text='Design Rule 7', highlightbackground='white', command=self.rule7)
        self.dr8_btn = tk.Button(self.cvs, text='Design Rule 8', highlightbackground='white', command=self.rule8)
        self.dr9_btn = tk.Button(self.cvs, text='Design Rule 9', highlightbackground='white', command=self.rule9)
        self.dr10_btn = tk.Button(self.cvs, text='Design Rule 10', highlightbackground='white', command=self.rule10)
        self.dr11_btn = tk.Button(self.cvs, text='Design Rule 11', highlightbackground='white', command=self.rule11)
        self.dr12_btn = tk.Button(self.cvs, text='Design Rule 12', highlightbackground='white', command=self.rule12)
        self.dr13_btn = tk.Button(self.cvs, text='Design Rule 13', highlightbackground='white', command=self.rule13)
        self.dr14_btn = tk.Button(self.cvs, text='Design Rule 14', highlightbackground='white', command=self.rule14)
        self.dr15_btn = tk.Button(self.cvs, text='Design Rule 15', highlightbackground='white', command=self.rule15)
        bx = 150 ; by = 100
        self.dr1_btn.place(x=bx, y=by) ; self.dr6_btn.place(x=bx, y=by+p*5)  ; self.dr11_btn.place(x=bx, y=by+p*10)
        self.dr2_btn.place(x=bx, y=by+p) ; self.dr7_btn.place(x=bx, y=by+p*6)  ; self.dr12_btn.place(x=bx, y=by+p*11)
        self.dr3_btn.place(x=bx, y=by+p*2) ; self.dr8_btn.place(x=bx, y=by+p*7)  ; self.dr13_btn.place(x=bx, y=by+p*12)
        self.dr4_btn.place(x=bx, y=by+p*3) ; self.dr9_btn.place(x=bx, y=by+p*8)  ; self.dr14_btn.place(x=bx, y=by+p*13)
        self.dr5_btn.place(x=bx, y=by+p*4) ; self.dr10_btn.place(x=bx, y=by+p*9) ; self.dr15_btn.place(x=bx, y=by+p*14)


    def rl2prg(self):
        if self.NOreprg_btn == 0:
            self.reprg_btn.destroy()
        if self.number == 1:
            self.rule1_l.destroy()
            self.rule1_btn = [self.rule1_1btn, self.rule1_2btn, self.rule1_3btn, self.rule1_4btn, self.rule1_5btn, self.rule1_6btn, self.rule1_7btn]
            for i in range(7):self.rule1_btn[i].destroy()
        elif self.number == 2:
            self.rule2_l.destroy()
            self.rule2_btn = [self.rule2_1btn, self.rule2_2btn, self.rule2_3btn]
            for i in range(3):self.rule2_btn[i].destroy()
        elif self.number == 3:
            self.rule3_l.destroy()
            self.rule3_btn = [self.rule3_1btn, self.rule3_2btn, self.rule3_3btn, self.rule3_4btn]
            for i in range(4):self.rule3_btn[i].destroy() 
        elif self.number == 4:
            self.rule4_l.destroy()
            self.rule4_btn = [self.rule4_1btn, self.rule4_2btn, self.rule4_3btn, self.rule4_4btn, self.rule4_5btn]
            for i in range(5):self.rule4_btn[i].destroy()
        elif self.number == 5:
            self.rule5_l.destroy()
            self.rule5_btn = [self.rule5_1btn, self.rule5_2btn, self.rule5_3btn, self.rule5_4btn]
            for i in range(4):self.rule5_btn[i].destroy()
        elif self.number == 6:
            self.rule6_l.destroy() ; self.rule6_1btn.destroy()
        elif self.number == 7:
            self.rule7_l.destroy() ; self.rule7_1btn.destroy()
        elif self.number == 8:
            self.rule8_l.destroy() ; self.rule8_1btn.destroy()
        elif self.number == 9:
            self.rule9_l.destroy() ; self.rule9_1btn.destroy()
        elif self.number == 10:
            self.rule10_l.destroy()
            self.rule10_btn = [self.rule10_1btn, self.rule10_2btn]
            for i in range(2):self.rule10_btn[i].destroy()
        elif self.number == 11:
            self.rule11_l.destroy() ; self.rule11_1btn.destroy()
        elif self.number == 12:
            self.rule12_l.destroy() ; self.rule12_1btn.destroy()
        elif self.number == 13:
            self.rule13_l.destroy() ; self.rule13_1btn.destroy()
        elif self.number == 14:
            self.rule14_l.destroy()
            self.rule14_btn = [self.rule14_1btn, self.rule14_2btn, self.rule14_3btn]
            for i in range(3):self.rule14_btn[i].destroy()
        elif self.number == 15:
            self.rule15_l.destroy() ; self.rule15_1btn.destroy()
        elif self.number == 99:
            self.Pra_delete()
        
        if self.signal > 0:
            return

        self.prg()

    def setprg(self):
        if self.signal == 0:
            self.prg_delete() ; self.reSt_btn.destroy()
        self.reprg_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.rl2prg)
        self.reprg_btn.place(x = 900, y = 680)

    def origin(self, i, j):
        self.cvs.delete('all')
        self.before_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j)  + '.png')
        self.cvs.create_image(1050/2, 750/2, anchor = 'c', image = self.before_img)
    def analyze(self, i, j):
        self.cvs.delete('all')
        self.after_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '_s' + '.png')
        self.cvs.create_image(1050/2, 750/2, anchor = 'c', image = self.after_img)
    def oriana(self):
        self.signal = 1 ; self.rl2prg() ; self.ori_btn.place(x=600, y=680) ; self.ana_btn.place(x=700, y=680)
        self.rerl_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.rerl)
        self.rerl_btn.place(x = 900, y = 680)
    def rerl(self):
        self.cvs.delete('all') ; self.rerl_btn.destroy()
        if 0 < self.number < 14:
            self.ori_btn.destroy() ; self.ana_btn.destroy()
        elif self.number > 13:
            self.create_dlt_btn.destroy() ; self.create_btn.destroy() ; self.next_btn.destroy() ; self.back_btn.destroy()
            self.hideB_label.destroy() ; self.hideN_label.destroy()
        if self.number == 1:self.rule1()
        elif self.number == 2:self.rule2()
        elif self.number == 3:self.rule3()
        elif self.number == 4:self.rule4()
        elif self.number == 5:self.rule5()
        elif self.number == 6:self.rule6()
        elif self.number == 7:self.rule7()
        elif self.number == 8:self.rule8()
        elif self.number == 9:self.rule9()
        elif self.number == 10:self.rule10()
        elif self.number == 11:self.rule11()
        elif self.number == 12:self.rule12()
        elif self.number == 13:self.rule13()
        elif self.number == 14:self.rule14()
        elif self.number == 15:self.rule15()
        elif self.number == 99:self.Practice()# ; self.signal = 0 # Practice後のDesign Ruleでバグがあったため修正を加えた
        elif self.number == -99:self.Practice() ; self.delete_Cmode()# ; self.signal = 0

# rule1
    def rule1(self):
        self.setprg() ; self.number = 1 ; self.reNum = 1 ; self.signal = 0
        self.rule1_l = tk.Label(text='シンボルマークに黄金比率', font=self.fB, fg='black', bg='white', justify='left')
        self.rule1_l.place(x=150, y=100)
        self.rule1_1btn = tk.Button(self.cvs, text='1. MGV', highlightbackground='white', font=self.fc, command=self.rule1_1)
        self.rule1_2btn = tk.Button(self.cvs, text='2. Conservation International', highlightbackground='white', font=self.fc, command=self.rule1_2)
        self.rule1_3btn = tk.Button(self.cvs, text='3. CRAFTMAN UNION', highlightbackground='white', font=self.fc, command=self.rule1_3)
        self.rule1_4btn = tk.Button(self.cvs, text='4. 中央大学', highlightbackground='white', font=self.fc, command=self.rule1_4)
        self.rule1_5btn = tk.Button(self.cvs, text='5. Azure Spa Hotel', highlightbackground='white', font=self.fc, command=self.rule1_5)
        self.rule1_6btn = tk.Button(self.cvs, text='6. Ontic', highlightbackground='white', font=self.fc, command=self.rule1_6)
        self.rule1_7btn = tk.Button(self.cvs, text='7. 東京都美術館', highlightbackground='white', font=self.fc, command=self.rule1_7)
        self.rule1_1btn.place(x=150, y =180) ; self.rule1_2btn.place(x=150, y=240) ; self.rule1_3btn.place(x=150, y=300)
        self.rule1_4btn.place(x=150, y =360) ; self.rule1_5btn.place(x=150, y=420) ; self.rule1_6btn.place(x=150, y=480)
        self.rule1_7btn.place(x=150, y =540)

    def rule1_1(self):
        self.origin(1,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_1)
        self.oriana()
    def ori1_1(self):self.origin(1,1)
    def ana1_1(self):self.analyze(1,1)
    
    def rule1_2(self):
        self.origin(1,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_2)
        self.oriana()
    def ori1_2(self):self.origin(1,2)
    def ana1_2(self):self.analyze(1,2)
    
    def rule1_3(self):
        self.origin(1,3)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_3)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_3)
        self.oriana()
    def ori1_3(self):self.origin(1,3)
    def ana1_3(self):self.analyze(1,3)
    
    def rule1_4(self):
        self.origin(1,4)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_4)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_4)
        self.oriana()
    def ori1_4(self):self.origin(1,4)
    def ana1_4(self):self.analyze(1,4)
    
    def rule1_5(self):
        self.origin(1,5)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_5)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_5)
        self.oriana()
    def ori1_5(self):self.origin(1,5)
    def ana1_5(self):self.analyze(1,5)

    def rule1_6(self):
        self.origin(1,6)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_6)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_6)
        self.oriana()
    def ori1_6(self):self.origin(1,6)
    def ana1_6(self):self.analyze(1,6)

    def rule1_7(self):
        self.origin(1,7)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori1_7)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana1_7)
        self.oriana()
    def ori1_7(self):self.origin(1,7)
    def ana1_7(self):self.analyze(1,7)

# rule2
    def rule2(self):
        self.setprg() ; self.number = 2 ; self.reNum = 1 ; self.signal = 0
        self.rule2_l = tk.Label(text='シンボルマーク、ロゴタイプの\nアスペクト比に黄金比率', font=self.fB, fg='black', bg='white', justify='left')
        self.rule2_l.place(x=150, y=100)
        self.rule2_1btn = tk.Button(self.cvs, text='1. National Geographic', highlightbackground='white', font=self.fc, command=self.rule2_1)
        self.rule2_2btn = tk.Button(self.cvs, text='2. Towson University', highlightbackground='white', font=self.fc, command=self.rule2_2)
        self.rule2_3btn = tk.Button(self.cvs, text='3. Hiway', highlightbackground='white', font=self.fc, command=self.rule2_3)
        self.rule2_1btn.place(x=150, y=220) ; self.rule2_2btn.place(x=150, y=280) ; self.rule2_3btn.place(x=150, y=340)
        
    def rule2_1(self):
        self.origin(2,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori2_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana2_1)
        self.oriana()
    def ori2_1(self):self.origin(2,1)
    def ana2_1(self):self.analyze(2,1)

    def rule2_2(self):
        self.origin(2,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori2_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana2_2)
        self.oriana()
    def ori2_2(self):self.origin(2,2)
    def ana2_2(self):self.analyze(2,2)

    def rule2_3(self):
        self.origin(2,3)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori2_3)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana2_3)
        self.oriana()
    def ori2_3(self):self.origin(2,3)
    def ana2_3(self):self.analyze(2,3)

# rule3
    def rule3(self):
        self.setprg() ; self.number = 3 ; self.reNum = 1 ; self.signal = 0
        self.rule3_l = tk.Label(text='シンボルマークとロゴタイプが\n黄金比率の関係', font=self.fB, fg='black', bg='white', justify='left')
        self.rule3_l.place(x=150, y=100)
        self.rule3_1btn = tk.Button(self.cvs, text='1. EQ Office', highlightbackground='white', font=self.fc, command=self.rule3_1)
        self.rule3_2btn = tk.Button(self.cvs, text='2. Qwant', highlightbackground='white', font=self.fc, command=self.rule3_2)
        self.rule3_3btn = tk.Button(self.cvs, text='3. Medscan', highlightbackground='white', font=self.fc, command=self.rule3_3)
        self.rule3_4btn = tk.Button(self.cvs, text='4. Midco', highlightbackground='white', font=self.fc, command=self.rule3_4)
        self.rule3_1btn.place(x=150, y=220) ; self.rule3_2btn.place(x=150, y=280) ; self.rule3_3btn.place(x=150, y=340)
        self.rule3_4btn.place(x=150, y=400)

    def rule3_1(self):
        self.origin(3,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori3_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana3_1)
        self.oriana()
    def ori3_1(self):self.origin(3,1)
    def ana3_1(self):self.analyze(3,1)

    def rule3_2(self):
        self.origin(3,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori3_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana3_2)
        self.oriana()
    def ori3_2(self):self.origin(3,2)
    def ana3_2(self):self.analyze(3,2)

    def rule3_3(self):
        self.origin(3,3)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori3_3)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana3_3)
        self.oriana()
    def ori3_3(self):self.origin(3,3)
    def ana3_3(self):self.analyze(3,3)

    def rule3_4(self):
        self.origin(3,4)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori3_4)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana3_4)
        self.oriana()
    def ori3_4(self):self.origin(3,4)
    def ana3_4(self):self.analyze(3,4)

# rule4
    def rule4(self):
        self.setprg() ; self.number = 4 ; self.reNum = 1 ; self.signal = 0
        self.rule4_l = tk.Label(text='黄金長方形による要素の位置決定', font=self.fB, fg='black', bg='white', justify='left')
        self.rule4_l.place(x=150, y=100)
        self.rule4_1btn = tk.Button(self.cvs, text='1. Mike Kelley', highlightbackground='white', font=self.fc, command = self.rule4_1)
        self.rule4_2btn = tk.Button(self.cvs, text='2. 台南市美術館', highlightbackground='white', font=self.fc, command = self.rule4_2)
        self.rule4_3btn = tk.Button(self.cvs, text='3. 長浜クリニック', highlightbackground='white', font=self.fc, command = self.rule4_3)
        self.rule4_4btn = tk.Button(self.cvs, text='4. Matterfund', highlightbackground='white', font=self.fc, command = self.rule4_4)
        self.rule4_5btn = tk.Button(self.cvs, text='5. MasterCard', highlightbackground='white', font=self.fc, command = self.rule4_5)
        self.rule4_1btn.place(x=150, y =180) ; self.rule4_2btn.place(x=150, y=240) ; self.rule4_3btn.place(x=150, y=300)
        self.rule4_4btn.place(x=150, y =360) ; self.rule4_5btn.place(x=150, y=420)

    def rule4_1(self):
        self.origin(4,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori4_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana4_1)
        self.oriana()
    def ori4_1(self):self.origin(4,1)
    def ana4_1(self):self.analyze(4,1)

    def rule4_2(self):
        self.origin(4,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori4_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana4_2)
        self.oriana()
    def ori4_2(self):self.origin(4,2)
    def ana4_2(self):self.analyze(4,2)

    def rule4_3(self):
        self.origin(4,3)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori4_3)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana4_3)
        self.oriana()
    def ori4_3(self):self.origin(4,3)
    def ana4_3(self):self.analyze(4,3)

    def rule4_4(self):
        self.origin(4,4)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori4_4)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana4_4)
        self.oriana()
    def ori4_4(self):self.origin(4,4)
    def ana4_4(self):self.analyze(4,4)

    def rule4_5(self):
        self.origin(4,5)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori4_5)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana4_5)
        self.oriana()
    def ori4_5(self):self.origin(4,5)
    def ana4_5(self):self.analyze(4,5)

# rule5
    def rule5(self):
        self.setprg() ; self.number = 5 ; self.reNum = 1 ; self.signal = 0
        self.rule5_l = tk.Label(text='黄金長方形による要素の量の決定', font=self.fB, fg='black', bg='white', justify='left')
        self.rule5_l.place(x=150, y=100)
        self.rule5_1btn = tk.Button(self.cvs, text='1. Yoga Id', highlightbackground='white', font=self.fc, command=self.rule5_1)
        self.rule5_2btn = tk.Button(self.cvs, text='2. Old Chatham Sheepherding Company', highlightbackground='white', font=self.fc, command=self.rule5_2)
        self.rule5_3btn = tk.Button(self.cvs, text='3. Cactus @ Alhambra', highlightbackground='white', font=self.fc, command=self.rule5_3)
        self.rule5_4btn = tk.Button(self.cvs, text='4. Vitali Bosch', highlightbackground='white', font=self.fc, command=self.rule5_4)
        self.rule5_1btn.place(x=150, y =180) ; self.rule5_2btn.place(x=150, y=240) ; self.rule5_3btn.place(x=150, y=300)
        self.rule5_4btn.place(x=150, y =360)
        
    def rule5_1(self):
        self.origin(5,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori5_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana5_1)
        self.oriana()
    def ori5_1(self):self.origin(5,1)
    def ana5_1(self):self.analyze(5,1)

    def rule5_2(self):
        self.origin(5,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori5_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana5_2)
        self.oriana()
    def ori5_2(self):self.origin(5,2)
    def ana5_2(self):self.analyze(5,2)

    def rule5_3(self):
        self.origin(5,3)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori5_3)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana5_3)
        self.oriana()
    def ori5_3(self):self.origin(5,3)
    def ana5_3(self):self.analyze(5,3)

    def rule5_4(self):
        self.origin(5,4)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori5_4)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana5_4)
        self.oriana()
    def ori5_4(self):self.origin(5,4)
    def ana5_4(self):self.analyze(5,4)

# rule6
    def rule6(self):
        self.setprg() ; self.number = 6 ; self.reNum = 1 ; self.signal = 0
        self.rule6_l = tk.Label(text='黄金螺旋によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule6_l.place(x=150, y=100)
        self.rule6_1btn = tk.Button(self.cvs, text='1. Ipek Koray Design', highlightbackground='white', font=self.fc, command=self.rule6_1)
        self.rule6_1btn.place(x=150, y =180)

    def rule6_1(self):
        self.origin(6,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori6_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana6_1)
        self.oriana()
    def ori6_1(self):self.origin(6,1)
    def ana6_1(self):self.analyze(6,1)

# rule7
    def rule7(self):
        self.setprg() ; self.number = 7 ; self.reNum = 1 ; self.signal = 0
        self.rule7_l = tk.Label(text='黄金円によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule7_l.place(x=150, y=100)
        self.rule7_1btn = tk.Button(self.cvs, text='1. Sail', highlightbackground='white', font=self.fc, command=self.rule7_1)
        self.rule7_1btn.place(x=150, y =180)

    def rule7_1(self):
        self.origin(7,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori7_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana7_1)
        self.oriana()
    def ori7_1(self):self.origin(7,1)
    def ana7_1(self):self.analyze(7,1)

# rule8
    def rule8(self):
        self.setprg() ; self.number = 8 ; self.reNum = 1 ; self.signal = 0
        self.rule8_l = tk.Label(text='黄金正方形によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule8_l.place(x=150, y=100)
        self.rule8_1btn = tk.Button(self.cvs, text='1. Arthur Gall', highlightbackground='white', font=self.fc, command=self.rule8_1)
        self.rule8_1btn.place(x=150, y =180)

    def rule8_1(self):
        self.origin(8,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori8_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana8_1)
        self.oriana()
    def ori8_1(self):self.origin(8,1)
    def ana8_1(self):self.analyze(8,1)

# rule9
    def rule9(self):
        self.setprg() ; self.number = 9 ; self.reNum = 1 ; self.signal = 0
        self.rule9_l = tk.Label(text='黄金長方形の応用によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule9_l.place(x=150, y=100)
        self.rule9_1btn = tk.Button(self.cvs, text='1. Muram', highlightbackground='white', font=self.fc, command=self.rule9_1)
        self.rule9_1btn.place(x=150, y =180)

    def rule9_1(self):
        self.origin(9,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori9_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana9_1)
        self.oriana()
    def ori9_1(self):self.origin(9,1)
    def ana9_1(self):self.analyze(9,1)

# rule10
    def rule10(self):
        self.setprg() ; self.number = 10 ; self.reNum = 1 ; self.signal = 0
        self.rule10_l = tk.Label(text='黄金長方形と黄金螺旋の組み合わせ', font=self.fB, fg='black', bg='white', justify='left')
        self.rule10_l.place(x=150, y=100)
        self.rule10_1btn = tk.Button(self.cvs, text='1. Artland', highlightbackground='white', font=self.fc, command=self.rule10_1)
        self.rule10_2btn = tk.Button(self.cvs, text='2. Dovetail Custom Nurseries', highlightbackground='white', font=self.fc, command=self.rule10_2)
        self.rule10_1btn.place(x=150, y =180) ; self.rule10_2btn.place(x=150, y=240)

    def rule10_1(self):
        self.origin(10,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori10_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana10_1)
        self.oriana()
    def ori10_1(self):self.origin(10,1)
    def ana10_1(self):self.analyze(10,1)

    def rule10_2(self):
        self.origin(10,2)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori10_2)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana10_2)
        self.oriana()
    def ori10_2(self):self.origin(10,2)
    def ana10_2(self):self.analyze(10,2)

# rule11
    def rule11(self):
        self.setprg() ; self.number = 11 ; self.reNum = 1 ; self.signal = 0
        self.rule11_l = tk.Label(text='黄金長方形と黄金円の組み合わせ', font=self.fB, fg='black', bg='white', justify='left')
        self.rule11_l.place(x=150, y=100)
        self.rule11_1btn = tk.Button(self.cvs, text='1. Andrea Pedretti', highlightbackground='white', font=self.fc, command=self.rule11_1)
        self.rule11_1btn.place(x=150, y =180)

    def rule11_1(self):
        self.origin(11,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori11_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana11_1)
        self.oriana()
    def ori11_1(self):self.origin(11,1)
    def ana11_1(self):self.analyze(11,1)

# rule12
    def rule12(self):
        self.setprg() ; self.number = 12 ; self.reNum = 1 ; self.signal = 0
        self.rule12_l = tk.Label(text='黄金円の応用によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule12_l.place(x=150, y=100)
        self.rule12_1btn = tk.Button(self.cvs, text='1. Motherbird', highlightbackground='white', font=self.fc, command=self.rule12_1)
        self.rule12_1btn.place(x=150, y =180)

    def rule12_1(self):
        self.origin(12,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori12_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana12_1)
        self.oriana()
    def ori12_1(self):self.origin(12,1)
    def ana12_1(self):self.analyze(12,1)

# rule13
    def rule13(self):
        self.setprg() ; self.number = 13 ; self.reNum = 1 ; self.signal = 0
        self.rule13_l = tk.Label(text='黄金三角形によるロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule13_l.place(x=150, y=100)
        self.rule13_1btn = tk.Button(self.cvs, text='1. GHEU', highlightbackground='white', font=self.fc, command=self.rule13_1)
        self.rule13_1btn.place(x=150, y =180)

    def rule13_1(self):
        self.origin(13,1)
        self.ori_btn = tk.Button(self.cvs, text='Origin', highlightbackground='white', command=self.ori13_1)
        self.ana_btn = tk.Button(self.cvs, text='Analyze', highlightbackground='white', command=self.ana13_1)
        self.oriana()
    def ori13_1(self):self.origin(13,1)
    def ana13_1(self):self.analyze(13,1)

# rule14
    def rule14(self):
        self.setprg() ; self.number = 14 ; self.reNum = 1 ; self.signal = 0
        self.rule14_l = tk.Label(text='黄金円によってシェイプを\n形成したロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule14_l.place(x=150, y=100)
        self.rule14_1btn = tk.Button(self.cvs, text='1. Twitter', highlightbackground='white', font=self.fc, command=self.rule14_1)
        self.rule14_2btn = tk.Button(self.cvs, text='2. UPC', highlightbackground='white', font=self.fc, command=self.rule14_2)
        self.rule14_3btn = tk.Button(self.cvs, text='3. Free Creative Studio', highlightbackground='white', font=self.fc, command=self.rule14_3)
        self.rule14_1btn.place(x=150, y =220) ; self.rule14_2btn.place(x=150, y=280) ; self.rule14_3btn.place(x=150, y=340)

    def rule14_pack(self):
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', highlightbackground = 'white', command = self.create_dlt)
        self.OrCr() ; self.create_btn.lift()
        
    def rule14_1(self):
        self.signal = 1 ; self.vargin(14, 1) ; self.Twitter()
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground = 'white', command = self.create14_1)
        self.rule14_pack()
    def create14_1(self):
        self.create(14, 1) ; self.create_btn.lower()

    def rule14_2(self):
        self.signal = 1 ; self.vargin(14, 2) ; self.Fire()
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground = 'white', command = self.create14_2)
        self.rule14_pack()
    def create14_2(self):
        self.create(14, 2) ; self.create_btn.lower()

    def rule14_3(self):
        self.signal = 1 ; self.vargin(14, 3) ; self.Free()
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground = 'white', command = self.create14_3)
        self.rule14_pack()
    def create14_3(self):
        self.create(14, 3) ; self.create_btn.lower()

# rule15
    def rule15(self):
        self.setprg() ; self.number = 15 ; self.reNum = 1 ; self.signal = 0
        self.rule15_l = tk.Label(text='黄金円と黄金螺旋によって\nシェイプを形成したロゴデザイン', font=self.fB, fg='black', bg='white', justify='left')
        self.rule15_l.place(x=150, y=100)
        self.rule15_1btn = tk.Button(self.cvs, text='1. Apple', highlightbackground='white', font=self.fc, command=self.rule15_1)
        self.rule15_1btn.place(x=150, y=220)

    def rule15_1(self):
        self.signal = 1 ; self.vargin(15, 1) ; self.Apple()
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground = 'white', command = self.create15_1)
        self.rule14_pack()
    def create15_1(self):
        self.create(15, 1) ; self.create_btn.lower()
#----------------------------------------------------------------------------------------------------------------------
# origin create
    def OrCr(self):
        self.create_dlt_btn.place(x = 250, y = 600)
        self.create_btn.place(x = 250, y = 600)
    def vargin(self, i, j):
        self.rl2prg()
        self.rerl_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.rerl)
        self.rerl_btn.place(x = 900, y = 680)
        self.vargin_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '.png')
        self.cvs.create_image(300, 300, anchor = 'c', image = self.vargin_img)
    def create(self, i, j):
        self.create_img = ImageTk.PhotoImage(file = 'image/logo_photo/' + str(i) + '_' + str(j) + '_s' + '.png')
        self.cvs.create_image(300, 300, anchor = 'c', image = self.create_img, tag = 'cr')
    def create_dlt(self):
        self.cvs.delete('cr') ; self.create_dlt_btn.lower()
    def oc_dlt(self):
        self.cvs.delete('all') ; self.create_dlt_btn.destroy() ; self.create_btn.destroy()
#----------------------------------------------------------------------------------------------------------------------
    def NBpack(self):
        self.count = 0
        self.hideB_label = tk.Label(text = 'xxxxx1', fg='white', bg='white', font=self.fD) ; self.hideB_label.place(x=645, y=600)
        self.hideN_label = tk.Label(text = 'xxxxx2', fg='white', bg='white', font=self.fD) ; self.hideN_label.place(x=725, y=600)
        self.Next() ; self.Back()  
    def Back(self):
        self.back_btn = tk.Button(self.cvs, text = 'back', highlightbackground = 'white', command = self.BackImage)
        self.back_btn.place(x=650, y=600)
    def Next(self):
        self.hideN_label.lower()
        self.next_btn = tk.Button(self.cvs, text = 'next', highlightbackground = 'white', command = self.NextImage)
        self.next_btn.place(x=730, y=600)
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
#----------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------
# Practice=============================================================================================================
    def Pra_delete(self):
        self.Pra_l = [self.pra1_l, self.pra2_l, self.p1a_l, self.p1b_l, self.p1c_l, self.p1d_l, self.p2a_l]
        for i in range(7):self.Pra_l[i].destroy()
        self.Pra_b = [self.p1a_btn, self.p1b_btn, self.p1c_btn, self.p1d_btn, self.p2a_btn]
        for i in range(5):self.Pra_b[i].destroy()
    def Pra2St(self):
        self.cvs.delete('all') ; self.Pra_delete() ; self.reSt_btn.destroy() ; self.Start()
    def Practice(self):
        if self.reNum == 0:self.start_delete()
        self.number = 99 ; self.reNum = 1 ; self.NOreprg_btn = 1  ; self.signal = 0
        self.reSt_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.Pra2St)
        self.reSt_btn.place(x = 900, y = 680)
        self.pra1_l = tk.Label(text='ロゴデザインにおけるシェイプ形成の練習(実例制作)', font=self.fC, fg='black', bg='white')
        self.pra2_l = tk.Label(text='ロゴデザインにおけるシェイプ形成の練習(自由制作)', font=self.fC, fg='black', bg='white')
        self.pra1_l.place(x=150, y=80) ; self.pra2_l.place(x=150, y=350)
        self.p1a_l = tk.Label(text='1. Twitter', font=self.ff, fg='black', bg='white')
        self.p1b_l = tk.Label(text='2. UPC', font=self.ff, fg='black', bg='white')
        self.p1c_l = tk.Label(text='3. Free Creative Studio', font=self.ff, fg='black', bg='white')
        self.p1d_l = tk.Label(text='4. Apple', font=self.ff, fg='black', bg='white')
        self.p2a_l = tk.Label(text='Design Your Logo', font=self.ff, fg='black', bg='white')
        self.p1a_l.place(x=300, y=150+3) ; self.p1c_l.place(x=650, y=150+3) ; self.p1b_l.place(x=300, y=200+3) ; self.p1d_l.place(x=650, y=200+3) ; self.p2a_l.place(x=300, y=420+3)
        self.p1a_btn = tk.Button(self.cvs, text='Go to Practice 1', highlightbackground='white', command=self.shape_1)
        self.p1b_btn = tk.Button(self.cvs, text='Go to Practice 2', highlightbackground='white', command=self.shape_2)
        self.p1c_btn = tk.Button(self.cvs, text='Go to Practice 3', highlightbackground='white', command=self.shape_3)
        self.p1d_btn = tk.Button(self.cvs, text='Go to Practice 4', highlightbackground='white', command=self.shape_4)
        self.p2a_btn = tk.Button(self.cvs, text='Creative Mode', highlightbackground='white', command=self.Creative_Mode)
        self.p1a_btn.place(x=150, y=150) ; self.p1c_btn.place(x=500, y=150) ; self.p1b_btn.place(x=150, y=200) ; self.p1d_btn.place(x=500, y=200) ; self.p2a_btn.place(x=150, y=420)

#----------------------------------------------------------------------------------------------------------------------
    def ReNBpack(self):
        self.count = 0
        self.hideB_label = tk.Label(text = 'xxxx', fg='white', bg='white', font=self.fC) ; self.hideB_label.place(x=835, y=190)
        self.hideN_label = tk.Label(text = 'xxxx', fg='white', bg='white', font=self.fC) ; self.hideN_label.place(x=915, y=190)
        self.ReNext() ; self.ReBack()
    def ReBack(self):
        self.back_btn = tk.Button(self.cvs, text = 'back', highlightbackground='white', command = self.ReBackImage)
        self.back_btn.place(x=840, y=200)
    def ReNext(self):
        self.hideN_label.lower()
        self.next_btn = tk.Button(self.cvs, text = 'next', highlightbackground='white', command = self.ReNextImage)
        self.next_btn.place(x=920, y=200)
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
#----------------------------------------------------------------------------------------------------------------------
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

    def S_pack(self):
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', highlightbackground='white', command = self.create_dlt)
        self.reSt_btn.destroy() ; self.OrCr() ; self.create_btn.lift()
#----------------------------------------------------------------------------------------------------------------------
# shape_1
    def shape_1(self):
        self.signal = 1 ; self.vargin(14, 1)
        self.create_dlt_btn = tk.Button(self.cvs, text = '配置を隠す', highlightbackground = 'white', command = self.create_dlt)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground = 'white', command = self.createS_1)
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
        self.signal = 1 ; self.vargin(14, 2)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground='white', command = self.createS_2)
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
        self.signal = 1 ; self.vargin(14, 3)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground='white', command = self.createS_3)
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
        self.signal = 1 ; self.vargin(15, 1)
        self.create_btn = tk.Button(self.cvs, text = '配置を見る', highlightbackground='white', command = self.createS_4)
        self.S_pack()
        PhotoMove1.canvas = self.cvs ; PhotoMove1()
        PhotoMove2.canvas = self.cvs ; PhotoMove2()
        x = 550 ; y = 400
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


# Creative Mode ============================================================================================================
    # Creative Mode終了時に消去するもの
    def delete_Cmode(self):
        # テキストの削除
        self.txt_box = [self.label_scale, self.label_d, self.txt1, self.label_w, self.txt2, self.label_h, self.txt3, self.label_Cal, self.txt4, self.label_Mul, self.label_Div,
                        self.txt_ex, self.txt_ey, self.label_lw, self.label_lh]
        for dtxt in self.txt_box : dtxt.destroy()
        # 計算の削除
        if self.calNum != 0:
            self.label_dMul.destroy() ; self.label_dDiv.destroy()
        # ボタンの削除
        self.btn_box = [self.crGRw_btn, self.crGRh_btn, self.crCoo_btn, self.deCoo_btn, self.cir_btn, self.rec_btn, self.Cal_btn, self.lin_btn, self.deCir_btn, self.deRec_btn, self.deLin_btn,
                        self.point_radio, self.write_radio, self.erase_radio, self.deLine_btn, self.deFig_btn, self.save_btn]
        for dbtn in self.btn_box : dbtn.destroy()
        # マウスのリセット
        self.cvs.bind('<B1-Motion>', self.reset)

    # Creative Modeのコア
    def Creative_Mode(self):
        # 前処理
        self.signal = 1 ; self.number = -99 ; self.calNum = 0
        self.Pra_delete() ; self.reSt_btn.destroy()
        self.rerl_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.rerl)
        self.rerl_btn.place(x = 900, y = 680)
        self.Coordinate()
        self.drawing()

        # テキスト配置
        # 円，矩形
        self.label_scale = tk.Label(text = 'グリッドの1マス = 10×10(pixel)    黄金長方形の１番大きい正方形 = 300×300(pixel)', bg = 'white') ; self.label_scale.place(x = 82, y = 25)
        #self.cvs.create_rectangle(650, 80, 650+300, 80+300, outline = '#aabbcc', tag = 'adam')
        self.label_d = tk.Label(text = '直径', bg = 'white') ; self.label_d.place(x = 700, y = 542)
        self.txt1 = tk.Entry(width = 6, highlightbackground = 'white') ; self.txt1.place(x = 730, y = 542)
        self.label_w = tk.Label(text = '横幅', bg = 'white') ; self.label_w.place(x = 600, y = 572)
        self.txt2 = tk.Entry(width = 6, highlightbackground = 'white') ; self.txt2.place(x = 630, y = 572)
        self.label_h = tk.Label(text = '高さ', bg = 'white') ; self.label_h.place(x = 700, y = 572)
        self.txt3 = tk.Entry(width = 6, highlightbackground = 'white') ; self.txt3.place(x = 730, y = 572)
        self.label_lw = tk.Label(text = '横幅', bg = 'white') ; self.label_lw.place(x = 600, y = 602)
        self.label_lh = tk.Label(text = '高さ', bg = 'white') ; self.label_lh.place(x = 700, y = 602)

        # 計算
        self.label_Cal = tk.Label(text = '黄金比計算', bg = 'white') ; self.label_Cal.place(x = 150, y = 600)
        self.txt4 = tk.Entry(width = 8, highlightbackground = 'white') ; self.txt4.place(x = 230, y = 600)
        self.label_Mul = tk.Label(text = '× 1.618 =', bg = 'white') ; self.label_Mul.place(x = 330, y = 600)
        self.label_Div = tk.Label(text = '÷ 1.618 =', bg = 'white') ; self.label_Div.place(x = 330, y = 630)
        # 線
        self.txt_ex = tk.Entry(width = 6, highlightbackground = 'white') ; self.txt_ex.place(x = 630, y = 600)
        self.txt_ey = tk.Entry(width = 6, highlightbackground = 'white') ; self.txt_ey.place(x = 730, y = 600)

        # ボタン配置
        # グリッド関係
        self.crGRh_btn = tk.Button(self.cvs, text = '黄金長方形：縦', highlightbackground = 'white', command = self.gridGRh) ; self.crGRh_btn.place(x = 75, y = 50)
        self.crGRw_btn = tk.Button(self.cvs, text = '黄金長方形：横', highlightbackground = 'white', command = self.gridGRw) ; self.crGRw_btn.place(x = 195, y = 50)
        self.crCoo_btn = tk.Button(self.cvs, text = '格子グリッド：ON', highlightbackground = 'white', command = self.gridLine) ; self.crCoo_btn.place(x = 315, y = 50)
        self.deCoo_btn = tk.Button(self.cvs, text = '全グリッド：Off', highlightbackground = 'white', command = self.deleteGrid) ; self.deCoo_btn.place(x = 455, y = 50)
        # 生成関係
        self.cir_btn = tk.Button(self.cvs, text = '円を生成', highlightbackground = 'white', command = self.circle) ; self.cir_btn.place(x = 800, y = 540)
        self.rec_btn = tk.Button(self.cvs, text = '矩形を生成', highlightbackground = 'white', command = self.rectangle) ; self.rec_btn.place(x = 800, y = 570)
        self.Cal_btn = tk.Button(self.cvs, text = '計算する', highlightbackground = 'white', command = self.calGR) ; self.Cal_btn.place(x = 230, y = 630)
        self.lin_btn = tk.Button(self.cvs, text = '線を生成', highlightbackground = 'white', command = self.linetool) ; self.lin_btn.place(x = 800, y = 600)
        # 削除関係
        self.deCir_btn = tk.Button(self.cvs, text = '円を削除', highlightbackground = 'white', command = self.deleteCir) ; self.deCir_btn.place(x = 900, y = 540)
        self.deRec_btn = tk.Button(self.cvs, text = '矩形を削除', highlightbackground = 'white', command = self.deleteRec) ; self.deRec_btn.place(x = 900, y = 570)
        self.deLin_btn = tk.Button(self.cvs, text = '線を削除', highlightbackground = 'white', command = self.deleteLin) ; self.deLin_btn.place(x = 900, y = 600)
        self.deFig_btn = tk.Button(self.cvs, text = '全て削除', highlightbackground = 'white', command = self.deleteFigure) ; self.deFig_btn.place(x = 900, y = 630)
        self.save_btn = tk.Button(self.cvs, text = '保存する', highlightbackground = 'white', command = self.save_canvas) ; self.save_btn.place(x = 800, y = 680)

    # 格子グリッドの作成
    def Coordinate(self):
        k = 80 ; l = 580 ; s = 0 ; t = 0
        for i in range(51):
            self.cvs.create_line(k, k+s, l, k+s, fill = '#aabbcc', tag='coo') ; s += 10
            self.cvs.create_line(k+t, k, k+t, l, fill = '#aabbcc', tag='coo') ; t += 10
    def gridLine(self):
        self.cvs.delete('GRw', 'GRh') ; self.Coordinate()
    # 黄金長方形グリッドの作成 その１
    def gridGRw(self):
        self.cvs.delete('coo', 'GRh')
        f = (1+math.sqrt(5))/2 ; f2 = pow(f,2) ; f3 = pow(f,3) ; f4 = pow(f,4) ; f5 = pow(f,5)
        wx01 = 80 ; wy01 = 180 ; wx11 = wx01+300 ; wy11 = wy01+300 ; ww = wx11-wx01 ; wh = wy11-wy01
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
    # 黄金長方形グリッドの作成　その２
    def gridGRh(self):
        self.cvs.delete('coo', 'GRw')
        f = (1+math.sqrt(5))/2 ; f2 = pow(f,2) ; f3 = pow(f,3) ; f4 = pow(f,4) ; f5 = pow(f,5)
        wx01 = 180 ; wy01 = 100 ; wx11 = wx01+300 ; wy11 = wy01+300 ; ww = wx11-wx01 ; wh = wy11-wy01
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
    # グリッド全削除
    def deleteGrid(self):
        self.cvs.delete('coo', 'GRw', 'GRh')
    # 円の生成
    def circle(self):
        a = float(self.txt1.get()) ; m = 650 ; n = 100
        CanvasOval.canvas = self.cvs
        cc = CanvasOval(m, n, m+a, n+a, outline='#6699ff', width=2.0, tag='crC') ; cc
    # 矩形の生成
    def rectangle(self):
        b = float(self.txt2.get()) ; c = float(self.txt3.get()) ; m = 650 ; n = 100
        Rectangle.canvas = self.cvs
        rt = Rectangle(m, n, m+b, n+c, outline='#6699ff', width=2.0, tag='crR') ; rt
    # 線の生成
    def linetool(self):
        sx = 700 ; sy = 250
        ex = float(self.txt_ex.get())+int(sx) ; ey = float(self.txt_ey.get())+int(sy)
        LINE.canvas = self.cvs
        ln = LINE(sx, sy, ex, ey, fill='#6699ff', width=2.0, tag='crL') ; ln
    # 要素の削除
    def deleteCir(self):self.cvs.delete('crC')
    def deleteRec(self):self.cvs.delete('crR')
    def deleteLin(self):self.cvs.delete('crL')
        
    # 黄金比の計算
    def calGR(self):
        if self.calNum != 0 : self.calGR_delete()
        d = float(self.txt4.get())
        dMul = round(d * ((1+math.sqrt(5))/2), 3) ; dDiv = round(d / ((1+math.sqrt(5))/2), 3)
        self.label_dMul = tk.Label(text = dMul, bg = 'white') ; self.label_dMul.place(x = 400, y = 600)
        self.label_dDiv = tk.Label(text = dDiv, bg ='white') ; self.label_dDiv.place(x = 400, y = 630)
        self.calNum += 1
    # 計算後の数値の削除（上書き）
    def calGR_delete(self):
        self.label_dMul.destroy() ; self.label_dDiv.destroy()

    # ペンツール
    def drawing(self):
        self.vr = tk.IntVar()
        self.vr.set(0)
        self.point_radio = tk.Radiobutton(text='選択ツール', bg = 'white', variable=self.vr, value=0, command=self.change_radio)
        self.point_radio.place(x = 600, y = 510)
        self.write_radio = tk.Radiobutton(text='手描きツール', bg = 'white', variable=self.vr, value=1, command=self.change_radio)
        self.write_radio.place(x = 693, y = 510)
        self.erase_radio = tk.Radiobutton(text='消しゴム', bg = 'white', variable=self.vr, value=2, command=self.change_radio)
        self.erase_radio.place(x = 800, y = 510)
        self.deLine_btn = tk.Button(text = '手描きを削除', highlightbackground = 'white', command = self.deleteLine)
        self.deLine_btn.place(x = 900, y = 510)
        self.cvs.bind('<B1-Motion>', self.paint) ; self.cvs.bind('<ButtonRelease-1>', self.reset)
        self.old_x = None ; self.old_y = None ; self.color = 'black' ; self.eraser_on = None
        self.im = Image.new('RGB', (1050, 650), 'white')
        self.draw = ImageDraw.Draw(self.im)
    def change_radio(self):
        if self.vr.get() == 0 : self.eraser_on = None
        elif self.vr.get() == 1 : self.eraser_on = False
        elif self.vr.get() == 2 : self.eraser_on = True
    def paint(self, event):
        if self.eraser_on == None:
            self.old_x = None ; self.old_y = None
        if self.eraser_on : paint_color = 'white'
        else : paint_color = '#6699ff'
        if self.old_x and self.old_y:
            self.cvs.create_line(self.old_x, self.old_y, event.x, event.y, width=3.0, fill=paint_color,
                                 capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36, tag = 'line')
            self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=paint_color, width=4)
        self.old_x = event.x ; self.old_y = event.y
    def reset(self, event):
        self.old_x, self.old_y = None, None
    def deleteLine(self):
        self.cvs.delete('line')

    # 全て削除
    def deleteFigure(self):
        self.cvs.delete('crC','crR','crL','line')
    
    # セーブ
    def save_canvas(self):
        self.save_num += 1
        self.cvs.postscript(file = 'saveimg/self' + str(self.save_num) + '.ps', colormode='color')


# All & URL============================================================================================================
    def toSt(self):
        self.cvs.delete('all') ; self.reSt_btn.destroy() ; self.Start()
# Logo All
    def LogoAll(self):
        self.start_delete()
        self.reSt_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.toSt)
        self.reSt_btn.place(x = 900, y = 680)
        self.lgall_img = ImageTk.PhotoImage(file = 'image/what_gr/logoall.png')
        self.cvs.create_image(1050/2, 750/2, anchor = 'c', image = self.lgall_img)
# Logo URL
    def LogoURL(self):
        self.start_delete()
        self.reSt_btn = tk.Button(self.cvs, text = 'Return', highlightbackground = 'white', command = self.toSt)
        self.reSt_btn.place(x = 900, y = 680)
        self.lgurl_img = ImageTk.PhotoImage(file = 'image/what_gr/logoURL.png')
        self.cvs.create_image(1050/2, 750/2, anchor = 'c', image = self.lgurl_img)

#======================================================================================================================
if __name__=="__main__":
    win = tk.Tk()
    win.geometry('1050x750')
    win.resizable(width = False, height = False)
    
    M = Main()
    M.pack()
    M.mainloop()