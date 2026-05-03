import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QProgressBar, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtCore import QSize

'''
Tutorials for:
Backgrounds - Line 27
Buttons - Line 53


'''
class MainWind(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Battle Simulator")
        self.setGeometry(0,0, 1280, 800)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        
        #Background
        labelbackground = QLabel(self)
        labelbackground.setGeometry(0,0,1280,800)
        background1 = QPixmap("assets/backgrounds/sampleground.png")
        labelbackground.setPixmap(background1)
        labelbackground.setScaledContents(True)
        
        '''
        QLabel(self) indicates the initialization as an image, and the purpose of Qlabel is to link itself to mainwindows
        setGeometry asks for 4 values: position x and y, height and width.
        QPixmap() asks for a file name, then stores it in a variable for it to be accessed later as can be seen on the next line.
        setScaledContents sets the image to be scaled with the values provided from setGeometry.
        '''
        
        #Hp bar
        labelhp = QLabel(self)
        labelhp.setGeometry(235,30,800,178)
        hpbar = QPixmap("assets/icons/hpbars.png")
        labelhp.setPixmap(hpbar)
        labelhp.setScaledContents(True)
        
        #Battle-related stuff initialization
        self.fightbtn = QPushButton(self)
        self.switchbtn = QPushButton(self)
        self.battle_message = QLabel("Choose your move!", self)
        self.move_slot1btn = QPushButton(self)
        self.move_slot2btn = QPushButton(self)
        self.move_slot3btn = QPushButton(self)
        self.move_slot4btn = QPushButton(self)

        #Ultra Instinct
        self.initUI()
        
    def initUI(self):
        #Pokemon Fight Button
        self.fightbtn.setGeometry(150,475, 500,250)
        self.fightbtn.setIcon(QIcon("assets/icons/fightbtn.png"))
        self.fightbtn.setIconSize(QSize(500, 250))
        self.fightbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.fightbtn.clicked.connect(self.on_click_fightbtn)

        #Pokemon Switch Button
        self.switchbtn.setGeometry(650,475, 500, 250)
        self.switchbtn.setIcon(QIcon("assets/icons/switchbtn.png"))
        self.switchbtn.setIconSize(QSize(500, 250))
        self.switchbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.switchbtn.clicked.connect(self.on_click_switchbtn)

        #Move 1 Button
        self.move_slot1btn.setGeometry(400,500, 200,100)
        self.move_slot1btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot1btn.setIconSize(QSize(200, 100))
        self.move_slot1btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.move_slot1btn.clicked.connect(self.on_click_move_slot1btn)
        self.move_slot1btn.setVisible(False)

        #Move 2 Button
        self.move_slot2btn.setGeometry(600,500, 200,100)
        self.move_slot2btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot2btn.setIconSize(QSize(200, 100))
        self.move_slot2btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.move_slot2btn.clicked.connect(self.on_click_move_slot2btn)
        self.move_slot2btn.setVisible(False)

        #Move 3 Button
        self.move_slot3btn.setGeometry(400,600, 200,100)
        self.move_slot3btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot3btn.setIconSize(QSize(200, 100))
        self.move_slot3btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.move_slot3btn.clicked.connect(self.on_click_move_slot3btn)
        self.move_slot3btn.setVisible(False)

        #Move 4 Button
        self.move_slot4btn.setGeometry(600,600, 200,100)
        self.move_slot4btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot4btn.setIconSize(QSize(200, 100))
        self.move_slot4btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""") #removes white lines around the button
        self.move_slot4btn.clicked.connect(self.on_click_move_slot4btn)
        self.move_slot4btn.setVisible(False)

        #Pokemon Battle Message
        self.battle_message.setGeometry(100, 450, 400, 50)
        self.battle_message.setStyleSheet("font-size: 30px")

        #Shows the Pokemon GIFs
        pkmn1lbl = QLabel(self)
        pkmn1lbl.setGeometry(100, 100, 400, 400)
        pkmn1 = QMovie("assets/pokemon_flipped/AERODACTYL.gif")
        pkmn1lbl.setMovie(pkmn1)
        pkmn1lbl.setScaledContents(True)
        pkmn1lbl.show()
        pkmn1.start()

        pkmn2lbl = QLabel(self)
        pkmn2lbl.setGeometry(800, 100, 400, 400)
        pkmn2 = QMovie("assets/pokemon/MEWTWO.gif")
        pkmn2lbl.setMovie(pkmn2)
        pkmn2lbl.setScaledContents(True)
        pkmn2lbl.show()
        pkmn2.start()

        #HP Bar
        self.max_hp_p1 = 270  #Place current pkmn hp here
        self.current_hp_p1 = self.max_hp_p1

        self.hp_bar_p1 = QProgressBar(self)
        self.hp_bar_p1.setGeometry(405, 43, 113, 20)
        self.hp_bar_p1.setMinimum(0)
        self.hp_bar_p1.setMaximum(self.max_hp_p1)
        self.hp_bar_p1.setValue(self.current_hp_p1)
        self.hp_bar_p1.setTextVisible(True)
        self.hp_bar_p1.setFormat(f"{self.current_hp_p1}/{self.max_hp_p1}")  # This shows "HP/MaxHP"
        self.hp_bar_p1.setStyleSheet("""
            QProgressBar {
                border: 2px solid #555;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00cc00;
                width: 10px;
            }
        """)

        #HP Bar 2
        self.max_hp_p2 = 285  #Place current pkmn hp here
        self.current_hp_p2 = self.max_hp_p2
        self.hp_bar_p2 = QProgressBar(self)
        self.hp_bar_p2.setGeometry(800, 43, 113, 20)
        self.hp_bar_p2.setMinimum(0)
        self.hp_bar_p2.setMaximum(self.max_hp_p2)
        self.hp_bar_p2.setValue(self.current_hp_p2)
        self.hp_bar_p2.setTextVisible(True)
        self.hp_bar_p2.setFormat(f"{self.current_hp_p2}/{self.max_hp_p2}")  # This shows "HP/MaxHP"
        self.hp_bar_p2.setStyleSheet("""
            QProgressBar {
                border: 2px solid #555;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00cc00;
                width: 10px;
            }
        """)
    
    def on_click_fightbtn(self):
        self.battle_message.setText("Fight Button clicked lmao")
        self.fightbtn.setVisible(False)
        self.switchbtn.setVisible(False)
        self.move_slot1btn.setVisible(True)
        self.move_slot2btn.setVisible(True)
        self.move_slot3btn.setVisible(True)
        self.move_slot4btn.setVisible(True)
    def on_click_switchbtn(self):
        self.battle_message.setText("Switch Button clicked you mf")

    def on_click_move_slot1btn(self):
        self.battle_message.setText("Did bro just used {Move 1}?")
        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)
    def on_click_move_slot2btn(self):
        self.battle_message.setText("Did bro just used {Move 2}?")
        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)
    def on_click_move_slot3btn(self):
        self.battle_message.setText("Did bro just used {Move 3}?")
        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)
    def on_click_move_slot4btn(self):
        self.battle_message.setText("Did bro just used {Move 4}?")
        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)
 
def main():
    app = QApplication(sys.argv)
    window = MainWind()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()        