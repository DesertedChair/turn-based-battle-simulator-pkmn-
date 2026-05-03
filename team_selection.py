from encodings.punycode import T
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QCheckBox, QScrollArea, QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, pyqtSignal, QPropertyAnimation, QPoint, QEasingCurve

def get_pokemon_data(name_or_id):
    pokemon_data = {
        1: {
            'name': 'bulbasaur',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 49}, {'base_stat': 49}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'vine-whip'}}, {'move': {'name': 'razor-leaf'}}],
        },
        2: {
            'name': 'ivysaur',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 62}, {'base_stat': 63}, {'base_stat': 80}, {'base_stat': 80}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'vine-whip'}}, {'move': {'name': 'razor-leaf'}}],
        },
        3: {
            'name': 'venusaur',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 82}, {'base_stat': 83}, {'base_stat': 100}, {'base_stat': 100}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'sludge-bomb'}}, {'move': {'name': 'giga-drain'}}, {'move': {'name': 'razor-leaf'}}, {'move': {'name': 'growth'}}],
        },
        4: {
            'name': 'charmander',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 188}, {'base_stat': 52}, {'base_stat': 43}, {'base_stat': 60}, {'base_stat': 50}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'ember'}}, {'move': {'name': 'flamethrower'}}],
        },
        5: {
            'name': 'charmeleon',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 226}, {'base_stat': 64}, {'base_stat': 58}, {'base_stat': 80}, {'base_stat': 65}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'ember'}}, {'move': {'name': 'flamethrower'}}],
        },
        6: {
            'name': 'charizard',
            'types': [{'type': {'name': 'fire'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 266}, {'base_stat': 84}, {'base_stat': 78}, {'base_stat': 109}, {'base_stat': 85}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'flare-blitz'}}, {'move': {'name': 'flamethrower'}}, {'move': {'name': 'fly'}}],
        },
        7: {
            'name': 'squirtle',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 198}, {'base_stat': 48}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 54}, {'base_stat': 43}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'bubble'}}, {'move': {'name': 'water gun'}}],
        },
        8: {
            'name': 'wartortle',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 228}, {'base_stat': 63}, {'base_stat': 80}, {'base_stat': 65}, {'base_stat': 80}, {'base_stat': 58}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'water-gun'}}, {'move': {'name': 'bubble-beam'}}],
        },
        9: {
            'name': 'blastoise',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 268}, {'base_stat': 83}, {'base_stat': 100}, {'base_stat': 85}, {'base_stat': 105}, {'base_stat': 78}],
            'moves': [{'move': {'name': 'bite'}}, {'move': {'name': 'water-pulse'}}, {'move': {'name': 'iron-defense'}}, {'move': {'name': 'hydro-pump'}}],
        },
        10: {
            'name': 'caterpie',
            'types': [{'type': {'name': 'bug'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 30}, {'base_stat': 35}, {'base_stat': 20}, {'base_stat': 20}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'bug-bite'}}],
        },
        11: {
            'name': 'metapod',
            'types': [{'type': {'name': 'bug'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 20}, {'base_stat': 55}, {'base_stat': 25}, {'base_stat': 25}, {'base_stat': 30}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'bug-bite'}}],
        },
        12: {
            'name': 'butterfree',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 45}, {'base_stat': 50}, {'base_stat': 90}, {'base_stat': 80}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'bug-bite'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'gust'}}],
        },
        13: {
            'name': 'weedle',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 35}, {'base_stat': 30}, {'base_stat': 20}, {'base_stat': 20}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'bug-bite'}}],
        },
        14: {
            'name': 'kakuna',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 25}, {'base_stat': 50}, {'base_stat': 25}, {'base_stat': 25}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'bug-bite'}}],
        },
        15: {
            'name': 'beedrill',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 90}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 80}, {'base_stat': 75}],
            'moves': [{'move': {'name': 'leech-life'}}, {'move': {'name': 'bug-bite'}}, {'move': {'name': 'twineedle'}}, {'move': {'name': 'venoshock'}}],
        },
        16: {
            'name': 'pidgey',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 45}, {'base_stat': 40}, {'base_stat': 35}, {'base_stat': 35}, {'base_stat': 56}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'gust'}}],
        },
        17: {
            'name': 'pidgeotto',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 236}, {'base_stat': 60}, {'base_stat': 55}, {'base_stat': 50}, {'base_stat': 50}, {'base_stat': 71}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'gust'}}, {'move': {'name': 'wing-attack'}}],
        },
        18: {
            'name': 'pidgeot',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 276}, {'base_stat': 80}, {'base_stat': 75}, {'base_stat': 70}, {'base_stat': 70}, {'base_stat': 91}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'brave-bird'}}, {'move': {'name': 'wing-attack'}},  {'move': {'name': 'air-slash'}}],
        },
        19: {
            'name': 'rattata',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 56}, {'base_stat': 35}, {'base_stat': 25}, {'base_stat': 35}, {'base_stat': 72}],
            'moves': [{'move': {'name': 'quick-attack'}}, {'move': {'name': 'bite'}}],
        },
        20: {
            'name': 'raticate',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 81}, {'base_stat': 60}, {'base_stat': 50}, {'base_stat': 70}, {'base_stat': 97}],
            'moves': [{'move': {'name': 'quick-attack'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'crunch'}}, {'move': {'name': 'take-down'}}],
        },
        21: {
            'name': 'spearow',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 60}, {'base_stat': 30}, {'base_stat': 31}, {'base_stat': 31}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'peck'}}, {'move': {'name': 'fury-attack'}}],
        },
        22: {
            'name': 'fearow',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 90}, {'base_stat': 65}, {'base_stat': 61}, {'base_stat': 61}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'peck'}}, {'move': {'name': 'drill-peck'}}, {'move': {'name': 'take-down'}}],
        },
        23: {
            'name': 'ekans',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 60}, {'base_stat': 44}, {'base_stat': 40}, {'base_stat': 54}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'bite'}}, {'move': {'name': 'acid'}}],
        },
        24: {
            'name': 'arbok',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 95}, {'base_stat': 69}, {'base_stat': 65}, {'base_stat': 79}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'bite'}}, {'move': {'name': 'crunch'}}, {'move': {'name': 'sludge-bomb'}}],
        },
        25: {
            'name': 'pikachu',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 55}, {'base_stat': 40}, {'base_stat': 50}, {'base_stat': 50}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'thunder-shock'}}, {'move': {'name': 'iron-tail'}}, {'move': {'name': 'volt-tackle'}}, {'move': {'name': 'quick-attack'}}],
        },
        26: {
            'name': 'raichu',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 90}, {'base_stat': 55}, {'base_stat': 90}, {'base_stat': 80}, {'base_stat': 110}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'thunderbolt'}}, {'move': {'name': 'thunder'}}],
        },
        27: {
            'name': 'sandshrew',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 75}, {'base_stat': 85}, {'base_stat': 20}, {'base_stat': 30}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'bulldoze'}}],
        },
        28: {
            'name': 'sandslash',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 260}, {'base_stat': 100}, {'base_stat': 110}, {'base_stat': 45}, {'base_stat': 55}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'bulldoze'}}, {'move': {'name': 'earthquake'}}],
        },
        29: {
            'name': 'nidoranf',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 47}, {'base_stat': 52}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 41}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'scratch'}}],
        },
        30: {
            'name': 'nidorina',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 62}, {'base_stat': 67}, {'base_stat': 55}, {'base_stat': 55}, {'base_stat': 56}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'scratch'}}, {'move': {'name': 'bite'}}],
        },
        31: {
            'name': 'nidoqueen',
            'types': [{'type': {'name': 'poison'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 82}, {'base_stat': 87}, {'base_stat': 75}, {'base_stat': 85}, {'base_stat': 76}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'earth-power'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'sludge-wave'}}],
        },
        32: {
            'name': 'nidoranm',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 202}, {'base_stat': 57}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'peck'}}],
        },
        33: {
            'name': 'nidorino',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 232}, {'base_stat': 72}, {'base_stat': 57}, {'base_stat': 55}, {'base_stat': 55}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'peck'}}, {'move': {'name': 'horn-attack'}}],
        },
        34: {
            'name': 'nidoking',
            'types': [{'type': {'name': 'poison'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 272}, {'base_stat': 92}, {'base_stat': 77}, {'base_stat': 85}, {'base_stat': 75}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'earth-power'}}, {'move': {'name': 'horn-attack'}}, {'move': {'name': 'sludge-wave'}}],
        },
        35: {
            'name': 'clefairy',
            'types': [{'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 344}, {'base_stat': 45}, {'base_stat': 48}, {'base_stat': 60}, {'base_stat': 65}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'stored-power'}}, {'move': {'name': 'disarming-voice'}}],
        },
        36: {
            'name': 'clefable',
            'types': [{'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 70}, {'base_stat': 73}, {'base_stat': 85}, {'base_stat': 90}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'stored-power'}}, {'move': {'name': 'disarming-voice'}}, {'move': {'name': 'meteor-mash'}}],
        },
        37: {
            'name': 'vulpix',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 186}, {'base_stat': 41}, {'base_stat': 40}, {'base_stat': 50}, {'base_stat': 65}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'ember'}}, {'move': {'name': 'quick-attack'}}, {'move': {'name': 'flamethrower'}}],
        },
        38: {
            'name': 'ninetales',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 256}, {'base_stat': 76}, {'base_stat': 75}, {'base_stat': 81}, {'base_stat': 100}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'ember'}}, {'move': {'name': 'extrasensory'}}, {'move': {'name': 'flamethrower'}}, {'move': {'name': 'fire-blast'}}],
        },
        39: {
            'name': 'jigglypuff',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 340}, {'base_stat': 45}, {'base_stat': 20}, {'base_stat': 45}, {'base_stat': 25}, {'base_stat': 20}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'covet'}}, {'move': {'name': 'disarming-voice'}}],
        },
        40: {
            'name': 'wigglytuff',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 390}, {'base_stat': 70}, {'base_stat': 45}, {'base_stat': 75}, {'base_stat': 50}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'covet'}}, {'move': {'name': 'disarming-voice'}}, {'move': {'name': 'play-rough'}}],
        },
        41: {
            'name': 'zubat',
            'types': [{'type': {'name': 'poison'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 45}, {'base_stat': 35}, {'base_stat': 30}, {'base_stat': 40}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'astonish'}}, {'move': {'name': 'poison-fang'}}, {'move': {'name': 'air-cutter'}}],
        },
        42: {
            'name': 'golbat',
            'types': [{'type': {'name': 'poison'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 260}, {'base_stat': 80}, {'base_stat': 70}, {'base_stat': 65}, {'base_stat': 75}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'astonish'}}, {'move': {'name': 'poison-fang'}}, {'move': {'name': 'air-cutter'}},  {'move': {'name': 'venoshock'}}],
        },
        43: {
            'name': 'oddish',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 50}, {'base_stat': 55}, {'base_stat': 75}, {'base_stat': 65}, {'base_stat': 30}],
            'moves': [{'move': {'name': 'absorb'}}, {'move': {'name': 'acid'}}],
        },
        44: {
            'name': 'gloom',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 65}, {'base_stat': 70}, {'base_stat': 85}, {'base_stat': 75}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'mega-drain'}}, {'move': {'name': 'acid'}}, {'move': {'name': 'moonblast'}}],
        },
        45: {
            'name': 'vileplume',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 260}, {'base_stat': 80}, {'base_stat': 85}, {'base_stat': 100}, {'base_stat': 90}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'mega-drain'}}, {'move': {'name': 'acid'}}, {'move': {'name': 'moonblast'}}, {'move': {'name': 'petal-dance'}}],
        },
        46: {
            'name': 'paras',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'grass'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 70}, {'base_stat': 55}, {'base_stat': 45}, {'base_stat': 55}, {'base_stat': 25}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'leech-life'}}],
        },
        47: {
            'name': 'parasect',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'grass'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 95}, {'base_stat': 80}, {'base_stat': 60}, {'base_stat': 80}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'leech-life'}}, {'move': {'name': 'mega-drain'}}, {'move': {'name': 'body-slam'}}],
        },
        48: {
            'name': 'venonat',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 55}, {'base_stat': 50}, {'base_stat': 40}, {'base_stat': 55}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'leech-life'}}, {'move': {'name': 'mega-drain'}}, {'move': {'name': 'confusion'}}],
        },
        49: {
            'name': 'venomoth',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 90}, {'base_stat': 75}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'solar-beam'}}, {'move': {'name': 'mega-drain'}}, {'move': {'name': 'tackle'}}],
        },
        50: {
            'name': 'diglett',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 130}, {'base_stat': 55}, {'base_stat': 25}, {'base_stat': 35}, {'base_stat': 45}, {'base_stat': 95}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'dig'}}, {'move': {'name': 'slash'}}, {'move': {'name': 'rock-slide'}}],
        },
        51: {
            'name': 'dugtrio',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 100}, {'base_stat': 50}, {'base_stat': 50}, {'base_stat': 70}, {'base_stat': 120}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'dig'}}, {'move': {'name': 'earthquake'}}, {'move': {'name': 'rock-slide'}}],
        },
        52: {
            'name': 'meowth',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 45}, {'base_stat': 35}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'pay-day'}}, {'move': {'name': 'rage'}}],
        },
        53: {
            'name': 'persian',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 70}, {'base_stat': 60}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 115}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'pay-day'}}, {'move': {'name': 'fury-attack'}}],
        },
        54: {
            'name': 'psyduck',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 52}, {'base_stat': 48}, {'base_stat': 65}, {'base_stat': 50}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'water-gun'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'swift'}}],
        },
        55: {
            'name': 'golduck',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 82}, {'base_stat': 78}, {'base_stat': 95}, {'base_stat': 80}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'hydro-pump'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'strength'}}],
        },
        56: {
            'name': 'mankey',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 80}, {'base_stat': 35}, {'base_stat': 35}, {'base_stat': 45}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'scratch'}}, {'move': {'name': 'karate-chop'}}, {'move': {'name': 'thrash'}}, {'move': {'name': 'low-kick'}}],
        },
        57: {
            'name': 'primeape',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 105}, {'base_stat': 60}, {'base_stat': 60}, {'base_stat': 70}, {'base_stat': 95}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'submission'}}, {'move': {'name': 'mega-kick'}}, {'move': {'name': 'low-kick'}}],
        },
        58: {
            'name': 'growlithe',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 70}, {'base_stat': 45}, {'base_stat': 70}, {'base_stat': 50}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'ember'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'flamethrower'}}],
        },
        59: {
            'name': 'arcanine',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 110}, {'base_stat': 80}, {'base_stat': 100}, {'base_stat': 80}, {'base_stat': 95}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'flare-blitz'}}, {'move': {'name': 'flamethrower'}}],
        },
        60: {
            'name': 'poliwag',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 50}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'bubble'}}, {'move': {'name': 'water-gun'}}, {'move': {'name': 'body-slam'}}, {'move': {'name': 'surf'}}],
        },
        61: {
            'name': 'poliwhirl',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 50}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'mega-punch'}}, {'move': {'name': 'ice-beam'}}, {'move': {'name': 'body-slam'}}, {'move': {'name': 'surf'}}],
        },
        62: {
            'name': 'poliwrath',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 95}, {'base_stat': 95}, {'base_stat': 70}, {'base_stat': 90}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'hydro-pump'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'mega-punch'}}, {'move': {'name': 'double-edge'}}],
        },
        63: {
            'name': 'abra',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 160}, {'base_stat': 20}, {'base_stat': 15}, {'base_stat': 105}, {'base_stat': 55}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'body-slam'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'tackle'}}, {'move': {'name': 'psybeam'}}],
        },
        64: {
            'name': 'kadabra',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 35}, {'base_stat': 30}, {'base_stat': 120}, {'base_stat': 70}, {'base_stat': 105}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'take-down'}}],
        },
        65: {
            'name': 'alakazam',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 50}, {'base_stat': 45}, {'base_stat': 135}, {'base_stat': 95}, {'base_stat': 120}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'hyper-beam'}}, {'move': {'name': 'thunder'}}],
        },
        66: {
            'name': 'machop',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 80}, {'base_stat': 50}, {'base_stat': 35}, {'base_stat': 35}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'karate-chop'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'submission'}}, {'move': {'name': 'body-slam'}}],
        },
        67: {
            'name': 'machoke',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 100}, {'base_stat': 70}, {'base_stat': 50}, {'base_stat': 60}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'mega-punch'}}, {'move': {'name': 'low-kick'}}, {'move': {'name': 'submission'}}, {'move': {'name': 'strength'}}],
        },
        68: {
            'name': 'machamp',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 130}, {'base_stat': 80}, {'base_stat': 65}, {'base_stat': 85}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'mega-punch'}}, {'move': {'name': 'low-kick'}}, {'move': {'name': 'submission'}}, {'move': {'name': 'mega-kick'}}],
        },
        69: {
            'name': 'bellsprout',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 75}, {'base_stat': 35}, {'base_stat': 70}, {'base_stat': 30}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'vine-whip'}}, {'move': {'name': 'acid'}}, {'move': {'name': 'slam'}}, {'move': {'name': 'razor-leaf'}}],
        },
        70: {
            'name': 'weepinbell',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 90}, {'base_stat': 50}, {'base_stat': 85}, {'base_stat': 45}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'vine-whip'}}, {'move': {'name': 'poison-jab'}}, {'move': {'name': 'slam'}}, {'move': {'name': 'razor-leaf'}}],
        },
        71: {
            'name': 'victreebel',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 105}, {'base_stat': 65}, {'base_stat': 100}, {'base_stat': 60}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'power-whip'}}, {'move': {'name': 'poison-jab'}}, {'move': {'name': 'slam'}}, {'move': {'name': 'mega-drain'}}],
        },
        72: {
            'name': 'tentacool',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 40}, {'base_stat': 35}, {'base_stat': 50}, {'base_stat': 100}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'water-gun'}}, {'move': {'name': 'acid'}}, {'move': {'name': 'water-pulse'}}],
        },
        73: {
            'name': 'tentacruel',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 70}, {'base_stat': 65}, {'base_stat': 80}, {'base_stat': 120}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'hydro-pump'}}, {'move': {'name': 'poison-jab'}}, {'move': {'name': 'water-pulse'}},  {'move': {'name': 'sludge-wave'}}],
        },
        74: {
            'name': 'geodude',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 80}, {'base_stat': 100}, {'base_stat': 30}, {'base_stat': 30}, {'base_stat': 20}],
            'moves': [{'move': {'name': 'roll-out'}}, {'move': {'name': 'bulldoze'}}, {'move': {'name': 'tackle'}}],
        },
        75: {
            'name': 'graveler',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 95}, {'base_stat': 115}, {'base_stat': 45}, {'base_stat': 45}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'roll-out'}}, {'move': {'name': 'smack-down'}}, {'move': {'name': 'double-edge'}}],
        },
        76: {
            'name': 'golem',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 110}, {'base_stat': 130}, {'base_stat': 55}, {'base_stat': 65}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'stone-edge'}}, {'move': {'name': 'explosion'}}, {'move': {'name': 'double-edge'}}, {'move': {'name': 'earthquake'}}],
        },
        77: {
            'name': 'ponyta',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 85}, {'base_stat': 55}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'ember'}}, {'move': {'name': 'flame-wheel'}}],
        },
        78: {
            'name': 'rapidash',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 100}, {'base_stat': 70}, {'base_stat': 80}, {'base_stat': 80}, {'base_stat': 105}],
            'moves': [{'move': {'name': 'megahorn'}}, {'move': {'name': 'stomp'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'flare-blitz'}}],
        },
        79: {
            'name': 'slowpoke',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 40}, {'base_stat': 40}, {'base_stat': 15}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'water-pulse'}}],
        },
        80: {
            'name': 'slowbro',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 300}, {'base_stat': 75}, {'base_stat': 110}, {'base_stat': 100}, {'base_stat': 80}, {'base_stat': 30}],
            'moves': [{'move': {'name': 'headbutt'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'water-pulse'}}, {'move': {'name': 'psychic'}}],
        },
        81: {
            'name': 'magnemite',
            'types': [{'type': {'name': 'electric'}}, {'type': {'name': 'steel'}}],
            'stats': [{'base_stat': 160}, {'base_stat': 35}, {'base_stat': 70}, {'base_stat': 95}, {'base_stat': 55}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'thunder-shock'}}, {'move': {'name': 'spark'}}],
        },
        82: {
            'name': 'magneton',
            'types': [{'type': {'name': 'electric'}}, {'type': {'name': 'steel'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 60}, {'base_stat': 95}, {'base_stat': 120}, {'base_stat': 70}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'tri-attack'}}, {'move': {'name': 'flash-cannon'}}, {'move': {'name': 'discharge'}}, {'move': {'name': 'zap-cannon'}}],
        },
        83: {
            'name': 'farfetchd',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 214}, {'base_stat': 65}, {'base_stat': 55}, {'base_stat': 58}, {'base_stat': 62}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'knock-off'}}, {'move': {'name': 'leaf-blade'}}, {'move': {'name': 'brave-bird'}}],
        },
        84: {
            'name': 'doduo',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 85}, {'base_stat': 45}, {'base_stat': 35}, {'base_stat': 35}, {'base_stat': 75}],
            'moves': [{'move': {'name': 'peck'}}, {'move': {'name': 'fury-attack'}}, {'move': {'name': 'double-hit'}}],
        },
        85: {
            'name': 'dodrio',
            'types': [{'type': {'name': 'normal'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 110}, {'base_stat': 70}, {'base_stat': 60}, {'base_stat': 60}, {'base_stat': 110}],
            'moves': [{'move': {'name': 'tri-attack'}}, {'move': {'name': 'double-hit'}}, {'move': {'name': 'pluck'}}, {'move': {'name': 'drill-peck'}}],
        },
        86: {
            'name': 'seel',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 45}, {'base_stat': 55}, {'base_stat': 45}, {'base_stat': 70}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'headbutt'}}, {'move': {'name': 'aurora-beam'}}, {'move': {'name': 'take-down'}}],
        },
        87: {
            'name': 'dewgong',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'ice'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 70}, {'base_stat': 80}, {'base_stat': 70}, {'base_stat': 95}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'ice-beam'}}, {'move': {'name': 'surf'}}, {'move': {'name': 'blizzard'}}],
        },
        88: {
            'name': 'grimer',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 80}, {'base_stat': 50}, {'base_stat': 40}, {'base_stat': 50}, {'base_stat': 25}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'sludge'}}, {'move': {'name': 'acid'}}],
        },
        89: {
            'name': 'muk',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 320}, {'base_stat': 105}, {'base_stat': 75}, {'base_stat': 65}, {'base_stat': 100}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'sludge'}}, {'move': {'name': 'sludge-bomb'}}, {'move': {'name': 'hyper-beam'}}],
        },
        90: {
            'name': 'shellder',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 65}, {'base_stat': 100}, {'base_stat': 45}, {'base_stat': 25}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'clamp'}}, {'move': {'name': 'bubble-beam'}}],
        },
        91: {
            'name': 'cloyster',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'ice'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 95}, {'base_stat': 180}, {'base_stat': 85}, {'base_stat': 45}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'double-edge'}}, {'move': {'name': 'surf'}}, {'move': {'name': 'aurora-beam'}}, {'move': {'name': 'ice-beam'}}],
        },
        92: {
            'name': 'gastly',
            'types': [{'type': {'name': 'ghost'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 35}, {'base_stat': 30}, {'base_stat': 100}, {'base_stat': 35}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'lick'}}, {'move': {'name': 'rage'}}, {'move': {'name': 'mega-drain'}}],
        },
        93: {
            'name': 'haunter',
            'types': [{'type': {'name': 'ghost'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 50}, {'base_stat': 45}, {'base_stat': 115}, {'base_stat': 55}, {'base_stat': 95}],
            'moves': [{'move': {'name': 'lick'}}, {'move': {'name': 'dream-eater'}}, {'move': {'name': 'thunderbolt'}}],
        },
        94: {
            'name': 'gengar',
            'types': [{'type': {'name': 'ghost'}}, {'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 130}, {'base_stat': 75}, {'base_stat': 110}],
            'moves': [{'move': {'name': 'dream-eater'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'mega-kick'}}, {'move': {'name': 'thunder'}}],
        },
        95: {
            'name': 'onix',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 45}, {'base_stat': 160}, {'base_stat': 30}, {'base_stat': 45}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'body-slam'}}, {'move': {'name': 'earthquake'}}, {'move': {'name': 'dig'}}, {'move': {'name': 'rock-slide'}}],
        },
        96: {
            'name': 'drowzee',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 48}, {'base_stat': 45}, {'base_stat': 43}, {'base_stat': 90}, {'base_stat': 42}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'confusion'}}, {'move': {'name': 'headbutt'}}],
        },
        97: {
            'name': 'hypno',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 280}, {'base_stat': 73}, {'base_stat': 70}, {'base_stat': 73}, {'base_stat': 115}, {'base_stat': 67}],
            'moves': [{'move': {'name': 'mega-punch'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'dream-eater'}}, {'move': {'name': 'submission'}}],
        },
        98: {
            'name': 'krabby',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 105}, {'base_stat': 90}, {'base_stat': 25}, {'base_stat': 25}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'bubble'}}, {'move': {'name': 'vice-grip'}}, {'move': {'name': 'water-gun'}}],
        },
        99: {
            'name': 'kingler',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 130}, {'base_stat': 115}, {'base_stat': 50}, {'base_stat': 50}, {'base_stat': 75}],
            'moves': [{'move': {'name': 'stomp'}}, {'move': {'name': 'crabhammer'}}, {'move': {'name': 'ice-beam'}}, {'move': {'name': 'hyper-beam'}}],
        },
        100: {
            'name': 'voltorb',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 30}, {'base_stat': 50}, {'base_stat': 55}, {'base_stat': 55}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'swift'}}, {'move': {'name': 'thunderbolt'}}],
        },
        101: {
            'name': 'electrode',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 50}, {'base_stat': 70}, {'base_stat': 80}, {'base_stat': 80}, {'base_stat': 150}],
            'moves': [{'move': {'name': 'take-down'}}, {'move': {'name': 'thunder'}}, {'move': {'name': 'explosion'}}, {'move': {'name': 'hyper-beam'}}],
        },
        102: {
            'name': 'exeggcute',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 40}, {'base_stat': 80}, {'base_stat': 60}, {'base_stat': 45}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'barrage'}}, {'move': {'name': 'absorb'}}, {'move': {'name': 'psychic'}}],
        },
        103: {
            'name': 'exeggutor',
            'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 300}, {'base_stat': 95}, {'base_stat': 85}, {'base_stat': 125}, {'base_stat': 75}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'body-slam'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'solar-beam'}}, {'move': {'name': 'giga-drain'}}],
        },
        104: {
            'name': 'cubone',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 50}, {'base_stat': 95}, {'base_stat': 40}, {'base_stat': 50}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'headbutt'}}, {'move': {'name': 'double-edge'}}, {'move': {'name': 'bonemerang'}}],
        },
        105: {
            'name': 'marowak',
            'types': [{'type': {'name': 'ground'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 80}, {'base_stat': 110}, {'base_stat': 50}, {'base_stat': 80}, {'base_stat': 45}],
            'moves': [{'move': {'name': 'headbutt'}}, {'move': {'name': 'belly-drum'}}, {'move': {'name': 'bone-rush'}}, {'move': {'name': 'bonemerang'}}],
        },
        106: {
            'name': 'hitmonlee',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 120}, {'base_stat': 53}, {'base_stat': 35}, {'base_stat': 110}, {'base_stat': 87}],
            'moves': [{'move': {'name': 'blaze-kick'}}, {'move': {'name': 'axe-kick'}}, {'move': {'name': 'high-jump-kick'}}, {'move': {'name': 'close-combat'}}],
        },
        107: {
            'name': 'hitmonchan',
            'types': [{'type': {'name': 'fighting'}}],
            'stats': [{'base_stat': 210}, {'base_stat': 105}, {'base_stat': 79}, {'base_stat': 35}, {'base_stat': 110}, {'base_stat': 76}],
            'moves': [{'move': {'name': 'fire-punch'}}, {'move': {'name': 'ice-punch'}}, {'move': {'name': 'thunder-punch'}}, {'move': {'name': 'close-combat'}}],
        },
        108: {
            'name': 'lickitung',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 55}, {'base_stat': 75}, {'base_stat': 60}, {'base_stat': 75}, {'base_stat': 30}],
            'moves': [{'move': {'name': 'lick'}}, {'move': {'name': 'rollout'}}, {'move': {'name': 'stomp'}}, {'move': {'name': 'belly-drum'}}],
        },
        109: {
            'name': 'koffing',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 65}, {'base_stat': 95}, {'base_stat': 60}, {'base_stat': 45}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'sludge'}}, {'move': {'name': 'acid'}}],
        },
        110: {
            'name': 'weezing',
            'types': [{'type': {'name': 'poison'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 90}, {'base_stat': 120}, {'base_stat': 85}, {'base_stat': 70}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'sludge-bomb'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'sludge-wave'}}, {'move': {'name': 'explosion'}}],
        },
        111: {
            'name': 'rhyhorn',
            'types': [{'type': {'name': 'ground'}}, {'type': {'name': 'rock'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 85}, {'base_stat': 95}, {'base_stat': 30}, {'base_stat': 30}, {'base_stat': 25}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'horn-attack'}}, {'move': {'name': 'bulldoze'}}],
        },
        112: {
            'name': 'rhydon',
            'types': [{'type': {'name': 'ground'}}, {'type': {'name': 'rock'}}],
            'stats': [{'base_stat': 320}, {'base_stat': 130}, {'base_stat': 120}, {'base_stat': 45}, {'base_stat': 45}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'earthquake'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'stone-edge'}}, {'move': {'name': 'megahorn'}}],
        },
        113: {
            'name': 'chansey',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 610}, {'base_stat': 5}, {'base_stat': 5}, {'base_stat': 35}, {'base_stat': 105}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'pound'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'double-edge'}}, {'move': {'name': 'swift'}}],
        },
        114: {
            'name': 'tangela',
            'types': [{'type': {'name': 'grass'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 55}, {'base_stat': 115}, {'base_stat': 100}, {'base_stat': 40}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'absorb'}}, {'move': {'name': 'wrap'}}, {'move': {'name': 'growth'}}, {'move': {'name': 'vine-whip'}}],
        },
        115: {
            'name': 'kangaskhan',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 320}, {'base_stat': 95}, {'base_stat': 80}, {'base_stat': 40}, {'base_stat': 80}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'bite'}}, {'move': {'name': 'outrage'}}, {'move': {'name': 'headbutt'}}, {'move': {'name': 'stomp'}}],
        },
        116: {
            'name': 'horsea',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 40}, {'base_stat': 70}, {'base_stat': 70}, {'base_stat': 25}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'twister'}}, {'move': {'name': 'water-gun'}}, {'move': {'name': 'bubble-beam'}}],
        },
        117: {
            'name': 'seadra',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 65}, {'base_stat': 95}, {'base_stat': 95}, {'base_stat': 45}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'dragon-breath'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'water-pulse'}}, {'move': {'name': 'giga-impact'}}],
        },
        118: {
            'name': 'goldeen',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 200}, {'base_stat': 67}, {'base_stat': 60}, {'base_stat': 35}, {'base_stat': 50}, {'base_stat': 63}],
            'moves': [{'move': {'name': 'peck'}}, {'move': {'name': 'water-pulse'}}, {'move': {'name': 'surf'}}],
        },
        119: {
            'name': 'seaking',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 92}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 80}, {'base_stat': 68}],
            'moves': [{'move': {'name': 'water-pulse'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'megahorn'}}, {'move': {'name': 'ice-beam'}}],
        },
        120: {
            'name': 'staryu',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 45}, {'base_stat': 55}, {'base_stat': 70}, {'base_stat': 55}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'water-gun'}}, {'move': {'name': 'surf'}}],
        },
        121: {
            'name': 'starmie',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 75}, {'base_stat': 85}, {'base_stat': 100}, {'base_stat': 85}, {'base_stat': 115}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'hyper-beam'}}],
        },
        122: {
            'name': 'mrmime',
            'types': [{'type': {'name': 'psychic'}}, {'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 45}, {'base_stat': 65}, {'base_stat': 100}, {'base_stat': 120}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'thunder'}}, {'move': {'name': 'dream-eater'}}],
        },
        123: {
            'name': 'scyther',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 110}, {'base_stat': 80}, {'base_stat': 55}, {'base_stat': 80}, {'base_stat': 105}],
            'moves': [{'move': {'name': 'double-hit'}}, {'move': {'name': 'pin-missile'}}, {'move': {'name': 'swords-dance'}}, {'move': {'name': 'slash'}}],
        },
        124: {
            'name': 'jynx',
            'types': [{'type': {'name': 'ice'}}, {'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 50}, {'base_stat': 35}, {'base_stat': 115}, {'base_stat': 95}, {'base_stat': 95}],
            'moves': [{'move': {'name': 'ice-punch'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'dream-eater'}}],
        },
        125: {
            'name': 'electabuzz',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 83}, {'base_stat': 57}, {'base_stat': 95}, {'base_stat': 85}, {'base_stat': 105}],
            'moves': [{'move': {'name': 'quick-attack'}}, {'move': {'name': 'thunder-punch'}}, {'move': {'name': 'thunder'}}, {'move': {'name': 'giga-impact'}}],
        },
        126: {
            'name': 'magmar',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 95}, {'base_stat': 57}, {'base_stat': 100}, {'base_stat': 85}, {'base_stat': 93}],
            'moves': [{'move': {'name': 'flamethrower'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'hyper-beam'}}, {'move': {'name': 'giga-impact'}}],
        },
        127: {
            'name': 'pinsir',
            'types': [{'type': {'name': 'bug'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 125}, {'base_stat': 100}, {'base_stat': 55}, {'base_stat': 70}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'vise-grip'}}, {'move': {'name': 'double-hit'}}, {'move': {'name': 'submission'}}, {'move': {'name': 'close-combat'}}],
        },
        128: {
            'name': 'tauros',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 260}, {'base_stat': 100}, {'base_stat': 95}, {'base_stat': 40}, {'base_stat': 70}, {'base_stat': 110}],
            'moves': [{'move': {'name': 'double-edge'}}, {'move': {'name': 'giga-impact'}}, {'move': {'name': 'dig'}}, {'move': {'name': 'flamethrower'}}],
        },
        129: {
            'name': 'magikarp',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 150}, {'base_stat': 10}, {'base_stat': 55}, {'base_stat': 15}, {'base_stat': 20}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'tackle'}}],
        },
        130: {
            'name': 'gyarados',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 300}, {'base_stat': 125}, {'base_stat': 79}, {'base_stat': 60}, {'base_stat': 100}, {'base_stat': 81}],
            'moves': [{'move': {'name': 'crunch'}}, {'move': {'name': 'outrage'}}, {'move': {'name': 'ice-fang'}}, {'move': {'name': 'dragon-dance'}}],
        },
        131: {
            'name': 'lapras',
            'types': [{'type': {'name': 'water'}}, {'type': {'name': 'ice'}}],
            'stats': [{'base_stat': 370}, {'base_stat': 85}, {'base_stat': 80}, {'base_stat': 85}, {'base_stat': 95}, {'base_stat': 60}],
            'moves': [{'move': {'name': 'water-pulse'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'ice-beam'}}],
        },
        132: {
            'name': 'ditto',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 206}, {'base_stat': 48}, {'base_stat': 48}, {'base_stat': 48}, {'base_stat': 48}, {'base_stat': 48}],
            'moves': [{'move': {'name': 'tackle'}}, {'move': {'name': 'take-down'}}, {'move': {'name': 'swift'}}, {'move': {'name': 'stored-power'}}],
        },
        133: {
            'name': 'eevee',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 220}, {'base_stat': 55}, {'base_stat': 50}, {'base_stat': 45}, {'base_stat': 65}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'quick-attack'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'take-down'}}],
        },
        134: {
            'name': 'vaporeon',
            'types': [{'type': {'name': 'water'}}],
            'stats': [{'base_stat': 370}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 110}, {'base_stat': 95}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'water-pulse'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'quick-attack'}}, {'move': {'name': 'aurora-beam'}}],
        },
        135: {
            'name': 'jolteon',
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 110}, {'base_stat': 95}, {'base_stat': 130}],
            'moves': [{'move': {'name': 'thunder'}}, {'move': {'name': 'discharge'}}, {'move': {'name': 'quick-attack'}}, {'move': {'name': 'thunderbolt'}}],
        },
        136: {
            'name': 'flareon',
            'types': [{'type': {'name': 'fire'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 130}, {'base_stat': 60}, {'base_stat': 95}, {'base_stat': 110}, {'base_stat': 65}],
            'moves': [{'move': {'name': 'flamethrower'}}, {'move': {'name': 'fire-fang'}}, {'move': {'name': 'quick-attack'}}, {'move': {'name': 'fire-blast'}}],
        },
        137: {
            'name': 'porygon',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 240}, {'base_stat': 60}, {'base_stat': 70}, {'base_stat': 85}, {'base_stat': 75}, {'base_stat': 40}],
            'moves': [{'move': {'name': 'discharge'}}, {'move': {'name': 'tri-attack'}}, {'move': {'name': 'swift'}}, {'move': {'name': 'psybeam'}}],
        },
        138: {
            'name': 'omanyte',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'water'}}],
            'stats': [{'base_stat': 180}, {'base_stat': 40}, {'base_stat': 100}, {'base_stat': 90}, {'base_stat': 55}, {'base_stat': 35}],
            'moves': [{'move': {'name': 'rock-blast'}}, {'move': {'name': 'rollout'}}, {'move': {'name': 'surf'}}],
        },
        139: {
            'name': 'omastar',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'water'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 60}, {'base_stat': 125}, {'base_stat': 115}, {'base_stat': 70}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'crunch'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'rollout'}}],
        },
        140: {
            'name': 'kabuto',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'water'}}],
            'stats': [{'base_stat': 170}, {'base_stat': 80}, {'base_stat': 90}, {'base_stat': 55}, {'base_stat': 45}, {'base_stat': 55}],
            'moves': [{'move': {'name': 'absorb'}}, {'move': {'name': 'scratch'}}, {'move': {'name': 'bubble-beam'}}],
        },
        141: {
            'name': 'kabutops',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'water'}}],
            'stats': [{'base_stat': 230}, {'base_stat': 115}, {'base_stat': 105}, {'base_stat': 65}, {'base_stat': 70}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'aurora-beam'}}, {'move': {'name': 'mega-drain'}}, {'move': {'name': 'surf'}}],
        },
        142: {
            'name': 'aerodactyl',
            'types': [{'type': {'name': 'rock'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 270}, {'base_stat': 105}, {'base_stat': 65}, {'base_stat': 60}, {'base_stat': 75}, {'base_stat': 130}],
            'moves': [{'move': {'name': 'fly'}}, {'move': {'name': 'aerial-ace'}}, {'move': {'name': 'rock-slide'}}, {'move': {'name': 'giga-impact'}}],
        },
        143: {
            'name': 'snorlax',
            'types': [{'type': {'name': 'normal'}}],
            'stats': [{'base_stat': 430}, {'base_stat': 110}, {'base_stat': 65}, {'base_stat': 65}, {'base_stat': 110}, {'base_stat': 30}],
            'moves': [{'move': {'name': 'bite'}}, {'move': {'name': 'body-slam'}}, {'move': {'name': 'dig'}}, {'move': {'name': 'surf'}}],
        },
        144: {
            'name': 'articuno',
            'types': [{'type': {'name': 'ice'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 85}, {'base_stat': 100}, {'base_stat': 95}, {'base_stat': 125}, {'base_stat': 85}],
            'moves': [{'move': {'name': 'fly'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'ice-beam'}}, {'move': {'name': 'agility'}}],
        },
        145: {
            'name': 'zapdos',
            'types': [{'type': {'name': 'electric'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 90}, {'base_stat': 85}, {'base_stat': 125}, {'base_stat': 90}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'fly'}}, {'move': {'name': 'thunder'}}, {'move': {'name': 'zap-cannon'}}, {'move': {'name': 'agility'}}],
        },
        146: {
            'name': 'moltres',
            'types': [{'type': {'name': 'fire'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 290}, {'base_stat': 100}, {'base_stat': 90}, {'base_stat': 125}, {'base_stat': 85}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'fly'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'inferno'}}, {'move': {'name': 'agility'}}],
        },
        147: {
            'name': 'dratini',
            'types': [{'type': {'name': 'dragon'}}],
            'stats': [{'base_stat': 192}, {'base_stat': 64}, {'base_stat': 45}, {'base_stat': 50}, {'base_stat': 50}, {'base_stat': 50}],
            'moves': [{'move': {'name': 'slam'}}, {'move': {'name': 'dragon-breath'}}, {'move': {'name': 'twister'}}],
        },
        148: {
            'name': 'dragonair',
            'types': [{'type': {'name': 'dragon'}}],
            'stats': [{'base_stat': 232}, {'base_stat': 84}, {'base_stat': 65}, {'base_stat': 70}, {'base_stat': 70}, {'base_stat': 70}],
            'moves': [{'move': {'name': 'thunderbolt'}}, {'move': {'name': 'dragon-tail'}}, {'move': {'name': 'agility'}}, {'move': {'name': 'aqua-tail'}}],
        },
        149: {
            'name': 'dragonite',
            'types': [{'type': {'name': 'dragon'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 292}, {'base_stat': 134}, {'base_stat': 95}, {'base_stat': 100}, {'base_stat': 100}, {'base_stat': 80}],
            'moves': [{'move': {'name': 'outrage'}}, {'move': {'name': 'earthquake'}}, {'move': {'name': 'dragon-dance'}}, {'move': {'name': 'draco-meteor'}}],
        },
        150: {
            'name': 'mewtwo',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 322}, {'base_stat': 110}, {'base_stat': 90}, {'base_stat': 154}, {'base_stat': 90}, {'base_stat': 130}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'agility'}}, {'move': {'name': 'extrasensory'}}, {'move': {'name': 'double-edge'}}],
        },
        151: {
            'name': 'mew',
            'types': [{'type': {'name': 'psychic'}}],
            'stats': [{'base_stat': 310}, {'base_stat': 100}, {'base_stat': 100}, {'base_stat': 100}, {'base_stat': 100}, {'base_stat': 100}],
            'moves': [{'move': {'name': 'blizzard'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'zap-cannon'}}],
        },
    }
    for data in pokemon_data.values():
        if data['name'] == name_or_id:
            return data
    
    return pokemon_data.get(name_or_id, None)

