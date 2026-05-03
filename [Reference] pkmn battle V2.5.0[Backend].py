#Changes V1.4
#switch option now implemented
#automatic opponent ai switching
#show PP
#battle win message

#Changes V1.5
#Attempting to implement pokemon stats and moves without using API
#bug fixes
#[def get_pokemon_data] - place pkmn stats
#[def get_move_data] - place pkmn moves

#Changes V1.5.1 (Jonathan)
#Added Pkmn #7 to #45
#New Moves Added on List
#Sorted Moves List based on Type
#Sorted Moves List in ascending order (based on power)

#Changes V1.5.2 (Adrian)
#Added Pkmn #46 to #69 ( ͡° ͜ʖ ͡°)
#New Moves Added on List

#Changes V1.5.3 (Bendo)
#Implemented Physical/Special split on moves and calculation
#Added STAB (Sam Type Attack Bonus)
#Added Ditto and Transfrom, including: define transform. As well as changes to define: select move, ai select move, battle, ai battle

#Changes V1.5.4 (Bendo)
#Implemented Speed priority and Turn order

#Changes V1.5.5 (Jonathan)
#Added Pkmn #70 to #85
#Adjusted power for moves with multi-hit to account for average damage rate
#Adjusted power for moves with move priority to increase value over regular moves
#Adjusted power for moves with life steal due to lack of life steal system
#New Moves Added on List

#Changes V1.5.5 (Bendo)
#bugs fixed: Fainted opponent pokemon attacks right before switching
#bugs fixed: Fainted opponent pokemon sometimes not switching out

#Changes V1.5.6 (Bendo)
#We don't talk about V1.5.6
'''
When I wrote this code, only God and I know what it did.
Now... only God knows
If you're reading this; Let this serve as a warning for future programmers.
I ask of you to increase this counter for every attempt done, working on this code.
So that they too shall know the horrors of what has transpired here.

Counter = 31
'''

#Changes V1.5.7 (Bendo)
#Summary of what changed since V1.5.5
#[Confirmed Working] - Added def choose_game_mode() 
#[Confirmed Working] - Altered def choose_team() to account for 2 Player Mode (game_mode == 1 for Single Player; game_mode == 2 for Two Player)
#[The Bane of my Existence, The Nemesis of my Soul] - Attempting to work on def battle() to account for 2 Player Mode. (game_mode == 1(All good); game_mode == 2(Problematic))

#Changes V1.5.8 (Bendo)
#2 Player Mode now confirmed working

#Changes V1.5.9 (Adrian)
#Added Pkmn #86 to #103
#New Moves Added on List (The KO mechanic after using explosion is still need to be coded)

#Changes V1.6 (Bendo)
#Makes pokemon faint after using explosion
#Gave Golem the move "Explosion"

#Changes V1.6.1 (Jonathan)
#[Confirmed Working] Recoil Damage System
#[Confirmed Working] Attack HP Drain System
#[Added] recoil multipliers - recoil_low for x0.25 and recoil_high for x0.33
#[Added] hp_drain multiplier x0.25 (due to HP cap lack of hp cap)
#[Added] Recoil related moves to recoil self-damage manager
#[Added] HP drain moves to hp drain manager
#[Changed] Power of Moves related to recoil and HP drain reverted back to original values

#Changes V1.6.2 (Bendo)
#Added missing recoil and drain moves into the list
#Gave those moves to some pokemons

#Changes V1.6.3 (Bendo)
#Added stat increase variables for every stat
#Added Dragonite line
#Added dragon type moves and Stat related moves
#Implemented real time stat changes during battle

#Changes V1.6.4 (Adrian and Gab)
#Replaced the hp value by their level 100 values (minimum)

#Changes V2.0.0 (Bendo)
#Implemented Items for both single player and two player modes
#Modified battle logic to account for items
#[Bug fixed] opponent cannot attack the turn the player switches
#[Bug fixed] game crash when both player switches pokemon at the same turn

#Changes V2.0.1 (Jonathan)
#Implemented Max HP limiter on HP Drain induced HP Recovery
#hp_drain multiplier increased from x0.25 to x0.50 as part of Max HP limiter update

#Changes V2.1.1 (Bendo)
#[Bug fixed] stat increase based on the current stats and not on the original stats
#Added growth and iron defense

#Changes V2.2.1 (Bendo)
#Added multi-hit attacks
#Added new status moves
#Added Pkmn #104 to #107

#Changes V2.3.1 (Bendo)
#Non-reliance on API update

#Changes V2.4.6 (Bendo)
#[Bug fixed] The player still being able to attack after using an item in Two Player mode
#[Bug fixed] The opponent not switching pokemons after it has been KO'd by a move that alters stats (Ex: Close Combat and Draco Meteor)
#[Bug fixed] A pokemon continues to beat up the opponent even if it has already fainted if it has still a number of hits left in a multi-hit move
#[Bug fixed] Pokemon still doing one last attack after it has fainted
#Added a 1 second pause after using each move for readability
#Added the option to play again
#Changes V2.4.7
#Removed "continue" next to status moves in battle

#Changes 2.4.8 (Noice) ᘛ⁐̤ᕐᐷ
#Added Pkmn #108 to #121

#Changes 2.4.9 (Noice) ᘛ⁐̤ᕐᐷ
#Added Pkmn #122 to #151
##New Moves Added on List

#Changes V2.4.6 (Bendo)
#[Bug fixed] fixed the game if keeps looping the prompt of asking you to play again by adding restart_game
#[Bug fixed] pokemon still attacking after it has fainted
#Corrected Moltres's name

