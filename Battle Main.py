from team_selection import get_pokemon_data, get_move_data
from team_selection import MainWind
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLabel, QProgressBar, QDialog, QMessageBox, QListWidgetItem, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt, QSize, QTimer, QPropertyAnimation, QPoint, QEasingCurve, QEvent, QUrl, QRect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys, queue

import random
import os
import time
import json
global_music_player = None
LEADERBOARD_FILE = "leaderboard.json"
class Leaderboard:
    def __init__(self):
        self.scores = {}  # {'Alice': 100, 'Liddell': 50}
        self.assigned_names = {"player1": None, "player2": None}

    def add_player(self, name):
        if name not in self.scores:
            self.scores[name] = 0

    def award_points(self, name, points=50):
        if name in self.scores:
            self.scores[name] += points
            self.save_leaderboard()

    def get_score(self, name):
        return self.scores.get(name, 0)

    def get_all(self):
        return sorted(self.scores.items(), key=lambda x: -x[1])
    
    def save_leaderboard(self):
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump({
                "scores": self.scores,
                "assigned_names": self.assigned_names
            }, f, indent=4)
        print("[DEBUG] Saving leaderboard with scores:", self.scores)

leaderboard = Leaderboard()

class ChooseGameModeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Game Mode")
        self.setGeometry(0, 0, 1280, 800)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.setup_ui()
        global global_music_player
        self.player = QMediaPlayer()
        global_music_player = self.player
        self.assigned_player1 = None
        self.assigned_player2 = None

        
        self.player.stop
        self.music_path = "assets/audio/Volt_Tackle_Instrumental.mp3"
        self.play_music(self.music_path)
        self.player.play()        

    def setup_ui(self):
        self.background_movie = QMovie("assets/backgrounds/TitleScreenGIF.gif")
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1280, 800)
        self.background_label.setMovie(self.background_movie)
        self.background_label.setScaledContents(True)
        self.background_movie.start()

        self.overlay = QWidget(self)
        self.overlay.setGeometry(0, 0, 1280, 800)
        self.overlay.raise_()  # Make sure it's above the background

        # Add the label inside overlay so it's never hidden by background
        self.press_key_label = QLabel("Press Any Key to Continue", self.overlay)
        self.press_key_label.setGeometry(340, 600, 600, 40)
        self.press_key_label.setAlignment(Qt.AlignCenter)
        self.press_key_label.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 128);
        """)
        self.press_key_label.setVisible(True)

        # Animation using opacity
        self.blink_state = True  # currently visible
        self.press_key_label.setVisible(True)

        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(self.blink_label)
        self.blink_timer.start(1000)

        self.show_buttons = False
        self.installEventFilter(self)

        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(330, 10, 650, 400)  # Adjust x, y, width, height as needed
        self.logo_label.setPixmap(QPixmap("assets/backgrounds/GameLogo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.raise_()


        self.button1 = QPushButton(self)
        self.button1.setGeometry(100, 400, 300, 150)
        self.button1.setIcon(QIcon("assets/icons/1playerbtn.png"))
        self.button1.setIconSize(QSize(300, 150))
        self.button1.setStyleSheet("QPushButton { border: none; }")
        self.button1.clicked.connect(lambda: self.set_mode(1))
        self.button1.hide()

        self.button2 = QPushButton(self)
        self.button2.setGeometry(350, 400, 300, 150)
        self.button2.setIcon(QIcon("assets/icons/2playerbtn.png"))
        self.button2.setIconSize(QSize(300, 150))
        self.button2.setStyleSheet("QPushButton { border: none; }")
        self.button2.clicked.connect(lambda: self.set_mode(2))
        self.button2.hide()

        self.leaderboard_button = QPushButton("", self)
        self.leaderboard_button.setGeometry(850, 400, 300, 150)
        self.leaderboard_button.setIcon(QIcon("assets/icons/halloffamebtn.png"))
        self.leaderboard_button.setIconSize(QSize(300, 150))
        self.leaderboard_button.setStyleSheet("QPushButton { border: none; }")
        self.leaderboard_button.clicked.connect(self.open_leaderboard)
        self.leaderboard_button.hide()

        self.challenge_button = QPushButton(self)
        self.challenge_button.setGeometry(600, 400, 300, 150)
        self.challenge_button.setIcon(QIcon("assets/icons/elite4btn.png"))  # Create this asset
        self.challenge_button.setIconSize(QSize(300, 150))
        self.challenge_button.setStyleSheet("QPushButton { border: none; }")
        self.challenge_button.clicked.connect(self.start_challenge_mode)
        self.challenge_button.hide()
        
        self.about_us = QPushButton(self)
        self.about_us.setGeometry(225, 600, 300, 150)
        self.about_us.setIcon(QIcon("assets/icons/aboutus.png"))  # Create this asset
        self.about_us.setIconSize(QSize(300, 150))
        self.about_us.setStyleSheet("QPushButton { border: none; }")
        self.about_us.clicked.connect(self.open_aboutus)
        self.about_us.hide()
        
        self.how_to_play = QPushButton(self)
        self.how_to_play.setGeometry(725, 600, 300, 150)
        self.how_to_play.setIcon(QIcon("assets/icons/howtoplay.png"))  # Create this asset
        self.how_to_play.setIconSize(QSize(300, 150))
        self.how_to_play.setStyleSheet("QPushButton { border: none; }")
        self.how_to_play.clicked.connect(self.open_howtoplay)
        self.how_to_play.hide()

        self.music_path = "assets/audio/Volt_Tackle_Instrumental.mp3"
        self.player = QMediaPlayer()
        self.player.mediaStatusChanged.connect(self.loop_music)
        self.play_music(self.music_path)
        self.player.setVolume(50)  #50% Volume
        self.player.play()

    def play_music(self, music_path):
        self.player.stop()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(music_path)))
        self.player.play()

    def loop_music(self, status):
        if status == QMediaPlayer.EndOfMedia:
            if "The_Elite_4" in self.music_path:
                self.player.play()

    def toggle_press_key_visibility(self):
        self.press_key_label.setVisible(not self.press_key_label.isVisible())
    def eventFilter(self, obj, event):
        if not self.show_buttons and event.type() in (QEvent.KeyPress, QEvent.MouseButtonPress):
            self.reveal_game_mode_buttons()
            return True
        return super().eventFilter(obj, event)
    def reveal_game_mode_buttons(self):
        self.button1.show()
        self.button2.show()
        self.leaderboard_button.show()
        self.challenge_button.show()
        self.about_us.show()
        self.how_to_play.show()
        self.press_key_label.hide()
        self.blink_timer.stop()
        self.show_buttons = True
    def blink_label(self):
        if self.blink_state:
            self.press_key_label.setVisible(False)
            self.blink_timer.start(400)
        else:
            self.press_key_label.setVisible(True)
            self.blink_timer.start(1000)
        self.blink_state = not self.blink_state

    def start_challenge_mode(self):
        self.music_path = "assets/audio/The_Elite_4.mp3"
        self.player.stop()
        self.play_music(self.music_path)
        self.loop_music(-1)
        self.challenge_mode = True
        self.slide_and_close("left", self.open_challenge_team_selector)

    def open_challenge_team_selector(self):
        if "Volt_Tackle_Instrumental" in self.music_path:
            self.player.stop()
        self.team_selector = MainWind(1)
        self.team_selector.challenge_callback = self.show_challenge_options
        self.team_selector.slide_in()
        self.team_selector.show()

    def open_leaderboard(self):
        self.player.stop()
        self.leaderboard_window = LeaderboardWindow(self)
        self.leaderboard_window.show()
        
    def open_aboutus(self):
        self.aboutus_window = aboutus(self)
        self.aboutus_window.show()
        
    def open_howtoplay(self):
        self.howtoplay = tutorial(self)
        self.howtoplay.show()
        print("The window should be showing...")

    def show_challenge_options(self, player_team):
        self.challenge_select_window = ChallengeSelectWindow(player_team)
        self.challenge_select_window.show()

    

    def set_mode(self, mode):
        self.slide_and_close("left", lambda: self._switch_mode(mode))
        if mode == 1:
            self.music_path = "assets/audio/1_Player_Music.mp3"
            self.player.stop()
            self.play_music(self.music_path)
            self.player.play()
            pass
        elif mode == 2:
            self.music_path = "assets/audio/2_Player_Music.mp3"
            self.player.stop()
            self.play_music(self.music_path)
            self.player.play()
            self.team_selector_p1 = MainWind(2)
            self.team_selector_p1.slide_in()
            self.team_selector_p1.setWindowTitle("Player 1: Select Your Team")
            self.team_selector_p1.closed.connect(self.select_player2_team)
            self.team_selector_p1.show()

    def _switch_mode(self, mode):
        if mode == 1:
            self.team_selector = MainWind(1)
            self.team_selector.closed.connect(lambda: self.launch_game(1))
            self.team_selector.show()
        elif mode == 2:
            self.team_selector_p1 = MainWind(2)
            self.team_selector_p1.setWindowTitle("Player 1: Select Your Team")
            self.team_selector_p1.closed.connect(self.select_player2_team)
            self.team_selector_p1.show()

    def slide_and_close(self, direction, after_slide_callback):
        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setDuration(500)
        start_pos = self.pos()
        if direction == "left":
            end_pos = QPoint(-self.width(), self.y())
        elif direction == "right":
            end_pos = QPoint(self.width() * 2, self.y())
        else:
            end_pos = QPoint(self.x(), self.y() + self.height())

        self.anim.setStartValue(start_pos)
        self.anim.setEndValue(end_pos)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(lambda: [self.close(), after_slide_callback()])
        self.anim.start()

    def select_player2_team(self):
        self.team_selector_p2 = MainWind(2)
        self.team_selector_p2.setWindowTitle("Player 2: Select Your Team")
        self.team_selector_p2.closed.connect(lambda: self.launch_game(2))
        self.team_selector_p2.show()

    def launch_game(self, mode):
        #self.player.stop()
        if mode == 1:
            player_team = self.team_selector.selected_team_p1
            opponent_team = generate_random_team()
        else:
            player_team = self.team_selector_p1.selected_team_p1
            opponent_team = self.team_selector_p2.selected_team_p1

        if not player_team or not opponent_team:
            QMessageBox.critical(None, "Error", "One or both teams are empty. Please try again.")
            return

        player1_name = leaderboard.assigned_names.get("player1")
        player2_name = leaderboard.assigned_names.get("player2")
        self.battle_window = battle(player_team, opponent_team, mode, player1_name, player2_name)
        self.battle_window.show()
    
    def choose_challenge_bot(self):
        player_team = self.team_selector.selected_team_p1
        if not player_team:
            QMessageBox.warning(self, "Team Incomplete", "You must choose a team to continue.")
            return

        self.challenge_select_window = ChallengeSelectWindow(player_team)
        self.challenge_select_window.show()

    
def get_challenge_bot_team(index):
    custom_teams = {
        1: [get_pokemon_data(87), get_pokemon_data(91), get_pokemon_data(124), get_pokemon_data(131), get_pokemon_data(134)],#Lorelei
        2: [get_pokemon_data(95), get_pokemon_data(76), get_pokemon_data(107), get_pokemon_data(106), get_pokemon_data(68)],#Bruno
        3: [get_pokemon_data(92), get_pokemon_data(93), get_pokemon_data(94), get_pokemon_data(42), get_pokemon_data(24)],#Agatha
        4: [get_pokemon_data(148), get_pokemon_data(142), get_pokemon_data(130), get_pokemon_data(6), get_pokemon_data(149)],#Lance
    }
    team = custom_teams.get(index)
    if not team:
        return []
    for p in team:
        p['hp'] = p['stats'][0]['base_stat']
        p['pp'] = {move['move']['name']: 10 for move in p['moves']}
        p['status'] = STATUS_NONE
    return team


class ChallengeSelectWindow(QWidget):
    def __init__(self, player_team, parent=None):
        super().__init__()
        self.setWindowTitle("Choose a Challenge")
        self.setGeometry(0, 0, 1280, 800)
        self.player_team = player_team

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1280, 800)
        pixmap = QPixmap("assets/backgrounds/E4Board.png")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        #Lorelei
        self.challenge1 = QPushButton(self)
        self.challenge1.setGeometry(200, 275, 500, 250)
        self.challenge1.setIcon(QIcon("assets/icons/E4-Lorelei.png"))
        self.challenge1.setIconSize(QSize(500, 250))
        self.challenge1.setStyleSheet("QPushButton { border: none; }")
        self.challenge1.clicked.connect(lambda: self.select_challenge(1))

        #Bruno
        self.challenge2 = QPushButton(self)
        self.challenge2.setGeometry(600, 275, 500, 250)
        self.challenge2.setIcon(QIcon("assets/icons/E4-Bruno.png"))
        self.challenge2.setIconSize(QSize(500, 250))
        self.challenge2.setStyleSheet("QPushButton { border: none; }")
        self.challenge2.clicked.connect(lambda: self.select_challenge(2))

        #Agatha
        self.challenge3 = QPushButton(self)
        self.challenge3.setGeometry(200, 550, 500, 250)
        self.challenge3.setIcon(QIcon("assets/icons/E4-Agatha.png"))
        self.challenge3.setIconSize(QSize(500, 250))
        self.challenge3.setStyleSheet("QPushButton { border: none; }")
        self.challenge3.clicked.connect(lambda: self.select_challenge(3))

        #Lance
        self.challenge4 = QPushButton(self)
        self.challenge4.setGeometry(600, 550, 500, 250)
        self.challenge4.setIcon(QIcon("assets/icons/E4-Lance.png"))
        self.challenge4.setIconSize(QSize(500, 250))
        self.challenge4.setStyleSheet("QPushButton { border: none; }")
        self.challenge4.clicked.connect(lambda: self.select_challenge(4))

    def select_challenge(self, index):
        bot_team = get_challenge_bot_team(index)
        self.battle = battle(self.player_team, bot_team, 1, leaderboard.assigned_names.get("player1"), "ChallengeBot")
        self.battle.show()
        self.close()

    


from PyQt5.QtWidgets import QLineEdit, QListWidget
class LeaderboardWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent_window = parent
        self.setWindowTitle("Leaderboard")
        self.setGeometry(400, 200, 600, 400)
        self.setStyleSheet("background-color: #222; color: white; font-size: 16px;")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter Player Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type name and press Add")
        self.add_button = QPushButton("Add Player")
        self.add_button.clicked.connect(self.add_player)

        self.list_widget = QListWidget()

        p1 = leaderboard.assigned_names.get("player1") or "None"
        p2 = leaderboard.assigned_names.get("player2") or "None"
        self.p1_label = QLabel(f"Player 1: {p1}")
        self.p2_label = QLabel(f"Player 2: {p2}")

        self.assign_p1_button = QPushButton("Assign to Player 1")
        self.assign_p2_button = QPushButton("Assign to Player 2")
        self.assign_p1_button.clicked.connect(lambda: self.assign_player(1))
        self.assign_p2_button.clicked.connect(lambda: self.assign_player(2))

        self.sort_button = QPushButton("Sort: Score ↓", self)
        self.sort_button.clicked.connect(self.toggle_sort_order)
        self.sort_order = 'score_desc'
        layout.addWidget(self.sort_button)

        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.add_button)
        layout.addWidget(QLabel("Players:"))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.p1_label)
        layout.addWidget(self.assign_p1_button)
        layout.addWidget(self.p2_label)
        layout.addWidget(self.assign_p2_button)

        self.setLayout(layout)
        self.update_list()

    def add_player(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Invalid Input", "Name cannot be empty.")
            return

        leaderboard.add_player(name)
        leaderboard.save_leaderboard()

        self.name_input.clear()
        self.update_list()

    def assign_player(self, player_num):
        selected = self.list_widget.currentItem()
        if not selected:
            QMessageBox.warning(self, "No Selection", "Please select a player from the list.")
            return

        name = selected.text().split(" - ")[0]
        leaderboard.add_player(name)
        leaderboard.award_points(name, 0)
        leaderboard.save_leaderboard()

        if player_num == 1:
            self.p1_label.setText(f"Player 1: {name}")
            self.parent_window.assigned_player1 = name
            leaderboard.assigned_names["player1"] = name
        else:
            self.p2_label.setText(f"Player 2: {name}")
            self.parent_window.assigned_player2 = name
            leaderboard.assigned_names["player2"] = name

        leaderboard.save_leaderboard()
        self.refresh_scores()
        self.update_list()

        if self.parent_window.assigned_player1 and self.parent_window.assigned_player2:
            self.parent_window.launch_game(2)
            self.close()


    def update_list(self):
        self.list_widget.clear()
        for name, score in self.get_sorted_scores():
            self.list_widget.addItem(f"{name} - {score}")
    
    def refresh_scores(self):
        load_leaderboard()
        self.update_list()

    def toggle_sort_order(self):
        orders = ['score_desc', 'score_asc', 'name_asc', 'name_desc']
        current_index = orders.index(self.sort_order)
        self.sort_order = orders[(current_index + 1) % len(orders)]

        label_map = {
            'score_desc': "Sort: Score (descending)",
            'score_asc': "Sort: Score (ascending)",
            'name_asc': "Sort: Name (A-Z)",
            'name_desc': "Sort: Name (Z-A)"
        }
        self.sort_button.setText(label_map[self.sort_order])
        self.update_list()

    def get_sorted_scores(self):
        scores = leaderboard.get_all()
        if self.sort_order == 'score_asc':
            return sorted(scores, key=lambda x: x[1])
        elif self.sort_order == 'score_desc':
            return sorted(scores, key=lambda x: -x[1])
        elif self.sort_order == 'name_asc':
            return sorted(scores, key=lambda x: x[0].lower())
        elif self.sort_order == 'name_desc':
            return sorted(scores, key=lambda x: x[0].lower(), reverse=True)
        return scores
    
class aboutus(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent_window = parent
        self.setWindowTitle("Meet the programmers!")
        self.setGeometry(0, 0, 1280, 750)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.init_ui()
    
    def init_ui(self):
        
        self.background1 = QLabel(self)
        self.background1.setGeometry(0, 0, 1280, 750)
        backpic1 = QPixmap("assets/backgrounds/backpic1.png")
        self.background1.setPixmap(backpic1)
        self.background1.setScaledContents(True)
        
        self.aboutuspic = QLabel(self)
        self.aboutuspic.setGeometry(35, 70, 1200, 600)
        aboutusp = QPixmap("assets/backgrounds/about_us.png")
        self.aboutuspic.setPixmap(aboutusp)
        self.aboutuspic.setScaledContents(True)
        
class tutorial(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent_window = parent
        self.setWindowTitle("How to play?")
        self.setGeometry(0, 0, 1280, 750)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.init_ui()
        self.page = 1

    def init_ui(self):
        #Background
        self.background1 = QLabel(self)
        self.background1.setGeometry(0, 0, 1280, 750)
        backpic1 = QPixmap("assets/backgrounds/backpic1.png")
        self.background1.setPixmap(backpic1)
        self.background1.setScaledContents(True)
        
        #Next button
        self.nextbtn = QPushButton(self)
        self.nextbtn.setGeometry(1050, 35, 180, 100)
        self.nextbtn.setIcon(QIcon("assets/icons/nextbtn.png"))
        self.nextbtn.setIconSize(QSize(300, 100))
        self.nextbtn.setStyleSheet("font-size: 20px")
        self.nextbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nextbtn.clicked.connect(self.next_page)
        
        #Previous button
        self.prevbtn = QPushButton(self)
        self.prevbtn.setGeometry(10, 35, 180, 100)
        self.prevbtn.setIcon(QIcon("assets/icons/prevbtn.png"))
        self.prevbtn.setIconSize(QSize(300, 100))
        self.prevbtn.setStyleSheet("font-size: 20px")
        self.prevbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.prevbtn.clicked.connect(self.prev_page)

        
        #Page 1
        self.helppage1 = QLabel(self)
        self.helppage1.setGeometry(35, 120, 1200, 600)
        page1 = QPixmap("assets/backgrounds/htp_page1.png")
        self.helppage1.setPixmap(page1)
        self.helppage1.setScaledContents(True)
        
        #Page 2
        self.helppage2 = QLabel(self)
        self.helppage2.setGeometry(35, 120, 1200, 600)
        page2 = QPixmap("assets/backgrounds/htp_page2.png")
        self.helppage2.setPixmap(page2)
        self.helppage2.setScaledContents(True)
        self.helppage2.hide()
        
        #Page 3
        self.helppage3 = QLabel(self)
        self.helppage3.setGeometry(35, 120, 1200, 600)
        page3 = QPixmap("assets/backgrounds/htp_page3.png")
        self.helppage3.setPixmap(page3)
        self.helppage3.setScaledContents(True)
        self.helppage3.hide()
        
        #Page 4
        self.helppage4 = QLabel(self)
        self.helppage4.setGeometry(35, 120, 1200, 600)
        page4 = QPixmap("assets/backgrounds/htp_page4.png")
        self.helppage4.setPixmap(page4)
        self.helppage4.setScaledContents(True)
        self.helppage4.hide()
    
    def page_handler(self, page):
        if self.page <= 0:
            self.page = 1
        elif self.page == 1:
            self.helppage1.show()
            self.helppage2.hide()
            self.helppage3.hide()
            self.helppage4.hide()
        elif self.page == 2:
            self.helppage1.hide()
            self.helppage2.show()
            self.helppage3.hide()
            self.helppage4.hide()
        elif self.page == 3:
            self.helppage1.hide()
            self.helppage2.hide()
            self.helppage3.show()
            self.helppage4.hide()
        elif self.page == 4:
            self.helppage1.hide()
            self.helppage2.hide()
            self.helppage3.hide()
            self.helppage4.show()
        elif self.page >= 5:
            self.page = 4
        
    def next_page(self):
        self.page += 1
        print("Next page...")
        self.page_handler(self.page)

    
    def prev_page(self):
        self.page -= 1
        print("Previous page...")
        self.page_handler(self.page)    

        
        


def choose_game_mode():
    global app
    global game_mode
    global choose_window_instance
    choose_window_instance = ChooseGameModeWindow()
    choose_window_instance.show()

def restart_game():
    clear_screen()
    if game_mode == 1:
        player_team = get_teams_from_gui(game_mode)
        opponent_team = generate_random_team()
        battle(player_team, opponent_team, None, None)
    elif game_mode == 2:
        team_p1, team_p2 = get_teams_from_gui(game_mode)
        battle(None, None, team_p1, team_p2)

def end_game():
    raise SystemExit

GEN1_POKEMON_COUNT = 151

STATUS_NONE = 'None'
STATUS_POISON = 'Poison'
STATUS_BURN = 'Burn'
game_mode = None

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)
            leaderboard.scores = data.get("scores", {})
            leaderboard.assigned_names = data.get("assigned_names", {"player1": None, "player2": None})
    else:
        leaderboard.scores = {}
        leaderboard.assigned_names = {"player1": None, "player2": None}






TYPE_EFFECTIVENESS = {
    "normal": {"rock": 0.5, "steel": 0.5, "ghost": 0},
    "fire": {"grass": 2, "ice": 2, "bug": 2, "steel": 2, "fire": 0.5, "water": 0.5, "rock": 0.5, "dragon": 0.5},
    "water": {"fire": 2, "ground": 2, "rock": 2, "water": 0.5, "grass": 0.5, "dragon": 0.5},
    "electric": {"water": 2, "flying": 2, "electric": 0.5, "grass": 0.5, "ground": 0, "dragon": 0.5},
    "grass": {"water": 2, "ground": 2, "rock": 2, "fire": 0.5, "grass": 0.5, "poison": 0.5, "flying": 0.5, "bug": 0.5, "dragon": 0.5, "steel": 0.5},
    "ice": {"grass": 2, "ground": 2, "flying": 2, "dragon": 2, "fire": 0.5, "water": 0.5, "ice": 0.5, "steel": 0.5},
    "fighting": {"normal": 2, "ice": 2, "rock": 2, "dark": 2, "steel": 2, "fairy": 0.5, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "ghost": 0},
    "poison": {"grass": 2, "fairy": 2, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0},
    "ground": {"fire": 2, "electric": 2, "poison": 2, "rock": 2, "steel": 2, "grass": 0.5, "flying": 0, "bug": 0.5},
    "flying": {"grass": 2, "fighting": 2, "bug": 2, "electric": 0.5, "rock": 0.5, "steel": 0.5},
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "dark": 0, "steel": 0.5},
    "bug": {"grass": 2, "psychic": 2, "fire": 0.5, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "ghost": 0.5, "steel": 0.5, "fairy": 0.5},
    "rock": {"fire": 2, "ice": 2, "dark": 2, "fighting": 0.5, "ground": 0.5, "flying": 2, "bug": 2, "steel": 0.5},
    "ghost": {"psychic": 2, "ghost": 2, "dark": 0.5, "normal": 0},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"psychic": 2, "ghost": 2, "fighting": 0.5, "bug": 0.5, "dark": 0.5, "fairy": 0.5},
    "steel": {"ice": 2, "rock": 2, "fairy": 2, "fire": 0.5, "water": 0.5, "electric": 0.5, "steel": 0.5},
    "fairy": {"fighting": 2, "dragon": 2, "dark": 2, "poison": 0.5, "fire": 0.5, "steel": 0.5},
}

STAT_INDEX = {
    'hp': 0,
    'attack': 1,
    'defense': 2,
    'special attack': 3,
    'special defense': 4,
    'speed': 5,
}

DRAIN_MOVES = {
    'leech-life': 0.5,
    'giga-drain': 0.5,
    'mega-drain': 0.5,
    'absorb': 0.5,
    'dream-eater': 0.5,
}

RECOIL_MOVES = {
    'take-down': 0.33,
    'explosion': 5.0,
    'double-edge': 0.33,
    'flare-blitz': 0.33,
    'volt-tackle': 0.33,
    'brave-bird': 0.33,
}

MULTI_HIT_MOVES = {
    'double-kick': (2, 2),
    'double-hit': (2, 2),
    'bonemerang': (2, 2),
    'twineedle': (2, 2),
    'bone-rush': (2, 5),
    'fury-attack': (2, 5),
    'rock-blast': (2, 5),
    'pin-missile': (2, 5),
    'bullet-seed': (2, 5),
}

STAT_BOOST_MOVES = {
    'swords-dance': {'attack': 2},
    'agility': {'speed': 2},
    'iron-defense': {'defense': 2},
    'belly-drum': {'attack': 6},
    'dragon-dance': {'attack': 1, 'speed': 1},
    'growth': {'special attack': 1, 'attack': 1},
    'calm-mind': {'special attack': 1, 'special defense': 1},
}
SELF_DEBUFF_MOVES = {
    'close-combat': {
        'defense': -1,
        'special defense': -1,
    },
    'draco-meteor': {
        'special attack': -2,
    },
}

def get_type_effectiveness(attacking_type, defending_type):
    return TYPE_EFFECTIVENESS.get(attacking_type, {}).get(defending_type, 1.0)

def display_pokemon_list():
    print("\nLoading Pokémon list... (This may take a while)")
    for i in range(1, GEN1_POKEMON_COUNT + 1):
        pokemon = get_pokemon_data(i)
        if pokemon:
            print(f"{i}. {pokemon['name'].capitalize()}")

def get_teams_from_gui(game_mode):
    global team_selector_window

    if game_mode == 1:
        team_selector_window = MainWind(game_mode)
        team_selector_window.show()
        app.exec_()
        return team_selector_window.selected_team_p1

    elif game_mode == 2:
        # Player 1 Selection
        team_selector_window = MainWind(game_mode)
        team_selector_window.setWindowTitle("Player 1: Select Your Team")
        team_selector_window.show()
        app.exec_()
        team_p1 = team_selector_window.selected_team_p1

        # Player 2 Selection
        team_selector_window = MainWind(game_mode)
        team_selector_window.setWindowTitle("Player 2: Select Your Team")
        team_selector_window.show()
        app.exec_()
        team_p2 = team_selector_window.selected_team_p1  #we reused selected_team_p1 for p2 selection

        return team_p1, team_p2


def generate_random_team(size=6):
    team = []
    while len(team) < size:
        poke_id = random.randint(1, GEN1_POKEMON_COUNT)
        pokemon = get_pokemon_data(poke_id)
        if pokemon:
            pokemon['hp'] = pokemon['stats'][0]['base_stat']
            pokemon['pp'] = {move['move']['name']: 10 for move in pokemon['moves']}
            pokemon['status'] = STATUS_NONE
            team.append(pokemon)
    return team

def transform(user_pokemon, target_pokemon):
    for i in range(1, len(user_pokemon['stats'])):
        user_pokemon['stats'][i]['base_stat'] = target_pokemon['stats'][i]['base_stat']

    user_pokemon['types'] = target_pokemon['types']

    user_pokemon['moves'] = target_pokemon['moves']
    user_pokemon['pp'] = {move['move']['name']: 15 for move in user_pokemon['moves']}


def select_move(pokemon, opponent):
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    print(f"\nAvailable moves for {pokemon['name'].capitalize()}:")
    for i, move in enumerate(moves):
        if move in pokemon['pp']:  # Ensure PP data exists for the move
            print(f"{i+1}. {move.capitalize()} (PP: {pokemon['pp'][move]})")

    while True:
        try:
            move_choice = int(input("Choose a move by number: ")) - 1
            if 0 <= move_choice < len(moves):
                selected_move = moves[move_choice]
                if pokemon['pp'][selected_move] > 0:
                    if selected_move == 'transform':
                        transform(pokemon, opponent)
                        print(f"{pokemon['name'].capitalize()} transformed into {opponent['name'].capitalize()}!")
                        time.sleep(2)
                    else:
                        pokemon['pp'][selected_move] -= 1
                    return selected_move
                print("No PP left for this move. Choose another.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def ai_select_move(pokemon, opponent):
    moves = [move['move']['name'] for move in pokemon['moves'][:4]]
    available_moves = [move for move in moves if pokemon['pp'].get(move, 0) > 0]

    if 'transform' in available_moves:
        transform(pokemon, opponent)
        print(f"{pokemon['name'].capitalize()} transformed into {opponent['name'].capitalize()}!")
        time.sleep(2)
        return 'transform'
    
    super_effective_moves = []
    for move in available_moves:
        move_data = get_move_data(move)
        if move_data:
            move_type = move_data['type']
            effectiveness = 1.0
            for d_type in [t['type']['name'] for t in opponent['types']]:
                effectiveness *= get_type_effectiveness(move_type, d_type)
            if effectiveness == 2.0:
                super_effective_moves.append(move)

    if super_effective_moves:
        selected = random.choice(super_effective_moves)
        pokemon['pp'][selected] -= 1
        return selected

    if available_moves:
        move = random.choice(available_moves)
        pokemon['pp'][move] -= 1
        return move
    return None


def calculate_damage(attacker, defender, move_name):
    move_data = get_move_data(move_name)
    if not move_data or 'power' not in move_data or move_data['power'] is None:
        return 0  

    power = move_data['power']
    attacking_type = move_data['type']
    defending_types = [t['type']['name'] for t in defender['types']]

    # --- Choose stats based on move category ---
    if move_data.get('category') == 'special':
        attack_stat = attacker['stats'][3]['base_stat']   # SpATK
        defense_stat = defender['stats'][4]['base_stat']  # SpDEF
    else:  # Defaults to physical if not specified
        attack_stat = attacker['stats'][1]['base_stat']   # ATK
        defense_stat = defender['stats'][2]['base_stat']  # DEF
    # ---------------------------------------------

    # --- STAB Calculation ---
    attacker_types = [t['type']['name'] for t in attacker['types']]
    stab = 1.5 if attacking_type in attacker_types else 1.0

    # --- Type Effectiveness ---
    effectiveness = 1.0
    for d_type in defending_types:
        effectiveness *= get_type_effectiveness(attacking_type, d_type)

    # --- Final Damage Formula ---
    damage = (((2 * 50 / 5 + 2) * power * (attack_stat / defense_stat)) / 50 + 2) * stab * effectiveness
    return max(1, int(damage)), effectiveness


def switch_pokemon(team):
    print("\nChoose a Pokémon to switch to:")
    for i, pokemon in enumerate(team):
        if pokemon['hp'] > 0:
            print(f"{i+1}. {pokemon['name'].capitalize()} (HP: {pokemon['hp']})")

    while True:
        try:
            choice = int(input("Enter the number of the Pokémon you want to switch to: ")) - 1
            if 0 <= choice < len(team) and team[choice]['hp'] > 0:
                return team[choice]
            print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def ai_switch_pokemon(team):
    for pokemon in team:
        if pokemon['hp'] > 0:
            return pokemon
    return None

def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


class battle(QWidget):
    def __init__(self, player_team, opponent_team, game_mode, player1_name=None, player2_name=None):
        super().__init__()
        self.sfx_player = QMediaPlayer()
        self.game_mode = game_mode
        if not player_team or not opponent_team:
            raise ValueError("Error: One of the teams is empty! Cannot start battle.")

        self.player1_name = player1_name
        self.player2_name = player2_name

        self.player_team = player_team
        self.opponent_team = opponent_team
        self.player_pokemon = player_team[0]
        self.opponent_pokemon = opponent_team[0]
        self.game_mode = game_mode

        self.message_queue = queue.Queue()
        self.message_timer = QTimer(self)
        self.message_timer.setSingleShot(True)
        self.message_timer.timeout.connect(self.show_next_message)

        self.message_timer2 = QTimer(self)
        self.message_timer2.setSingleShot(True)
        self.message_timer2.timeout.connect(self.update_battle_message2)

        self.player_switched = False
        self.opponent_switched = False

        self.p1_ready = False
        self.p2_ready = False
        self.p1_action = None
        self.p2_action = None

        self.initUI()

    def initUI(self):
        print(f"[DEBUG] Starting battle: player1_name = {self.player1_name}, player2_name = {self.player2_name}")

        self.setWindowTitle("Pokemon Battle Simulator")
        self.setGeometry(0, 0, 1280, 800)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))

        player_name = self.player_pokemon['name'].upper().replace("-", "").replace(" ", "").replace(".", "")
        opponent_name = self.opponent_pokemon['name'].upper().replace("-", "").replace(" ", "").replace(".", "")

        # Background
        self.labelbackground = QLabel(self)
        self.labelbackground.setGeometry(0, 0, 1280, 800)
        background1 = QPixmap("assets/backgrounds/sampleground.png")
        self.labelbackground.setPixmap(background1)
        self.labelbackground.setScaledContents(True)
        
        # Pokemon tile 1 
        self.tile1 = QLabel(self)
        self.tile1.setGeometry(100, 340, 400, 160)
        tilemon = QPixmap("assets/backgrounds/tile.png")
        self.tile1.setPixmap(tilemon)
        self.tile1.setScaledContents(True)
        
        # Pokemon tile 2 
        self.tile2 = QLabel(self)
        self.tile2.setGeometry(750, 340, 400, 160)
        tilemon2 = QPixmap("assets/backgrounds/tile2.png")
        self.tile2.setPixmap(tilemon2)
        self.tile2.setScaledContents(True)

        #Hp bar
        labelhp = QLabel(self)
        labelhp.setGeometry(235,30,800,178)
        hpbar = QPixmap("assets/icons/hpbars.png")
        labelhp.setPixmap(hpbar)
        labelhp.setScaledContents(True)

        #Dialog Box
        self.dialogbox = QLabel(self)
        self.dialogbox.setGeometry(490, 580, 750, 110)
        dialogbox = QPixmap("assets/icons/dialogboxshort.png")
        self.dialogbox.setPixmap(dialogbox)
        self.dialogbox.setScaledContents(True)

        # Battle Message
        self.battle_message1 = QLabel("", self)
        self.battle_message1.setGeometry(540, 600, 800, 25)
        self.battle_message1.setStyleSheet("font-size: 20px; color: black;")

        self.battle_message2 = QLabel("", self)
        self.battle_message2.setGeometry(540, 630, 800, 25)
        self.battle_message2.setStyleSheet("font-size: 20px; color: black;")

        # Fight Button
        self.fightbtn = QPushButton(self)
        self.fightbtn.setGeometry(80, 525, 200, 80)
        self.fightbtn.setIcon(QIcon("assets/icons/fightbtn.png"))
        self.fightbtn.setIconSize(QSize(200, 80))
        self.fightbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.fightbtn.clicked.connect(self.show_move_buttons)

        # Switch Button
        self.switchbtn = QPushButton(self)
        self.switchbtn.setGeometry(80, 600, 200, 80)
        self.switchbtn.setIcon(QIcon("assets/icons/switchbtn.png"))
        self.switchbtn.setIconSize(QSize(200, 80))
        self.switchbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.switchbtn.clicked.connect(self.switch_pokemon)
        if len(self.player_team) == 1:
            self.switchbtn.setEnabled(False)
        else:
            self.switchbtn.setEnabled(True)
        

        # Move Buttons
        self.move_slot1btn = QPushButton(self)
        self.move_slot1btn.setGeometry(80, 500, 200, 100)
        self.move_slot1btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot1btn.setIconSize(QSize(200, 100))
        self.move_slot1btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot1btn.clicked.connect(lambda: self.use_move(0))
        self.move_slot1btn.setVisible(False)

        self.move_slot2btn = QPushButton(self)
        self.move_slot2btn.setGeometry(280, 500, 200, 100)
        self.move_slot2btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot2btn.setIconSize(QSize(200, 100))
        self.move_slot2btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot2btn.clicked.connect(lambda: self.use_move(1))
        self.move_slot2btn.setVisible(False)

        self.move_slot3btn = QPushButton(self)
        self.move_slot3btn.setGeometry(80, 600, 200, 100)
        self.move_slot3btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot3btn.setIconSize(QSize(200, 100))
        self.move_slot3btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot3btn.clicked.connect(lambda: self.use_move(2))
        self.move_slot3btn.setVisible(False)

        self.move_slot4btn = QPushButton(self)
        self.move_slot4btn.setGeometry(280, 600, 200, 100)
        self.move_slot4btn.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot4btn.setIconSize(QSize(200, 100))
        self.move_slot4btn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot4btn.clicked.connect(lambda: self.use_move(3))
        self.move_slot4btn.setVisible(False)

        # Pokémon GIFs
        self.pkmn1lbl = QLabel(self)
        self.pkmn1lbl.setGeometry(100, 100, 350, 350)
        self.pkmn1gif = QMovie(f"assets/pokemon_flipped/{player_name}.gif")
        self.pkmn1lbl.setMovie(self.pkmn1gif)
        self.pkmn1lbl.setScaledContents(True)
        self.pkmn1gif.start()

        self.pkmn2lbl = QLabel(self)
        self.pkmn2lbl.setGeometry(800, 100, 350, 350)
        self.pkmn2gif = QMovie(f"assets/pokemon/{opponent_name}.gif")
        self.pkmn2lbl.setMovie(self.pkmn2gif)
        self.pkmn2lbl.setScaledContents(True)
        self.pkmn2gif.start()

        # Player 1 Attack(Fire) GIF
        self.p1FireAttacklbl = QLabel(self)
        self.p1FireAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1FireAttackgif = QMovie(f"assets/animation/FIRE_ATTACK.gif")
        self.p1FireAttacklbl.setMovie(self.p1FireAttackgif)
        self.p1FireAttacklbl.setScaledContents(True)
        #self.p1FireAttackgif.start()
        # Player 2 Attack(Fire) GIF
        self.p2FireAttacklbl = QLabel(self)
        self.p2FireAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2FireAttackgif = QMovie(f"assets/animation/FIRE_ATTACK.gif")
        self.p2FireAttacklbl.setMovie(self.p2FireAttackgif)
        self.p2FireAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Electric) GIF
        self.p1ElectricAttacklbl = QLabel(self)
        self.p1ElectricAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1ElectricAttackgif = QMovie(f"assets/animation/ELECTRIC_ATTACK.gif")
        self.p1ElectricAttacklbl.setMovie(self.p1ElectricAttackgif)
        self.p1ElectricAttacklbl.setScaledContents(True)
        #self.p1FireAttackgif.start()
        # Player 2 Attack(Electric) GIF
        self.p2ElectricAttacklbl = QLabel(self)
        self.p2ElectricAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2ElectricAttackgif = QMovie(f"assets/animation/ELECTRIC_ATTACK.gif")
        self.p2ElectricAttacklbl.setMovie(self.p2ElectricAttackgif)
        self.p2ElectricAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Bug) GIF
        self.p1BugAttacklbl = QLabel(self)
        self.p1BugAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1BugAttackgif = QMovie(f"assets/animation/BUG_ATTACK.gif")
        self.p1BugAttacklbl.setMovie(self.p1BugAttackgif)
        self.p1BugAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Bug) GIF
        self.p2BugAttacklbl = QLabel(self)
        self.p2BugAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2BugAttackgif = QMovie(f"assets/animation/BUG_ATTACK.gif")
        self.p2BugAttacklbl.setMovie(self.p2BugAttackgif)
        self.p2BugAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Dark) GIF
        self.p1DarkAttacklbl = QLabel(self)
        self.p1DarkAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1DarkAttackgif = QMovie(f"assets/animation/DARK_ATTACK.gif")
        self.p1DarkAttacklbl.setMovie(self.p1DarkAttackgif)
        self.p1DarkAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Dark) GIF
        self.p2DarkAttacklbl = QLabel(self)
        self.p2DarkAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2DarkAttackgif = QMovie(f"assets/animation/DARK_ATTACK.gif")
        self.p2DarkAttacklbl.setMovie(self.p2DarkAttackgif)
        self.p2DarkAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Dragon) GIF
        self.p1DragonAttacklbl = QLabel(self)
        self.p1DragonAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1DragonAttackgif = QMovie(f"assets/animation/DRAGON_ATTACK.gif")
        self.p1DragonAttacklbl.setMovie(self.p1DragonAttackgif)
        self.p1DragonAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Dark) GIF
        self.p2DragonAttacklbl = QLabel(self)
        self.p2DragonAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2DragonAttackgif = QMovie(f"assets/animation/DRAGON_ATTACK.gif")
        self.p2DragonAttacklbl.setMovie(self.p2DragonAttackgif)
        self.p2DragonAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Fairy) GIF
        self.p1FairyAttacklbl = QLabel(self)
        self.p1FairyAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1FairyAttackgif = QMovie(f"assets/animation/FAIRY_ATTACK.gif")
        self.p1FairyAttacklbl.setMovie(self.p1FairyAttackgif)
        self.p1FairyAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Fairy) GIF
        self.p2FairyAttacklbl = QLabel(self)
        self.p2FairyAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2FairyAttackgif = QMovie(f"assets/animation/FAIRY_ATTACK.gif")
        self.p2FairyAttacklbl.setMovie(self.p2FairyAttackgif)
        self.p2FairyAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Fighting) GIF
        self.p1FightingAttacklbl = QLabel(self)
        self.p1FightingAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1FightingAttackgif = QMovie(f"assets/animation/FIGHTING_ATTACK.gif")
        self.p1FightingAttacklbl.setMovie(self.p1FightingAttackgif)
        self.p1FightingAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Fighting) GIF
        self.p2FightingAttacklbl = QLabel(self)
        self.p2FightingAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2FightingAttackgif = QMovie(f"assets/animation/FIGHTING_ATTACK.gif")
        self.p2FightingAttacklbl.setMovie(self.p2FightingAttackgif)
        self.p2FightingAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Flying) GIF
        self.p1FlyingAttacklbl = QLabel(self)
        self.p1FlyingAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1FlyingAttackgif = QMovie(f"assets/animation/FLYING_ATTACK.gif")
        self.p1FlyingAttacklbl.setMovie(self.p1FlyingAttackgif)
        self.p1FlyingAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Flying) GIF
        self.p2FlyingAttacklbl = QLabel(self)
        self.p2FlyingAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2FlyingAttackgif = QMovie(f"assets/animation/FLYING_ATTACK.gif")
        self.p2FlyingAttacklbl.setMovie(self.p2FlyingAttackgif)
        self.p2FlyingAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Ghost) GIF
        self.p1GhostAttacklbl = QLabel(self)
        self.p1GhostAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1GhostAttackgif = QMovie(f"assets/animation/GHOST_ATTACK.gif")
        self.p1GhostAttacklbl.setMovie(self.p1GhostAttackgif)
        self.p1GhostAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Ghost) GIF
        self.p2GhostAttacklbl = QLabel(self)
        self.p2GhostAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2GhostAttackgif = QMovie(f"assets/animation/GHOST_ATTACK.gif")
        self.p2GhostAttacklbl.setMovie(self.p2GhostAttackgif)
        self.p2GhostAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Grass) GIF
        self.p1GrassAttacklbl = QLabel(self)
        self.p1GrassAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1GrassAttackgif = QMovie(f"assets/animation/GRASS_ATTACK.gif")
        self.p1GrassAttacklbl.setMovie(self.p1GrassAttackgif)
        self.p1GrassAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Grass) GIF
        self.p2GrassAttacklbl = QLabel(self)
        self.p2GrassAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2GrassAttackgif = QMovie(f"assets/animation/GRASS_ATTACK.gif")
        self.p2GrassAttacklbl.setMovie(self.p2GrassAttackgif)
        self.p2GrassAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Ground) GIF
        self.p1GroundAttacklbl = QLabel(self)
        self.p1GroundAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1GroundAttackgif = QMovie(f"assets/animation/GROUND_ATTACK.gif")
        self.p1GroundAttacklbl.setMovie(self.p1GroundAttackgif)
        self.p1GroundAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Ground) GIF
        self.p2GroundAttacklbl = QLabel(self)
        self.p2GroundAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2GroundAttackgif = QMovie(f"assets/animation/GROUND_ATTACK.gif")
        self.p2GroundAttacklbl.setMovie(self.p2GroundAttackgif)
        self.p2GroundAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Ice) GIF
        self.p1IceAttacklbl = QLabel(self)
        self.p1IceAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1IceAttackgif = QMovie(f"assets/animation/ICE_ATTACK.gif")
        self.p1IceAttacklbl.setMovie(self.p1IceAttackgif)
        self.p1IceAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Ice) GIF
        self.p2IceAttacklbl = QLabel(self)
        self.p2IceAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2IceAttackgif = QMovie(f"assets/animation/ICE_ATTACK.gif")
        self.p2IceAttacklbl.setMovie(self.p2IceAttackgif)
        self.p2IceAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Normal) GIF
        self.p1NormalAttacklbl = QLabel(self)
        self.p1NormalAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1NormalAttackgif = QMovie(f"assets/animation/NORMAL_ATTACK.gif")
        self.p1NormalAttacklbl.setMovie(self.p1NormalAttackgif)
        self.p1NormalAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Normal) GIF
        self.p2NormalAttacklbl = QLabel(self)
        self.p2NormalAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2NormalAttackgif = QMovie(f"assets/animation/NORMAL_ATTACK.gif")
        self.p2NormalAttacklbl.setMovie(self.p2NormalAttackgif)
        self.p2NormalAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Poison) GIF
        self.p1PoisonAttacklbl = QLabel(self)
        self.p1PoisonAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1PoisonAttackgif = QMovie(f"assets/animation/POISON_ATTACK.gif")
        self.p1PoisonAttacklbl.setMovie(self.p1PoisonAttackgif)
        self.p1PoisonAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Poison) GIF
        self.p2PoisonAttacklbl = QLabel(self)
        self.p2PoisonAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2PoisonAttackgif = QMovie(f"assets/animation/POISON_ATTACK.gif")
        self.p2PoisonAttacklbl.setMovie(self.p2PoisonAttackgif)
        self.p2PoisonAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Psychic) GIF
        self.p1PsychicAttacklbl = QLabel(self)
        self.p1PsychicAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1PsychicAttackgif = QMovie(f"assets/animation/PSYCHIC_ATTACK.gif")
        self.p1PsychicAttacklbl.setMovie(self.p1PsychicAttackgif)
        self.p1PsychicAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Psychic) GIF
        self.p2PsychicAttacklbl = QLabel(self)
        self.p2PsychicAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2PsychicAttackgif = QMovie(f"assets/animation/PSYCHIC_ATTACK.gif")
        self.p2PsychicAttacklbl.setMovie(self.p2PsychicAttackgif)
        self.p2PsychicAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Rock) GIF
        self.p1RockAttacklbl = QLabel(self)
        self.p1RockAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1RockAttackgif = QMovie(f"assets/animation/ROCK_ATTACK.gif")
        self.p1RockAttacklbl.setMovie(self.p1RockAttackgif)
        self.p1RockAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Psychic) GIF
        self.p2RockAttacklbl = QLabel(self)
        self.p2RockAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2RockAttackgif = QMovie(f"assets/animation/ROCK_ATTACK.gif")
        self.p2RockAttacklbl.setMovie(self.p2RockAttackgif)
        self.p2RockAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Steel) GIF
        self.p1SteelAttacklbl = QLabel(self)
        self.p1SteelAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1SteelAttackgif = QMovie(f"assets/animation/STEEL_ATTACK.gif")
        self.p1SteelAttacklbl.setMovie(self.p1SteelAttackgif)
        self.p1SteelAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Steel) GIF
        self.p2SteelAttacklbl = QLabel(self)
        self.p2SteelAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2SteelAttackgif = QMovie(f"assets/animation/STEEL_ATTACK.gif")
        self.p2SteelAttacklbl.setMovie(self.p2SteelAttackgif)
        self.p2SteelAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        
        # Player 1 Attack(Water) GIF
        self.p1WaterAttacklbl = QLabel(self)
        self.p1WaterAttacklbl.setGeometry(800, 100, 350, 350)
        self.p1WaterAttackgif = QMovie(f"assets/animation/WATER_ATTACK.gif")
        self.p1WaterAttacklbl.setMovie(self.p1WaterAttackgif)
        self.p1WaterAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()
        # Player 2 Attack(Steel) GIF
        self.p2WaterAttacklbl = QLabel(self)
        self.p2WaterAttacklbl.setGeometry(100, 100, 350, 350)
        self.p2WaterAttackgif = QMovie(f"assets/animation/WATER_ATTACK.gif")
        self.p2WaterAttacklbl.setMovie(self.p2WaterAttackgif)
        self.p2WaterAttacklbl.setScaledContents(True)
        #self.p2FireAttackgif.start()

        # Player 1 Switching GIF
        self.p1pokeballlbl = QLabel(self)
        self.p1pokeballlbl.setGeometry(100, 100, 350, 350)
        self.p1pokeballgif = QMovie(f"assets/animation/Pokeball.gif")
        self.p1pokeballlbl.setMovie(self.p1pokeballgif)
        self.p1pokeballlbl.setScaledContents(True)
        # Player 2 Switching GIF
        self.p2pokeballlbl = QLabel(self)
        self.p2pokeballlbl.setGeometry(800, 100, 350, 350)
        self.p2pokeballgif = QMovie(f"assets/animation/Pokeball.gif")
        self.p2pokeballlbl.setMovie(self.p2pokeballgif)
        self.p2pokeballlbl.setScaledContents(True)

        # HP Bars
        self.max_hp_p1 = self.player_pokemon['stats'][0]['base_stat']
        self.hp_bar_p1 = QProgressBar(self)
        self.hp_bar_p1.setGeometry(405, 43, 113, 20)
        self.hp_bar_p1.setMinimum(0)
        self.hp_bar_p1.setMaximum(self.max_hp_p1)
        self.hp_bar_p1.setValue(self.player_pokemon['hp'])
        self.hp_bar_p1.setFormat(f"{self.player_pokemon['hp']}/{self.max_hp_p1}")
        self.hp_bar_p1.setStyleSheet("""
            QProgressBar { border: 2px solid #555; border-radius: 5px; text-align: center; }
            QProgressBar::chunk { background-color: #00cc00; width: 10px; }
        """)

        self.max_hp_p2 = self.opponent_pokemon['stats'][0]['base_stat']
        self.hp_bar_p2 = QProgressBar(self)
        self.hp_bar_p2.setGeometry(800, 43, 113, 20)
        self.hp_bar_p2.setMinimum(0)
        self.hp_bar_p2.setMaximum(self.max_hp_p2)
        self.hp_bar_p2.setValue(self.opponent_pokemon['hp'])
        self.hp_bar_p2.setFormat(f"{self.opponent_pokemon['hp']}/{self.max_hp_p2}")
        self.hp_bar_p2.setStyleSheet("""
            QProgressBar { border: 2px solid #555; border-radius: 5px; text-align: center; }
            QProgressBar::chunk { background-color: #00cc00; width: 10px; }
        """)
    
    def play_sfx(self):
        self.sfx_player.setMedia(QMediaContent(QUrl.fromLocalFile("assets/audio/Damage_Sound.mp3")))
        self.sfx_player.setVolume(100)
        self.sfx_player.play()

    def queue_battle_messages(self, messages, final_callback=None):
        """Queue a list of messages to be displayed one after another."""
        self.message_queue = messages
        self.final_callback = final_callback
        # Disable all move buttons and fight/switch buttons
        self.fightbtn.setEnabled(False)
        self.switchbtn.setEnabled(False)
        self.move_slot1btn.setEnabled(False)
        self.move_slot2btn.setEnabled(False)
        self.move_slot3btn.setEnabled(False)
        self.move_slot4btn.setEnabled(False)
        self.show_next_message()

    def show_next_message(self):
        if self.message_queue:
            next_message = self.message_queue.pop(0)
            self.full_message = next_message
            self.current_message_index = 0
            self.battle_message2.setText(self.battle_message1.text())
            self.battle_message1.setText("")
            self.typewriter_timer = QTimer(self)
            self.typewriter_timer.timeout.connect(self.update_typewriter_text)
            self.typewriter_timer.start(30)
        else:
            self.battle_message1.setText("")
            self.battle_message2.setText("")

            if self.final_callback:
                self.final_callback()
    def update_typewriter_text(self):
        if self.current_message_index < len(self.full_message):
            self.current_message_index += 1
            self.battle_message1.setText(self.full_message[:self.current_message_index])
        else:
            self.typewriter_timer.stop()
            QTimer.singleShot(800, self.show_next_message)
    
    def update_battle_message2(self):
        self.battle_message2.setText(self.delayed_message_text)

    def check_game_over(self):
        if all(p['hp'] == 0 for p in self.player_team):
            self.battle_message1.setText("You have no more Pokémon! You lose!")
            self.fightbtn.setVisible(False)
            self.switchbtn.setVisible(False)
            QTimer.singleShot(500, self.ask_play_again)
        elif all(p['hp'] == 0 for p in self.opponent_team):
            self.battle_message1.setText("You defeated all your opponent's Pokémon! You win!")
            self.fightbtn.setVisible(False)
            self.switchbtn.setVisible(False)
            QTimer.singleShot(500, self.ask_play_again)
    def ask_play_again(self):
        global global_music_player
        if global_music_player:
            global_music_player.stop()

        reply = QMessageBox.question(
            self, 'Play Again?', "Do you want to play again?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        )

        defeated_by_p1 = sum(1 for p in self.opponent_team if p['hp'] == 0)
        defeated_by_p2 = sum(1 for p in self.player_team if p['hp'] == 0)

        if self.player1_name:
            points = defeated_by_p1 * 50
            leaderboard.award_points(self.player1_name, points)
        if self.player2_name:
            points = defeated_by_p2 * 50
            leaderboard.award_points(self.player2_name, points)

        leaderboard.save_leaderboard()
        if hasattr(self, 'leaderboard_window') and self.leaderboard_window:
            self.leaderboard_window.refresh_scores()

        if reply == QMessageBox.Yes:
            self.close()
            self.choose_window = ChooseGameModeWindow()
            self.choose_window.show()
        else:
            self.close()
            end_game()

    def check_winner(self):
        p1_alive = any(p['hp'] > 0 for p in self.player_team)
        p2_alive = any(p['hp'] > 0 for p in self.opponent_team)
        if p1_alive and not p2_alive:
            return "player1"
        elif p2_alive and not p1_alive:
            return "player2"
        return None

    def end_move_turn(self):
        # After player finishes move, now opponent (AI) moves
        if self.opponent_pokemon['hp'] > 0:
            self.opponent_turn()
        else:
            # Opponent fainted, player wins or battle continues
            self.move_slot1btn.setVisible(False)
            self.move_slot2btn.setVisible(False)
            self.move_slot3btn.setVisible(False)
            self.move_slot4btn.setVisible(False)
            self.fightbtn.setVisible(True)
            self.switchbtn.setVisible(True)

    def animate_hp_barp1(self, bar, start_value, end_value):
        animationp1 = QPropertyAnimation(bar, b"value")
        animationp1.setDuration(500)  # 0.5 seconds for the animation
        animationp1.setStartValue(start_value)
        animationp1.setEndValue(end_value)
        animationp1.setEasingCurve(QEasingCurve.Linear)
        animationp1.start()
        self.current_hp_animation = animationp1
    def animate_hp_barp2(self, bar, start_value, end_value):
        animationp2 = QPropertyAnimation(bar, b"value")
        animationp2.setDuration(500)
        animationp2.setStartValue(start_value)
        animationp2.setEndValue(end_value)
        animationp2.setEasingCurve(QEasingCurve.Linear)
        animationp2.start()
        self.current_hp_animation = animationp2
    def screen_shake(self):
        original_pos = self.pos()
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(300)
        animation.setLoopCount(1)
        animation.setKeyValueAt(0, original_pos)
        animation.setKeyValueAt(0.25, original_pos + QPoint(10, 0))
        animation.setKeyValueAt(0.5, original_pos - QPoint(10, 0))
        animation.setKeyValueAt(0.75, original_pos + QPoint(10, 0))
        animation.setKeyValueAt(1, original_pos)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start()
        self.current_shake_animation = animation
        self.repaint()
    def shake_widget(self, widget):
        original_pos = widget.pos()
        animation = QPropertyAnimation(widget, b"pos")
        animation.setDuration(200)
        animation.setKeyValueAt(0, original_pos)
        animation.setKeyValueAt(0.25, original_pos + QPoint(5, 0))
        animation.setKeyValueAt(0.5, original_pos - QPoint(5, 0))
        animation.setKeyValueAt(0.75, original_pos + QPoint(5, 0))
        animation.setKeyValueAt(1, original_pos)
        animation.setEasingCurve(QEasingCurve.Linear)
        animation.start()
        widget.shake_animation = animation


    def update_hp_bars(self):
        # Player HP
        self.hp_bar_p1.setMaximum(self.max_hp_p1)
        if self.hp_bar_p1.value() != self.player_pokemon['hp']:
            self.animate_hp_barp1(self.hp_bar_p1, self.hp_bar_p1.value(), self.player_pokemon['hp'])
        else:
            self.hp_bar_p1.setValue(self.player_pokemon['hp'])
        self.hp_bar_p1.setFormat(f"{self.player_pokemon['hp']}/{self.max_hp_p1}")

        # Opponent HP
        self.hp_bar_p2.setMaximum(self.max_hp_p2)
        if self.hp_bar_p2.value() != self.opponent_pokemon['hp']:
            self.animate_hp_barp2(self.hp_bar_p2, self.hp_bar_p2.value(), self.opponent_pokemon['hp'])
        else:
            self.hp_bar_p2.setValue(self.opponent_pokemon['hp'])
        self.hp_bar_p2.setFormat(f"{self.opponent_pokemon['hp']}/{self.max_hp_p2}")

    def update_pokemon_gifs(self):
        # Make sure names are properly formatted
        player_name = self.player_pokemon['name'].upper().replace("-", "").replace(" ", "").replace(".", "")
        opponent_name = self.opponent_pokemon['name'].upper().replace("-", "").replace(" ", "").replace(".", "")

        player_gif_path = f"assets/pokemon_flipped/{player_name}.gif"
        opponent_gif_path = f"assets/pokemon/{opponent_name}.gif"

        print(f"Trying to load player gif: {player_gif_path}")
        print(f"Trying to load opponent gif: {opponent_gif_path}")

        # Update Player Pokémon GIF
        if os.path.exists(player_gif_path):
            self.pkmn1gif.stop()
            self.pkmn1gif = QMovie(player_gif_path)
            self.pkmn1lbl.setMovie(self.pkmn1gif)
            self.pkmn1lbl.setScaledContents(True)
            self.pkmn1gif.start()
        else:
            print(f"Player gif not found: {player_gif_path}")

        # Update Opponent Pokémon GIF
        if os.path.exists(opponent_gif_path):
            self.pkmn2gif.stop()
            self.pkmn2gif = QMovie(opponent_gif_path)
            self.pkmn2lbl.setMovie(self.pkmn2gif)
            self.pkmn2lbl.setScaledContents(True)
            self.pkmn2gif.start()
        else:
            print(f"Opponent gif not found: {opponent_gif_path}")

    def update_move_buttons(self):
        moves = [move['move']['name'] for move in self.player_pokemon['moves'][:4]]

        move_buttons = [self.move_slot1btn, self.move_slot2btn, self.move_slot3btn, self.move_slot4btn]
        for i, button in enumerate(move_buttons):
            if i < len(moves):
                move_name = moves[i]
                move_icon_path = f"assets/moves/{move_name}.png"
                button.setIcon(QIcon(move_icon_path))
                button.setToolTip(move_name.capitalize())
                button.setEnabled(True)
            else:
                button.setEnabled(False)

    def show_move_buttons(self):
        self.fightbtn.setVisible(False)
        self.switchbtn.setVisible(False)
        self.move_slot1btn.setVisible(True)
        self.move_slot2btn.setVisible(True)
        self.move_slot3btn.setVisible(True)
        self.move_slot4btn.setVisible(True)
        self.battle_message1.setText("")
        self.battle_message2.setText("")
        self.update_move_buttons()

    def update_hp_bar_for(self, pokemon):
        if pokemon == self.player_pokemon:
            self.hp_bar_p1.setValue(self.player_pokemon['hp'])
        else:
            self.hp_bar_p2.setValue(self.opponent_pokemon['hp'])

    def process_moves_in_order(self, moves_list, get_type_multiplier, move_type, defender_type):
        if not moves_list:
            self.after_both_turns()
            return

        attacker, move_name = moves_list.pop(0)

        if attacker == 'player1':
            user = self.player_pokemon
            target = self.opponent_pokemon
        else:
            user = self.opponent_pokemon
            target = self.player_pokemon

        # If the attacker fainted before moving, skip their turn
        if user['hp'] == 0:
            self.process_moves_in_order(moves_list)
            return

        move_name = move_name.lower()
        messages = []

        # --- Stat boost moves
        if move_name in STAT_BOOST_MOVES:
            boosts = STAT_BOOST_MOVES[move_name]
            for stat, stages in boosts.items():
                index = STAT_INDEX[stat.replace('-', ' ')]
                original = user['stats'][index]['base_stat']
                user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} rose!")

            self.queue_battle_messages(messages, final_callback=lambda: self.process_moves_in_order(moves_list))
            return

        # --- Multi-hit moves
        if move_name in MULTI_HIT_MOVES:
            min_hits, max_hits = MULTI_HIT_MOVES[move_name]
            num_hits = random.randint(min_hits, max_hits)
            self.perform_multi_hit(user, target, move_name, num_hits, attacker == 'player1')
            return

        # --- Normal attack
        damage, effectiveness = calculate_damage(user, target, move_name)
        target['hp'] = max(0, target['hp'] - damage)
        self.clamp_hp(target)
        self.update_hp_bars()
        self.play_sfx()

        messages.append(f"{user['name'].capitalize()} used {move_name.capitalize()}!")
        # --- Type effectiveness message
        if effectiveness > 1:
            messages.append("It's super effective!")
        elif 0 < effectiveness < 1:
            messages.append("It's not very effective...")
        elif effectiveness == 0:
            messages.append("It had no effect.")
        messages.append(f"{target['name'].capitalize()} took {damage} damage!")
        if damage > 1:
            self.screen_shake()

        # --- Drain moves
        if move_name in DRAIN_MOVES:
            heal_amount = int(damage * DRAIN_MOVES[move_name])
            max_hp = self.max_hp_p1 if attacker == 'player1' else self.max_hp_p2
            user['hp'] = min(max_hp, user['hp'] + heal_amount)
            self.clamp_hp(user)
            self.update_hp_bars()
            messages.append(f"{user['name'].capitalize()} drained and recovered {heal_amount} HP!")

        # --- Recoil moves
        if move_name in RECOIL_MOVES:
            recoil_amount = int(damage * RECOIL_MOVES[move_name])
            user['hp'] = max(0, user['hp'] - recoil_amount)
            self.clamp_hp(user)
            self.update_hp_bars()
            messages.append(f"{user['name'].capitalize()} took {recoil_amount} recoil damage!")

        # --- Self-debuff moves
        if move_name in SELF_DEBUFF_MOVES:
            debuffs = SELF_DEBUFF_MOVES[move_name]
            for stat, stages in debuffs.items():
                index = STAT_INDEX[stat.replace('-', ' ')]
                original = user['stats'][index]['base_stat']
                user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} fell!")

        # Check if target fainted
        if target['hp'] == 0:
            messages.append(f"{target['name'].capitalize()} fainted!")
            # Award 50 points to the player who defeated the Pokémon
            if attacker == 'player1' and self.player1_name:
                leaderboard.award_points(self.player1_name, 50)
                print(f"[DEBUG] {self.player1_name} gains 50 points for defeating {target['name']}")
            elif attacker == 'player2' and self.player2_name:
                leaderboard.award_points(self.player2_name, 50)
                print(f"[DEBUG] {self.player2_name} gains 50 points for defeating {target['name']}")
            self.turn_order = []
            if attacker == 'player1':
                self.queue_battle_messages(messages, final_callback=self.opponent_force_switch)
            else:
                self.queue_battle_messages(messages, final_callback=self.after_both_turns)
            return

        # If not fainted, continue to next move
        self.queue_battle_messages(messages, final_callback=lambda: self.process_moves_in_order(moves_list))

    def perform_multi_hit(self, user, target, move_name, num_hits, is_player, hit_number=1, total_damage=0, messages=None):
        if messages is None:
            messages = [f"{user['name'].capitalize()} used {move_name.capitalize()}!"]

        if hit_number > num_hits or target['hp'] == 0:
            if hit_number > 1:
                messages.append(f"Hit {hit_number - 1} times!")

            self.clamp_hp(target)
            self.update_hp_bars()

            if target['hp'] == 0:
                messages.append(f"{target['name'].capitalize()} fainted!")
                self.turn_order = []

                if self.opponent_pokemon['hp'] <= 0:
                    self.queue_battle_messages(
                        messages,
                        final_callback=self.opponent_force_switch
                    )
                elif self.player_pokemon['hp'] <= 0:
                    self.queue_battle_messages(
                        messages,
                        final_callback=self.after_both_turns
                    )
                else:
                    self.queue_battle_messages(messages, final_callback=self.perform_turns)
            else:
                self.queue_battle_messages(messages, final_callback=self.perform_turns)
            return

        damage, effectiveness = calculate_damage(user, target, move_name)
        target['hp'] = max(0, target['hp'] - damage)
        self.clamp_hp(target)
        self.update_hp_bars()
        self.play_sfx()

        if effectiveness > 1:
            messages.append("It's super effective!")
        elif 0 < effectiveness < 1:
            messages.append("It's not very effective...")
        elif effectiveness == 0:
            messages.append("It had no effect.")
        messages.append(f"{target['name'].capitalize()} took {damage} damage!")

        if damage > 1:
            self.screen_shake()

        QTimer.singleShot(700, lambda: self.perform_multi_hit(
            user, target, move_name, num_hits, is_player,
            hit_number + 1, total_damage + damage, messages
        ))

    def update_move_buttons_p2(self):
        moves = [move['move']['name'] for move in self.opponent_pokemon['moves'][:4]]

        move_buttons = [
            getattr(self, 'move_slot1btn_p2', None),
            getattr(self, 'move_slot2btn_p2', None),
            getattr(self, 'move_slot3btn_p2', None),
            getattr(self, 'move_slot4btn_p2', None),
        ]
        for i, button in enumerate(move_buttons):
            if button is None:
                continue
            if i < len(moves):
                move_name = moves[i]
                move_icon_path = f"assets/moves/{move_name}.png"
                button.setIcon(QIcon(move_icon_path))
                button.setToolTip(move_name.capitalize())
                button.setEnabled(True)
            else:
                button.setEnabled(False)

    def check_faint_during_turn(self, is_player_attacker):
        if self.opponent_pokemon['hp'] <= 0:
            self.turn_order = []
            self.queue_battle_messages(
                [f"{self.opponent_pokemon['name'].capitalize()} fainted!"],
                final_callback=self.opponent_force_switch
            )
            return True
        elif self.player_pokemon['hp'] <= 0:
            self.turn_order = []
            self.queue_battle_messages(
                [f"{self.player_pokemon['name'].capitalize()} fainted!"],
                final_callback=self.after_both_turns
            )
            return True
        return False
    def use_move(self, move_index):
        player_moves = [move['move']['name'] for move in self.player_pokemon['moves'][:4]]
        if move_index >= len(player_moves):
            return

        player_move = player_moves[move_index]
        self.p1_action = ('move', player_move)
        self.p1_ready = True

        if self.game_mode == 2:
            self.player2_choose_action()  # Just sets up UI
        else:
            opponent_move = ai_select_move(self.opponent_pokemon, self.player_pokemon)
            player_speed = self.player_pokemon['stats'][5]['base_stat']
            opponent_speed = self.opponent_pokemon['stats'][5]['base_stat']

            if player_speed >= opponent_speed:
                self.turn_order = [('player', player_move), ('opponent', opponent_move)]
            else:
                self.turn_order = [('opponent', opponent_move), ('player', player_move)]
            print("Turn order:", self.turn_order)
            self.perform_turns()

    def player2_choose_action(self):
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)
        self.fightbtn.setVisible(False)
        self.switchbtn.setVisible(False)

        self.fightbtn_p2 = QPushButton(self)
        self.fightbtn_p2.setGeometry(80, 525, 200, 80)
        self.fightbtn_p2.setIcon(QIcon("assets/icons/fightbtn.png"))
        self.fightbtn_p2.setIconSize(QSize(200, 80))
        self.fightbtn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.fightbtn_p2.clicked.connect(self.ask_player2_for_move)
        self.fightbtn_p2.show()

        self.switchbtn_p2 = QPushButton(self)
        self.switchbtn_p2.setGeometry(80, 600, 200, 80)
        self.switchbtn_p2.setIcon(QIcon("assets/icons/switchbtn.png"))
        self.switchbtn_p2.setIconSize(QSize(200, 80))
        self.switchbtn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.switchbtn_p2.clicked.connect(self.player2_switch_pokemon)
        self.switchbtn_p2.show()

        self.update_move_buttons_p2()

    def ask_player2_for_move(self):
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)

        if hasattr(self, 'fightbtn_p2'):
            self.fightbtn_p2.hide()
        if hasattr(self, 'switchbtn_p2'):
            self.switchbtn_p2.hide()

        self.move_slot1btn_p2 = QPushButton(self)
        self.move_slot1btn_p2.setGeometry(80, 500, 200, 100)
        self.move_slot1btn_p2.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot1btn_p2.setIconSize(QSize(200, 100))
        self.move_slot1btn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot1btn_p2.clicked.connect(lambda: self.player2_move_chosen(0))
        self.move_slot1btn_p2.show()

        self.move_slot2btn_p2 = QPushButton(self)
        self.move_slot2btn_p2.setGeometry(280, 500, 200, 100)
        self.move_slot2btn_p2.setIcon(QIcon("assets/moves/normal/explosion.png"))
        self.move_slot2btn_p2.setIconSize(QSize(200, 100))
        self.move_slot2btn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.move_slot2btn_p2.clicked.connect(lambda: self.player2_move_chosen(1))
        self.move_slot2btn_p2.show()

        if len(self.opponent_pokemon['moves']) > 2:
            self.move_slot3btn_p2 = QPushButton(self)
            self.move_slot3btn_p2.setGeometry(80, 600, 200, 100)
            self.move_slot3btn_p2.setIcon(QIcon("assets/moves/normal/explosion.png"))
            self.move_slot3btn_p2.setIconSize(QSize(200, 100))
            self.move_slot3btn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
            self.move_slot3btn_p2.clicked.connect(lambda: self.player2_move_chosen(2))
            self.move_slot3btn_p2.show()

        if len(self.opponent_pokemon['moves']) > 3:
            self.move_slot4btn_p2 = QPushButton(self)
            self.move_slot4btn_p2.setGeometry(280, 600, 200, 100)
            self.move_slot4btn_p2.setIcon(QIcon("assets/moves/normal/explosion.png"))
            self.move_slot4btn_p2.setIconSize(QSize(200, 100))
            self.move_slot4btn_p2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
            self.move_slot4btn_p2.clicked.connect(lambda: self.player2_move_chosen(3))
            self.move_slot4btn_p2.show()
        self.update_move_buttons_p2()

    def player2_move_chosen(self, move_index):
        opponent_moves = [move['move']['name'] for move in self.opponent_pokemon['moves'][:4]]
        if move_index >= len(opponent_moves):
            return

        opponent_move = opponent_moves[move_index]
        self.p2_action = ('move', opponent_move)
        self.p2_ready = True

        self.hide_player2_buttons()
        self.check_both_players_ready()

        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
    def hide_player2_buttons(self):
        for attr in ['move_slot1btn_p2', 'move_slot2btn_p2', 'move_slot3btn_p2', 'move_slot4btn_p2', 'switchbtn_p2']:
            if hasattr(self, attr):
                getattr(self, attr).hide()
    def player2_switch_pokemon(self):
        if self.p1_action[0] == 'switch' and self.p2_action[0] == 'switch':
            self.after_both_turns()
            return
        if hasattr(self, 'fightbtn_p2'):
            self.fightbtn_p2.hide()
        if hasattr(self, 'switchbtn_p2'):
            self.switchbtn_p2.hide()

        self.hide_player2_buttons()

        self.switch_window_p2 = SwitchPokemonWindow(self.opponent_team, self)
        self.switch_window_p2.exec_()
        self.on_player2_switch_complete(self.switch_window_p2.selected_pokemon)
        self.p2_action = ('switch', self.switch_window_p2.selected_pokemon)
        self.p2_ready = True
        self.check_both_players_ready()
    def on_player2_switch_complete(self, new_pokemon):
        self.opponent_pokemon = new_pokemon
        self.max_hp_p2 = self.opponent_pokemon['stats'][0]['base_stat']
        self.update_hp_bars()
        self.update_pokemon_gifs()
        self.update_move_buttons_p2()
        

        

    def process_turn(self, move_p1, move_p2):
        messages = []

        # Exit early if actions are not yet set
        if self.p1_action is None or self.p2_action is None:
            return

        if self.p1_action[0] == 'switch':
            self.player_pokemon = self.p1_action[1]
            self.max_hp_p1 = self.player_pokemon['stats'][0]['base_stat']
            self.update_hp_bars()
            self.update_pokemon_gifs()
            self.update_move_buttons()
            #messages.append(f"You switched to {self.player_pokemon['name'].capitalize()}!")

        if self.p2_action[0] == 'switch':
            self.opponent_pokemon = self.p2_action[1]
            self.max_hp_p2 = self.opponent_pokemon['stats'][0]['base_stat']
            self.update_hp_bars()
            self.update_pokemon_gifs()
            self.update_move_buttons_p2()
            messages.append(f"Opponent switched to {self.opponent_pokemon['name'].capitalize()}!")

        # If both switched, no one attacks
        if self.p1_action[0] == 'switch' and self.p2_action[0] == 'switch':
            self.queue_battle_messages(messages, final_callback=self.after_both_turns)
            return

        # If only one switched, show switch message first, then process the remaining attack
        elif self.p1_action[0] == 'switch' or self.p2_action[0] == 'switch':
            self.queue_battle_messages(messages, final_callback=self.process_remaining_action_after_switch)
            return

        # Otherwise, both are attacking; determine order by speed
        player1_speed = self.player_pokemon['stats'][5]['base_stat']
        player2_speed = self.opponent_pokemon['stats'][5]['base_stat']

        moves = []
        if self.p1_action[0] == 'move':
            moves.append(('player1', move_p1))
        if self.p2_action[0] == 'move':
            moves.append(('player2', move_p2))

        if len(moves) == 2 and player2_speed > player1_speed:
            moves.reverse()

        self.turn_order = moves
        self.perform_turns()

    def process_remaining_action_after_switch(self):
        player1_speed = self.player_pokemon['stats'][5]['base_stat']
        player2_speed = self.opponent_pokemon['stats'][5]['base_stat']

        moves = []
        if self.p1_action and self.p1_action[0] == 'move':
            moves.append(('player', self.p1_action[1]))
        if self.p2_action and self.p2_action[0] == 'move':
            moves.append(('opponent', self.p2_action[1]))

        if len(moves) == 2 and player2_speed > player1_speed:
            moves.reverse()

        self.turn_order = moves
        self.perform_turns()



    def opponent_turn(self):
        move_name = ai_select_move(self.opponent_pokemon, self.player_pokemon)

        if move_name:
            damage, effectiveness = calculate_damage(self.opponent_pokemon, self.player_pokemon, move_name)
            self.player_pokemon['hp'] = max(0, self.player_pokemon['hp'] - damage)
            self.update_hp_bars()

            messages = [
                f"The opponent's {self.opponent_pokemon['name'].capitalize()} used {move_name.capitalize()}!",
                f"{self.player_pokemon['name'].capitalize()} took {damage} damage!",
            ]

            if self.player_pokemon['hp'] == 0:
                messages.append(f"{self.player_pokemon['name'].capitalize()} fainted!")

            self.queue_battle_messages(messages, final_callback=self.after_opponent_turn)
        else:
            # No move selected (no PP maybe?), skip to after
            self.after_opponent_turn()

    def after_opponent_turn(self):
        if self.player_pokemon['hp'] == 0:
            self.move_slot1btn.setVisible(False)
            self.move_slot2btn.setVisible(False)
            self.move_slot3btn.setVisible(False)
            self.move_slot4btn.setVisible(False)
            self.fightbtn.setVisible(False)
            self.switchbtn.setVisible(True)
            self.fightbtn.setEnabled(False)
            if len(self.player_team) <= 1:
                self.switchbtn.setEnabled(False)
            else:
                self.switchbtn.setEnabled(True)
            self.battle_message1.setText("Choose a new Pokémon to send out!")
            self.battle_message2.setText("")
        else:
            self.fightbtn.setVisible(True)
            self.switchbtn.setVisible(True)
            self.fightbtn.setEnabled(True)
            self.move_slot1btn.setEnabled(True)
            self.move_slot2btn.setEnabled(True)
            self.move_slot3btn.setEnabled(True)
            self.move_slot4btn.setEnabled(True)
            self.battle_message1.setText("")
            self.battle_message2.setText("")
    def opponent_force_switch(self):
        if len(self.opponent_team) == 1:
            self.switchbtn.setEnabled(False)
        else:
            self.switchbtn.setEnabled(True)

        self.p2pokeballlbl.show()
        self.p2pokeballgif.start()
        QTimer.singleShot(2250, lambda: self.p2pokeballlbl.hide())

        next_pokemon = next((p for p in self.opponent_team if p['hp'] > 0), None)
        if next_pokemon:
            self.opponent_pokemon = next_pokemon
            self.max_hp_p2 = self.opponent_pokemon['stats'][0]['base_stat']
            self.opponent_pokemon['hp'] = self.max_hp_p2

            self.max_hp_p2 = self.opponent_pokemon['stats'][0]['base_stat']
            
            self.update_hp_bars()
            self.update_pokemon_gifs()
            self.opponent_switched = True

            self.queue_battle_messages(
                [f"The opponent sent out {next_pokemon['name'].capitalize()}!"],
                final_callback=self.after_opponent_switch
            )
        else:
            # No Pokémon left
            self.queue_battle_messages(
                ["The opponent has no Pokémon left! You win!"],
                final_callback=self.check_game_over
            )

    def clamp_hp(self, pokemon):
        if pokemon['hp'] < 0:
            pokemon['hp'] = 0

    def after_opponent_switch(self):
        if len(self.opponent_team) == 1:
            self.switchbtn.setEnabled(False)
        else:
            self.switchbtn.setEnabled(True)
        self.move_slot1btn.setVisible(False)
        self.move_slot2btn.setVisible(False)
        self.move_slot3btn.setVisible(False)
        self.move_slot4btn.setVisible(False)

        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)

        self.fightbtn.setEnabled(True)

        self.move_slot1btn.setEnabled(True)
        self.move_slot2btn.setEnabled(True)
        self.move_slot3btn.setEnabled(True)
        self.move_slot4btn.setEnabled(True)

        self.battle_message1.setText("")
        self.battle_message2.setText("")

    def perform_turns(self):
        if len(self.player_team) <= 1:
            self.switchbtn.setEnabled(True)
        else:
            self.switchbtn.setEnabled(False)
        if not self.turn_order:
            self.after_both_turns()
            return
        
        if self.game_mode == 1:
            turn_entry = self.turn_order.pop(0)
            if len(turn_entry) == 2:
                attacker, move = turn_entry
            else:
                print("[ERROR] Invalid turn entry format.")
                return
            if attacker == 'player' and self.player_pokemon['hp'] == 0:
                self.after_both_turns()
                return
            if attacker == 'opponent' and self.opponent_pokemon['hp'] == 0:
                self.after_both_turns()
                return

            if attacker == 'player':
                self.screen_shake()
                if self.player_pokemon['hp'] > 0:
                    user = self.player_pokemon
                    target = self.opponent_pokemon
                    is_player = True
                else:
                    self.after_both_turns()
                    return
            else:
                self.screen_shake()
                if self.opponent_pokemon['hp'] > 0:
                    user = self.opponent_pokemon
                    target = self.player_pokemon
                    is_player = False
                else:
                    self.after_both_turns()
                    return
            move_name = move['name'] if isinstance(move, dict) else move
            move_name = move_name.lower()

            if move_name in STAT_BOOST_MOVES:
                boosts = STAT_BOOST_MOVES[move_name]
                messages = []
                for stat, stages in boosts.items():
                    index = STAT_INDEX[stat.replace('-', ' ')]
                    original = user['stats'][index]['base_stat']
                    user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                    messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} rose!")
                self.queue_battle_messages(messages, final_callback=self.perform_turns)
                return

            move_data = get_move_data(move_name)
            if not move_data:
                print(f"[ERROR] Move data not found for: {move_name}")
                self.queue_battle_messages([
                    f"{user['name'].capitalize()} sent out their next pokemon."
                ], final_callback=self.after_both_turns)
                return

            if move_data['type'] == "fire":
                if attacker == 'player':
                    self.p1FireAttacklbl.show()
                    self.p1FireAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FireAttacklbl.hide())
                else:
                    self.p2FireAttacklbl.show()
                    self.p2FireAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FireAttacklbl.hide())
            if move_data['type'] == "electric":
                if attacker == 'player':
                    self.p1ElectricAttacklbl.show()
                    self.p1ElectricAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1ElectricAttacklbl.hide())
                else:
                    self.p2ElectricAttacklbl.show()
                    self.p2ElectricAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2ElectricAttacklbl.hide())       
            if move_data['type'] == "bug":
                if attacker == 'player':
                    self.p1BugAttacklbl.show()
                    self.p1BugAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1BugAttacklbl.hide())
                else:
                    self.p2BugAttacklbl.show()
                    self.p2BugAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2BugAttacklbl.hide())      
            if move_data['type'] == "dark":
                if attacker == 'player':
                    self.p1DarkAttacklbl.show()
                    self.p1DarkAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1DarkAttacklbl.hide())
                else:
                    self.p2DarkAttacklbl.show()
                    self.p2DarkAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2DarkAttacklbl.hide())     
            if move_data['type'] == "dragon":
                if attacker == 'player':
                    self.p1DragonAttacklbl.show()
                    self.p1DragonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1DragonAttacklbl.hide())
                else:
                    self.p2DragonAttacklbl.show()
                    self.p2DragonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2DragonAttacklbl.hide())     
            if move_data['type'] == "fairy":
                if attacker == 'player':
                    self.p1FairyAttacklbl.show()
                    self.p1FairyAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FairyAttacklbl.hide())
                else:
                    self.p2FairyAttacklbl.show()
                    self.p2FairyAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FairyAttacklbl.hide())  
            if move_data['type'] == "fighting":
                if attacker == 'player':
                    self.p1FightingAttacklbl.show()
                    self.p1FightingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FightingAttacklbl.hide())
                else:
                    self.p2FightingAttacklbl.show()
                    self.p2FightingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FightingAttacklbl.hide())  
            if move_data['type'] == "flying":
                if attacker == 'player':
                    self.p1FlyingAttacklbl.show()
                    self.p1FlyingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FlyingAttacklbl.hide())
                else:
                    self.p2FlyingAttacklbl.show()
                    self.p2FlyingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FlyingAttacklbl.hide())  
            if move_data['type'] == "ghost":
                if attacker == 'player':
                    self.p1GhostAttacklbl.show()
                    self.p1GhostAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GhostAttacklbl.hide())
                else:
                    self.p2GhostAttacklbl.show()
                    self.p2GhostAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GhostAttacklbl.hide())  
            if move_data['type'] == "grass":
                if attacker == 'player':
                    self.p1GrassAttacklbl.show()
                    self.p1GrassAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GrassAttacklbl.hide())
                else:
                    self.p2GrassAttacklbl.show()
                    self.p2GrassAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GrassAttacklbl.hide())  
            if move_data['type'] == "ground":
                if attacker == 'player':
                    self.p1GroundAttacklbl.show()
                    self.p1GroundAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GroundAttacklbl.hide())
                else:
                    self.p2GroundAttacklbl.show()
                    self.p2GroundAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GroundAttacklbl.hide())  
            if move_data['type'] == "ice":
                if attacker == 'player':
                    self.p1IceAttacklbl.show()
                    self.p1IceAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1IceAttacklbl.hide())
                else:
                    self.p2IceAttacklbl.show()
                    self.p2IceAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2IceAttacklbl.hide())  
            if move_data['type'] == "normal":
                if attacker == 'player':
                    self.p1NormalAttacklbl.show()
                    self.p1NormalAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1NormalAttacklbl.hide())
                else:
                    self.p2NormalAttacklbl.show()
                    self.p2NormalAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2NormalAttacklbl.hide())  
            if move_data['type'] == "poison":
                if attacker == 'player':
                    self.p1PoisonAttacklbl.show()
                    self.p1PoisonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1PoisonAttacklbl.hide())
                else:
                    self.p2PoisonAttacklbl.show()
                    self.p2PoisonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2PoisonAttacklbl.hide())  
            if move_data['type'] == "psychic":
                if attacker == 'player':
                    self.p1PsychicAttacklbl.show()
                    self.p1PsychicAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1PsychicAttacklbl.hide())
                else:
                    self.p2PsychicAttacklbl.show()
                    self.p2PsychicAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2PsychicAttacklbl.hide())  
            if move_data['type'] == "rock":
                if attacker == 'player':
                    self.p1RockAttacklbl.show()
                    self.p1RockAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1RockAttacklbl.hide())
                else:
                    self.p2RockAttacklbl.show()
                    self.p2RockAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2RockAttacklbl.hide())  
            if move_data['type'] == "steel":
                if attacker == 'player':
                    self.p1SteelAttacklbl.show()
                    self.p1SteelAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1SteelAttacklbl.hide())
                else:
                    self.p2SteelAttacklbl.show()
                    self.p2SteelAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2SteelAttacklbl.hide())  
            if move_data['type'] == "water":
                if attacker == 'player':
                    self.p1WaterAttacklbl.show()
                    self.p1WaterAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1WaterAttacklbl.hide())
                else:
                    self.p2WaterAttacklbl.show()
                    self.p2WaterAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2WaterAttacklbl.hide())  

        if self.game_mode == 2:
            attacker_label, action = self.turn_order.pop(0)
            action_type, move = action
            move_name = move['name'] if isinstance(move, dict) else move
            move_name = move_name.lower()

            if attacker_label == 'player':
                self.screen_shake()
                if self.player_pokemon['hp'] == 0:
                    self.after_both_turns()
                    return
                user = self.player_pokemon
                target = self.opponent_pokemon
                is_player = True
            else:
                self.screen_shake()
                if self.opponent_pokemon['hp'] == 0:
                    self.after_both_turns()
                    return
                user = self.opponent_pokemon
                target = self.player_pokemon
                is_player = False

            if move_name in STAT_BOOST_MOVES:
                boosts = STAT_BOOST_MOVES[move_name]
                messages = []
                for stat, stages in boosts.items():
                    index = STAT_INDEX[stat.replace('-', ' ')]
                    original = user['stats'][index]['base_stat']
                    user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                    messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} rose!")
                self.queue_battle_messages(messages, final_callback=self.perform_turns)
                return

            move_data = get_move_data(move_name)
            if not move_data:
                print(f"[ERROR] Move data not found for: {move_name}")
                self.queue_battle_messages([
                    f"{user['name'].capitalize()} sent out their next pokemon."
                ], final_callback=self.after_both_turns)
                return
            if move_data['type'] == "fire":
                if attacker_label == 'player':
                    self.p1FireAttacklbl.show()
                    self.p1FireAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FireAttacklbl.hide())
                else:
                    self.p2FireAttacklbl.show()
                    self.p2FireAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FireAttacklbl.hide())
            if move_data['type'] == "electric":
                if attacker_label == 'player':
                    self.p1ElectricAttacklbl.show()
                    self.p1ElectricAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1ElectricAttacklbl.hide())
                else:
                    self.p2ElectricAttacklbl.show()
                    self.p2ElectricAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2ElectricAttacklbl.hide())       
            if move_data['type'] == "bug":
                if attacker_label == 'player':
                    self.p1BugAttacklbl.show()
                    self.p1BugAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1BugAttacklbl.hide())
                else:
                    self.p2BugAttacklbl.show()
                    self.p2BugAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2BugAttacklbl.hide())      
            if move_data['type'] == "dark":
                if attacker_label == 'player':
                    self.p1DarkAttacklbl.show()
                    self.p1DarkAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1DarkAttacklbl.hide())
                else:
                    self.p2DarkAttacklbl.show()
                    self.p2DarkAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2DarkAttacklbl.hide())     
            if move_data['type'] == "dragon":
                if attacker_label == 'player':
                    self.p1DragonAttacklbl.show()
                    self.p1DragonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1DragonAttacklbl.hide())
                else:
                    self.p2DragonAttacklbl.show()
                    self.p2DragonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2DragonAttacklbl.hide())     
            if move_data['type'] == "fairy":
                if attacker_label == 'player':
                    self.p1FairyAttacklbl.show()
                    self.p1FairyAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FairyAttacklbl.hide())
                else:
                    self.p2FairyAttacklbl.show()
                    self.p2FairyAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FairyAttacklbl.hide())  
            if move_data['type'] == "fighting":
                if attacker_label == 'player':
                    self.p1FightingAttacklbl.show()
                    self.p1FightingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FightingAttacklbl.hide())
                else:
                    self.p2FightingAttacklbl.show()
                    self.p2FightingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FightingAttacklbl.hide())  
            if move_data['type'] == "flying":
                if attacker_label == 'player':
                    self.p1FlyingAttacklbl.show()
                    self.p1FlyingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1FlyingAttacklbl.hide())
                else:
                    self.p2FlyingAttacklbl.show()
                    self.p2FlyingAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2FlyingAttacklbl.hide())  
            if move_data['type'] == "ghost":
                if attacker_label == 'player':
                    self.p1GhostAttacklbl.show()
                    self.p1GhostAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GhostAttacklbl.hide())
                else:
                    self.p2GhostAttacklbl.show()
                    self.p2GhostAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GhostAttacklbl.hide())  
            if move_data['type'] == "grass":
                if attacker_label == 'player':
                    self.p1GrassAttacklbl.show()
                    self.p1GrassAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GrassAttacklbl.hide())
                else:
                    self.p2GrassAttacklbl.show()
                    self.p2GrassAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GrassAttacklbl.hide())  
            if move_data['type'] == "ground":
                if attacker_label == 'player':
                    self.p1GroundAttacklbl.show()
                    self.p1GroundAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1GroundAttacklbl.hide())
                else:
                    self.p2GroundAttacklbl.show()
                    self.p2GroundAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2GroundAttacklbl.hide())  
            if move_data['type'] == "ice":
                if attacker_label == 'player':
                    self.p1IceAttacklbl.show()
                    self.p1IceAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1IceAttacklbl.hide())
                else:
                    self.p2IceAttacklbl.show()
                    self.p2IceAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2IceAttacklbl.hide())  
            if move_data['type'] == "normal":
                if attacker_label == 'player':
                    self.p1NormalAttacklbl.show()
                    self.p1NormalAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1NormalAttacklbl.hide())
                else:
                    self.p2NormalAttacklbl.show()
                    self.p2NormalAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2NormalAttacklbl.hide())  
            if move_data['type'] == "poison":
                if attacker_label == 'player':
                    self.p1PoisonAttacklbl.show()
                    self.p1PoisonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1PoisonAttacklbl.hide())
                else:
                    self.p2PoisonAttacklbl.show()
                    self.p2PoisonAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2PoisonAttacklbl.hide())  
            if move_data['type'] == "psychic":
                if attacker_label == 'player':
                    self.p1PsychicAttacklbl.show()
                    self.p1PsychicAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1PsychicAttacklbl.hide())
                else:
                    self.p2PsychicAttacklbl.show()
                    self.p2PsychicAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2PsychicAttacklbl.hide())  
            if move_data['type'] == "rock":
                if attacker_label == 'player':
                    self.p1RockAttacklbl.show()
                    self.p1RockAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1RockAttacklbl.hide())
                else:
                    self.p2RockAttacklbl.show()
                    self.p2RockAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2RockAttacklbl.hide())  
            if move_data['type'] == "steel":
                if attacker_label == 'player':
                    self.p1SteelAttacklbl.show()
                    self.p1SteelAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1SteelAttacklbl.hide())
                else:
                    self.p2SteelAttacklbl.show()
                    self.p2SteelAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2SteelAttacklbl.hide())  
            if move_data['type'] == "water":
                if attacker_label == 'player':
                    self.p1WaterAttacklbl.show()
                    self.p1WaterAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p1WaterAttacklbl.hide())
                else:
                    self.p2WaterAttacklbl.show()
                    self.p2WaterAttackgif.start()
                    QTimer.singleShot(1000, lambda: self.p2WaterAttacklbl.hide()) 
            # Handle switching
            if action_type == 'switch':
                if attacker_label == 'player':
                    self.on_player1_switch_complete(move)
                else:
                    self.on_player2_switch_complete(move)
                self.perform_turns()
                return

        move_name = move.lower()
        messages = []
        total_damage = 0

        # --- Stat boost moves
        if move_name in STAT_BOOST_MOVES:
            boosts = STAT_BOOST_MOVES[move_name]
            for stat, stages in boosts.items():
                index = STAT_INDEX[stat.replace('-', ' ')]
                original = user['stats'][index]['base_stat']
                user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} rose!")
            
            self.queue_battle_messages(messages, final_callback=self.perform_turns)
            return

        # --- Multi-hit moves
        if move_name in MULTI_HIT_MOVES:
            min_hits, max_hits = MULTI_HIT_MOVES[move_name]
            num_hits = random.randint(min_hits, max_hits)
            self.perform_multi_hit(user, target, move_name, num_hits, is_player)
            return
        else:
            # Normal attack
            damage, effectiveness = calculate_damage(user, target, move_name)
            target['hp'] = max(0, target['hp'] - damage)
            self.clamp_hp(target)
            self.update_hp_bars()
            self.play_sfx()

            messages.append(f"{user['name'].capitalize()} used {move_name.capitalize()}!")
            if effectiveness > 1:
                messages.append("It's super effective!")
            elif 0 < effectiveness < 1:
                messages.append("It's not very effective...")
            elif effectiveness == 0:
                messages.append("It had no effect.")
            messages.append(f"{target['name'].capitalize()} took {damage} damage!")

        # --- Drain moves
        if move_name in DRAIN_MOVES:
            heal_amount = int(damage * DRAIN_MOVES[move_name])
            max_hp = self.max_hp_p1 if is_player else self.max_hp_p2
            user['hp'] = min(max_hp, user['hp'] + heal_amount)
            self.clamp_hp(user)
            self.update_hp_bar_for(target)
            self.update_hp_bar_for(user)
            self.update_hp_bars()
            messages.append(f"{user['name'].capitalize()} drained and recovered {heal_amount} HP!")

        # --- Recoil moves
        if move_name in RECOIL_MOVES:
            recoil_amount = int(damage * RECOIL_MOVES[move_name])
            user['hp'] = max(0, user['hp'] - recoil_amount)
            self.clamp_hp(user)
            self.update_hp_bar_for(target)
            self.update_hp_bar_for(user)
            self.update_hp_bars()
            messages.append(f"{user['name'].capitalize()} took {recoil_amount} recoil damage!")

        # --- Self-debuff moves
        if move_name in SELF_DEBUFF_MOVES:
            debuffs = SELF_DEBUFF_MOVES[move_name]
            for stat, stages in debuffs.items():
                index = STAT_INDEX[stat.replace('-', ' ')]
                original = user['stats'][index]['base_stat']
                user['stats'][index]['base_stat'] = int(original * (1 + 0.5 * stages))
                messages.append(f"{user['name'].capitalize()}'s {stat.replace('-', ' ').capitalize()} fell!")

        self.update_hp_bars()

        if target['hp'] == 0:
            messages.append(f"{target['name'].capitalize()} fainted!")
            self.turn_order = []
            if self.opponent_pokemon['hp'] <= 0:
                self.queue_battle_messages(messages, final_callback=self.opponent_force_switch)
                return True
            elif self.player_pokemon['hp'] <= 0:
                self.queue_battle_messages(messages, final_callback=self.after_both_turns)
                return True
            return False

        self.queue_battle_messages(messages, final_callback=self.perform_turns)

    

    def after_player_switch(self):
        if self.opponent_pokemon['hp'] > 0:
            self.opponent_turn()
        else:
            self.fightbtn.setVisible(True)
            self.switchbtn.setVisible(True)
            self.fightbtn.setEnabled(True)
            if len(self.player_team) <= 1:
                self.switchbtn.setEnabled(False)
            else:
                self.switchbtn.setEnabled(True)
            
            self.move_slot1btn.setEnabled(True)
            self.move_slot2btn.setEnabled(True)
            self.move_slot3btn.setEnabled(True)
            self.move_slot4btn.setEnabled(True)
            self.battle_message1.setText("")
            self.battle_message2.setText("")
    def switch_pokemon(self):
        self.switch_window = SwitchPokemonWindow(self.player_team, self)
        self.switch_window.setStyleSheet("QDialog { background-image: url('assets/backgrounds/selectbackground.png'); background-repeat: no-repeat; background-position: center; }")
        self.switch_window.setWindowTitle("Select a Pokemon!")
        self.switch_window.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.switch_window.exec_()
        new_poke = self.switch_window.selected_pokemon

        self.p1pokeballlbl.show()
        self.p1pokeballgif.start()
        QTimer.singleShot(2250, lambda: self.p1pokeballlbl.hide())

        if new_poke:
            self.p1_action = ('switch', new_poke)
            self.p1_ready = True
            self.queue_battle_messages(
                [f"You switched to {new_poke['name'].capitalize()}!"],
                final_callback=lambda: self.on_player1_switch_complete(new_poke)
            )
            if game_mode == 2:
                self.player2_choose_action()
    def on_player1_switch_complete(self, new_pokemon, from_switch=False):
        
        self.player_pokemon = new_pokemon
        self.max_hp_p1 = self.player_pokemon['stats'][0]['base_stat']
        self.update_hp_bars()
        self.update_pokemon_gifs()
        self.update_move_buttons()
        self.fightbtn.setVisible(True)
        self.switchbtn.setVisible(True)
        self.fightbtn.setEnabled(True)
        if len(self.player_team) <= 1:
            self.switchbtn.setEnabled(True)
        else:
            self.switchbtn.setEnabled(False)

        self.battle_message1.setText("")
        self.battle_message2.setText("")
        if self.p1_action is None and self.p2_action is None:
            self.fightbtn.setVisible(True)
            self.switchbtn.setVisible(True)
            self.fightbtn.setEnabled(True)
            if len(self.player_team) <= 1:
                self.switchbtn.setEnabled(False)
            else:
                self.switchbtn.setEnabled(True)
            self.move_slot1btn.setEnabled(True)
            self.move_slot2btn.setEnabled(True)
            self.move_slot3btn.setEnabled(True)
            self.move_slot4btn.setEnabled(True)
            self.battle_message1.setText("")
            self.battle_message2.setText("")
            return
        if self.game_mode == 1:
            self.queue_battle_messages([], final_callback=self.opponent_turn)
        else:
            self.check_both_players_ready()
    def check_both_players_ready(self):
        if self.p1_ready and self.p2_ready:
            # Decide who goes first based on speed
            p1_speed = self.player_pokemon['stats'][5]['base_stat']
            p2_speed = self.opponent_pokemon['stats'][5]['base_stat']

            # Use switch priority if needed
            if self.p1_action[0] == 'switch' and self.p2_action[0] != 'switch':
                self.turn_order = [('player', self.p1_action), ('opponent', self.p2_action)]
            elif self.p2_action[0] == 'switch' and self.p1_action[0] != 'switch':
                self.turn_order = [('opponent', self.p2_action), ('player', self.p1_action)]
            else:
                if p1_speed >= p2_speed:
                    self.turn_order = [('player', self.p1_action), ('opponent', self.p2_action)]
                else:
                    self.turn_order = [('opponent', self.p2_action), ('player', self.p1_action)]

            self.p1_ready = False
            self.p2_ready = False
            self.perform_turns()

    def check_post_turn_events(self):
        if self.player_switched:
            self.player_switched = False
            self.queue_battle_messages(
                [f"{self.player_pokemon['name'].capitalize()} is getting ready!"],
                final_callback=self.update_move_buttons  # or whatever comes next
            )
            return

        # handle auto-switch if Pokémon fainted
        if self.player_pokemon['hp'] <= 0:
            self.handle_player_faint()
        elif self.opponent_pokemon['hp'] <= 0:
            self.handle_opponent_faint()

    def after_both_turns(self):
        if len(self.player_team) <= 1:
            self.switchbtn.setEnabled(True)
        else:
            self.switchbtn.setEnabled(False)
        if self.player_pokemon['hp'] == 0:
            # Player fainted
            self.move_slot1btn.setVisible(False)
            self.move_slot2btn.setVisible(False)
            self.move_slot3btn.setVisible(False)
            self.move_slot4btn.setVisible(False)
            self.fightbtn.setVisible(False)
            self.switchbtn.setVisible(True)
            self.battle_message1.setText("Your Pokémon fainted! Choose a new one!")
            self.battle_message2.setText("")
            
            # Force the switch window to appear immediately
            QTimer.singleShot(1000, self.force_player_switch)
        else:
            self.move_slot1btn.setVisible(False)
            self.move_slot2btn.setVisible(False)
            self.move_slot3btn.setVisible(False)
            self.move_slot4btn.setVisible(False)

            self.fightbtn.setVisible(True)
            self.switchbtn.setVisible(True)

            self.fightbtn.setEnabled(True)
            if len(self.player_team) <= 1:
                self.switchbtn.setEnabled(False)
            else:
                self.switchbtn.setEnabled(True)
            self.move_slot1btn.setEnabled(True)
            self.move_slot2btn.setEnabled(True)
            self.move_slot3btn.setEnabled(True)
            self.move_slot4btn.setEnabled(True)

            self.battle_message1.setText("")
            self.battle_message2.setText("")
    def force_player_switch(self):
        remaining = [p for p in self.player_team if p['hp'] > 0 and p != self.player_pokemon]
        if not remaining:
            self.queue_battle_messages(
                ["You have no more Pokémon! You lose!"],
                final_callback=self.ask_play_again
            )
            return
        
        self.p1pokeballlbl.show()
        self.p1pokeballgif.start()
        QTimer.singleShot(2250, lambda: self.p1pokeballlbl.hide())
        
        self.switch_window = SwitchPokemonWindow(self.player_team, self)
        self.switch_window.exec_()
        new_poke = self.switch_window.selected_pokemon
        if new_poke:
            self.on_player1_switch_complete(new_poke)

    
    
    

    

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtCore import Qt

class SwitchPokemonWindow(QDialog):
    def __init__(self, team, battle_instance, is_player1=True):
        super().__init__()
        self.setWindowTitle("Switch Pokémon")
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.setGeometry(500, 200, 300, 400)
        self.team = team
        self.battle_instance = battle_instance
        self.is_player1 = is_player1

        layout = QVBoxLayout()

        current_pokemon = battle_instance.player_pokemon if is_player1 else battle_instance.opponent_pokemon

        for pokemon in self.team:
            if pokemon['hp'] > 0 and pokemon is not current_pokemon:
                text = f"{pokemon['name'].capitalize()} (HP: {pokemon['hp']}/{pokemon['stats'][0]['base_stat']})"
                btn = QPushButton(text, self)
                btn.setIcon(QIcon(f"assets/pokemon/{pokemon['name']}.gif"))
                btn.setIconSize(QSize(80, 80))
                btn.setStyleSheet(f"""QPushButton {{border: none; padding: 10px; border-image: url(assets/icons/selectbtn2.png) 0 0 0 0 stretch stretch; background-repeat: no-repeat;background-position: center;color: white; }} """)
                btn.setFixedSize(250, 70) 
                btn.clicked.connect(lambda checked, p=pokemon: self.choose_pokemon(p))
                layout.addWidget(btn, alignment=Qt.AlignHCenter)

        self.setLayout(layout)
    
    def on_pokemon_selected(self, item):
        self.selected_pokemon = item.data(Qt.UserRole)
        self.accept()

    def choose_pokemon(self, chosen_pokemon):
        self.selected_pokemon = chosen_pokemon
        self.accept()
        self.close()

def start_new_game(game_mode):
    if game_mode == 1:
        player_team = get_teams_from_gui(game_mode)
        opponent_team = generate_random_team()
    else:
        player_team, opponent_team = get_teams_from_gui(game_mode)
    
    battle_window = battle(player_team, opponent_team, game_mode)
    battle_window.show()






if __name__ == '__main__':
    leaderboard = Leaderboard()
    load_leaderboard()
    app = QApplication(sys.argv)

    print("Welcome to Pokémon Battle Simulator!")
    choose_window = ChooseGameModeWindow()
    choose_window.show()
    app.exec_()

    if game_mode == 1:
        player_team = get_teams_from_gui(game_mode)
        opponent_team = generate_random_team()
        battle_window = battle(player_team, opponent_team, game_mode)
        battle_window.show()
        app.exec_()
    elif game_mode == 2:
        player_team, team_p2 = get_teams_from_gui(game_mode)
        battle_window = battle(player_team, team_p2, game_mode)
        battle_window.show()
        app.exec_()
        
        