def get_move_data(move_name):
    move_data = {
        # Normal Type Moves (Mostly Physical except Swift, Tri-Attack, Hyper Beam)
        'barrage': {'power': 15, 'type': 'normal', 'category': 'physical'},
        'wrap': {'power': 15, 'type': 'normal', 'category': 'physical'},
        'fury-attack': {'power': 15, 'type': 'normal', 'category': 'physical'}, #power adjusted 15 to 45, average 3 hits
        'double-hit': {'power': 35, 'type': 'normal', 'category': 'physical'},
        'scratch': {'power': 40, 'type': 'normal', 'category': 'physical'},
        'tackle': {'power': 40, 'type': 'normal', 'category': 'physical'},
        'pound': {'power': 40, 'type': 'normal', 'category': 'physical'},
        'pay-day': {'power': 40, 'type': 'normal', 'category': 'physical'},
        'rage': {'power': 40, 'type': 'normal', 'category': 'physical'},
        'quick-attack': {'power': 50, 'type': 'normal', 'category': 'physical'}, #power adjusted 40 to 50
        'cut': {'power': 50, 'type': 'normal', 'category': 'physical'},
        'rapid-spin': {'power': 50, 'type': 'normal', 'category': 'physical'},
        'karate-chop': {'power': 50, 'type': 'normal', 'category': 'physical'},
        'vice-grip': {'power': 55, 'type': 'normal', 'category': 'physical'},
        'covet': {'power': 60, 'type': 'normal', 'category': 'physical'},
        'swift': {'power': 60, 'type': 'normal', 'category': 'special'},  # Special in Gen 3+
        'horn-attack': {'power': 65, 'type': 'normal', 'category': 'physical'},
        'stomp': {'power': 65, 'type': 'normal', 'category': 'physical'},
        'slash': {'power': 70, 'type': 'normal', 'category': 'physical'},
        'headbutt': {'power': 70, 'type': 'normal', 'category': 'physical'},
        'crush-claw': {'power': 75, 'type': 'normal', 'category': 'physical'},
        'strength': {'power': 80, 'type': 'normal', 'category': 'physical'},
        'tri-attack': {'power': 80, 'type': 'normal', 'category': 'special'},
        'mega-punch': {'power': 80, 'type': 'normal', 'category': 'physical'},
        'slam': {'power': 80, 'type': 'normal', 'category': 'physical'},
        'body-slam': {'power': 85, 'type': 'normal', 'category': 'physical'},
        'take-down': {'power': 90, 'type': 'normal', 'category': 'physical'},
        'thrash': {'power': 90, 'type': 'normal', 'category': 'physical'},
        'double-edge': {'power': 120, 'type': 'normal', 'category': 'physical'},
        'mega-kick': {'power': 120, 'type': 'normal', 'category': 'physical'},
        'giga-impact': {'power': 150, 'type': 'normal', 'category': 'physical'},
        'hyper-beam': {'power': 150, 'type': 'normal', 'category': 'special'},
        'explosion': {'power': 500, 'type': 'normal', 'category': 'physical'},

        # Fighting Type Moves (Physical)
        'double-kick': {'power': 30, 'type': 'fighting', 'category': 'physical'},
        'low-kick': {'power': 50, 'type': 'fighting', 'category': 'physical'},
        'submission': {'power': 80, 'type': 'fighting', 'category': 'physical'},
        'close-combat': {'power': 120, 'type': 'fighting', 'category': 'physical'},
        'close-combat': {'power': 120, 'type': 'fighting', 'category': 'physical'},
        'axe-kick': {'power': 120, 'type': 'fighting', 'category': 'physical'},
        'high-jump-kick': {'power': 130, 'type': 'fighting', 'category': 'physical'},

        # Fairy Type Moves (Special except Play Rough)
        'disarming-voice': {'power': 40, 'type': 'fairy', 'category': 'special'},
        'play-rough': {'power': 90, 'type': 'fairy', 'category': 'physical'},
        'moonblast': {'power': 95, 'type': 'fairy', 'category': 'special'},

        # Grass Type Moves (Special except Vine Whip and Razor Leaf)
        'absorb': {'power': 20, 'type': 'grass', 'category': 'special'},
        'bullet-seed': {'power': 25, 'type': 'grass', 'category': 'physical'},
        'vine-whip': {'power': 45, 'type': 'grass', 'category': 'physical'},
        'mega-drain': {'power': 40, 'type': 'grass', 'category': 'special'},
        'razor-leaf': {'power': 55, 'type': 'grass', 'category': 'physical'},
        'giga-drain': {'power': 75, 'type': 'grass', 'category': 'special'},
        'leaf-blade': {'power': 90, 'type': 'grass', 'category': 'physical'},
        'petal-dance': {'power': 120, 'type': 'grass', 'category': 'special'},
        'solar-beam': {'power': 120, 'type': 'grass', 'category': 'special'},
        'power-whip': {'power': 120, 'type': 'grass', 'category': 'physical'},
        'leaf-storm': {'power': 130, 'type': 'grass', 'category': 'special'},

        # Fire Type Moves (Special)
        'ember': {'power': 40, 'type': 'fire', 'category': 'special'},
        'flame-wheel': {'power': 60, 'type': 'fire', 'category': 'physical'},
        'incinerate': {'power': 60, 'type': 'fire', 'category': 'special'},
        'fire-fang': {'power': 65, 'type': 'fire', 'category': 'physical'},
        'fire-punch': {'power': 75, 'type': 'fire', 'category': 'physical'},
        'blaze-kick': {'power': 85, 'type': 'fire', 'category': 'physical'},
        'flamethrower': {'power': 90, 'type': 'fire', 'category': 'special'},
        'inferno': {'power': 100, 'type': 'fire', 'category': 'special'},
        'fire-blast': {'power': 110, 'type': 'fire', 'category': 'special'},
        'flare-blitz': {'power': 120, 'type': 'fire', 'category': 'physical'},

        # Electric Type Moves (Special except Thunder Punch)
        'thunder-shock': {'power': 40, 'type': 'electric', 'category': 'special'},
        'spark': {'power': 65, 'type': 'electric', 'category': 'physical'},
        'thunder-punch': {'power': 75, 'type': 'electric', 'category': 'physical'},
        'discharge': {'power': 80, 'type': 'electric', 'category': 'special'},
        'thunderbolt': {'power': 90, 'type': 'electric', 'category': 'special'},
        'thunder': {'power': 110, 'type': 'electric', 'category': 'special'},
        'zap-cannon': {'power': 120, 'type': 'electric', 'category': 'special'},
        'volt-tackle': {'power': 120, 'type': 'electric', 'category': 'physical'},

        # Water Type Moves (Special)
        'clamp': {'power': 35, 'type': 'water', 'category': 'physical'},
        'water-gun': {'power': 40, 'type': 'water', 'category': 'special'},
        'bubble': {'power': 40, 'type': 'water', 'category': 'special'},
        'water-pulse': {'power': 60, 'type': 'water', 'category': 'special'},
        'bubble-beam': {'power': 65, 'type': 'water', 'category': 'special'},
        'surf': {'power': 90, 'type': 'water', 'category': 'special'},
        'aqua-tail': {'power': 90, 'type': 'water', 'category': 'physical'},
        'crabhammer': {'power': 90, 'type': 'water', 'category': 'physical'},
        'hydro-pump': {'power': 110, 'type': 'water', 'category': 'special'},

        # Flying Type Moves (Physical except Air Cutter & Air Slash)
        'peck': {'power': 35, 'type': 'flying', 'category': 'physical'},
        'gust': {'power': 40, 'type': 'flying', 'category': 'special'},
        'aerial-ace': {'power': 60, 'type': 'flying', 'category': 'physical'},
        'air-cutter': {'power': 60, 'type': 'flying', 'category': 'special'},
        'pluck': {'power': 60, 'type': 'flying', 'category': 'physical'},
        'wing-attack': {'power': 60, 'type': 'flying', 'category': 'physical'},
        'air-slash': {'power': 75, 'type': 'flying', 'category': 'special'},
        'drill-peck': {'power': 80, 'type': 'flying', 'category': 'physical'},
        'fly': {'power': 90, 'type': 'flying', 'category': 'physical'},
        'brave-bird': {'power': 120, 'type': 'flying', 'category': 'physical'},
        'hurricane': {'power': 140, 'type': 'flying', 'category': 'special'},

        # Rock Type Moves (Physical)
        'rock-blast': {'power': 25, 'type': 'rock', 'category': 'physical'},
        'rollout': {'power': 50, 'type': 'rock', 'category': 'physical'}, #power adjusted 30 to 50
        'smack-down': {'power': 50, 'type': 'rock', 'category': 'physical'},
        'rock-slide': {'power': 75, 'type': 'rock', 'category': 'physical'},
        'stone-edge': {'power': 100, 'type': 'rock', 'category': 'physical'},

        # Ground Type Moves (Physical except Earth Power)
        'bone-rush': {'power': 25, 'type': 'ground', 'category': 'physical'},
        'bonemerang': {'power': 50, 'type': 'ground', 'category': 'physical'},
        'bulldoze': {'power': 60, 'type': 'ground', 'category': 'physical'},
        'dig': {'power': 80, 'type': 'ground', 'category': 'physical'},
        'earth-power': {'power': 90, 'type': 'ground', 'category': 'special'},
        'earthquake': {'power': 100, 'type': 'ground', 'category': 'physical'},

        # Steel Type Moves (Physical)
        'flash-cannon': {'power': 80, 'type': 'steel', 'category': 'special'},
        'meteor-mash': {'power': 100, 'type': 'steel', 'category': 'physical'},
        'iron-tail': {'power': 100, 'type': 'steel', 'category': 'physical'},

        # Ice Type Moves (Special except ice fang and ice punch)
        'aurora-beam': {'power': 65, 'type': 'ice', 'category': 'special'},
        'ice-fang': {'power': 65, 'type': 'ice', 'category': 'physical'},
        'ice-punch': {'power': 75, 'type': 'ice', 'category': 'physical'},
        'ice-beam': {'power': 90, 'type': 'ice', 'category': 'special'},
        'blizzard': {'power': 120, 'type': 'ice', 'category': 'special'},

        # Psychic Type Moves (Special)
        'stored-power': {'power': 20, 'type': 'psychic', 'category': 'special'},
        'confusion': {'power': 50, 'type': 'psychic', 'category': 'special'},
        'psybeam': {'power': 65, 'type': 'psychic', 'category': 'special'},
        'dream-eater': {'power': 70, 'type': 'psychic', 'category': 'special'}, #power adjusted 100 to 70
        'extrasensory': {'power': 80, 'type': 'psychic', 'category': 'special'},
        'psychic': {'power': 90, 'type': 'psychic', 'category': 'special'},

        # Ghost Type Moves (Physical in early gens for Astonish)
        'lick': {'power': 20, 'type': 'ghost', 'category': 'physical'},
        'astonish': {'power': 30, 'type': 'ghost', 'category': 'physical'},

        # Bug Type Moves (Physical)
        'twineedle': {'power': 25, 'type': 'bug', 'category': 'physical'},
        'pin-missile': {'power': 25, 'type': 'bug', 'category': 'physical'},
        'fury-cutter': {'power': 40, 'type': 'bug', 'category': 'physical'},
        'leech-life': {'power': 40, 'type': 'bug', 'category': 'physical'},
        'bug-bite': {'power': 60, 'type': 'bug', 'category': 'physical'},
        'megahorn': {'power': 120, 'type': 'bug', 'category': 'physical'},

        # Poison Type Moves (Special except Poison Fang)
        'poison-sting': {'power': 15, 'type': 'poison', 'category': 'physical'},
        'acid': {'power': 40, 'type': 'poison', 'category': 'special'},
        'poison-fang': {'power': 50, 'type': 'poison', 'category': 'physical'},
        'sludge': {'power': 65, 'type': 'poison', 'category': 'special'},
        'venoshock': {'power': 65, 'type': 'poison', 'category': 'special'},
        'poison-jab': {'power': 80, 'type': 'poison', 'category': 'physical'},
        'sludge-bomb': {'power': 90, 'type': 'poison', 'category': 'special'},
        'sludge-wave': {'power': 95, 'type': 'poison', 'category': 'special'},

        # Dark Type Moves (Physical)
        'bite': {'power': 60, 'type': 'dark', 'category': 'physical'},
        'knock-off': {'power': 65, 'type': 'dark', 'category': 'physical'},
        'crunch': {'power': 80, 'type': 'dark', 'category': 'physical'},
        
        # Dragon type Moves
        'twister': {'power': 40, 'type': 'dragon', 'category': 'special'},
        'dragon-breath': {'power': 60, 'type': 'dragon', 'category': 'special'},
        'dragon-tail': {'power': 60, 'type': 'dragon', 'category': 'physical'},
        'dragon-claw': {'power': 80, 'type': 'dragon', 'category': 'physical'},
        'outrage': {'power': 120, 'type': 'dragon', 'category': 'physical'},
        'draco-meteor': {'power': 130, 'type': 'dragon', 'category': 'special'},
        
        #Status-related Moves
        'agility': {'power': -100, 'type': 'psychic', 'category': 'physical'},
        'calm-mind': {'power': -100, 'type': 'psychic', 'category': 'special'},
        'dragon-dance': {'power': -100, 'type': 'dragon', 'category': 'physical'},
        'growth': {'power': -100, 'type': 'normal', 'category': 'physical'},
        'iron-defense': {'power': -100, 'type': 'steel', 'category': 'physical'},
        'belly-drum': {'power': -100, 'type': 'normal', 'category': 'physical'},
    }

    # Return the data for the move, or None if the move is not found
    return move_data.get(move_name, None)