import random
import os
import time


GEN1_POKEMON_COUNT = 151

STATUS_NONE = 'None'
STATUS_POISON = 'Poison'
STATUS_BURN = 'Burn'
game_mode = None

def get_pokemon_data(name_or_id):
    # Hardcoded Pokémon data (name, types(HP, ATK, DEF, SpATK,SpDEF, SPD. in order ), stats, moves)
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
            'moves': [{'move': {'name': 'poison-sting'}}, {'move': {'name': 'bug-bite'}},  {'move': {'name': 'fury-cutter'}}, {'move': {'name': 'venoshock'}}],
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
            'name': 'nidoran♀',
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
            'name': 'nidoran♂',
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
            'moves': [{'move': {'name': 'slash'}}, {'move': {'name': 'bite'}}, {'move': {'name': 'pay-day'}}, {'move': {'name': 'swift'}}],
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
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'tri-attack'}}, {'move': {'name': 'hyper-beam'}}],
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
            'name': 'grimmer',
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
            'name': 'mr. mime',
            'types': [{'type': {'name': 'psychic'}}, {'type': {'name': 'fairy'}}],
            'stats': [{'base_stat': 190}, {'base_stat': 45}, {'base_stat': 65}, {'base_stat': 100}, {'base_stat': 120}, {'base_stat': 90}],
            'moves': [{'move': {'name': 'psychic'}}, {'move': {'name': 'psybeam'}}, {'move': {'name': 'thunder'}}, {'move': {'name': 'dream-eater'}}],
        },
        123: {
            'name': 'scyther',
            'types': [{'type': {'name': 'bug'}}, {'type': {'name': 'flying'}}],
            'stats': [{'base_stat': 250}, {'base_stat': 110}, {'base_stat': 80}, {'base_stat': 55}, {'base_stat': 80}, {'base_stat': 105}],
            'moves': [{'move': {'name': 'quick-attack'}}, {'move': {'name': 'fury-cutter'}}, {'move': {'name': 'agility'}}, {'move': {'name': 'take-down'}}],
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
            'moves': [{'move': {'name': 'ice-fang'}}, {'move': {'name': 'blizzard'}}, {'move': {'name': 'hydro-pump'}}, {'move': {'name': 'hyper-beam'}}],
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
            'moves': [{'move': {'name': 'transform'}}],
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
            'moves': [{'move': {'name': 'transform'}}, {'move': {'name': 'psychic'}}, {'move': {'name': 'fire-blast'}}, {'move': {'name': 'zap-cannon'}}],
        },


        # Add more Pokémon as needed until 151...
    }
    
    # Return the Pokémon data for the given ID, or None if not found
    return pokemon_data.get(name_or_id, None)


def get_move_data(move_name):
    # Hardcoded move data with move details (power, type, category)
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
        'hyper-beam': {'power': 150, 'type': 'normal', 'category': 'special'},
        'explosion': {'power': 170, 'type': 'normal', 'category': 'physical'},

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
        'dragon-dance': {'power': -100, 'type': 'dragon', 'category': 'physical'},
        'growth': {'power': -100, 'type': 'normal', 'category': 'physical'},
        'iron-defense': {'power': -100, 'type': 'steel', 'category': 'physical'},
        'belly-drum': {'power': -100, 'type': 'normal', 'category': 'physical'},
    }

    # Return the data for the move, or None if the move is not found
    return move_data.get(move_name, None)




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

def get_type_effectiveness(attacking_type, defending_type):
    return TYPE_EFFECTIVENESS.get(attacking_type, {}).get(defending_type, 1.0)

def display_pokemon_list():
    print("\nLoading Pokémon list... (This may take a while)")
    for i in range(1, GEN1_POKEMON_COUNT + 1):
        pokemon = get_pokemon_data(i)
        if pokemon:
            print(f"{i}. {pokemon['name'].capitalize()}")

def choose_team():
    team = []
    team_p1 = []
    team_p2 = []
    display_pokemon_list()
    # Game Mode 1: Player vs. PC
    if game_mode == 1:
        while len(team) < 6:
            choice = input(f"Choose Pokémon {len(team) + 1} (or type 'done' to finish): ").lower()
            if choice == 'done' and team:
                break
            try:
                poke_id = int(choice)
                if 1 <= poke_id <= GEN1_POKEMON_COUNT:
                    pokemon = get_pokemon_data(poke_id)
                    if pokemon:
                        pokemon['hp'] = pokemon['stats'][0]['base_stat']
                        pokemon['pp'] = {move['move']['name']: 10 for move in pokemon['moves']}
                        pokemon['status'] = STATUS_NONE
                        team.append(pokemon)
                        print(f"{pokemon['name'].capitalize()} added to your team!")
                    else:
                        print("Error fetching Pokémon data. Try again.")
                else:
                    print("Invalid Pokémon ID.")
            except ValueError:
                print("Invalid input.")
        return team

    # Game Mode 2: Player 1 vs. Player 2
    elif game_mode == 2:
        print("Player 1, choose your team:")
        while len(team_p1) < 6:
            choice = input(f"\nPlayer 1, choose Pokémon {len(team_p1) + 1} (or type 'done' to finish): ").lower()
            if choice == 'done' and team_p1:
                break
            try:
                poke_id = int(choice)
                if 1 <= poke_id <= GEN1_POKEMON_COUNT:
                    pokemon = get_pokemon_data(poke_id)
                    if pokemon:
                        pokemon['hp'] = pokemon['stats'][0]['base_stat']
                        pokemon['pp'] = {move['move']['name']: 10 for move in pokemon['moves']}
                        pokemon['status'] = STATUS_NONE
                        team_p1.append(pokemon)
                        print(f"{pokemon['name'].capitalize()} added to Player 1's team!")
                    else:
                        print("Error fetching Pokémon data. Try again.")
                else:
                    print("Invalid Pokémon ID.")
            except ValueError:
                print("Invalid input.")

        print("\n\nPlayer 2, choose your team:")
        while len(team_p2) < 6:
            choice = input(f"\nPlayer 2, choose Pokémon {len(team_p2) + 1} (or type 'done' to finish): ").lower()
            if choice == 'done' and team_p2:
                break
            try:
                poke_id = int(choice)
                if 1 <= poke_id <= GEN1_POKEMON_COUNT:
                    pokemon = get_pokemon_data(poke_id)
                    if pokemon:
                        pokemon['hp'] = pokemon['stats'][0]['base_stat']
                        pokemon['pp'] = {move['move']['name']: 10 for move in pokemon['moves']}
                        pokemon['status'] = STATUS_NONE
                        team_p2.append(pokemon)
                        print(f"{pokemon['name'].capitalize()} added to Player 2's team!")
                    else:
                        print("Error fetching Pokémon data. Try again.")
                else:
                    print("Invalid Pokémon ID.")
            except ValueError:
                print("Invalid input.")
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
    # Copy stats (except HP)
    for i in range(1, len(user_pokemon['stats'])):
        user_pokemon['stats'][i]['base_stat'] = target_pokemon['stats'][i]['base_stat']

    # Copy types
    user_pokemon['types'] = target_pokemon['types']

    # Copy moves (with default PP)
    user_pokemon['moves'] = target_pokemon['moves']
    user_pokemon['pp'] = {move['move']['name']: 5 for move in user_pokemon['moves']}  # Transform grants 5 PP each


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
    return max(1, int(damage))


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