class MainWind(QMainWindow):
    def __init__(self, game_mode):
        super().__init__()
        self.challenge_callback = None
        self.is_challenge_mode = False
        self.game_mode = game_mode
        self.selected_team_p1 = []
        self.selected_team_p2 = []
        self.page = 1

        self.setWindowTitle("Pokemon Battle Simulator")
        self.setGeometry(0,0, 1280, 800)
        self.setWindowIcon(QIcon("assets/icons/pokeballicon.png"))
        self.team = []
        self.MAX_TEAM_SIZE = 6

        #Background
        labelbackground = QLabel(self)
        labelbackground.setGeometry(0,0,1280,800)
        background1 = QPixmap("assets/backgrounds/Menu_Background.png")
        labelbackground.setPixmap(background1)
        labelbackground.setScaledContents(True)

        #Selection background: Spring
        self.selectionspring = QLabel(self)
        self.selectionspring.setGeometry(50,50,915,400)
        spring_background = QPixmap("assets/backgrounds/spring.png")
        self.selectionspring.setPixmap(spring_background)
        self.selectionspring.setScaledContents(True)
        
        #Selection background: Summer
        self.selectionsummer = QLabel(self)
        self.selectionsummer.setGeometry(50,50,915,400)
        summer_background = QPixmap("assets/backgrounds/summer.png")
        self.selectionsummer.setPixmap(summer_background)
        self.selectionsummer.setScaledContents(True)
        self.selectionsummer.setVisible(False)
        
        #Selection background: Autumn
        self.selectionautumn = QLabel(self)
        self.selectionautumn.setGeometry(50,50,915,400)
        autumn_background = QPixmap("assets/backgrounds/autumn.png")
        self.selectionautumn.setPixmap(autumn_background)
        self.selectionautumn.setScaledContents(True)
        self.selectionautumn.setVisible(False)
        
        #Selection background: Winter
        self.selectionwinter = QLabel(self)
        self.selectionwinter.setGeometry(50,50,915,400)
        winter_background = QPixmap("assets/backgrounds/winter.png")
        self.selectionwinter.setPixmap(winter_background)
        self.selectionwinter.setScaledContents(True)
        self.selectionwinter.setVisible(False)
        
        #Text box 1
        textbox1 = QLabel(self)
        textbox1.setGeometry(300,10,400,55)
        textbox = QPixmap("assets/icons/dialogboxshort.png")
        textbox1.setPixmap(textbox)
        textbox1.setScaledContents(True)

        #Battle-related stuff initialization
        #Page 1
        self.bulbasaur = QPushButton(self)
        self.ivysaur = QPushButton(self)
        self.venusaur = QPushButton(self)
        self.charmander = QPushButton(self)
        self.charmeleon = QPushButton(self)
        self.charizard = QPushButton(self)
        self.squirtle = QPushButton(self)
        self.wartortle = QPushButton(self)
        self.blastoise = QPushButton(self)
        self.caterpie = QPushButton(self)
        self.metapod = QPushButton(self)
        self.butterfree = QPushButton(self)
        self.weedle = QPushButton(self)
        self.kakuna = QPushButton(self)
        self.beedrill = QPushButton(self)
        self.pidgey = QPushButton(self)
        self.pidgeotto = QPushButton(self)
        self.pidgeot = QPushButton(self)
        self.rattata = QPushButton(self)
        self.raticate = QPushButton(self)
        self.spearow = QPushButton(self)
        self.fearow = QPushButton(self)
        self.ekans = QPushButton(self)
        self.arbok = QPushButton(self)
        self.pikachu = QPushButton(self)
        self.raichu = QPushButton(self)
        self.sandshrew = QPushButton(self)
        self.sandslash = QPushButton(self)
        self.nidoranf = QPushButton(self)
        self.nidorina = QPushButton(self)
        self.nidoqueen = QPushButton(self)
        self.nidoranm = QPushButton(self)
        self.nidorino = QPushButton(self)
        self.nidoking = QPushButton(self)
        self.clefairy = QPushButton(self)
        self.clefable = QPushButton(self)
        self.vulpix = QPushButton(self)

        #Page 2
        self.ninetales = QPushButton(self)
        self.jigglypuff = QPushButton(self)
        self.wigglytuff = QPushButton(self)
        self.zubat = QPushButton(self)
        self.golbat = QPushButton(self)
        self.oddish = QPushButton(self)
        self.vileplume = QPushButton(self)
        self.paras = QPushButton(self)
        self.parasect = QPushButton(self)
        self.venonat = QPushButton(self)
        self.venomoth = QPushButton(self)
        self.diglett = QPushButton(self)
        self.dugtrio = QPushButton(self)
        self.meowth = QPushButton(self)
        self.persian = QPushButton(self)
        self.psyduck = QPushButton(self)
        self.golduck = QPushButton(self)
        self.mankey = QPushButton(self)
        self.primeape = QPushButton(self)
        self.growlithe = QPushButton(self)
        self.arcanine = QPushButton(self)
        self.poliwag = QPushButton(self)
        self.poliwhirl = QPushButton(self)
        self.poliwrath = QPushButton(self)
        self.abra = QPushButton(self)
        self.kadabra = QPushButton(self)
        self.alakazam = QPushButton(self)
        self.machop = QPushButton(self)
        self.machoke = QPushButton(self)
        self.machamp = QPushButton(self)
        self.bellsprout = QPushButton(self)
        self.weepinbell = QPushButton(self)
        self.victreebel = QPushButton(self)
        self.tentacool = QPushButton(self)
        self.tentacruel = QPushButton(self)
        self.geodude = QPushButton(self)

        #Page 3
        self.graveler = QPushButton(self)
        self.golem = QPushButton(self)
        self.ponyta = QPushButton(self)
        self.rapidash = QPushButton(self)
        self.slowpoke = QPushButton(self)
        self.slowbro = QPushButton(self)
        self.magnemite = QPushButton(self)
        self.magneton = QPushButton(self)
        self.farfetchd = QPushButton(self)
        self.doduo = QPushButton(self)
        self.dodrio = QPushButton(self)
        self.seel = QPushButton(self)
        self.dewgong = QPushButton(self)
        self.grimer = QPushButton(self)
        self.muk = QPushButton(self)
        self.shellder = QPushButton(self)
        self.cloyster = QPushButton(self)
        self.gastly = QPushButton(self)
        self.haunter = QPushButton(self)
        self.gengar = QPushButton(self)
        self.onix = QPushButton(self)
        self.drowzee = QPushButton(self)
        self.hypno = QPushButton(self)
        self.krabby = QPushButton(self)
        self.kingler = QPushButton(self)
        self.voltorb = QPushButton(self)
        self.electrode = QPushButton(self)
        self.exeggcute = QPushButton(self)
        self.exeggutor = QPushButton(self)
        self.cubone = QPushButton(self)
        self.marowak = QPushButton(self)
        self.hitmonlee = QPushButton(self)
        self.hitmonchan = QPushButton(self)
        self.lickitung = QPushButton(self)
        self.koffing = QPushButton(self)
        self.weezing = QPushButton(self)

        #Page 4
        self.rhyhorn = QPushButton(self)
        self.rhydon = QPushButton(self)
        self.chansey = QPushButton(self)
        self.tangela = QPushButton(self)
        self.kangaskhan = QPushButton(self)
        self.horsea = QPushButton(self)
        self.seadra = QPushButton(self)
        self.goldeen = QPushButton(self)
        self.seaking = QPushButton(self)
        self.staryu = QPushButton(self)
        self.starmie = QPushButton(self)
        self.mrmime = QPushButton(self)
        self.scyther = QPushButton(self)
        self.jynx = QPushButton(self)
        self.electabuzz = QPushButton(self)
        self.magmar = QPushButton(self)
        self.pinsir = QPushButton(self)
        self.tauros = QPushButton(self)
        self.magikarp = QPushButton(self)
        self.gyarados = QPushButton(self)
        self.lapras = QPushButton(self)
        self.ditto = QPushButton(self)
        self.eevee = QPushButton(self)
        self.vaporeon = QPushButton(self)
        self.jolteon = QPushButton(self)
        self.flareon = QPushButton(self)
        self.porygon = QPushButton(self)
        self.omanyte = QPushButton(self)
        self.omastar = QPushButton(self)
        self.kabuto = QPushButton(self)
        self.kabutops = QPushButton(self)
        self.aerodactyl = QPushButton(self)
        self.snorlax = QPushButton(self)
        self.articuno = QPushButton(self)
        self.zapdos = QPushButton(self)
        self.moltres = QPushButton(self)
        self.dratini = QPushButton(self)
        self.dragonair = QPushButton(self)
        self.dragonite = QPushButton(self)
        self.mewtwo = QPushButton(self)
        self.mew = QPushButton(self)

        

        self.P1_pkmn1 = QPushButton(self)
        self.P1_pkmn2 = QPushButton(self)
        self.P1_pkmn3 = QPushButton(self)
        self.P1_pkmn4 = QPushButton(self)
        self.P1_pkmn5 = QPushButton(self)
        self.P1_pkmn6 = QPushButton(self)
        

        self.P1_slots = [self.P1_pkmn1, self.P1_pkmn2, self.P1_pkmn3, self.P1_pkmn4, self.P1_pkmn5, self.P1_pkmn6]
        self.slot_pokemon_names = [None] * 6  # 6 slots, initially empty

        
            
        self.nextbtn = QPushButton(self)
        self.prevbtn = QPushButton(self)
        
        self.menu_message = QLabel("Select your Pokemon!", self)
        self.team_message = QLabel("", self)
        self.your_team_message = QLabel("Your Team:", self)



        #Calls the UI
        self.initUI()

    def get_teams(self):
        if self.game_mode == 1:
            return self.selected_team_p1
        elif self.game_mode == 2:
            return self.selected_team_p1, self.selected_team_p2

    closed = pyqtSignal()  # Add this at the class level

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def slide_in(self):
        screen_width = QApplication.primaryScreen().geometry().width()
        self.move(screen_width, self.y())
        self.show()

        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setDuration(500)
        self.anim.setStartValue(self.pos())
        self.anim.setEndValue(QPoint((screen_width - self.width()) // 2, self.y()))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.start()

    def initUI(self):
        #Page 1
        #Bulbasaur
        self.bulbasaur.setGeometry(50,50, 100,100)
        self.bulbasaur.setIcon(QIcon("assets/pokemon/BULBASAUR.gif"))
        self.bulbasaur.setIconSize(QSize(100, 100))
        self.bulbasaur.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.bulbasaur.clicked.connect(self.on_click_bulbasaur)

        #Ivysaur
        self.ivysaur.setGeometry(150,50, 100, 100)
        self.ivysaur.setIcon(QIcon("assets/pokemon/IVYSAUR.gif"))
        self.ivysaur.setIconSize(QSize(100, 100))
        self.ivysaur.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.ivysaur.clicked.connect(self.on_click_ivysaur)

        #Venusaur
        self.venusaur.setGeometry(250,50, 100, 100)
        self.venusaur.setIcon(QIcon("assets/pokemon/VENUSAUR.gif"))
        self.venusaur.setIconSize(QSize(100, 100))
        self.venusaur.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.venusaur.clicked.connect(self.on_click_venusaur)

        #Charmander
        self.charmander.setGeometry(350,50, 100, 100)
        self.charmander.setIcon(QIcon("assets/pokemon/CHARMANDER.gif"))
        self.charmander.setIconSize(QSize(100, 100))
        self.charmander.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.charmander.clicked.connect(self.on_click_charmander)

        #Charmeleon
        self.charmeleon.setGeometry(450,50, 100, 100)
        self.charmeleon.setIcon(QIcon("assets/pokemon/CHARMELEON.gif"))
        self.charmeleon.setIconSize(QSize(100, 100))
        self.charmeleon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.charmeleon.clicked.connect(self.on_click_charmeleon)

        #Charizard
        self.charizard.setGeometry(550,50, 100, 100)
        self.charizard.setIcon(QIcon("assets/pokemon/CHARIZARD.gif"))
        self.charizard.setIconSize(QSize(100, 100))
        self.charizard.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.charizard.clicked.connect(self.on_click_charizard)

        #Squirtle
        self.squirtle.setGeometry(650,50, 100, 100)
        self.squirtle.setIcon(QIcon("assets/pokemon/SQUIRTLE.gif"))
        self.squirtle.setIconSize(QSize(100, 100))
        self.squirtle.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.squirtle.clicked.connect(self.on_click_squirtle)

        #Wartortle
        self.wartortle.setGeometry(750,50, 100, 100)
        self.wartortle.setIcon(QIcon("assets/pokemon/WARTORTLE.gif"))
        self.wartortle.setIconSize(QSize(100, 100))
        self.wartortle.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.wartortle.clicked.connect(self.on_click_wartortle)

        #Blastoise
        self.blastoise.setGeometry(850,50, 100, 100)
        self.blastoise.setIcon(QIcon("assets/pokemon/BLASTOISE.gif"))
        self.blastoise.setIconSize(QSize(100, 100))
        self.blastoise.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.blastoise.clicked.connect(self.on_click_blastoise)
        
        #Caterpie
        self.caterpie.setGeometry(50,150, 100, 100)
        self.caterpie.setIcon(QIcon("assets/pokemon/CATERPIE.gif"))
        self.caterpie.setIconSize(QSize(100, 100))
        self.caterpie.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.caterpie.clicked.connect(self.on_click_caterpie)
        
        #Metapod
        self.metapod.setGeometry(150,150, 100, 100)
        self.metapod.setIcon(QIcon("assets/pokemon/METAPOD.gif"))
        self.metapod.setIconSize(QSize(100, 100))
        self.metapod.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.metapod.clicked.connect(self.on_click_metapod)
        
        #Butterfree
        self.butterfree.setGeometry(250,150, 100, 100)
        self.butterfree.setIcon(QIcon("assets/pokemon/BUTTERFREE.gif"))
        self.butterfree.setIconSize(QSize(100, 100))
        self.butterfree.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.butterfree.clicked.connect(self.on_click_butterfree)
        
        #Weedle
        self.weedle.setGeometry(350,150, 100, 100)
        self.weedle.setIcon(QIcon("assets/pokemon/WEEDLE.gif"))
        self.weedle.setIconSize(QSize(100, 100))
        self.weedle.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.weedle.clicked.connect(self.on_click_weedle)
        
        #Kakuna
        self.kakuna.setGeometry(450,150, 100, 100)
        self.kakuna.setIcon(QIcon("assets/pokemon/KAKUNA.gif"))
        self.kakuna.setIconSize(QSize(100, 100))
        self.kakuna.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kakuna.clicked.connect(self.on_click_kakuna)
        
        #Beedrill
        self.beedrill.setGeometry(550,150, 100, 100)
        self.beedrill.setIcon(QIcon("assets/pokemon/BEEDRILL.gif"))
        self.beedrill.setIconSize(QSize(100, 100))
        self.beedrill.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.beedrill.clicked.connect(self.on_click_beedrill)
        
        #Pidgey
        self.pidgey.setGeometry(650,150, 100, 100)
        self.pidgey.setIcon(QIcon("assets/pokemon/PIDGEY.gif"))
        self.pidgey.setIconSize(QSize(100, 100))
        self.pidgey.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.pidgey.clicked.connect(self.on_click_pidgey)
        
        #Pidgeotto
        self.pidgeotto.setGeometry(750,150, 100, 100)
        self.pidgeotto.setIcon(QIcon("assets/pokemon/PIDGEOTTO.gif"))
        self.pidgeotto.setIconSize(QSize(100, 100))
        self.pidgeotto.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.pidgeotto.clicked.connect(self.on_click_pidgeotto)
        
        #Pidgeot
        self.pidgeot.setGeometry(850,150, 100, 100)
        self.pidgeot.setIcon(QIcon("assets/pokemon/PIDGEOT.gif"))
        self.pidgeot.setIconSize(QSize(100, 100))
        self.pidgeot.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.pidgeot.clicked.connect(self.on_click_pidgeot)
        
        #Rattata
        self.rattata.setGeometry(50,250, 100, 100)
        self.rattata.setIcon(QIcon("assets/pokemon/RATTATA.gif"))
        self.rattata.setIconSize(QSize(100, 100))
        self.rattata.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.rattata.clicked.connect(self.on_click_rattata)
        
        #Raticate
        self.raticate.setGeometry(150,250, 100, 100)
        self.raticate.setIcon(QIcon("assets/pokemon/RATICATE.gif"))
        self.raticate.setIconSize(QSize(100, 100))
        self.raticate.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.raticate.clicked.connect(self.on_click_raticate)
        
        #Spearow
        self.spearow.setGeometry(250,250, 100, 100)
        self.spearow.setIcon(QIcon("assets/pokemon/SPEAROW.gif"))
        self.spearow.setIconSize(QSize(100, 100))
        self.spearow.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.spearow.clicked.connect(self.on_click_spearow)
        
        #Fearow
        self.fearow.setGeometry(350,250, 100, 100)
        self.fearow.setIcon(QIcon("assets/pokemon/FEAROW.gif"))
        self.fearow.setIconSize(QSize(100, 100))
        self.fearow.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.fearow.clicked.connect(self.on_click_fearow)
        
        #Ekans
        self.ekans.setGeometry(450,250, 100, 100)
        self.ekans.setIcon(QIcon("assets/pokemon/EKANS.gif"))
        self.ekans.setIconSize(QSize(100, 100))
        self.ekans.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.ekans.clicked.connect(self.on_click_ekans)
        
        #Arbok
        self.arbok.setGeometry(550,250, 100, 100)
        self.arbok.setIcon(QIcon("assets/pokemon/ARBOK.gif"))
        self.arbok.setIconSize(QSize(100, 100))
        self.arbok.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.arbok.clicked.connect(self.on_click_arbok)
        
        #Pikachu
        self.pikachu.setGeometry(650,250, 100, 100)
        self.pikachu.setIcon(QIcon("assets/pokemon/PIKACHU.gif"))
        self.pikachu.setIconSize(QSize(100, 100))
        self.pikachu.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.pikachu.clicked.connect(self.on_click_pikachu)
        
        #Raichu
        self.raichu.setGeometry(750,250, 100, 100)
        self.raichu.setIcon(QIcon("assets/pokemon/RAICHU.gif"))
        self.raichu.setIconSize(QSize(100, 100))
        self.raichu.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.raichu.clicked.connect(self.on_click_raichu)
        
        #Sandshrew
        self.sandshrew.setGeometry(850,250, 100, 100)
        self.sandshrew.setIcon(QIcon("assets/pokemon/SANDSHREW.gif"))
        self.sandshrew.setIconSize(QSize(100, 100))
        self.sandshrew.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.sandshrew.clicked.connect(self.on_click_sandshrew)
        
        #Sandslash
        self.sandslash.setGeometry(850,250, 100, 100)
        self.sandslash.setIcon(QIcon("assets/pokemon/SANDSLASH.gif"))
        self.sandslash.setIconSize(QSize(100, 100))
        self.sandslash.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.sandslash.clicked.connect(self.on_click_sandslash)
        
        #Nidoran♀
        self.nidoranf.setGeometry(50,350, 100, 100)
        self.nidoranf.setIcon(QIcon("assets/pokemon/NIDORANF.gif"))
        self.nidoranf.setIconSize(QSize(100, 100))
        self.nidoranf.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidoranf.clicked.connect(self.on_click_nidoranf)
        
        #Nidorana
        self.nidorina.setGeometry(150,350, 100, 100)
        self.nidorina.setIcon(QIcon("assets/pokemon/NIDORINA.gif"))
        self.nidorina.setIconSize(QSize(100, 100))
        self.nidorina.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidorina.clicked.connect(self.on_click_nidorina)
        
        #Nidoqueen
        self.nidoqueen.setGeometry(250,350, 100, 100)
        self.nidoqueen.setIcon(QIcon("assets/pokemon/NIDOQUEEN.gif"))
        self.nidoqueen.setIconSize(QSize(100, 100))
        self.nidoqueen.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidoqueen.clicked.connect(self.on_click_nidoqueen)
        
        #Nidoran♂
        self.nidoranm.setGeometry(350,350, 100, 100)
        self.nidoranm.setIcon(QIcon("assets/pokemon/NIDORANM.gif"))
        self.nidoranm.setIconSize(QSize(100, 100))
        self.nidoranm.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidoranm.clicked.connect(self.on_click_nidoranm)
        
        #Nidorino
        self.nidorino.setGeometry(450,350, 100, 100)
        self.nidorino.setIcon(QIcon("assets/pokemon/NIDORINO.gif"))
        self.nidorino.setIconSize(QSize(100, 100))
        self.nidorino.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidorino.clicked.connect(self.on_click_nidorino)
        
        #Nidoking
        self.nidoking.setGeometry(550,350, 100, 100)
        self.nidoking.setIcon(QIcon("assets/pokemon/NIDOKING.gif"))
        self.nidoking.setIconSize(QSize(100, 100))
        self.nidoking.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nidoking.clicked.connect(self.on_click_nidoking)
        
        #Clefairy
        self.clefairy.setGeometry(650,350, 100, 100)
        self.clefairy.setIcon(QIcon("assets/pokemon/CLEFAIRY.gif"))
        self.clefairy.setIconSize(QSize(100, 100))
        self.clefairy.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.clefairy.clicked.connect(self.on_click_clefairy)
        
        #Clefable
        self.clefable.setGeometry(750,350, 100, 100)
        self.clefable.setIcon(QIcon("assets/pokemon/clefable.gif"))
        self.clefable.setIconSize(QSize(100, 100))
        self.clefable.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.clefable.clicked.connect(self.on_click_clefable)
        
        #Vulpix
        self.vulpix.setGeometry(850,350, 100, 100)
        self.vulpix.setIcon(QIcon("assets/pokemon/VULPIX.gif"))
        self.vulpix.setIconSize(QSize(100, 100))
        self.vulpix.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.vulpix.clicked.connect(self.on_click_vulpix)
        
        #Page 2
        #Ninetales
        self.ninetales.setGeometry(50,50, 100, 100)
        self.ninetales.setIcon(QIcon("assets/pokemon/NINETALES.gif"))
        self.ninetales.setIconSize(QSize(100, 100))
        self.ninetales.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.ninetales.clicked.connect(self.on_click_ninetales)
        self.ninetales.setVisible(False)
        
        #Jigglypuff
        self.jigglypuff.setGeometry(150,50, 100, 100)
        self.jigglypuff.setIcon(QIcon("assets/pokemon/JIGGLYPUFF.gif"))
        self.jigglypuff.setIconSize(QSize(100, 100))
        self.jigglypuff.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.jigglypuff.clicked.connect(self.on_click_jigglypuff)
        self.jigglypuff.setVisible(False)
        
        #Wigglytuff
        self.wigglytuff.setGeometry(250,50, 100, 100)
        self.wigglytuff.setIcon(QIcon("assets/pokemon/WIGGLYTUFF.gif"))
        self.wigglytuff.setIconSize(QSize(100, 100))
        self.wigglytuff.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.wigglytuff.clicked.connect(self.on_click_wigglytuff)
        self.wigglytuff.setVisible(False)
        
        #Zubat
        self.zubat.setGeometry(350,50, 100, 100)
        self.zubat.setIcon(QIcon("assets/pokemon/ZUBAT.gif"))
        self.zubat.setIconSize(QSize(100, 100))
        self.zubat.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.zubat.clicked.connect(self.on_click_zubat)
        self.zubat.setVisible(False)
        
        #Golbat
        self.golbat.setGeometry(450,50, 100, 100)
        self.golbat.setIcon(QIcon("assets/pokemon/GOLBAT.gif"))
        self.golbat.setIconSize(QSize(100, 100))
        self.golbat.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.golbat.clicked.connect(self.on_click_golbat)
        self.golbat.setVisible(False)
        
        #Oddish
        self.oddish.setGeometry(550,50, 100, 100)
        self.oddish.setIcon(QIcon("assets/pokemon/ODDISH.gif"))
        self.oddish.setIconSize(QSize(100, 100))
        self.oddish.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.oddish.clicked.connect(self.on_click_oddish)
        self.oddish.setVisible(False)
        
        #Vileplume
        self.vileplume.setGeometry(650,50, 100, 100)
        self.vileplume.setIcon(QIcon("assets/pokemon/VILEPLUME.gif"))
        self.vileplume.setIconSize(QSize(100, 100))
        self.vileplume.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.vileplume.clicked.connect(self.on_click_vileplume)
        self.vileplume.setVisible(False)
        
        #Paras
        self.paras.setGeometry(750,50, 100, 100)
        self.paras.setIcon(QIcon("assets/pokemon/PARAS.gif"))
        self.paras.setIconSize(QSize(100, 100))
        self.paras.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.paras.clicked.connect(self.on_click_paras)
        self.paras.setVisible(False)
        
        #Parasect
        self.parasect.setGeometry(850,50, 100, 100)
        self.parasect.setIcon(QIcon("assets/pokemon/PARASECT.gif"))
        self.parasect.setIconSize(QSize(100, 100))
        self.parasect.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.parasect.clicked.connect(self.on_click_parasect)
        self.parasect.setVisible(False)

        #Venonat
        self.venonat.setGeometry(50,150, 100, 100)
        self.venonat.setIcon(QIcon("assets/pokemon/VENONAT.gif"))
        self.venonat.setIconSize(QSize(100, 100))
        self.venonat.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.venonat.clicked.connect(self.on_click_venonat)
        self.venonat.setVisible(False)

        #Venomoth
        self.venomoth.setGeometry(150,150, 100, 100)
        self.venomoth.setIcon(QIcon("assets/pokemon/VENOMOTH.gif"))
        self.venomoth.setIconSize(QSize(100, 100))
        self.venomoth.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.venomoth.clicked.connect(self.on_click_venomoth)
        self.venomoth.setVisible(False)

        #Diglett
        self.diglett.setGeometry(250,150, 100, 100)
        self.diglett.setIcon(QIcon("assets/pokemon/DIGLETT.gif"))
        self.diglett.setIconSize(QSize(100, 100))
        self.diglett.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.diglett.clicked.connect(self.on_click_diglett)
        self.diglett.setVisible(False)

        #Dugtrio
        self.dugtrio.setGeometry(350,150, 100, 100)
        self.dugtrio.setIcon(QIcon("assets/pokemon/DUGTRIO.gif"))
        self.dugtrio.setIconSize(QSize(100, 100))
        self.dugtrio.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dugtrio.clicked.connect(self.on_click_dugtrio)
        self.dugtrio.setVisible(False)

        #Meowth
        self.meowth.setGeometry(450,150, 100, 100)
        self.meowth.setIcon(QIcon("assets/pokemon/MEOWTH.gif"))
        self.meowth.setIconSize(QSize(100, 100))
        self.meowth.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.meowth.clicked.connect(self.on_click_meowth)
        self.meowth.setVisible(False)

        #Persian
        self.persian.setGeometry(550,150, 100, 100)
        self.persian.setIcon(QIcon("assets/pokemon/PERSIAN.gif"))
        self.persian.setIconSize(QSize(100, 100))
        self.persian.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.persian.clicked.connect(self.on_click_persian)
        self.persian.setVisible(False)

        #Psyduck
        self.psyduck.setGeometry(650,150, 100, 100)
        self.psyduck.setIcon(QIcon("assets/pokemon/PSYDUCK.gif"))
        self.psyduck.setIconSize(QSize(100, 100))
        self.psyduck.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.psyduck.clicked.connect(self.on_click_psyduck)
        self.psyduck.setVisible(False)

        #Golduck
        self.golduck.setGeometry(750,150, 100, 100)
        self.golduck.setIcon(QIcon("assets/pokemon/GOLDUCK.gif"))
        self.golduck.setIconSize(QSize(100, 100))
        self.golduck.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.golduck.clicked.connect(self.on_click_golduck)
        self.golduck.setVisible(False)

        #Mankey
        self.mankey.setGeometry(850,150, 100, 100)
        self.mankey.setIcon(QIcon("assets/pokemon/MANKEY.gif"))
        self.mankey.setIconSize(QSize(100, 100))
        self.mankey.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.mankey.clicked.connect(self.on_click_mankey)
        self.mankey.setVisible(False)

        #Primeape
        self.primeape.setGeometry(50,250, 100, 100)
        self.primeape.setIcon(QIcon("assets/pokemon/PRIMEAPE.gif"))
        self.primeape.setIconSize(QSize(100, 100))
        self.primeape.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.primeape.clicked.connect(self.on_click_primeape)
        self.primeape.setVisible(False)

        #Growlithe
        self.growlithe.setGeometry(150,250, 100, 100)
        self.growlithe.setIcon(QIcon("assets/pokemon/GROWLITHE.gif"))
        self.growlithe.setIconSize(QSize(100, 100))
        self.growlithe.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.growlithe.clicked.connect(self.on_click_growlithe)
        self.growlithe.setVisible(False)

        #Arcanine
        self.arcanine.setGeometry(250,250, 100, 100)
        self.arcanine.setIcon(QIcon("assets/pokemon/ARCANINE.gif"))
        self.arcanine.setIconSize(QSize(100, 100))
        self.arcanine.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.arcanine.clicked.connect(self.on_click_arcanine)
        self.arcanine.setVisible(False)

        #Poliwag
        self.poliwag.setGeometry(350,250, 100, 100)
        self.poliwag.setIcon(QIcon("assets/pokemon/POLIWAG.gif"))
        self.poliwag.setIconSize(QSize(100, 100))
        self.poliwag.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.poliwag.clicked.connect(self.on_click_poliwag)
        self.poliwag.setVisible(False)

        #Poliwhirl
        self.poliwhirl.setGeometry(450,250, 100, 100)
        self.poliwhirl.setIcon(QIcon("assets/pokemon/POLIWHIRL.gif"))
        self.poliwhirl.setIconSize(QSize(100, 100))
        self.poliwhirl.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.poliwhirl.clicked.connect(self.on_click_poliwhirl)
        self.poliwhirl.setVisible(False)

        #Poliwrath
        self.poliwrath.setGeometry(550,250, 100, 100)
        self.poliwrath.setIcon(QIcon("assets/pokemon/POLIWRATH.gif"))
        self.poliwrath.setIconSize(QSize(100, 100))
        self.poliwrath.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.poliwrath.clicked.connect(self.on_click_poliwrath)
        self.poliwrath.setVisible(False)

        #Abra
        self.abra.setGeometry(650,250, 100, 100)
        self.abra.setIcon(QIcon("assets/pokemon/ABRA.gif"))
        self.abra.setIconSize(QSize(100, 100))
        self.abra.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.abra.clicked.connect(self.on_click_abra)
        self.abra.setVisible(False)

        #Kadabra
        self.kadabra.setGeometry(750,250, 100, 100)
        self.kadabra.setIcon(QIcon("assets/pokemon/KADABRA.gif"))
        self.kadabra.setIconSize(QSize(100, 100))
        self.kadabra.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kadabra.clicked.connect(self.on_click_kadabra)
        self.kadabra.setVisible(False)

        #Alakazam
        self.alakazam.setGeometry(850,250, 100, 100)
        self.alakazam.setIcon(QIcon("assets/pokemon/ALAKAZAM.gif"))
        self.alakazam.setIconSize(QSize(100, 100))
        self.alakazam.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.alakazam.clicked.connect(self.on_click_alakazam)
        self.alakazam.setVisible(False)

        #Machop
        self.machop.setGeometry(50,350, 100, 100)
        self.machop.setIcon(QIcon("assets/pokemon/MACHOP.gif"))
        self.machop.setIconSize(QSize(100, 100))
        self.machop.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.machop.clicked.connect(self.on_click_machop)
        self.machop.setVisible(False)

        #Machoke
        self.machoke.setGeometry(150,350, 100, 100)
        self.machoke.setIcon(QIcon("assets/pokemon/MACHOKE.gif"))
        self.machoke.setIconSize(QSize(100, 100))
        self.machoke.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.machoke.clicked.connect(self.on_click_machoke)
        self.machoke.setVisible(False)

        #Machamp
        self.machamp.setGeometry(250,350, 100, 100)
        self.machamp.setIcon(QIcon("assets/pokemon/MACHAMP.gif"))
        self.machamp.setIconSize(QSize(100, 100))
        self.machamp.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.machamp.clicked.connect(self.on_click_machamp)
        self.machamp.setVisible(False)

        #Bellsprout
        self.bellsprout.setGeometry(350,350, 100, 100)
        self.bellsprout.setIcon(QIcon("assets/pokemon/BELLSPROUT.gif"))
        self.bellsprout.setIconSize(QSize(100, 100))
        self.bellsprout.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.bellsprout.clicked.connect(self.on_click_bellsprout)
        self.bellsprout.setVisible(False)

        #Weepinbell
        self.weepinbell.setGeometry(450,350, 100, 100)
        self.weepinbell.setIcon(QIcon("assets/pokemon/WEEPINBELL.gif"))
        self.weepinbell.setIconSize(QSize(100, 100))
        self.weepinbell.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.weepinbell.clicked.connect(self.on_click_weepinbell)
        self.weepinbell.setVisible(False)

        #Victreebel
        self.victreebel.setGeometry(550,350, 100, 100)
        self.victreebel.setIcon(QIcon("assets/pokemon/VICTREEBEL.gif"))
        self.victreebel.setIconSize(QSize(100, 100))
        self.victreebel.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.victreebel.clicked.connect(self.on_click_victreebel)
        self.victreebel.setVisible(False)

        #Tentacool
        self.tentacool.setGeometry(650,350, 100, 100)
        self.tentacool.setIcon(QIcon("assets/pokemon/TENTACOOL.gif"))
        self.tentacool.setIconSize(QSize(100, 100))
        self.tentacool.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.tentacool.clicked.connect(self.on_click_tentacool)
        self.tentacool.setVisible(False)

        #Tentacruel
        self.tentacruel.setGeometry(750,350, 100, 100)
        self.tentacruel.setIcon(QIcon("assets/pokemon/TENTACRUEL.gif"))
        self.tentacruel.setIconSize(QSize(100, 100))
        self.tentacruel.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.tentacruel.clicked.connect(self.on_click_tentacruel)
        self.tentacruel.setVisible(False)

        #Geodude
        self.geodude.setGeometry(850,350, 100, 100)
        self.geodude.setIcon(QIcon("assets/pokemon/GEODUDE.gif"))
        self.geodude.setIconSize(QSize(100, 100))
        self.geodude.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.geodude.clicked.connect(self.on_click_geodude)
        self.geodude.setVisible(False)

        #Graveler
        self.graveler.setGeometry(50,50, 100, 100)
        self.graveler.setIcon(QIcon("assets/pokemon/GRAVELER.gif"))
        self.graveler.setIconSize(QSize(100, 100))
        self.graveler.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.graveler.clicked.connect(self.on_click_graveler)
        self.graveler.setVisible(False)

        #Golem
        self.golem.setGeometry(150,50, 100, 100)
        self.golem.setIcon(QIcon("assets/pokemon/GOLEM.gif"))
        self.golem.setIconSize(QSize(100, 100))
        self.golem.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.golem.clicked.connect(self.on_click_golem)
        self.golem.setVisible(False)

        #Ponyta
        self.ponyta.setGeometry(250,50, 100, 100)
        self.ponyta.setIcon(QIcon("assets/pokemon/PONYTA.gif"))
        self.ponyta.setIconSize(QSize(100, 100))
        self.ponyta.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.ponyta.clicked.connect(self.on_click_ponyta)
        self.ponyta.setVisible(False)

        #Rapidash
        self.rapidash.setGeometry(350,50, 100, 100)
        self.rapidash.setIcon(QIcon("assets/pokemon/RAPIDASH.gif"))
        self.rapidash.setIconSize(QSize(100, 100))
        self.rapidash.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.rapidash.clicked.connect(self.on_click_rapidash)
        self.rapidash.setVisible(False)

        #Slowpoke
        self.slowpoke.setGeometry(450,50, 100, 100)
        self.slowpoke.setIcon(QIcon("assets/pokemon/SLOWPOKE.gif"))
        self.slowpoke.setIconSize(QSize(100, 100))
        self.slowpoke.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.slowpoke.clicked.connect(self.on_click_slowpoke)
        self.slowpoke.setVisible(False)

        #Slowbro
        self.slowbro.setGeometry(550,50, 100, 100)
        self.slowbro.setIcon(QIcon("assets/pokemon/SLOWBRO.gif"))
        self.slowbro.setIconSize(QSize(100, 100))
        self.slowbro.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.slowbro.clicked.connect(self.on_click_slowbro)
        self.slowbro.setVisible(False)

        #Magnemite
        self.magnemite.setGeometry(650,50, 100, 100)
        self.magnemite.setIcon(QIcon("assets/pokemon/MAGNEMITE.gif"))
        self.magnemite.setIconSize(QSize(100, 100))
        self.magnemite.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.magnemite.clicked.connect(self.on_click_magnemite)
        self.magnemite.setVisible(False)

        #Magneton
        self.magneton.setGeometry(750,50, 100, 100)
        self.magneton.setIcon(QIcon("assets/pokemon/MAGNETON.gif"))
        self.magneton.setIconSize(QSize(100, 100))
        self.magneton.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.magneton.clicked.connect(self.on_click_magneton)
        self.magneton.setVisible(False)

        #Farfetchd
        self.farfetchd.setGeometry(850,50, 100, 100)
        self.farfetchd.setIcon(QIcon("assets/pokemon/FARFETCHD.gif"))
        self.farfetchd.setIconSize(QSize(100, 100))
        self.farfetchd.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.farfetchd.clicked.connect(self.on_click_farfetchd)
        self.farfetchd.setVisible(False)

        #Doduo
        self.doduo.setGeometry(50,150, 100, 100)
        self.doduo.setIcon(QIcon("assets/pokemon/DODUO.gif"))
        self.doduo.setIconSize(QSize(100, 100))
        self.doduo.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.doduo.clicked.connect(self.on_click_doduo)
        self.doduo.setVisible(False)

        #Dodrio
        self.dodrio.setGeometry(150,150, 100, 100)
        self.dodrio.setIcon(QIcon("assets/pokemon/DODRIO.gif"))
        self.dodrio.setIconSize(QSize(100, 100))
        self.dodrio.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dodrio.clicked.connect(self.on_click_dodrio)
        self.dodrio.setVisible(False)

        #Seel
        self.seel.setGeometry(250,150, 100, 100)
        self.seel.setIcon(QIcon("assets/pokemon/SEEL.gif"))
        self.seel.setIconSize(QSize(100, 100))
        self.seel.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.seel.clicked.connect(self.on_click_seel)
        self.seel.setVisible(False)

        #Dewgong
        self.dewgong.setGeometry(350,150, 100, 100)
        self.dewgong.setIcon(QIcon("assets/pokemon/DEWGONG.gif"))
        self.dewgong.setIconSize(QSize(100, 100))
        self.dewgong.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dewgong.clicked.connect(self.on_click_dewgong)
        self.dewgong.setVisible(False)

        #Grimer
        self.grimer.setGeometry(450,150, 100, 100)
        self.grimer.setIcon(QIcon("assets/pokemon/GRIMER.gif"))
        self.grimer.setIconSize(QSize(100, 100))
        self.grimer.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.grimer.clicked.connect(self.on_click_grimer)
        self.grimer.setVisible(False)

        #Muk
        self.muk.setGeometry(550,150, 100, 100)
        self.muk.setIcon(QIcon("assets/pokemon/MUK.gif"))
        self.muk.setIconSize(QSize(100, 100))
        self.muk.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.muk.clicked.connect(self.on_click_muk)
        self.muk.setVisible(False)

        #Shellder
        self.shellder.setGeometry(650,150, 100, 100)
        self.shellder.setIcon(QIcon("assets/pokemon/SHELLDER.gif"))
        self.shellder.setIconSize(QSize(100, 100))
        self.shellder.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.shellder.clicked.connect(self.on_click_shellder)
        self.shellder.setVisible(False)

        #Cloyster
        self.cloyster.setGeometry(750,150, 100, 100)
        self.cloyster.setIcon(QIcon("assets/pokemon/CLOYSTER.gif"))
        self.cloyster.setIconSize(QSize(100, 100))
        self.cloyster.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.cloyster.clicked.connect(self.on_click_cloyster)
        self.cloyster.setVisible(False)

        #Gastly
        self.gastly.setGeometry(850,150, 100, 100)
        self.gastly.setIcon(QIcon("assets/pokemon/GASTLY.gif"))
        self.gastly.setIconSize(QSize(100, 100))
        self.gastly.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.gastly.clicked.connect(self.on_click_gastly)
        self.gastly.setVisible(False)

        #Haunter
        self.haunter.setGeometry(50,250, 100, 100)
        self.haunter.setIcon(QIcon("assets/pokemon/HAUNTER.gif"))
        self.haunter.setIconSize(QSize(100, 100))
        self.haunter.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.haunter.clicked.connect(self.on_click_haunter)
        self.haunter.setVisible(False)

        #Gengar
        self.gengar.setGeometry(150,250, 100, 100)
        self.gengar.setIcon(QIcon("assets/pokemon/GENGAR.gif"))
        self.gengar.setIconSize(QSize(100, 100))
        self.gengar.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.gengar.clicked.connect(self.on_click_gengar)
        self.gengar.setVisible(False)

        #Onix
        self.onix.setGeometry(250,250, 100, 100)
        self.onix.setIcon(QIcon("assets/pokemon/ONIX.gif"))
        self.onix.setIconSize(QSize(100, 100))
        self.onix.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.onix.clicked.connect(self.on_click_onix)
        self.onix.setVisible(False)

        #Drowzee
        self.drowzee.setGeometry(350,250, 100, 100)
        self.drowzee.setIcon(QIcon("assets/pokemon/DROWZEE.gif"))
        self.drowzee.setIconSize(QSize(100, 100))
        self.drowzee.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.drowzee.clicked.connect(self.on_click_drowzee)
        self.drowzee.setVisible(False)

        #Hypno
        self.hypno.setGeometry(450,250, 100, 100)
        self.hypno.setIcon(QIcon("assets/pokemon/HYPNO.gif"))
        self.hypno.setIconSize(QSize(100, 100))
        self.hypno.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.hypno.clicked.connect(self.on_click_hypno)
        self.hypno.setVisible(False)

        #Krabby
        self.krabby.setGeometry(550,250, 100, 100)
        self.krabby.setIcon(QIcon("assets/pokemon/KRABBY.gif"))
        self.krabby.setIconSize(QSize(100, 100))
        self.krabby.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.krabby.clicked.connect(self.on_click_krabby)
        self.krabby.setVisible(False)

        #Kingler
        self.kingler.setGeometry(650,250, 100, 100)
        self.kingler.setIcon(QIcon("assets/pokemon/KINGLER.gif"))
        self.kingler.setIconSize(QSize(100, 100))
        self.kingler.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kingler.clicked.connect(self.on_click_kingler)
        self.kingler.setVisible(False)

        #Voltorb
        self.voltorb.setGeometry(750,250, 100, 100)
        self.voltorb.setIcon(QIcon("assets/pokemon/VOLTORB.gif"))
        self.voltorb.setIconSize(QSize(100, 100))
        self.voltorb.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.voltorb.clicked.connect(self.on_click_voltorb)
        self.voltorb.setVisible(False)

        #Electrode
        self.electrode.setGeometry(850,250, 100, 100)
        self.electrode.setIcon(QIcon("assets/pokemon/ELECTRODE.gif"))
        self.electrode.setIconSize(QSize(100, 100))
        self.electrode.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.electrode.clicked.connect(self.on_click_electrode)
        self.electrode.setVisible(False)

        #Exeggcute
        self.exeggcute.setGeometry(50,350, 100, 100)
        self.exeggcute.setIcon(QIcon("assets/pokemon/EXEGGCUTE.gif"))
        self.exeggcute.setIconSize(QSize(100, 100))
        self.exeggcute.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.exeggcute.clicked.connect(self.on_click_exeggcute)
        self.exeggcute.setVisible(False)

        #Exeggutor
        self.exeggutor.setGeometry(150,350, 100, 100)
        self.exeggutor.setIcon(QIcon("assets/pokemon/EXEGGUTOR.gif"))
        self.exeggutor.setIconSize(QSize(100, 100))
        self.exeggutor.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.exeggutor.clicked.connect(self.on_click_exeggutor)
        self.exeggutor.setVisible(False)

        #Cubone
        self.cubone.setGeometry(250,350, 100, 100)
        self.cubone.setIcon(QIcon("assets/pokemon/CUBONE.gif"))
        self.cubone.setIconSize(QSize(100, 100))
        self.cubone.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.cubone.clicked.connect(self.on_click_cubone)
        self.cubone.setVisible(False)

        #Marowak
        self.marowak.setGeometry(350,350, 100, 100)
        self.marowak.setIcon(QIcon("assets/pokemon/MAROWAK.gif"))
        self.marowak.setIconSize(QSize(100, 100))
        self.marowak.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.marowak.clicked.connect(self.on_click_marowak)
        self.marowak.setVisible(False)

        #Hitmonlee
        self.hitmonlee.setGeometry(450,350, 100, 100)
        self.hitmonlee.setIcon(QIcon("assets/pokemon/HITMONLEE.gif"))
        self.hitmonlee.setIconSize(QSize(100, 100))
        self.hitmonlee.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.hitmonlee.clicked.connect(self.on_click_hitmonlee)
        self.hitmonlee.setVisible(False)

        #Hitmonchan
        self.hitmonchan.setGeometry(550,350, 100, 100)
        self.hitmonchan.setIcon(QIcon("assets/pokemon/HITMONCHAN.gif"))
        self.hitmonchan.setIconSize(QSize(100, 100))
        self.hitmonchan.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.hitmonchan.clicked.connect(self.on_click_hitmonchan)
        self.hitmonchan.setVisible(False)

        #Lickitung
        self.lickitung.setGeometry(650,350, 100, 100)
        self.lickitung.setIcon(QIcon("assets/pokemon/LICKITUNG.gif"))
        self.lickitung.setIconSize(QSize(100, 100))
        self.lickitung.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.lickitung.clicked.connect(self.on_click_lickitung)
        self.lickitung.setVisible(False)

        #Koffing
        self.koffing.setGeometry(750,350, 100, 100)
        self.koffing.setIcon(QIcon("assets/pokemon/KOFFING.gif"))
        self.koffing.setIconSize(QSize(100, 100))
        self.koffing.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.koffing.clicked.connect(self.on_click_koffing)
        self.koffing.setVisible(False)

        #Weezing
        self.weezing.setGeometry(850,350, 100, 100)
        self.weezing.setIcon(QIcon("assets/pokemon/WEEZING.gif"))
        self.weezing.setIconSize(QSize(100, 100))
        self.weezing.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.weezing.clicked.connect(self.on_click_weezing)
        self.weezing.setVisible(False)
        
        #Rhyhorn
        self.rhyhorn.setGeometry(50,50, 100, 100)
        self.rhyhorn.setIcon(QIcon("assets/pokemon/RHYHORN.gif"))
        self.rhyhorn.setIconSize(QSize(100, 100))
        self.rhyhorn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.rhyhorn.clicked.connect(self.on_click_rhyhorn)
        self.rhyhorn.setVisible(False)
        
        #Rhydon
        self.rhydon.setGeometry(150,50, 100, 100)
        self.rhydon.setIcon(QIcon("assets/pokemon/RHYDON.gif"))
        self.rhydon.setIconSize(QSize(100, 100))
        self.rhydon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.rhydon.clicked.connect(self.on_click_rhydon)
        self.rhydon.setVisible(False)
        
        #Chansey
        self.chansey.setGeometry(250,50, 100, 100)
        self.chansey.setIcon(QIcon("assets/pokemon/CHANSEY.gif"))
        self.chansey.setIconSize(QSize(100, 100))
        self.chansey.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.chansey.clicked.connect(self.on_click_chansey)
        self.chansey.setVisible(False)
        
        #Tangela
        self.tangela.setGeometry(350,50, 100, 100)
        self.tangela.setIcon(QIcon("assets/pokemon/TANGELA.gif"))
        self.tangela.setIconSize(QSize(100, 100))
        self.tangela.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.tangela.clicked.connect(self.on_click_tangela)
        self.tangela.setVisible(False)
        
        #Kangaskhan
        self.kangaskhan.setGeometry(450,50, 100, 100)
        self.kangaskhan.setIcon(QIcon("assets/pokemon/KANGASKHAN.gif"))
        self.kangaskhan.setIconSize(QSize(100, 100))
        self.kangaskhan.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kangaskhan.clicked.connect(self.on_click_kangaskhan)
        self.kangaskhan.setVisible(False)
        
        #Horsea
        self.horsea.setGeometry(550,50, 100, 100)
        self.horsea.setIcon(QIcon("assets/pokemon/HORSEA.gif"))
        self.horsea.setIconSize(QSize(100, 100))
        self.horsea.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.horsea.clicked.connect(self.on_click_horsea)
        self.horsea.setVisible(False)
        
        #Seadra
        self.seadra.setGeometry(650,50, 100, 100)
        self.seadra.setIcon(QIcon("assets/pokemon/SEADRA.gif"))
        self.seadra.setIconSize(QSize(100, 100))
        self.seadra.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.seadra.clicked.connect(self.on_click_seadra)
        self.seadra.setVisible(False)
        
        #Goldeen
        self.goldeen.setGeometry(750,50, 100, 100)
        self.goldeen.setIcon(QIcon("assets/pokemon/GOLDEEN.gif"))
        self.goldeen.setIconSize(QSize(100, 100))
        self.goldeen.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.goldeen.clicked.connect(self.on_click_goldeen)
        self.goldeen.setVisible(False)
        
        #Seaking
        self.seaking.setGeometry(850,50, 100, 100)
        self.seaking.setIcon(QIcon("assets/pokemon/SEAKING.gif"))
        self.seaking.setIconSize(QSize(100, 100))
        self.seaking.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.seaking.clicked.connect(self.on_click_seaking)
        self.seaking.setVisible(False)
        
        #Staryu
        self.staryu.setGeometry(50,150, 100, 100)
        self.staryu.setIcon(QIcon("assets/pokemon/STARYU.gif"))
        self.staryu.setIconSize(QSize(100, 100))
        self.staryu.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.staryu.clicked.connect(self.on_click_staryu)
        self.staryu.setVisible(False)
        
        #Starmie
        self.starmie.setGeometry(150,150, 100, 100)
        self.starmie.setIcon(QIcon("assets/pokemon/STARMIE.gif"))
        self.starmie.setIconSize(QSize(100, 100))
        self.starmie.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.starmie.clicked.connect(self.on_click_starmie)
        self.starmie.setVisible(False)
        
        #Mr. Mme
        self.mrmime.setGeometry(250,150, 100, 100)
        self.mrmime.setIcon(QIcon("assets/pokemon/MRMIME.gif"))
        self.mrmime.setIconSize(QSize(100, 100))
        self.mrmime.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.mrmime.clicked.connect(self.on_click_mrmime)
        self.mrmime.setVisible(False)
        
        #Scyther
        self.scyther.setGeometry(350,150, 100, 100)
        self.scyther.setIcon(QIcon("assets/pokemon/SCYTHER.gif"))
        self.scyther.setIconSize(QSize(100, 100))
        self.scyther.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.scyther.clicked.connect(self.on_click_scyther)
        self.scyther.setVisible(False)
        
        #Jynx
        self.jynx.setGeometry(450,150, 100, 100)
        self.jynx.setIcon(QIcon("assets/pokemon/JYNX.gif"))
        self.jynx.setIconSize(QSize(100, 100))
        self.jynx.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.jynx.clicked.connect(self.on_click_jynx)
        self.jynx.setVisible(False)
        
        #Electabuzz
        self.electabuzz.setGeometry(550,150, 100, 100)
        self.electabuzz.setIcon(QIcon("assets/pokemon/ELECTABUZZ.gif"))
        self.electabuzz.setIconSize(QSize(100, 100))
        self.electabuzz.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.electabuzz.clicked.connect(self.on_click_electabuzz)
        self.electabuzz.setVisible(False)
        
        #Magmar
        self.magmar.setGeometry(650,150, 100, 100)
        self.magmar.setIcon(QIcon("assets/pokemon/MAGMAR.gif"))
        self.magmar.setIconSize(QSize(100, 100))
        self.magmar.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.magmar.clicked.connect(self.on_click_magmar)
        self.magmar.setVisible(False)
        
        #Pinsir
        self.pinsir.setGeometry(750,150, 100, 100)
        self.pinsir.setIcon(QIcon("assets/pokemon/PINSIR.gif"))
        self.pinsir.setIconSize(QSize(100, 100))
        self.pinsir.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.pinsir.clicked.connect(self.on_click_pinsir)
        self.pinsir.setVisible(False)
        
        #Tauros
        self.tauros.setGeometry(850,150, 100, 100)
        self.tauros.setIcon(QIcon("assets/pokemon/TAUROS.gif"))
        self.tauros.setIconSize(QSize(100, 100))
        self.tauros.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.tauros.clicked.connect(self.on_click_tauros)
        self.tauros.setVisible(False)
        
        #Magikarp
        self.magikarp.setGeometry(50,250, 100, 100)
        self.magikarp.setIcon(QIcon("assets/pokemon/MAGIKARP.gif"))
        self.magikarp.setIconSize(QSize(100, 100))
        self.magikarp.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.magikarp.clicked.connect(self.on_click_magikarp)
        self.magikarp.setVisible(False)
        
        #Gyarados
        self.gyarados.setGeometry(150,250, 100, 100)
        self.gyarados.setIcon(QIcon("assets/pokemon/GYARADOS.gif"))
        self.gyarados.setIconSize(QSize(100, 100))
        self.gyarados.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.gyarados.clicked.connect(self.on_click_gyarados)
        self.gyarados.setVisible(False)
        
        #Lapras
        self.lapras.setGeometry(250,250, 100, 100)
        self.lapras.setIcon(QIcon("assets/pokemon/LAPRAS.gif"))
        self.lapras.setIconSize(QSize(100, 100))
        self.lapras.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.lapras.clicked.connect(self.on_click_lapras)
        self.lapras.setVisible(False)
        
        #Ditto
        self.ditto.setGeometry(350,250, 100, 100)
        self.ditto.setIcon(QIcon("assets/pokemon/DITTO.gif"))
        self.ditto.setIconSize(QSize(100, 100))
        self.ditto.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.ditto.clicked.connect(self.on_click_ditto)
        self.ditto.setVisible(False)
        
        #Eevee
        self.eevee.setGeometry(450,250, 100, 100)
        self.eevee.setIcon(QIcon("assets/pokemon/EEVEE.gif"))
        self.eevee.setIconSize(QSize(100, 100))
        self.eevee.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.eevee.clicked.connect(self.on_click_eevee)
        self.eevee.setVisible(False)
        
        #Vaporeon
        self.vaporeon.setGeometry(550,250, 100, 100)
        self.vaporeon.setIcon(QIcon("assets/pokemon/VAPOREON.gif"))
        self.vaporeon.setIconSize(QSize(100, 100))
        self.vaporeon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.vaporeon.clicked.connect(self.on_click_vaporeon)
        self.vaporeon.setVisible(False)
        
        #Jolteon
        self.jolteon.setGeometry(650,250, 100, 100)
        self.jolteon.setIcon(QIcon("assets/pokemon/JOLTEON.gif"))
        self.jolteon.setIconSize(QSize(100, 100))
        self.jolteon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.jolteon.clicked.connect(self.on_click_jolteon)
        self.jolteon.setVisible(False)
        
        #Flareon
        self.flareon.setGeometry(750,250, 100, 100)
        self.flareon.setIcon(QIcon("assets/pokemon/FLAREON.gif"))
        self.flareon.setIconSize(QSize(100, 100))
        self.flareon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.flareon.clicked.connect(self.on_click_flareon)
        self.flareon.setVisible(False)
        
        #Porygon
        self.porygon.setGeometry(850,250, 100, 100)
        self.porygon.setIcon(QIcon("assets/pokemon/PORYGON.gif"))
        self.porygon.setIconSize(QSize(100, 100))
        self.porygon.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.porygon.clicked.connect(self.on_click_porygon)
        self.porygon.setVisible(False)
        
        #Omanyte
        self.omanyte.setGeometry(50,350, 100, 100)
        self.omanyte.setIcon(QIcon("assets/pokemon/OMANYTE.gif"))
        self.omanyte.setIconSize(QSize(100, 100))
        self.omanyte.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.omanyte.clicked.connect(self.on_click_omanyte)
        self.omanyte.setVisible(False)
        
        #Omastar
        self.omastar.setGeometry(150,350, 100, 100)
        self.omastar.setIcon(QIcon("assets/pokemon/OMASTAR.gif"))
        self.omastar.setIconSize(QSize(100, 100))
        self.omastar.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.omastar.clicked.connect(self.on_click_omastar)
        self.omastar.setVisible(False)
        
        #Kabuto
        self.kabuto.setGeometry(250,350, 100, 100)
        self.kabuto.setIcon(QIcon("assets/pokemon/KABUTO.gif"))
        self.kabuto.setIconSize(QSize(100, 100))
        self.kabuto.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kabuto.clicked.connect(self.on_click_kabuto)
        self.kabuto.setVisible(False)
        
        #Kabutops
        self.kabutops.setGeometry(350,350, 100, 100)
        self.kabutops.setIcon(QIcon("assets/pokemon/KABUTOPS.gif"))
        self.kabutops.setIconSize(QSize(100, 100))
        self.kabutops.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.kabutops.clicked.connect(self.on_click_kabutops)
        self.kabutops.setVisible(False)
        
        #Aerodactyl
        self.aerodactyl.setGeometry(450,350, 100, 100)
        self.aerodactyl.setIcon(QIcon("assets/pokemon/AERODACTYL.gif"))
        self.aerodactyl.setIconSize(QSize(100, 100))
        self.aerodactyl.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.aerodactyl.clicked.connect(self.on_click_aerodactyl)
        self.aerodactyl.setVisible(False)
        
        #Snorlax
        self.snorlax.setGeometry(550,350, 100, 100)
        self.snorlax.setIcon(QIcon("assets/pokemon/SNORLAX.gif"))
        self.snorlax.setIconSize(QSize(100, 100))
        self.snorlax.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.snorlax.clicked.connect(self.on_click_snorlax)
        self.snorlax.setVisible(False)
        
        #Articuno
        self.articuno.setGeometry(650,350, 100, 100)
        self.articuno.setIcon(QIcon("assets/pokemon/ARTICUNO.gif"))
        self.articuno.setIconSize(QSize(100, 100))
        self.articuno.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.articuno.clicked.connect(self.on_click_articuno)
        self.articuno.setVisible(False)
        
        #Zapdos
        self.zapdos.setGeometry(750,350, 100, 100)
        self.zapdos.setIcon(QIcon("assets/pokemon/ZAPDOS.gif"))
        self.zapdos.setIconSize(QSize(100, 100))
        self.zapdos.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.zapdos.clicked.connect(self.on_click_zapdos)
        self.zapdos.setVisible(False)
        
        #Moltres
        self.moltres.setGeometry(850,350, 100, 100)
        self.moltres.setIcon(QIcon("assets/pokemon/MOLTRES.gif"))
        self.moltres.setIconSize(QSize(100, 100))
        self.moltres.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.moltres.clicked.connect(self.on_click_moltres)
        self.moltres.setVisible(False)
        
        #Dratini
        self.dratini.setGeometry(50,50, 100, 100)
        self.dratini.setIcon(QIcon("assets/pokemon/DRATINI.gif"))
        self.dratini.setIconSize(QSize(100, 100))
        self.dratini.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dratini.clicked.connect(self.on_click_dratini)
        self.dratini.setVisible(False)
        
        #Dragonair
        self.dragonair.setGeometry(150,50, 100, 100)
        self.dragonair.setIcon(QIcon("assets/pokemon/DRAGONAIR.gif"))
        self.dragonair.setIconSize(QSize(100, 100))
        self.dragonair.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dragonair.clicked.connect(self.on_click_dragonair)
        self.dragonair.setVisible(False)
        
        #Dragonite
        self.dragonite.setGeometry(250,50, 100, 100)
        self.dragonite.setIcon(QIcon("assets/pokemon/DRAGONITE.gif"))
        self.dragonite.setIconSize(QSize(100, 100))
        self.dragonite.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.dragonite.clicked.connect(self.on_click_dragonite)
        self.dragonite.setVisible(False)
        
        #Mewtwo
        self.mewtwo.setGeometry(350,50, 100, 100)
        self.mewtwo.setIcon(QIcon("assets/pokemon/MEWTWO.gif"))
        self.mewtwo.setIconSize(QSize(100, 100))
        self.mewtwo.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.mewtwo.clicked.connect(self.on_click_mewtwo)
        self.mewtwo.setVisible(False)
        
        #Mew
        self.mew.setGeometry(450,50, 100, 100)
        self.mew.setIcon(QIcon("assets/pokemon/MEW.gif"))
        self.mew.setIconSize(QSize(100, 100))
        self.mew.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.mew.clicked.connect(self.on_click_mew)
        self.mew.setVisible(False)


        
        #self.your_team_message.setStyleSheet("font-size: 30px; color: white;")


        #Pokemon Battle Message
        self.menu_message.setGeometry(350, 10, 700, 50)
        self.menu_message.setStyleSheet("font-size: 30px; color: white;")
        self.your_team_message.setGeometry(80, 545, 400, 50)
        self.your_team_message.setStyleSheet("font-size: 30px; color: white;")
        self.team_message.setGeometry(300, 545, 700, 50)
        self.team_message.setStyleSheet("font-size: 30px; color: white;")

        #Pokemon Team slots
        self.P1_pkmn1.setGeometry(80,590, 100, 100)
        self.P1_pkmn1.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn1.setIconSize(QSize(100, 100))
        self.P1_pkmn1.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn1.clicked.connect(self.on_click_P1_pkmn1)

        self.P1_pkmn2.setGeometry(200,590, 100, 100)
        self.P1_pkmn2.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn2.setIconSize(QSize(100, 100))
        self.P1_pkmn2.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn2.clicked.connect(self.on_click_P1_pkmn2)

        self.P1_pkmn3.setGeometry(320,590, 100, 100)
        self.P1_pkmn3.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn3.setIconSize(QSize(100, 100))
        self.P1_pkmn3.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn3.clicked.connect(self.on_click_P1_pkmn3)

        self.P1_pkmn4.setGeometry(440,590, 100, 100)
        self.P1_pkmn4.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn4.setIconSize(QSize(100, 100))
        self.P1_pkmn4.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn4.clicked.connect(self.on_click_P1_pkmn4)

        self.P1_pkmn5.setGeometry(560,590, 100, 100)
        self.P1_pkmn5.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn5.setIconSize(QSize(100, 100))
        self.P1_pkmn5.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn5.clicked.connect(self.on_click_P1_pkmn5)

        self.P1_pkmn6.setGeometry(680,590, 100, 100)
        self.P1_pkmn6.setIcon(QIcon("assets/icons/pokeballicon.png"))
        self.P1_pkmn6.setIconSize(QSize(100, 100))
        self.P1_pkmn6.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.P1_pkmn6.clicked.connect(self.on_click_P1_pkmn6)

        #Confirm button
        self.confirm_button = QPushButton(self)
        self.confirm_button.setGeometry(100, 450, 230, 100)
        self.confirm_button.setIcon(QIcon("assets/icons/confirmbtn.png"))
        self.confirm_button.setIconSize(QSize(230, 100))
        self.confirm_button.setStyleSheet("font-size: 20px")
        self.confirm_button.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.confirm_button.clicked.connect(self.custom_handle_confirm)
        
        #Next button
        self.nextbtn = QPushButton(self)
        self.nextbtn.setGeometry(750, 450, 180, 100)
        self.nextbtn.setIcon(QIcon("assets/icons/nextbtn.png"))
        self.nextbtn.setIconSize(QSize(300, 100))
        self.nextbtn.setStyleSheet("font-size: 20px")
        self.nextbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.nextbtn.clicked.connect(self.next_page)
        
        #Previous button
        self.prevbtn = QPushButton(self)
        self.prevbtn.setGeometry(550, 450, 180, 100)
        self.prevbtn.setIcon(QIcon("assets/icons/prevbtn.png"))
        self.prevbtn.setIconSize(QSize(300, 100))
        self.prevbtn.setStyleSheet("font-size: 20px")
        self.prevbtn.setStyleSheet("""QPushButton{border:none; padding:0px; margin:0px;}""")
        self.prevbtn.clicked.connect(self.prev_page)


    def custom_handle_confirm(self):
        if len(self.team) == 0:
            QMessageBox.warning(self, "Team Not Selected", "You must select at least one Pokémon.")
            return

        self.selected_team_p1 = self.team

        if self.challenge_callback:
            self.challenge_callback(self.selected_team_p1)
            self.close()
        else:
            self.close()

    

    def on_click_bulbasaur(self):
        self.team_message.setText("Bulbasaur added to your team")
        self.add_pokemon_to_team("bulbasaur")
    def on_click_ivysaur(self):
        self.team_message.setText("Ivysaur added to your team")
        self.add_pokemon_to_team("ivysaur")
    def on_click_venusaur(self):
        self.team_message.setText("Venusaur added to your team")
        self.add_pokemon_to_team("venusaur")
    def on_click_charmander(self):
        self.team_message.setText("Charmander added to your team")
        self.add_pokemon_to_team("charmander")
    def on_click_charmeleon(self):
        self.team_message.setText("Charmeleon added to your team")
        self.add_pokemon_to_team("charmeleon")
    def on_click_charizard(self):
        self.team_message.setText("Charizard added to your team")
        self.add_pokemon_to_team("charizard")
    def on_click_squirtle(self):
        self.team_message.setText("Squirtle added to your team")
        self.add_pokemon_to_team("squirtle")
    def on_click_wartortle(self):
        self.team_message.setText("Wartortle added to your team")
        self.add_pokemon_to_team("wartortle")
    def on_click_blastoise(self):
        self.team_message.setText("Blastoise added to your team")
        self.add_pokemon_to_team("blastoise")
    def on_click_caterpie(self):
        self.team_message.setText("Caterpie added to your team")
        self.add_pokemon_to_team("caterpie")  
    def on_click_metapod(self):
        self.team_message.setText("Metapod added to your team")
        self.add_pokemon_to_team("metapod")   
    def on_click_butterfree(self):
        self.team_message.setText("Butterfree added to your team")
        self.add_pokemon_to_team("butterfree")   
    def on_click_weedle(self):
        self.team_message.setText("Butterfree added to your team")
        self.add_pokemon_to_team("weedle") 
    def on_click_kakuna(self):
        self.team_message.setText("Kakuna added to your team")
        self.add_pokemon_to_team("kakuna")
    def on_click_beedrill(self):
        self.team_message.setText("Beedrill added to your team")
        self.add_pokemon_to_team("beedrill")
    def on_click_pidgey(self):
        self.team_message.setText("Pidgey added to your team")
        self.add_pokemon_to_team("pidgey")
    def on_click_pidgeotto(self):
        self.team_message.setText("Pidgeotto added to your team")
        self.add_pokemon_to_team("pidgeotto")
    def on_click_pidgeot(self):
        self.team_message.setText("Pidgeot added to your team")
        self.add_pokemon_to_team("pidgeot")  
    def on_click_rattata(self):
        self.team_message.setText("Rattata added to your team")
        self.add_pokemon_to_team("rattata")   
    def on_click_raticate(self):
        self.team_message.setText("Raticate added to your team")
        self.add_pokemon_to_team("raticate") 
    def on_click_spearow(self):
        self.team_message.setText("Spearow added to your team")
        self.add_pokemon_to_team("spearow")  
    def on_click_fearow(self):
        self.team_message.setText("Fearow added to your team")
        self.add_pokemon_to_team("fearow")
    def on_click_ekans(self):
        self.team_message.setText("Ekans added to your team")
        self.add_pokemon_to_team("ekans")
    def on_click_arbok(self):
        self.team_message.setText("Arbok added to your team")
        self.add_pokemon_to_team("arbok")
    def on_click_pikachu(self):
        self.team_message.setText("Pikachu added to your team")
        self.add_pokemon_to_team("pikachu")   
    def on_click_raichu(self):
        self.team_message.setText("Raichu added to your team")
        self.add_pokemon_to_team("raichu") 
    def on_click_sandshrew(self):
        self.team_message.setText("Sandshrew added to your team")
        self.add_pokemon_to_team("sandshrew")
    def on_click_sandslash(self):
        self.team_message.setText("Sandslash added to your team")
        self.add_pokemon_to_team("sandslash") 
    def on_click_nidoranf(self):
        self.team_message.setText("Nidoran♀ added to your team")
        self.add_pokemon_to_team("nidoranf") 
    def on_click_nidorina(self):
        self.team_message.setText("Nidorina added to your team")
        self.add_pokemon_to_team("nidorina") 
    def on_click_nidoqueen(self):
        self.team_message.setText("Nidoqueen added to your team")
        self.add_pokemon_to_team("nidoqueen") 
    def on_click_nidoranm(self):
        self.team_message.setText("Nidoran♂ added to your team")
        self.add_pokemon_to_team("nidoranm")
    def on_click_nidorino(self):
        self.team_message.setText("Nidorino added to your team")
        self.add_pokemon_to_team("nidorino")    
    def on_click_nidoking(self):
        self.team_message.setText("Nidoking added to your team")
        self.add_pokemon_to_team("nidoking")   
    def on_click_clefairy(self):
        self.team_message.setText("Clefairy added to your team")
        self.add_pokemon_to_team("clefairy")  
    def on_click_clefable(self):
        self.team_message.setText("Clefable added to your team")
        self.add_pokemon_to_team("clefable")  
    def on_click_vulpix(self):
        self.team_message.setText("Vulpix added to your team")
        self.add_pokemon_to_team("vulpix")  
    def on_click_ninetales(self):
        self.team_message.setText("Ninetales added to your team")
        self.add_pokemon_to_team("ninetales")   
    def on_click_jigglypuff(self):
        self.team_message.setText("Jigglypuff added to your team")
        self.add_pokemon_to_team("jigglypuff") 
    def on_click_wigglytuff(self):
        self.team_message.setText("Wigglytuff added to your team")
        self.add_pokemon_to_team("wigglytuff") 
    def on_click_zubat(self):
        self.team_message.setText("Zubat added to your team")
        self.add_pokemon_to_team("zubat") 
    def on_click_golbat(self):
        self.team_message.setText("Golbat added to your team")
        self.add_pokemon_to_team("golbat")
    def on_click_oddish(self):
        self.team_message.setText("Oddish added to your team")
        self.add_pokemon_to_team("oddish") 
    def on_click_vileplume(self):
        self.team_message.setText("Vileplume added to your team")
        self.add_pokemon_to_team("vileplume") 
    def on_click_paras(self):
        self.team_message.setText("Paras added to your team")
        self.add_pokemon_to_team("paras")   
    def on_click_parasect(self):
        self.team_message.setText("Parasect added to your team")
        self.add_pokemon_to_team("parasect")
    def on_click_venonat(self):
        self.team_message.setText("Venonat added to your team")
        self.add_pokemon_to_team("venonat")
    def on_click_venomoth(self):
        self.team_message.setText("Venomoth added to your team")
        self.add_pokemon_to_team("venomoth")
    def on_click_diglett(self):
        self.team_message.setText("Diglett added to your team")
        self.add_pokemon_to_team("diglett")
    def on_click_dugtrio(self):
        self.team_message.setText("Dugtrio added to your team")
        self.add_pokemon_to_team("dugtrio")
    def on_click_meowth(self):
        self.team_message.setText("Meowth added to your team")
        self.add_pokemon_to_team("meowth")
    def on_click_persian(self):
        self.team_message.setText("Persian added to your team")
        self.add_pokemon_to_team("persian")
    def on_click_psyduck(self):
        self.team_message.setText("Psyduck added to your team")
        self.add_pokemon_to_team("psyduck")
    def on_click_golduck(self):
        self.team_message.setText("Golduck added to your team")
        self.add_pokemon_to_team("golduck")
    def on_click_mankey(self):
        self.team_message.setText("Mankey added to your team")
        self.add_pokemon_to_team("mankey")
    def on_click_primeape(self):
        self.team_message.setText("Primeape added to your team")
        self.add_pokemon_to_team("primeape")
    def on_click_growlithe(self):
        self.team_message.setText("Growlithe added to your team")
        self.add_pokemon_to_team("growlithe")
    def on_click_arcanine(self):
        self.team_message.setText("Arcanine added to your team")
        self.add_pokemon_to_team("arcanine")
    def on_click_poliwag(self):
        self.team_message.setText("Poliwag added to your team")
        self.add_pokemon_to_team("poliwag")
    def on_click_poliwhirl(self):
        self.team_message.setText("Poliwhirl added to your team")
        self.add_pokemon_to_team("poliwhirl")
    def on_click_poliwrath(self):
        self.team_message.setText("Poliwrath added to your team")
        self.add_pokemon_to_team("poliwrath")
    def on_click_abra(self):
        self.team_message.setText("Abra added to your team")
        self.add_pokemon_to_team("abra")
    def on_click_kadabra(self):
        self.team_message.setText("Kadabra added to your team")
        self.add_pokemon_to_team("kadabra")
    def on_click_alakazam(self):
        self.team_message.setText("Alakazam added to your team")
        self.add_pokemon_to_team("alakazam")
    def on_click_machop(self):
        self.team_message.setText("Machop added to your team")
        self.add_pokemon_to_team("machop")
    def on_click_machoke(self):
        self.team_message.setText("Machoke added to your team")
        self.add_pokemon_to_team("machoke")
    def on_click_machamp(self):
        self.team_message.setText("Machamp added to your team")
        self.add_pokemon_to_team("machamp")
    def on_click_bellsprout(self):
        self.team_message.setText("Bellsprout added to your team")
        self.add_pokemon_to_team("bellsprout")
    def on_click_weepinbell(self):
        self.team_message.setText("Weepinbell added to your team")
        self.add_pokemon_to_team("weepinbell")
    def on_click_victreebel(self):
        self.team_message.setText("Victreebel added to your team")
        self.add_pokemon_to_team("victreebel")
    def on_click_tentacool(self):
        self.team_message.setText("Tentacool added to your team")
        self.add_pokemon_to_team("tentacool")
    def on_click_tentacruel(self):
        self.team_message.setText("Tentacruel added to your team")
        self.add_pokemon_to_team("tentacruel")
    def on_click_geodude(self):
        self.team_message.setText("Geodude added to your team")
        self.add_pokemon_to_team("geodude")
    def on_click_graveler(self):
        self.team_message.setText("Graveler added to your team")
        self.add_pokemon_to_team("graveler")
    def on_click_golem(self):
        self.team_message.setText("Golem added to your team")
        self.add_pokemon_to_team("golem")
    def on_click_ponyta(self):
        self.team_message.setText("Ponyta added to your team")
        self.add_pokemon_to_team("ponyta")
    def on_click_rapidash(self):
        self.team_message.setText("Rapidash added to your team")
        self.add_pokemon_to_team("rapidash")
    def on_click_slowpoke(self):
        self.team_message.setText("Slowpoke added to your team")
        self.add_pokemon_to_team("slowpoke")
    def on_click_slowbro(self):
        self.team_message.setText("Slowbro added to your team")
        self.add_pokemon_to_team("slowbro")
    def on_click_magnemite(self):
        self.team_message.setText("Magnemite added to your team")
        self.add_pokemon_to_team("magnemite")
    def on_click_magneton(self):
        self.team_message.setText("Magneton added to your team")
        self.add_pokemon_to_team("magneton")
    def on_click_farfetchd(self):
        self.team_message.setText("Farfetch'd added to your team")
        self.add_pokemon_to_team("farfetchd")
    def on_click_doduo(self):
        self.team_message.setText("Doduo added to your team")
        self.add_pokemon_to_team("doduo")
    def on_click_dodrio(self):
        self.team_message.setText("Dodrio added to your team")
        self.add_pokemon_to_team("dodrio")
    def on_click_seel(self):
        self.team_message.setText("Seel added to your team")
        self.add_pokemon_to_team("seel")
    def on_click_dewgong(self):
        self.team_message.setText("Dewgong added to your team")
        self.add_pokemon_to_team("dewgong")
    def on_click_grimer(self):
        self.team_message.setText("Grimer added to your team")
        self.add_pokemon_to_team("grimer")
    def on_click_muk(self):
        self.team_message.setText("Muk added to your team")
        self.add_pokemon_to_team("muk")
    def on_click_shellder(self):
        self.team_message.setText("Shellder added to your team")
        self.add_pokemon_to_team("shellder")
    def on_click_cloyster(self):
        self.team_message.setText("Cloyster added to your team")
        self.add_pokemon_to_team("cloyster")
    def on_click_gastly(self):
        self.team_message.setText("Gastly added to your team")
        self.add_pokemon_to_team("gastly")
    def on_click_haunter(self):
        self.team_message.setText("Haunter added to your team")
        self.add_pokemon_to_team("haunter")
    def on_click_gengar(self):
        self.team_message.setText("Gengar added to your team")
        self.add_pokemon_to_team("gengar")
    def on_click_onix(self):
        self.team_message.setText("Onix added to your team")
        self.add_pokemon_to_team("onix")
    def on_click_drowzee(self):
        self.team_message.setText("Drowzee added to your team")
        self.add_pokemon_to_team("drowzee")
    def on_click_hypno(self):
        self.team_message.setText("Hypno added to your team")
        self.add_pokemon_to_team("hypno")
    def on_click_krabby(self):
        self.team_message.setText("Krabby added to your team")
        self.add_pokemon_to_team("krabby")
    def on_click_kingler(self):
        self.team_message.setText("Kingler added to your team")
        self.add_pokemon_to_team("kingler")
    def on_click_voltorb(self):
        self.team_message.setText("Voltorb added to your team")
        self.add_pokemon_to_team("voltorb")
    def on_click_electrode(self):
        self.team_message.setText("Electrode added to your team")
        self.add_pokemon_to_team("electrode")
    def on_click_exeggcute(self):
        self.team_message.setText("Exeggcute added to your team")
        self.add_pokemon_to_team("exeggcute")
    def on_click_exeggutor(self):
        self.team_message.setText("Exeggutor added to your team")
        self.add_pokemon_to_team("exeggutor")
    def on_click_cubone(self):
        self.team_message.setText("Cubone added to your team")
        self.add_pokemon_to_team("cubone")
    def on_click_marowak(self):
        self.team_message.setText("Marowak added to your team")
        self.add_pokemon_to_team("marowak")
    def on_click_hitmonlee(self):
        self.team_message.setText("Hitmonlee added to your team")
        self.add_pokemon_to_team("hitmonlee")
    def on_click_hitmonchan(self):
        self.team_message.setText("Hitmonchan added to your team")
        self.add_pokemon_to_team("hitmonchan")
    def on_click_lickitung(self):
        self.team_message.setText("Lickitung added to your team")
        self.add_pokemon_to_team("lickitung")
    def on_click_koffing(self):
        self.team_message.setText("Koffing added to your team")
        self.add_pokemon_to_team("koffing")
    def on_click_weezing(self):
        self.team_message.setText("Weezing added to your team")
        self.add_pokemon_to_team("weezing")
    def on_click_rhyhorn(self):
        self.team_message.setText("Rhyhorn added to your team")
        self.add_pokemon_to_team("rhyhorn")   
    def on_click_rhydon(self):
        self.team_message.setText("Rhydon added to your team")
        self.add_pokemon_to_team("rhydon") 
    def on_click_chansey(self):
        self.team_message.setText("Chansey added to your team")
        self.add_pokemon_to_team("chansey")
    def on_click_tangela(self):
        self.team_message.setText("Tangela added to your team")
        self.add_pokemon_to_team("tangela")     
    def on_click_kangaskhan(self):
        self.team_message.setText("Kangaskhan added to your team")
        self.add_pokemon_to_team("kangaskhan")
    def on_click_horsea(self):
        self.team_message.setText("Horsea added to your team")
        self.add_pokemon_to_team("horsea")   
    def on_click_seadra(self):
        self.team_message.setText("Seadra added to your team")
        self.add_pokemon_to_team("seadra")      
    def on_click_goldeen(self):
        self.team_message.setText("Goldeen added to your team")
        self.add_pokemon_to_team("goldeen")    
    def on_click_seaking(self):
        self.team_message.setText("Seaking added to your team")
        self.add_pokemon_to_team("seaking")   
    def on_click_staryu(self):
        self.team_message.setText("Staryu added to your team")
        self.add_pokemon_to_team("staryu")  
    def on_click_starmie(self):
        self.team_message.setText("Starmie added to your team")
        self.add_pokemon_to_team("starmie")  
    def on_click_mrmime(self):
        self.team_message.setText("Mr. Mime added to your team")
        self.add_pokemon_to_team("mrmime") 
    def on_click_scyther(self):
        self.team_message.setText("Scyther added to your team")
        self.add_pokemon_to_team("scyther")   
    def on_click_jynx(self):
        self.team_message.setText("Jynx added to your team")
        self.add_pokemon_to_team("jynx") 
    def on_click_electabuzz(self):
        self.team_message.setText("Electabuzz added to your team")
        self.add_pokemon_to_team("electabuzz")
    def on_click_magmar(self):
        self.team_message.setText("Magmar added to your team")
        self.add_pokemon_to_team("magmar")    
    def on_click_pinsir(self):
        self.team_message.setText("Pinsir added to your team")
        self.add_pokemon_to_team("pinsir")  
    def on_click_tauros(self):
        self.team_message.setText("Tauros added to your team")
        self.add_pokemon_to_team("tauros")
    def on_click_magikarp(self):
        self.team_message.setText("Magikarp added to your team")
        self.add_pokemon_to_team("magikarp")
    def on_click_gyarados(self):
        self.team_message.setText("Gyarados added to your team")
        self.add_pokemon_to_team("gyarados")
    def on_click_lapras(self):
        self.team_message.setText("Lapras added to your team")
        self.add_pokemon_to_team("lapras")
    def on_click_ditto(self):
        self.team_message.setText("Ditto added to your team")
        self.add_pokemon_to_team("ditto")
    def on_click_eevee(self):
        self.team_message.setText("Eevee added to your team")
        self.add_pokemon_to_team("eevee")
    def on_click_vaporeon(self):
        self.team_message.setText("Vaporeon added to your team")
        self.add_pokemon_to_team("vaporeon")
    def on_click_jolteon(self):
        self.team_message.setText("Jolteon added to your team")
        self.add_pokemon_to_team("jolteon")
    def on_click_flareon(self):
        self.team_message.setText("Flareon added to your team")
        self.add_pokemon_to_team("flareon")
    def on_click_porygon(self):
        self.team_message.setText("Porygon added to your team")
        self.add_pokemon_to_team("porygon")
    def on_click_omanyte(self):
        self.team_message.setText("Omanyte added to your team")
        self.add_pokemon_to_team("omanyte")
    def on_click_omastar(self):
        self.team_message.setText("Omastar added to your team")
        self.add_pokemon_to_team("omastar")
    def on_click_kabuto(self):
        self.team_message.setText("Kabuto added to your team")
        self.add_pokemon_to_team("kabuto")
    def on_click_kabutops(self):
        self.team_message.setText("Kabutops added to your team")
        self.add_pokemon_to_team("kabutops")
    def on_click_aerodactyl(self):
        self.team_message.setText("Aerodactyl added to your team")
        self.add_pokemon_to_team("aerodactyl")
    def on_click_snorlax(self):
        self.team_message.setText("Snorlax added to your team")
        self.add_pokemon_to_team("snorlax")
    def on_click_articuno(self):
        self.team_message.setText("Articuno added to your team")
        self.add_pokemon_to_team("articuno")
    def on_click_zapdos(self):
        self.team_message.setText("Zapdos added to your team")
        self.add_pokemon_to_team("zapdos")
    def on_click_moltres(self):
        self.team_message.setText("Moltres added to your team")
        self.add_pokemon_to_team("moltres")
    def on_click_dratini(self):
        self.team_message.setText("Dratini added to your team")
        self.add_pokemon_to_team("dratini")
    def on_click_dragonair(self):
        self.team_message.setText("Dragonair added to your team")
        self.add_pokemon_to_team("dragonair")
    def on_click_dragonite(self):
        self.team_message.setText("Dragonite added to your team")
        self.add_pokemon_to_team("dragonite")
    def on_click_mewtwo(self):
        self.team_message.setText("Mewtwo added to your team")
        self.add_pokemon_to_team("mewtwo")
    def on_click_mew(self):
        self.team_message.setText("Mew added to your team")
        self.add_pokemon_to_team("mew")

    #def on_click_(self): TEMPLATE
    #    self.team_message.setText(" added to your team")
    #    self.add_pokemon_to_team("")

    def page_handler(self, page):
        if self.page <= 0:
            self.page = 1
        elif self.page == 1:
            
            self.selectionspring.setVisible(True)
            self.selectionsummer.setVisible(False)
            self.selectionautumn.setVisible(False)
            self.selectionwinter.setVisible(False)

            #Page 1 Content Visible
            self.bulbasaur.setVisible(True)
            self.ivysaur.setVisible(True)
            self.venusaur.setVisible(True)
            self.charmander.setVisible(True)
            self.charmeleon.setVisible(True)
            self.charizard.setVisible(True)
            self.squirtle.setVisible(True)
            self.wartortle.setVisible(True)
            self.blastoise.setVisible(True)
            self.caterpie.setVisible(True)
            self.metapod.setVisible(True)
            self.butterfree.setVisible(True)
            self.weedle.setVisible(True)
            self.kakuna.setVisible(True)
            self.beedrill.setVisible(True)
            self.pidgey.setVisible(True)
            self.pidgeotto.setVisible(True)
            self.pidgeot.setVisible(True)
            self.rattata.setVisible(True)
            self.raticate.setVisible(True)
            self.spearow.setVisible(True)
            self.fearow.setVisible(True)
            self.ekans.setVisible(True)
            self.arbok.setVisible(True)
            self.pikachu.setVisible(True)
            self.raichu.setVisible(True)
            self.sandshrew.setVisible(True)
            self.sandslash.setVisible(True)
            self.nidoranf.setVisible(True)
            self.nidorina.setVisible(True)
            self.nidoqueen.setVisible(True)
            self.nidoranm.setVisible(True)
            self.nidorino.setVisible(True)
            self.nidoking.setVisible(True)
            self.clefairy.setVisible(True)
            self.clefable.setVisible(True)
            self.vulpix.setVisible(True)

            #Page 2 Content Hidden
            self.ninetales.setVisible(False)
            self.jigglypuff.setVisible(False)
            self.wigglytuff.setVisible(False)
            self.zubat.setVisible(False)
            self.golbat.setVisible(False)
            self.oddish.setVisible(False)
            self.vileplume.setVisible(False)
            self.paras.setVisible(False)
            self.parasect.setVisible(False)
            self.venonat.setVisible(False)
            self.venomoth.setVisible(False)
            self.diglett.setVisible(False)
            self.dugtrio.setVisible(False)
            self.meowth.setVisible(False)
            self.persian.setVisible(False)
            self.psyduck.setVisible(False)
            self.golduck.setVisible(False)
            self.mankey.setVisible(False)
            self.primeape.setVisible(False)
            self.growlithe.setVisible(False)
            self.arcanine.setVisible(False)
            self.poliwag.setVisible(False)
            self.poliwhirl.setVisible(False)
            self.poliwrath.setVisible(False)
            self.abra.setVisible(False)
            self.kadabra.setVisible(False)
            self.alakazam.setVisible(False)
            self.machop.setVisible(False)
            self.machoke.setVisible(False)
            self.machamp.setVisible(False)
            self.bellsprout.setVisible(False)
            self.weepinbell.setVisible(False)
            self.victreebel.setVisible(False)
            self.tentacool.setVisible(False)
            self.tentacruel.setVisible(False)
            self.geodude.setVisible(False)

            #Page 3 Content Hidden
            self.graveler.setVisible(False)
            self.golem.setVisible(False)
            self.ponyta.setVisible(False)
            self.rapidash.setVisible(False)
            self.slowpoke.setVisible(False)
            self.slowbro.setVisible(False)
            self.magnemite.setVisible(False)
            self.magneton.setVisible(False)
            self.farfetchd.setVisible(False)
            self.doduo.setVisible(False)
            self.dodrio.setVisible(False)
            self.seel.setVisible(False)
            self.dewgong.setVisible(False)
            self.grimer.setVisible(False)
            self.muk.setVisible(False)
            self.shellder.setVisible(False)
            self.cloyster.setVisible(False)
            self.gastly.setVisible(False)
            self.haunter.setVisible(False)
            self.gengar.setVisible(False)
            self.onix.setVisible(False)
            self.drowzee.setVisible(False)
            self.hypno.setVisible(False)
            self.krabby.setVisible(False)
            self.krabby.setVisible(False)
            self.kingler.setVisible(False)
            self.voltorb.setVisible(False)
            self.electrode.setVisible(False)
            self.exeggcute.setVisible(False)
            self.exeggutor.setVisible(False)
            self.cubone.setVisible(False)
            self.marowak.setVisible(False)
            self.hitmonlee.setVisible(False)
            self.hitmonchan.setVisible(False)
            self.lickitung.setVisible(False)
            self.koffing.setVisible(False)
            self.weezing.setVisible(False)

            #Page 4 Content Hidden
            self.rhyhorn.setVisible(False)
            self.rhydon.setVisible(False)
            self.chansey.setVisible(False)
            self.tangela.setVisible(False)
            self.kangaskhan.setVisible(False)
            self.horsea.setVisible(False)
            self.seadra.setVisible(False)
            self.goldeen.setVisible(False)
            self.seaking.setVisible(False)
            self.staryu.setVisible(False)
            self.starmie.setVisible(False)
            self.mrmime.setVisible(False)
            self.scyther.setVisible(False)
            self.jynx.setVisible(False)
            self.electabuzz.setVisible(False)
            self.magmar.setVisible(False)
            self.pinsir.setVisible(False)
            self.tauros.setVisible(False)
            self.magikarp.setVisible(False)
            self.gyarados.setVisible(False)
            self.lapras.setVisible(False)
            self.ditto.setVisible(False)
            self.eevee.setVisible(False)
            self.vaporeon.setVisible(False)
            self.jolteon.setVisible(False)
            self.flareon.setVisible(False)
            self.porygon.setVisible(False)
            self.omanyte.setVisible(False)
            self.omastar.setVisible(False)
            self.kabuto.setVisible(False)
            self.kabutops.setVisible(False)
            self.aerodactyl.setVisible(False)
            self.snorlax.setVisible(False)
            self.articuno.setVisible(False)
            self.zapdos.setVisible(False)
            self.moltres.setVisible(False)
            
            #Page 5 Content Hidden
            self.dratini.setVisible(False)
            self.dragonair.setVisible(False)
            self.dragonite.setVisible(False)
            self.mewtwo.setVisible(False)
            self.mew.setVisible(False)

        elif self.page == 2:
            
            self.selectionspring.setVisible(False)
            self.selectionsummer.setVisible(True)
            self.selectionautumn.setVisible(False)
            self.selectionwinter.setVisible(False)

            #Page 1 Content Hidden
            self.bulbasaur.setVisible(False)
            self.ivysaur.setVisible(False)
            self.venusaur.setVisible(False)
            self.charmander.setVisible(False)
            self.charmeleon.setVisible(False)
            self.charizard.setVisible(False)
            self.squirtle.setVisible(False)
            self.wartortle.setVisible(False)
            self.blastoise.setVisible(False)
            self.caterpie.setVisible(False)
            self.metapod.setVisible(False)
            self.butterfree.setVisible(False)
            self.weedle.setVisible(False)
            self.kakuna.setVisible(False)
            self.beedrill.setVisible(False)
            self.pidgey.setVisible(False)
            self.pidgeotto.setVisible(False)
            self.pidgeot.setVisible(False)
            self.rattata.setVisible(False)
            self.raticate.setVisible(False)
            self.spearow.setVisible(False)
            self.fearow.setVisible(False)
            self.ekans.setVisible(False)
            self.arbok.setVisible(False)
            self.pikachu.setVisible(False)
            self.raichu.setVisible(False)
            self.sandshrew.setVisible(False)
            self.sandslash.setVisible(False)
            self.nidoranf.setVisible(False)
            self.nidorina.setVisible(False)
            self.nidoqueen.setVisible(False)
            self.nidoranm.setVisible(False)
            self.nidorino.setVisible(False)
            self.nidoking.setVisible(False)
            self.clefairy.setVisible(False)
            self.clefable.setVisible(False)
            self.vulpix.setVisible(False)    
            
            #Page 2 Content Visible
            self.ninetales.setVisible(True) 
            self.jigglypuff.setVisible(True)
            self.wigglytuff.setVisible(True)
            self.zubat.setVisible(True)
            self.golbat.setVisible(True)
            self.oddish.setVisible(True)
            self.vileplume.setVisible(True)
            self.paras.setVisible(True)
            self.parasect.setVisible(True)
            self.venonat.setVisible(True)
            self.venomoth.setVisible(True)
            self.diglett.setVisible(True)
            self.dugtrio.setVisible(True)
            self.meowth.setVisible(True)
            self.persian.setVisible(True)
            self.psyduck.setVisible(True)
            self.golduck.setVisible(True)
            self.mankey.setVisible(True)
            self.primeape.setVisible(True)
            self.growlithe.setVisible(True)
            self.arcanine.setVisible(True)
            self.poliwag.setVisible(True)
            self.poliwhirl.setVisible(True)
            self.poliwrath.setVisible(True)
            self.abra.setVisible(True)
            self.kadabra.setVisible(True)
            self.alakazam.setVisible(True)
            self.machop.setVisible(True)
            self.machoke.setVisible(True)
            self.machamp.setVisible(True)
            self.bellsprout.setVisible(True)
            self.weepinbell.setVisible(True)
            self.victreebel.setVisible(True)
            self.tentacool.setVisible(True)
            self.tentacruel.setVisible(True)
            self.geodude.setVisible(True)

            #Page 3 Content Hidden
            self.graveler.setVisible(False)
            self.golem.setVisible(False)
            self.ponyta.setVisible(False)
            self.rapidash.setVisible(False)
            self.slowpoke.setVisible(False)
            self.slowbro.setVisible(False)
            self.magnemite.setVisible(False)
            self.magneton.setVisible(False)
            self.farfetchd.setVisible(False)
            self.doduo.setVisible(False)
            self.dodrio.setVisible(False)
            self.seel.setVisible(False)
            self.dewgong.setVisible(False)
            self.grimer.setVisible(False)
            self.muk.setVisible(False)
            self.shellder.setVisible(False)
            self.cloyster.setVisible(False)
            self.gastly.setVisible(False)
            self.haunter.setVisible(False)
            self.gengar.setVisible(False)
            self.onix.setVisible(False)
            self.drowzee.setVisible(False)
            self.hypno.setVisible(False)
            self.krabby.setVisible(False)
            self.krabby.setVisible(False)
            self.kingler.setVisible(False)
            self.voltorb.setVisible(False)
            self.electrode.setVisible(False)
            self.exeggcute.setVisible(False)
            self.exeggutor.setVisible(False)
            self.cubone.setVisible(False)
            self.marowak.setVisible(False)
            self.hitmonlee.setVisible(False)
            self.hitmonchan.setVisible(False)
            self.lickitung.setVisible(False)
            self.koffing.setVisible(False)
            self.weezing.setVisible(False)

            #Page 4 Content Hidden
            self.rhyhorn.setVisible(False)
            self.rhydon.setVisible(False)
            self.chansey.setVisible(False)
            self.tangela.setVisible(False)
            self.kangaskhan.setVisible(False)
            self.horsea.setVisible(False)
            self.seadra.setVisible(False)
            self.goldeen.setVisible(False)
            self.seaking.setVisible(False)
            self.staryu.setVisible(False)
            self.starmie.setVisible(False)
            self.mrmime.setVisible(False)
            self.scyther.setVisible(False)
            self.jynx.setVisible(False)
            self.electabuzz.setVisible(False)
            self.magmar.setVisible(False)
            self.pinsir.setVisible(False)
            self.tauros.setVisible(False)
            self.magikarp.setVisible(False)
            self.gyarados.setVisible(False)
            self.lapras.setVisible(False)
            self.ditto.setVisible(False)
            self.eevee.setVisible(False)
            self.vaporeon.setVisible(False)
            self.jolteon.setVisible(False)
            self.flareon.setVisible(False)
            self.porygon.setVisible(False)
            self.omanyte.setVisible(False)
            self.omastar.setVisible(False)
            self.kabuto.setVisible(False)
            self.kabutops.setVisible(False)
            self.aerodactyl.setVisible(False)
            self.snorlax.setVisible(False)
            self.articuno.setVisible(False)
            self.zapdos.setVisible(False)
            self.moltres.setVisible(False)
            
            #Page 5 Content Hidden
            self.dratini.setVisible(False)
            self.dragonair.setVisible(False)
            self.dragonite.setVisible(False)
            self.mewtwo.setVisible(False)
            self.mew.setVisible(False)


        elif self.page == 3:
            
            self.selectionspring.setVisible(False)
            self.selectionsummer.setVisible(False)
            self.selectionautumn.setVisible(True)
            self.selectionwinter.setVisible(False)

            #Page 1 Content Hidden
            self.bulbasaur.setVisible(False)
            self.ivysaur.setVisible(False)
            self.venusaur.setVisible(False)
            self.charmander.setVisible(False)
            self.charmeleon.setVisible(False)
            self.charizard.setVisible(False)
            self.squirtle.setVisible(False)
            self.wartortle.setVisible(False)
            self.blastoise.setVisible(False)
            self.caterpie.setVisible(False)
            self.metapod.setVisible(False)
            self.butterfree.setVisible(False)
            self.weedle.setVisible(False)
            self.kakuna.setVisible(False)
            self.beedrill.setVisible(False)
            self.pidgey.setVisible(False)
            self.pidgeotto.setVisible(False)
            self.pidgeot.setVisible(False)
            self.rattata.setVisible(False)
            self.raticate.setVisible(False)
            self.spearow.setVisible(False)
            self.fearow.setVisible(False)
            self.ekans.setVisible(False)
            self.arbok.setVisible(False)
            self.pikachu.setVisible(False)
            self.raichu.setVisible(False)
            self.sandshrew.setVisible(False)
            self.sandslash.setVisible(False)
            self.nidoranf.setVisible(False)
            self.nidorina.setVisible(False)
            self.nidoqueen.setVisible(False)
            self.nidoranm.setVisible(False)
            self.nidorino.setVisible(False)
            self.nidoking.setVisible(False)
            self.clefairy.setVisible(False)
            self.clefable.setVisible(False)
            self.vulpix.setVisible(False)

            #Page 2 Content Hidden
            self.ninetales.setVisible(False)
            self.jigglypuff.setVisible(False)
            self.wigglytuff.setVisible(False)
            self.zubat.setVisible(False)
            self.golbat.setVisible(False)
            self.oddish.setVisible(False)
            self.vileplume.setVisible(False)
            self.paras.setVisible(False)
            self.parasect.setVisible(False)
            self.venonat.setVisible(False)
            self.venomoth.setVisible(False)
            self.diglett.setVisible(False)
            self.dugtrio.setVisible(False)
            self.meowth.setVisible(False)
            self.persian.setVisible(False)
            self.psyduck.setVisible(False)
            self.golduck.setVisible(False)
            self.mankey.setVisible(False)
            self.primeape.setVisible(False)
            self.growlithe.setVisible(False)
            self.arcanine.setVisible(False)
            self.poliwag.setVisible(False)
            self.poliwhirl.setVisible(False)
            self.poliwrath.setVisible(False)
            self.abra.setVisible(False)
            self.kadabra.setVisible(False)
            self.alakazam.setVisible(False)
            self.machop.setVisible(False)
            self.machoke.setVisible(False)
            self.machamp.setVisible(False)
            self.bellsprout.setVisible(False)
            self.weepinbell.setVisible(False)
            self.victreebel.setVisible(False)
            self.tentacool.setVisible(False)
            self.tentacruel.setVisible(False)
            self.geodude.setVisible(False)

            #Page 3 Content Visible
            self.graveler.setVisible(True)
            self.golem.setVisible(True)
            self.ponyta.setVisible(True)
            self.rapidash.setVisible(True)
            self.slowpoke.setVisible(True)
            self.slowbro.setVisible(True)
            self.magnemite.setVisible(True)
            self.magneton.setVisible(True)
            self.farfetchd.setVisible(True)
            self.doduo.setVisible(True)
            self.dodrio.setVisible(True)
            self.seel.setVisible(True)
            self.dewgong.setVisible(True)
            self.grimer.setVisible(True)
            self.muk.setVisible(True)
            self.shellder.setVisible(True)
            self.cloyster.setVisible(True)
            self.gastly.setVisible(True)
            self.haunter.setVisible(True)
            self.gengar.setVisible(True)
            self.onix.setVisible(True)
            self.drowzee.setVisible(True)
            self.hypno.setVisible(True)
            self.krabby.setVisible(True)
            self.krabby.setVisible(True)
            self.kingler.setVisible(True)
            self.voltorb.setVisible(True)
            self.electrode.setVisible(True)
            self.exeggcute.setVisible(True)
            self.exeggutor.setVisible(True)
            self.cubone.setVisible(True)
            self.marowak.setVisible(True)
            self.hitmonlee.setVisible(True)
            self.hitmonchan.setVisible(True)
            self.lickitung.setVisible(True)
            self.koffing.setVisible(True)
            self.weezing.setVisible(True)

            #Page 4 Content Hidden
            self.rhyhorn.setVisible(False)
            self.rhydon.setVisible(False)
            self.chansey.setVisible(False)
            self.tangela.setVisible(False)
            self.kangaskhan.setVisible(False)
            self.horsea.setVisible(False)
            self.seadra.setVisible(False)
            self.goldeen.setVisible(False)
            self.seaking.setVisible(False)
            self.staryu.setVisible(False)
            self.starmie.setVisible(False)
            self.mrmime.setVisible(False)
            self.scyther.setVisible(False)
            self.jynx.setVisible(False)
            self.electabuzz.setVisible(False)
            self.magmar.setVisible(False)
            self.pinsir.setVisible(False)
            self.tauros.setVisible(False)
            self.magikarp.setVisible(False)
            self.gyarados.setVisible(False)
            self.lapras.setVisible(False)
            self.ditto.setVisible(False)
            self.eevee.setVisible(False)
            self.vaporeon.setVisible(False)
            self.jolteon.setVisible(False)
            self.flareon.setVisible(False)
            self.porygon.setVisible(False)
            self.omanyte.setVisible(False)
            self.omastar.setVisible(False)
            self.kabuto.setVisible(False)
            self.kabutops.setVisible(False)
            self.aerodactyl.setVisible(False)
            self.snorlax.setVisible(False)
            self.articuno.setVisible(False)
            self.zapdos.setVisible(False)
            self.moltres.setVisible(False)
            
            #Page 5 Content Hidden
            self.dratini.setVisible(False)
            self.dragonair.setVisible(False)
            self.dragonite.setVisible(False)
            self.mewtwo.setVisible(False)
            self.mew.setVisible(False)


        elif self.page == 4:
            
            self.selectionspring.setVisible(False)
            self.selectionsummer.setVisible(False)
            self.selectionautumn.setVisible(False)
            self.selectionwinter.setVisible(True)

            #Page 1 Content Hidden
            self.bulbasaur.setVisible(False)
            self.ivysaur.setVisible(False)
            self.venusaur.setVisible(False)
            self.charmander.setVisible(False)
            self.charmeleon.setVisible(False)
            self.charizard.setVisible(False)
            self.squirtle.setVisible(False)
            self.wartortle.setVisible(False)
            self.blastoise.setVisible(False)
            self.caterpie.setVisible(False)
            self.metapod.setVisible(False)
            self.butterfree.setVisible(False)
            self.weedle.setVisible(False)
            self.kakuna.setVisible(False)
            self.beedrill.setVisible(False)
            self.pidgey.setVisible(False)
            self.pidgeotto.setVisible(False)
            self.pidgeot.setVisible(False)
            self.rattata.setVisible(False)
            self.raticate.setVisible(False)
            self.spearow.setVisible(False)
            self.fearow.setVisible(False)
            self.ekans.setVisible(False)
            self.arbok.setVisible(False)
            self.pikachu.setVisible(False)
            self.raichu.setVisible(False)
            self.sandshrew.setVisible(False)
            self.sandslash.setVisible(False)
            self.nidoranf.setVisible(False)
            self.nidorina.setVisible(False)
            self.nidoqueen.setVisible(False)
            self.nidoranm.setVisible(False)
            self.nidorino.setVisible(False)
            self.nidoking.setVisible(False)
            self.clefairy.setVisible(False)
            self.clefable.setVisible(False)
            self.vulpix.setVisible(False)

            #Page 2 Content Hidden
            self.ninetales.setVisible(False)
            self.jigglypuff.setVisible(False)
            self.wigglytuff.setVisible(False)
            self.zubat.setVisible(False)
            self.golbat.setVisible(False)
            self.oddish.setVisible(False)
            self.vileplume.setVisible(False)
            self.paras.setVisible(False)
            self.parasect.setVisible(False)
            self.venonat.setVisible(False)
            self.venomoth.setVisible(False)
            self.diglett.setVisible(False)
            self.dugtrio.setVisible(False)
            self.meowth.setVisible(False)
            self.persian.setVisible(False)
            self.psyduck.setVisible(False)
            self.golduck.setVisible(False)
            self.mankey.setVisible(False)
            self.primeape.setVisible(False)
            self.growlithe.setVisible(False)
            self.arcanine.setVisible(False)
            self.poliwag.setVisible(False)
            self.poliwhirl.setVisible(False)
            self.poliwrath.setVisible(False)
            self.abra.setVisible(False)
            self.kadabra.setVisible(False)
            self.alakazam.setVisible(False)
            self.machop.setVisible(False)
            self.machoke.setVisible(False)
            self.machamp.setVisible(False)
            self.bellsprout.setVisible(False)
            self.weepinbell.setVisible(False)
            self.victreebel.setVisible(False)
            self.tentacool.setVisible(False)
            self.tentacruel.setVisible(False)
            self.geodude.setVisible(False)

            #Page 3 Content Hidden
            self.graveler.setVisible(False)
            self.golem.setVisible(False)
            self.ponyta.setVisible(False)
            self.rapidash.setVisible(False)
            self.slowpoke.setVisible(False)
            self.slowbro.setVisible(False)
            self.magnemite.setVisible(False)
            self.magneton.setVisible(False)
            self.farfetchd.setVisible(False)
            self.doduo.setVisible(False)
            self.dodrio.setVisible(False)
            self.seel.setVisible(False)
            self.dewgong.setVisible(False)
            self.grimer.setVisible(False)
            self.muk.setVisible(False)
            self.shellder.setVisible(False)
            self.cloyster.setVisible(False)
            self.gastly.setVisible(False)
            self.haunter.setVisible(False)
            self.gengar.setVisible(False)
            self.onix.setVisible(False)
            self.drowzee.setVisible(False)
            self.hypno.setVisible(False)
            self.krabby.setVisible(False)
            self.krabby.setVisible(False)
            self.kingler.setVisible(False)
            self.voltorb.setVisible(False)
            self.electrode.setVisible(False)
            self.exeggcute.setVisible(False)
            self.exeggutor.setVisible(False)
            self.cubone.setVisible(False)
            self.marowak.setVisible(False)
            self.hitmonlee.setVisible(False)
            self.hitmonchan.setVisible(False)
            self.lickitung.setVisible(False)
            self.koffing.setVisible(False)
            self.weezing.setVisible(False)

            #Page 4 Content Visible
            self.rhyhorn.setVisible(True)
            self.rhydon.setVisible(True)
            self.chansey.setVisible(True)
            self.tangela.setVisible(True)
            self.kangaskhan.setVisible(True)
            self.horsea.setVisible(True)
            self.seadra.setVisible(True)
            self.goldeen.setVisible(True)
            self.seaking.setVisible(True)
            self.staryu.setVisible(True)
            self.starmie.setVisible(True)
            self.mrmime.setVisible(True)
            self.scyther.setVisible(True)
            self.jynx.setVisible(True)
            self.electabuzz.setVisible(True)
            self.magmar.setVisible(True)
            self.pinsir.setVisible(True)
            self.tauros.setVisible(True)
            self.magikarp.setVisible(True)
            self.gyarados.setVisible(True)
            self.lapras.setVisible(True)
            self.ditto.setVisible(True)
            self.eevee.setVisible(True)
            self.vaporeon.setVisible(True)
            self.jolteon.setVisible(True)
            self.flareon.setVisible(True)
            self.porygon.setVisible(True)
            self.omanyte.setVisible(True)
            self.omastar.setVisible(True)
            self.kabuto.setVisible(True)
            self.kabutops.setVisible(True)
            self.aerodactyl.setVisible(True)
            self.snorlax.setVisible(True)
            self.articuno.setVisible(True)
            self.zapdos.setVisible(True)
            self.moltres.setVisible(True)
            
            #Page 5 Content Hidden
            self.dratini.setVisible(False)
            self.dragonair.setVisible(False)
            self.dragonite.setVisible(False)
            self.mewtwo.setVisible(False)
            self.mew.setVisible(False)
        
        elif self.page == 5:
            
            self.selectionspring.setVisible(True)
            self.selectionsummer.setVisible(False)
            self.selectionautumn.setVisible(False)
            self.selectionwinter.setVisible(False)
            
            #Page 1 Content Hidden
            self.bulbasaur.setVisible(False)
            self.ivysaur.setVisible(False)
            self.venusaur.setVisible(False)
            self.charmander.setVisible(False)
            self.charmeleon.setVisible(False)
            self.charizard.setVisible(False)
            self.squirtle.setVisible(False)
            self.wartortle.setVisible(False)
            self.blastoise.setVisible(False)
            self.caterpie.setVisible(False)
            self.metapod.setVisible(False)
            self.butterfree.setVisible(False)
            self.weedle.setVisible(False)
            self.kakuna.setVisible(False)
            self.beedrill.setVisible(False)
            self.pidgey.setVisible(False)
            self.pidgeotto.setVisible(False)
            self.pidgeot.setVisible(False)
            self.rattata.setVisible(False)
            self.raticate.setVisible(False)
            self.spearow.setVisible(False)
            self.fearow.setVisible(False)
            self.ekans.setVisible(False)
            self.arbok.setVisible(False)
            self.pikachu.setVisible(False)
            self.raichu.setVisible(False)
            self.sandshrew.setVisible(False)
            self.sandslash.setVisible(False)
            self.nidoranf.setVisible(False)
            self.nidorina.setVisible(False)
            self.nidoqueen.setVisible(False)
            self.nidoranm.setVisible(False)
            self.nidorino.setVisible(False)
            self.nidoking.setVisible(False)
            self.clefairy.setVisible(False)
            self.clefable.setVisible(False)
            self.vulpix.setVisible(False)

            #Page 2 Content Hidden
            self.ninetales.setVisible(False)
            self.jigglypuff.setVisible(False)
            self.wigglytuff.setVisible(False)
            self.zubat.setVisible(False)
            self.golbat.setVisible(False)
            self.oddish.setVisible(False)
            self.vileplume.setVisible(False)
            self.paras.setVisible(False)
            self.parasect.setVisible(False)
            self.venonat.setVisible(False)
            self.venomoth.setVisible(False)
            self.diglett.setVisible(False)
            self.dugtrio.setVisible(False)
            self.meowth.setVisible(False)
            self.persian.setVisible(False)
            self.psyduck.setVisible(False)
            self.golduck.setVisible(False)
            self.mankey.setVisible(False)
            self.primeape.setVisible(False)
            self.growlithe.setVisible(False)
            self.arcanine.setVisible(False)
            self.poliwag.setVisible(False)
            self.poliwhirl.setVisible(False)
            self.poliwrath.setVisible(False)
            self.abra.setVisible(False)
            self.kadabra.setVisible(False)
            self.alakazam.setVisible(False)
            self.machop.setVisible(False)
            self.machoke.setVisible(False)
            self.machamp.setVisible(False)
            self.bellsprout.setVisible(False)
            self.weepinbell.setVisible(False)
            self.victreebel.setVisible(False)
            self.tentacool.setVisible(False)
            self.tentacruel.setVisible(False)
            self.geodude.setVisible(False)

            #Page 3 Content Hidden
            self.graveler.setVisible(False)
            self.golem.setVisible(False)
            self.ponyta.setVisible(False)
            self.rapidash.setVisible(False)
            self.slowpoke.setVisible(False)
            self.slowbro.setVisible(False)
            self.magnemite.setVisible(False)
            self.magneton.setVisible(False)
            self.farfetchd.setVisible(False)
            self.doduo.setVisible(False)
            self.dodrio.setVisible(False)
            self.seel.setVisible(False)
            self.dewgong.setVisible(False)
            self.grimer.setVisible(False)
            self.muk.setVisible(False)
            self.shellder.setVisible(False)
            self.cloyster.setVisible(False)
            self.gastly.setVisible(False)
            self.haunter.setVisible(False)
            self.gengar.setVisible(False)
            self.onix.setVisible(False)
            self.drowzee.setVisible(False)
            self.hypno.setVisible(False)
            self.krabby.setVisible(False)
            self.krabby.setVisible(False)
            self.kingler.setVisible(False)
            self.voltorb.setVisible(False)
            self.electrode.setVisible(False)
            self.exeggcute.setVisible(False)
            self.exeggutor.setVisible(False)
            self.cubone.setVisible(False)
            self.marowak.setVisible(False)
            self.hitmonlee.setVisible(False)
            self.hitmonchan.setVisible(False)
            self.lickitung.setVisible(False)
            self.koffing.setVisible(False)
            self.weezing.setVisible(False)

            #Page 4 Content Hidden
            self.rhyhorn.setVisible(False)
            self.rhydon.setVisible(False)
            self.chansey.setVisible(False)
            self.tangela.setVisible(False)
            self.kangaskhan.setVisible(False)
            self.horsea.setVisible(False)
            self.seadra.setVisible(False)
            self.goldeen.setVisible(False)
            self.seaking.setVisible(False)
            self.staryu.setVisible(False)
            self.starmie.setVisible(False)
            self.mrmime.setVisible(False)
            self.scyther.setVisible(False)
            self.jynx.setVisible(False)
            self.electabuzz.setVisible(False)
            self.magmar.setVisible(False)
            self.pinsir.setVisible(False)
            self.tauros.setVisible(False)
            self.magikarp.setVisible(False)
            self.gyarados.setVisible(False)
            self.lapras.setVisible(False)
            self.ditto.setVisible(False)
            self.eevee.setVisible(False)
            self.vaporeon.setVisible(False)
            self.jolteon.setVisible(False)
            self.flareon.setVisible(False)
            self.porygon.setVisible(False)
            self.omanyte.setVisible(False)
            self.omastar.setVisible(False)
            self.kabuto.setVisible(False)
            self.kabutops.setVisible(False)
            self.aerodactyl.setVisible(False)
            self.snorlax.setVisible(False)
            self.articuno.setVisible(False)
            self.zapdos.setVisible(False)
            self.moltres.setVisible(False)
            
            #Page 5 Content Visible
            self.dratini.setVisible(True)
            self.dragonair.setVisible(True)
            self.dragonite.setVisible(True)
            self.mewtwo.setVisible(True)
            self.mew.setVisible(True)
        
        elif self.page >= 6:
            self.page = 5
            


            
                 
    def next_page(self):
        self.page += 1
        self.page_handler(self.page)
    
    def prev_page(self):
        self.page -= 1
        self.page_handler(self.page)    
                                
    def on_click_P1_pkmn1(self):
        name_or_id = self.slot_pokemon_names[0]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[0] = None
            self.P1_pkmn1.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 1")
    def on_click_P1_pkmn2(self):
        name_or_id = self.slot_pokemon_names[1]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[1] = None
            self.P1_pkmn2.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 2")
    def on_click_P1_pkmn3(self):
        name_or_id = self.slot_pokemon_names[2]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[2] = None
            self.P1_pkmn3.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 3")
    def on_click_P1_pkmn4(self):
        name_or_id = self.slot_pokemon_names[3]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[3] = None
            self.P1_pkmn4.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 4")
    def on_click_P1_pkmn5(self):
        name_or_id = self.slot_pokemon_names[4]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[4] = None
            self.P1_pkmn5.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 5")
    def on_click_P1_pkmn6(self):
        name_or_id = self.slot_pokemon_names[5]
        if name_or_id:
            self.team_message.setText(f"{name_or_id.capitalize()} removed from your team")
            self.slot_pokemon_names[5] = None
            self.P1_pkmn6.setIcon(QIcon("assets/icons/pokeballicon.png"))
            self.team = [pokemon for pokemon in self.team if pokemon['name'] != name_or_id]
        else:
            self.team_message.setText("No Pokémon in slot 6")

    def add_pokemon_to_team(self, name_or_id):
        if len(self.team) >= self.MAX_TEAM_SIZE:
            self.team_message.setText("Your team is full!")
            return

        pokemon = get_pokemon_data(name_or_id)
        if pokemon:
            pokemon['hp'] = pokemon['stats'][0]['base_stat']
            pokemon['pp'] = {move['move']['name']: 10 for move in pokemon['moves']}

            self.team.append(pokemon)
            self.team_message.setText(f"{name_or_id.capitalize()} added to your team!")

            for index, slot_name in enumerate(self.slot_pokemon_names):
                if slot_name is None:
                    # Place Pokémon in the first empty slot
                    self.slot_pokemon_names[index] = name_or_id
                    self.P1_slots[index].setIcon(QIcon(f"assets/pokemon/{name_or_id}.gif"))
                    self.P1_slots[index].setIconSize(QSize(100, 100))
                    break
        else:
            self.team_message.setText("Error fetching Pokémon data.")

    def confirm_team(self):
        if len(self.team) == 0:
            QMessageBox.warning(self, "Team Incomplete", "Please select at least one Pokémon before confirming.")
            return

        self.selected_team_p1 = self.team  # Save to be fetched by get_teams()
        self.close()  # Closes the window and resumes app.exec_() in battle.py
        



def main():
    app = QApplication(sys.argv)
    window = MainWind()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