def battle(player_team, opponent_team, team_p1, team_p2):

    #2 Player Mode
    if game_mode == 2:
        player1_team = team_p1
        player2_team = team_p2
        player1_pokemon = team_p1[0]
        player2_pokemon = team_p2[0]
        skip_turn_p1 = False
        skip_turn_p2 = False

        
        print(f"\nBattle Start! Player 1's {player1_pokemon['name'].capitalize()} vs Player 2's {player2_pokemon['name'].capitalize()}!")
        
        inventory_p1 = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 2}
        inventory_p2 = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 2}
        
        while True:
            clear_screen()
            print(f"\nPlayer 1: {player1_pokemon['name'].capitalize()} (HP: {max(0, player1_pokemon['hp'])})")
            print(f"Player 2: {player2_pokemon['name'].capitalize()} (HP: {max(0, player2_pokemon['hp'])})")
            item_used_p1 = False
            item_used_p2 = False
            switch_p1 = False
            switch_p2 = False
            
            # Player 1's turn
            print("\nPlayer 1's Turn")
            action1 = input("\nWhat will you do?\n1. Attack\n2. Switch Pokémon\n3. Use Item\nChoose an action: ")
            
            if action1 == "1":
                move1 = select_move(player1_pokemon, player2_pokemon)
            elif action1 == "2":
                switch_p1 = True
                player1_pokemon = switch_pokemon(player1_team)
                print(f"You sent out {player1_pokemon['name'].capitalize()}!")
                time.sleep(1)

            elif action1 == "3":
                item_p1 = input(f"\n1. X Attack ({inventory_p1['1']} Left)\n2. X Defend ({inventory_p1['2']} Left)\n3. X Special ({inventory_p1['3']} Left)\n4. X Sp. Def ({inventory_p1['4']} Left)\n5. X Speed ({inventory_p1['5']} Left)\n6. Hyper Potion ({inventory_p1['6']} Left)\nChoose an item: ")
                item_used_p1 = True
                
                # Check if the item is available
                if inventory_p1.get(item_p1, 0) == 0:
                    print("You have already used this item!")
                    continue

                if item_p1 == "1":
                    player1_pokemon['stats'][1]['base_stat'] += attack_increase*2
                    print(f"You used X Attack, {player1_pokemon['name'].capitalize()}'s Attack sharply rose!")

                elif item_p1 == "2":
                    player1_pokemon['stats'][2]['base_stat'] += defense_increase*2
                    print(f"You used X Defend, {player1_pokemon['name'].capitalize()}'s Defense sharply rose!")

                elif item_p1 == "3":
                    player1_pokemon['stats'][3]['base_stat'] += sp_attack_increase*2
                    print(f"You used X Special, {player1_pokemon['name'].capitalize()}'s Sp. Attack sharply rose!")

                elif item_p1 == "4":
                    player1_pokemon['stats'][4]['base_stat'] += sp_defense_increase*2
                    print(f"You used X Sp. Def, {player1_pokemon['name'].capitalize()}'s Sp. Defense sharply rose!")

                elif item_p1 == "5":
                    player1_pokemon['stats'][5]['base_stat'] += speed_increase*2
                    print(f"You used X Speed, {player1_pokemon['name'].capitalize()}'s Speed sharply rose!")

                elif item_p1 == "6":
                    max_hp_p1 = player1_pokemon['stats'][0]['base_stat']
                    player1_pokemon['hp'] = min(max_hp_p1, player1_pokemon['hp'] + 200)
                    print(f"You used Hyper Potion, {player1_pokemon['name'].capitalize()} regained 200 HP")

                else:
                    print("Invalid item!")
                    continue

                # Mark item as used
                inventory_p1[item_p1] -= 1
                skip_turn_p1 = True

            else:
                print("Invalid choice.")
                time.sleep(1)
                continue
            
            # Player 2's turn
            print("\nPlayer 2's Turn")
            action2 = input("\nWhat will you do?\n1. Attack\n2. Switch Pokémon\n3. Use Item\nChoose an action: ")
            
            if action2 == "1":
                move2 = select_move(player2_pokemon, player1_pokemon)
            elif action2 == "2":
                switch_p2 = True
                player2_pokemon = switch_pokemon(player2_team)
                print(f"You sent out {player2_pokemon['name'].capitalize()}!")
                time.sleep(1)

            elif action2 == "3":
                
                item_p2 = input(f"\n1. X Attack ({inventory_p2['1']} Left)\n2. X Defend ({inventory_p2['2']} Left)\n3. X Special ({inventory_p2['3']} Left)\n4. X Sp. Def ({inventory_p2['4']} Left)\n5. X Speed ({inventory_p2['5']} Left)\n6. Hyper Potion ({inventory_p2['6']} Left)\nChoose an item: ")
                item_used_p2 = True
                
                # Check if the item is available
                if inventory_p2.get(item_p2, 0) == 0:
                    print("You have already used this item!")
                    continue

                if item_p2 == "1":
                    player2_pokemon['stats'][1]['base_stat'] += attack_increase*2
                    print(f"You used X Attack, {player2_pokemon['name'].capitalize()}'s Attack sharply rose!")

                elif item_p2 == "2":
                    player2_pokemon['stats'][2]['base_stat'] += defense_increase*2
                    print(f"You used X Defend, {player2_pokemon['name'].capitalize()}'s Defense sharply rose!")

                elif item_p2 == "3":
                    player2_pokemon['stats'][3]['base_stat'] += sp_attack_increase*2
                    print(f"You used X Special, {player2_pokemon['name'].capitalize()}'s Sp. Attack sharply rose!")

                elif item_p2 == "4":
                    player2_pokemon['stats'][4]['base_stat'] += sp_defense_increase*2
                    print(f"You used X Sp. Def, {player2_pokemon['name'].capitalize()}'s Sp. Defense sharply rose!")

                elif item_p2 == "5":
                    player2_pokemon['stats'][5]['base_stat'] += speed_increase*2
                    print(f"You used X Speed, {player2_pokemon['name'].capitalize()}'s Speed sharply rose!")

                elif item_p2 == "6":
                    max_hp = player2_pokemon['stats'][0]['base_stat']
                    player2_pokemon['hp'] = min(max_hp, player2_pokemon['hp'] + 200)
                    print(f"You used Hyper Potion, {player2_pokemon['name'].capitalize()} regained 200 HP")

                else:
                    print("Invalid item!")
                    continue

                # Mark item as used
                inventory_p2[item_p2] -= 1
                skip_turn_p2 = True

            else:
                print("Invalid choice.")
                time.sleep(1)
                continue
            
            # If both players used an item, skip attacks
            if item_used_p1 and item_used_p2:
                continue
            
            if switch_p1 and switch_p2:
                continue
            
            player1_speed = player1_pokemon['stats'][5]['base_stat']
            player2_speed = player2_pokemon['stats'][5]['base_stat']

            # Determine turn order based on speed
            turn_order = [(player1_pokemon, player2_pokemon, move1), (player2_pokemon, player1_pokemon, move2)]
            if player2_speed > player1_speed:
                turn_order.reverse()

            for attacker, defender, chosen_move in turn_order:
                if attacker['hp'] == 0:
                    continue
                if defender['hp'] == 0:
                    print(f"{defender['name'].capitalize()} fainted!")
                    time.sleep(1)
                        
                    # Force opponent to switch Pokémon immediately
                    if defender == player2_pokemon:
                        player2_team.remove(player2_pokemon)
                        if not player2_team:
                            print("\nAll of the Player 2's Pokémon have fainted! Player 1 Wins!")
                            return
                            player2_pokemon = switch_pokemon(player2_team)
                        print(f"Player 2 sent out {player2_pokemon['name'].capitalize()}!")
                        time.sleep(1)
                        break
                        
                    # Force player to switch Pokémon if fainted
                    if defender == player1_pokemon:
                        player1_team.remove(player1_pokemon)
                        if not player1_team:
                            print("\nAll your Player 1's Pokémon have fainted... Player 2 Wins!")
                            return
                        player1_pokemon = switch_pokemon(player1_team)
                        print(f"You sent out {player1_pokemon['name'].capitalize()}!")
                        time.sleep(1)
                        break
                
                hits = (
                    random.randint(2, 5) if chosen_move in ['fury-attack', 'bullet-seed', 'rock-blast', 'pin-missile', 'bone-rush']
                    else 2 if chosen_move in ['double-kick', 'double-hit', 'bonemerang', 'twineedle']
                    else 1
                )

                for _ in range(hits):
                    time.sleep(1)
                    if defender['hp'] > 0 and chosen_move:
                        if attacker == player1_pokemon and skip_turn_p1 == True and skip_turn_p2 == False:
                            skip_turn_p1 = False
                            time.sleep(1)
                            break
                        elif attacker == player2_pokemon and skip_turn_p1 == False and skip_turn_p2 == True:
                            skip_turn_p2 = False
                            time.sleep(1)
                            break
                        damage = calculate_damage(attacker, defender, chosen_move)
                        max_hp = attacker['stats'][0]['base_stat']
                        recoil_low = (damage)*0.25
                        recoil_high = (damage)*0.33
                        hp_drain = (damage)*0.5
                            
                        # Stat increase variables
                        if 'original_stats' not in player1_pokemon:
                            player1_pokemon['original_stats'] = {i: stat['base_stat'] for i, stat in enumerate(player1_pokemon['stats'])}

                        if 'original_stats' not in player2_pokemon:
                            player2_pokemon['original_stats'] = {i: stat['base_stat'] for i, stat in enumerate(player2_pokemon['stats'])}

                        attack_increase = int(attacker['original_stats'][1] * 0.5)
                        defense_increase = int(attacker['original_stats'][2] * 0.5)
                        sp_attack_increase = int(attacker['original_stats'][3] * 0.5)
                        sp_defense_increase = int(attacker['original_stats'][4] * 0.5)
                        speed_increase = int(attacker['original_stats'][5] * 0.5)
                            
                        defender['hp'] = max(0, defender['hp'] - damage)
                        print(f"{attacker['name'].capitalize()} used {chosen_move.capitalize()}! It dealt {damage} damage.")
                            
                        if chosen_move == 'explosion': attacker['hp'] = 0; print(f"{attacker['name'].capitalize()} has exploded and faints!"); time.sleep(1)
                            
                        #Recoil self-damage manager
                        if chosen_move == 'take-down': attacker['hp'] = max(0, int(attacker['hp'] - recoil_low)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_low) + "recoil damage!"); time.sleep(1)
                        if chosen_move == 'double-edge': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                        if chosen_move == 'brave-bird': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                        if chosen_move == 'flare-blitz': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                        if chosen_move == 'volt-tackle': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                        
                        #HP Drain Manager
                        if chosen_move == 'leech-life': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                        if chosen_move == 'absorb': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                        if chosen_move == 'mega-drain': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                        if chosen_move == 'giga-drain': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                            
                        #Stat Increase manager
                        if chosen_move == 'agility': attacker['stats'][5]['base_stat'] += (speed_increase*2); print(f"{attacker['name'].capitalize()}'s speed sharply rose by " + str(speed_increase*2)); time.sleep(1);
                        if chosen_move == 'dragon-dance': attacker['stats'][1]['base_stat'] += attack_increase; print(f"{attacker['name'].capitalize()}'s attack rose by " + str(attack_increase)); time.sleep(1);
                        if chosen_move == 'dragon-dance': attacker['stats'][5]['base_stat'] += speed_increase; print(f"{attacker['name'].capitalize()}'s speed rose by " + str(speed_increase)); time.sleep(1);
                        if chosen_move == 'draco-meteor': attacker['stats'][3]['base_stat'] -= (attacker['stats'][3]['base_stat']*0.66); print(f"{attacker['name'].capitalize()}'s special attack harshly fell by " + str(attacker['stats'][3]['base_stat']*0.66)); time.sleep(1);
                        if chosen_move == 'growth': attacker['stats'][1]['base_stat'] += attack_increase; print(f"{attacker['name'].capitalize()}'s attack rose by " + str(attack_increase)); time.sleep(1);
                        if chosen_move == 'growth': attacker['stats'][3]['base_stat'] += sp_attack_increase; print(f"{attacker['name'].capitalize()}'s special attack rose by " + str(sp_attack_increase)); time.sleep(1);
                        if chosen_move == 'iron-defense': attacker['stats'][2]['base_stat'] += (defense_increase*2); print(f"{attacker['name'].capitalize()}'s defense sharply rose by " + str(defense_increase*2)); time.sleep(1);
                        if chosen_move == 'belly-drum': attacker['hp'] = max(1, attacker['hp'] // 2); attacker['stats'][1]['base_stat'] += (attack_increase*6); print(f"{attacker['name'].capitalize()} cut its own HP by half and massively increased its attack by " + str(attack_increase*6)); time.sleep(1);
                        if chosen_move == 'close-combat': attacker['stats'][2]['base_stat'] -= defense_increase; print(f"{attacker['name'].capitalize()}'s defense fell by " + str(attack_increase)); time.sleep(1);
                        if chosen_move == 'close-combat': attacker['stats'][4]['base_stat'] -= sp_defense_increase; print(f"{attacker['name'].capitalize()}'s special defense fell by " + str(speed_increase)); time.sleep(1);
                        
                        if defender['hp'] == 0:
                            print(f"{defender['name'].capitalize()} fainted!")
                            time.sleep(1)

                        # Handle player Pokémon fainting
                        if player1_pokemon['hp'] == 0:
                            player1_team.remove(player1_pokemon)
                            if not player1_team:
                                print("\nAll of Player 1's Pokémon have fainted! Player 2 Wins!")
                                while True:
                                    play_again = input("\nDo you want to play again? (y/n): ").lower()
                                    if play_again == 'y':
                                        print("\nRestarting game...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        time.sleep(1)
                                        clear_screen()
                                        choose_game_mode()
                                    elif play_again == 'n':
                                        print("Thanks for playing!")
                                        end_game()
                                    else:
                                        print("Invalid input. Please enter 'y' or 'n'.")
                            player1_pokemon = switch_pokemon(player1_team)
                            print(f"Player 1 sent out {player1_pokemon['name'].capitalize()}!")
                            time.sleep(1)

                        # Handle opponent Pokémon fainting
                        if player2_pokemon['hp'] == 0:
                            player2_team.remove(player2_pokemon)
                            if not player2_team:
                                print("\nAll of Player 2's Pokémon have fainted! Player 1 Wins!")
                                while True:
                                    play_again = input("\nDo you want to play again? (y/n): ").lower()
                                    if play_again == 'y':
                                        print("\nRestarting game...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        time.sleep(1)
                                        clear_screen()
                                        choose_game_mode()
                                    elif play_again == 'n':
                                        print("Thanks for playing! Goodbye.")
                                        end_game()
                                    else:
                                        print("Invalid input. Please enter 'y' or 'n'.")
                            player2_pokemon = switch_pokemon(player2_team)
                            print(f"Player 2 sent out {player2_pokemon['name'].capitalize()}!")
                            time.sleep(1)
            
    #1 Player Mode
    if game_mode == 1:
        player_pokemon = player_team[0]
        opponent_pokemon = opponent_team[0]

        print(f"\nBattle Start! {player_pokemon['name'].capitalize()} vs {opponent_pokemon['name'].capitalize()}!")
        
        inventory = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 2}
        
        while True:
            clear_screen()
            print(f"\n{player_pokemon['name'].capitalize()} (HP: {max(0, player_pokemon['hp'])}) vs {opponent_pokemon['name'].capitalize()} (HP: {max(0, opponent_pokemon['hp'])})")

            action = input("\nWhat will you do?\n1. Attack\n2. Switch Pokémon\n3. Use Item\nChoose an action: ")

            if action == "1":
                move = select_move(player_pokemon, opponent_pokemon)
                ai_move = ai_select_move(opponent_pokemon, player_pokemon)

                player_speed = player_pokemon['stats'][5]['base_stat']
                opponent_speed = opponent_pokemon['stats'][5]['base_stat']

                # Determine turn order based on speed
                turn_order = [(player_pokemon, opponent_pokemon, move), (opponent_pokemon, player_pokemon, ai_move)]
                if opponent_speed > player_speed:
                    turn_order.reverse()

                for attacker, defender, chosen_move in turn_order:
                    if attacker['hp'] == 0:
                        continue
                    
                    if defender['hp'] == 0:
                        print(f"{defender['name'].capitalize()} fainted!")
                        time.sleep(1)

                        if defender == opponent_pokemon:
                            opponent_team.remove(opponent_pokemon)
                            if not opponent_team:
                                print("\nAll of the opponent's Pokémon have fainted! You Win!")
                                return
                            opponent_pokemon = ai_switch_pokemon(opponent_team)
                            print(f"Opponent sent out {opponent_pokemon['name'].capitalize()}!")
                            time.sleep(1)
                            break

                        if defender == player_pokemon:
                            player_team.remove(player_pokemon)
                            if not player_team:
                                print("\nAll your Pokémon have fainted... You Lose!")
                                return
                            player_pokemon = switch_pokemon(player_team)
                            print(f"You sent out {player_pokemon['name'].capitalize()}!")
                            time.sleep(1)
                            break
                    
                    if defender['hp'] > 0 and chosen_move:
                        hits = (
                            random.randint(2, 5) if chosen_move in ['fury-attack', 'bullet-seed', 'rock-blast', 'pin-missile', 'bone-rush']
                            else 2 if chosen_move in ['double-kick', 'double-hit', 'bonemerang', 'twineedle']
                            else 1
                        )

                        for _ in range(hits):
                            time.sleep(1)
                            damage = calculate_damage(attacker, defender, chosen_move)
                            max_hp = attacker['stats'][0]['base_stat']
                            recoil_low = (damage)*0.25
                            recoil_high = (damage)*0.33
                            hp_drain = (damage)*0.5
                            
                            if defender['hp'] == 0:
                                print(f"{defender['name'].capitalize()} fainted!")
                                time.sleep(1)

                                # Handle player Pokémon fainting
                                if defender == player_pokemon:
                                    player_team.remove(player_pokemon)
                                    if not player_team:
                                        print("\nAll your Pokémon have fainted... You Lose!")
                                        end_game()
                                    player_pokemon = switch_pokemon(player_team)
                                    print(f"You sent out {player_pokemon['name'].capitalize()}!")
                                    time.sleep(1)
                                # Handle opponent Pokémon fainting
                                elif defender == opponent_pokemon:
                                    opponent_team.remove(opponent_pokemon)
                                    if not opponent_team:
                                        print("\nAll of the opponent's Pokémon have fainted! You Win!")
                                        end_game()
                                    opponent_pokemon = ai_switch_pokemon(opponent_team)
                                    print(f"Opponent sent out {opponent_pokemon['name'].capitalize()}!")
                                    time.sleep(1)

                                # Stop multi-hit attack if opponent faints
                                break
                            
                            # Stat increase variables
                            if 'original_stats' not in player_pokemon:
                                player_pokemon['original_stats'] = {i: stat['base_stat'] for i, stat in enumerate(player_pokemon['stats'])}

                            if 'original_stats' not in opponent_pokemon:
                                opponent_pokemon['original_stats'] = {i: stat['base_stat'] for i, stat in enumerate(opponent_pokemon['stats'])}

                            attack_increase = int(attacker['original_stats'][1] * 0.5)
                            defense_increase = int(attacker['original_stats'][2] * 0.5)
                            sp_attack_increase = int(attacker['original_stats'][3] * 0.5)
                            sp_defense_increase = int(attacker['original_stats'][4] * 0.5)
                            speed_increase = int(attacker['original_stats'][5] * 0.5)
                            
                            defender['hp'] = max(0, defender['hp'] - damage)
                            print(f"{attacker['name'].capitalize()} used {chosen_move.capitalize()}! It dealt {damage} damage.")
                            
                            if chosen_move == 'explosion': attacker['hp'] = 0; print(f"{attacker['name'].capitalize()} has exploded and faints!"); time.sleep(1)
                            
                            #Recoil self-damage manager
                            if chosen_move == 'take-down': attacker['hp'] = max(0, int(attacker['hp'] - recoil_low)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_low) + "recoil damage!"); time.sleep(1)
                            if chosen_move == 'double-edge': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                            if chosen_move == 'brave-bird': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                            if chosen_move == 'flare-blitz': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                            if chosen_move == 'volt-tackle': attacker['hp'] = max(0, int(attacker['hp'] - recoil_high)); print(f"{attacker['name'].capitalize()} has received " + str(recoil_high) + "recoil damage!"); time.sleep(1)
                        
                            #HP Drain Manager
                            if chosen_move == 'leech-life': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                            if chosen_move == 'absorb': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                            if chosen_move == 'mega-drain': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                            if chosen_move == 'giga-drain': attacker['hp'] = min(max_hp, int(attacker['hp'] + hp_drain)); print(f"{attacker['name'].capitalize()} has recovered " + str(hp_drain) + " hp!"); time.sleep(1)
                            
                            #Stat Increase manager
                            if chosen_move == 'agility': attacker['stats'][5]['base_stat'] += (speed_increase*2); print(f"{attacker['name'].capitalize()}'s speed sharply rose by " + str(speed_increase*2)); time.sleep(1);
                            if chosen_move == 'dragon-dance': attacker['stats'][1]['base_stat'] += attack_increase; print(f"{attacker['name'].capitalize()}'s attack rose by " + str(attack_increase)); time.sleep(1);
                            if chosen_move == 'dragon-dance': attacker['stats'][5]['base_stat'] += speed_increase; print(f"{attacker['name'].capitalize()}'s speed rose by " + str(speed_increase)); time.sleep(1);
                            if chosen_move == 'draco-meteor': attacker['stats'][3]['base_stat'] -= (attacker['stats'][3]['base_stat']*0.66); print(f"{attacker['name'].capitalize()}'s special attack harshly fell by " + str(attacker['stats'][3]['base_stat']*0.66)); time.sleep(1);
                            if chosen_move == 'growth': attacker['stats'][1]['base_stat'] += attack_increase; print(f"{attacker['name'].capitalize()}'s attack rose by " + str(attack_increase)); time.sleep(1);
                            if chosen_move == 'growth': attacker['stats'][3]['base_stat'] += sp_attack_increase; print(f"{attacker['name'].capitalize()}'s special attack rose by " + str(sp_attack_increase)); time.sleep(1);
                            if chosen_move == 'iron-defense': attacker['stats'][2]['base_stat'] += (defense_increase*2); print(f"{attacker['name'].capitalize()}'s defense sharply rose by " + str(defense_increase*2)); time.sleep(1);
                            if chosen_move == 'belly-drum': attacker['hp'] = max(1, attacker['hp'] // 2); attacker['stats'][1]['base_stat'] += (attack_increase*6); print(f"{attacker['name'].capitalize()} cut its own HP by half and massively increased its attack by " + str(attack_increase*6)); time.sleep(1);
                            if chosen_move == 'close-combat': attacker['stats'][2]['base_stat'] -= defense_increase; print(f"{attacker['name'].capitalize()}'s defense fell by " + str(attack_increase)); time.sleep(1);
                            if chosen_move == 'close-combat': attacker['stats'][4]['base_stat'] -= sp_defense_increase; print(f"{attacker['name'].capitalize()}'s special defense fell by " + str(speed_increase)); time.sleep(1);
                            
                            if defender['hp'] == 0:
                                print(f"{defender['name'].capitalize()} fainted!")
                                time.sleep(1)

                            # Handle player Pokémon fainting
                            if player_pokemon['hp'] == 0:
                                player_team.remove(player_pokemon)
                                if not player_team:
                                    print("\nAll your Pokémon have fainted... You Lose!")
                                    while True:
                                        play_again = input("\nDo you want to play again? (y/n): ").lower()
                                        if play_again == 'y':
                                            print("\nRestarting game...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                            time.sleep(1)
                                            clear_screen()
                                            choose_game_mode()
                                        elif play_again == 'n':
                                            print("Thanks for playing! Goodbye.")
                                            break
                                        else:
                                            print("Invalid input. Please enter 'y' or 'n'.")
                                player_pokemon = switch_pokemon(player_team)
                                print(f"You sent out {player_pokemon['name'].capitalize()}!")
                                time.sleep(1)

                            # Handle opponent Pokémon fainting
                            if opponent_pokemon['hp'] == 0:
                                opponent_team.remove(opponent_pokemon)
                                if not opponent_team:
                                    print("\nAll of the opponent's Pokémon have fainted! You Win!")
                                    while True:
                                        play_again = input("\nDo you want to play again? (y/n): ").lower()
                                        if play_again == 'y':
                                            print("\nRestarting game...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                            time.sleep(1)
                                            clear_screen()
                                            choose_game_mode()
                                        elif play_again == 'n':
                                            print("Thanks for playing!")
                                            end_game()
                                        else:
                                            print("Invalid input. Please enter 'y' or 'n'.")
                                opponent_pokemon = ai_switch_pokemon(opponent_team)
                                print(f"Opponent sent out {opponent_pokemon['name'].capitalize()}!")
                                time.sleep(1)


            elif action == "2":
                player_pokemon = switch_pokemon(player_team)
                print(f"You sent out {player_pokemon['name'].capitalize()}!")
                # AI selects a move after the player switches
                ai_move = ai_select_move(opponent_pokemon, player_pokemon)

                if opponent_pokemon['hp'] > 0 and ai_move:
                    damage = calculate_damage(opponent_pokemon, player_pokemon, ai_move)
                    player_pokemon['hp'] = max(0, player_pokemon['hp'] - damage)
                    print(f"{opponent_pokemon['name'].capitalize()} used {ai_move.capitalize()}! It dealt {damage} damage.")
                    time.sleep(1)

                    # Check if the player's Pokémon faints
                    if player_pokemon['hp'] == 0:
                        print(f"{player_pokemon['name'].capitalize()} fainted!")
                        time.sleep(1)
                        player_team.remove(player_pokemon)
                        if not player_team:
                            print("\nAll your Pokémon have fainted... You Lose!")
                            while True:
                                play_again = input("\nDo you want to play again? (y/n): ").lower()
                                if play_again == 'y':
                                    print("\nRestarting game...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                    time.sleep(1)
                                    clear_screen()
                                    choose_game_mode()
                                elif play_again == 'n':
                                    print("Thanks for playing!")
                                    end_game()
                                else:
                                    print("Invalid input. Please enter 'y' or 'n'.")
                        player_pokemon = switch_pokemon(player_team)
                        print(f"You sent out {player_pokemon['name'].capitalize()}!")
                        time.sleep(1)
                

            elif action == "3":
                attack_increase = min(50, int(player_pokemon['stats'][1]['base_stat'] * 0.5))
                defense_increase = min(50, int(player_pokemon['stats'][2]['base_stat'] * 0.5))
                sp_attack_increase = min(50, int(player_pokemon['stats'][3]['base_stat'] * 0.5))
                sp_defense_increase = min(50, int(player_pokemon['stats'][4]['base_stat'] * 0.5))
                speed_increase = min(50, int(player_pokemon['stats'][5]['base_stat'] * 0.5))
                
                item = input(f"\n1. X Attack ({inventory['1']} Left)\n2. X Defend ({inventory['2']} Left)\n3. X Special ({inventory['3']} Left)\n4. X Sp. Def ({inventory['4']} Left)\n5. X Speed ({inventory['5']} Left)\n6. Hyper Potion ({inventory['6']} Left)\nChoose an item: ")
    
                # Check if the item is available
                if inventory.get(item, 0) == 0:
                    print("You have already used this item!")
                    continue

                if item == "1":
                    player_pokemon['stats'][1]['base_stat'] += attack_increase*2
                    print(f"You used X Attack, {player_pokemon['name'].capitalize()}'s Attack sharply rose!")

                elif item == "2":
                    player_pokemon['stats'][2]['base_stat'] += defense_increase*2
                    print(f"You used X Defend, {player_pokemon['name'].capitalize()}'s Defense sharply rose!")

                elif item == "3":
                    player_pokemon['stats'][3]['base_stat'] += sp_attack_increase*2
                    print(f"You used X Special, {player_pokemon['name'].capitalize()}'s Sp. Attack sharply rose! {attack_increase*2}")

                elif item == "4":
                    player_pokemon['stats'][4]['base_stat'] += sp_defense_increase*2
                    print(f"You used X Sp. Def, {player_pokemon['name'].capitalize()}'s Sp. Defense sharply rose!")

                elif item == "5":
                    player_pokemon['stats'][5]['base_stat'] += speed_increase*2
                    print(f"You used X Speed, {player_pokemon['name'].capitalize()}'s Speed sharply rose!")

                elif item == "6":
                    max_hp = player_pokemon['stats'][0]['base_stat']
                    player_pokemon['hp'] = min(max_hp, player_pokemon['hp'] + 200)
                    print(f"You used Hyper Potion, {player_pokemon['name'].capitalize()} regained 200 HP")

                else:
                    print("Invalid item!")
                    continue

                # Mark item as used
                inventory[item] -= 1


            else:
                print("Invalid choice.")
                continue

def choose_game_mode():
    global game_mode
    print("Choose Game Mode:")
    print("1. 1 Player (Player vs PC)")
    print("2. 2 Player (Player 1 vs Player 2)")
    
    while True:
        option = input("Enter 1 or 2: ")
        if option == "1":
            game_mode = 1
            break
        elif option == "2":
            game_mode = 2
            break
        else:
            print("Invalid choice. Please select a valid option.")
    
    restart_game()

def restart_game():
    clear_screen()
    if game_mode == 1:
        player_team = choose_team()
        opponent_team = generate_random_team()
        battle(player_team, opponent_team, None, None)
    elif game_mode == 2:
        team_p1, team_p2 = choose_team()
        battle(None, None, team_p1, team_p2)

def end_game():
    raise SystemExit








print("Welcome to Pokémon Battle Simulator!")
game_mode = choose_game_mode()
if game_mode == 1:
    player_team = choose_team()
    opponent_team = generate_random_team()
    battle(player_team, opponent_team, None, None)
elif game_mode == 2:
    team_p1, team_p2 = choose_team()  # Ensure it returns both teams
    battle(None, None, team_p1, team_p2)
opponent_team = generate_random_team()
battle(player_team, opponent_team, team_p1, team_p2)





