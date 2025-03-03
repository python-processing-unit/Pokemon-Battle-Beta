import moves as mv
import os
import pokemon as pkmn
try:
    import win32com.client
except:
    pass
import random
import sys
import time
import trainers
import type_matrix as ty
path = os.path.abspath(sys.argv[0])
path = path.replace("POKéMON BATTLE.py","")
os.system('color')
def rgb(r,g,b):
    return(f"\033[38;2;{r};{g};{b}m")
def prnt(text,r=204,g=204,b=204):
    print(rgb(r,g,b)+text+"\033[0m")
    try:
        text = text.replace("/"," out of ")
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
    except:
        time.sleep(1.2)
#Calculate effectiveness of one type attacking another
def effective(e,t1,t2=None):#Attack Type, Defending Pokemon Type 1, Defending Pokemon Type 2
    list_index1 = -1
    list_index2 = -1
    if(isinstance(t1, int)):
        list_index1 = t1
    else:
        for index, type_info in enumerate(ty.types):
            if(type_info[-1] == t1):
                list_index1 = index
                break
    if(t2):
        if(isinstance(t2, int)):
            list_index2 = t2
        else:
            for index, type_info in enumerate(ty.types):
                if(type_info[-1] == t2):
                    list_index2 = index
                    break
    effectiveness = e[list_index1]
    if(list_index2 != -1):
        effectiveness *= e[list_index2]
    return effectiveness
na = None
#LCG PRNG from Pokémon Gen-I
class LCG:
    def __init__(self, seed):
        self.a = 1103515245
        self.c = 24691
        self.m = 2**32
        self.seed = seed
    def next_32(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed
    def next(self):
        return self.next_32() & 0xFF
#User inputs attack choice
def get_attack(poke):
    while(True):
        try:
            print(str(active.move1.name)+" (1)")
            print(str(active.move2.name)+" (2)")
            print(str(active.move3.name)+" (3)")
            print(str(active.move4.name)+" (4)")
            attk = input("Attack = ")
            return(poke.move_list[int(attk)-1])
        except:
            prnt("Invalid input")
#Code for a physical attack
def physical_attack(pokea,poked,attack_name,active_attacker):#Attacking Pokemon, Defending Pokemon, Attack
    try:
        damage = (((14.285714285714286*attack_name.power*(pokea.attack/poked.defense))/50)+2)
        try:
            damage = damage * effective(attack_name.move_type,poked.type1,poked.type2)
        except:
            damage = damage * effective(attack_name.move_type,poked.type1)
        if((attack_name.move_type == pokea.type1) or (attack_name.move_type==pokea.type2)):
            damage = damage * 1.5
        poked.handle_attack(damage)
        if(active_attacker==True):
            prnt("Player's "+pokea.name+" used "+attack_name.name)
        else:
            prnt(opponent_name+"'s "+pokea.name+" used "+attack_name.name)
        if((effective(attack_name.move_type,poked.type1) == 2.0) or (effective(attack_name.move_type,poked.type2) == 2.0)):
            prnt("It's Super Effective!!!",r=0,g=255,b=0)
        elif((effective(attack_name.move_type,poked.type1) == 0.5) or (effective(attack_name.move_type,poked.type2) == 0.5)):
            prnt("It's not very effective",r=255,g=0,b=0)
        if(active_attacker==True):
            prnt("Did "+str(int(damage))+" damage to "+opponent_name+"'s "+poked.name)
        else:
            prnt("Did "+str(int(damage))+" damage to player's "+poked.name)
    except Exception as E:
        prnt(pokea.name+" used "+attack_name.name)
        prnt("But it did nothing")
        if(active_attacker==True):
            prnt("Player's "+pokea.name+" used "+attack_name.name)
            prnt("But it did nothing")
        else:
            prnt(opponent_name+"'s "+pokea.name+" used "+attack_name.name)
            prnt("But it did nothing")
#Code for a special attack
def special_attack(pokea,poked,attack_name,active_attacker):#Attacking Pokemon, Defending Pokemon, Attack
    try:
        damage = (((14.285714285714286*attack_name.power*(pokea.special/poked.special))/50)+2)*(random.randint(85,100)/100)
        try:
            damage = damage * effective(attack_name.move_type,poked.type1,poked.type2)
        except:
            damage = damage * effective(attack_name.move_type,poked.type1)
        if((attack_name.move_type == pokea.type1) or (attack_name.move_type==pokea.type2)):
            damage = damage * 1.5
        poked.handle_attack(damage)
        if(active_attacker==True):
            prnt("Player's "+pokea.name+" used "+attack_name.name)
        else:
            prnt(opponent_name+"'s "+pokea.name+" used "+attack_name.name)
        if((effective(attack_name.move_type,poked.type1) == 2.0) or (effective(attack_name.move_type,poked.type2) == 2.0)):
            prnt("It's Super Effective!!!",r=0,g=255,b=0)
        elif((effective(attack_name.move_type,poked.type1) == 0.5) or (effective(attack_name.move_type,poked.type2) == 0.5)):
            prnt("It's not very effective",r=255,g=0,b=0)
        if(active_attacker==True):
            prnt("Did "+str(int(damage))+" damage to "+opponent_name+"'s "+poked.name)
        else:
            prnt("Did "+str(int(damage))+" damage to player's "+poked.name)
    except Exception as E:
        prnt(pokea.name+" used "+attack_name.name)
        prnt("But it did nothing")
        if(active_attacker==True):
            prnt("Player's "+pokea.name+" used "+attack_name.name)
            prnt("But it did nothing")
        else:
            prnt(opponent_name+"'s "+pokea.name+" used "+attack_name.name)
            prnt("But it did nothing")
def attack(pokea,poked,attack_name,active_attacker):#Attacking Pokemon, Defending Pokemon, Attack
    ran = lcg.next()
    if(attack_name == None):
        pass
    else:
        if(ran <= (attack_name.accuracy * 2.5)):
            if(attack_name.move_type in [ty.fire, ty.water, ty.grass, ty.electric, ty.psychic]):
                special_attack(pokea,poked,attack_name,active_attacker)
            else:
                physical_attack(pokea,poked,attack_name,active_attacker)
        else:
            if(active_attacker==True):
                prnt("Player's "+pokea.name+" used "+attack_name.name)
                prnt("But it missed")
            else:
                prnt(opponent_name+"'s "+pokea.name+" used "+attack_name.name)
                prnt("But it missed")
#Opponent Logic
def opponent_attack():
    atk_select = random.randint(1,4)
    if(atk_select == 1):
        attack(opponent,active,opponent.move1,False)
    elif(atk_select == 2):
        attack(opponent,active,opponent.move2,False)
    elif(atk_select == 3):
        attack(opponent,active,opponent.move3,False)
    else:
        attack(opponent,active,opponent.move4,False)
#Code to launch a battle, and the battle logic
def battle():
    global active
    prnt("Player's "+active.name+"'s HP: "+str(int(active.hp))+"/"+str(int(active.max_hp)))
    prnt(opponent_name+"'s "+opponent.name+"'s HP: "+str(int(opponent.hp))+"/"+str(int(opponent.max_hp)))
    while((active.hp > 0) and (opponent.hp > 0)):
        print("Attack (1)")
        print("Switch (2)")
        action = input("")
        if(action=="1"):
            got_attack = get_attack(active)
            if(active.speed > opponent.speed):
                attack(active,opponent,got_attack,True)
                if((active.hp > 0) and (opponent.hp > 0)):
                    opponent_attack()
                else:
                    pass
            elif(active.speed < opponent.speed):
                opponent_attack()
                if((active.hp > 0) and (opponent.hp > 0)):
                    attack(active,opponent,got_attack,True)
            else:
                if(random.randint(1,2)==1):
                    opponent_attack()
                    if((active.hp > 0) and (opponent.hp > 0)):
                        attack(active,opponent,got_attack,True)
                else:
                    attack(active,opponent,got_attack,True)
                    if((active.hp > 0) and (opponent.hp > 0)):
                        opponent_attack()
            if(active.poisoned and not((active.type1==ty.poison)or(active.type2==ty.poison))):
                active.handle_attack(active.max_hp/16)
                prnt("Player's "+active.name+" is hurt by poison",r=160,g=120,b=160)
                prnt("Took "+str(active.max_hp/16)+" damage",r=160,g=120,b=160)
            if(opponent.poisoned and not((active.type1==ty.poison)or(active.type2==ty.poison))):
                opponent.handle_attack(opponent.max_hp/16)
                prnt(opponent_name+"'s "+active.name+" is hurt by poison",r=160,g=120,b=160)
                prnt("Took "+str(active.max_hp/16)+" damage",r=160,g=120,b=160)
            if(active.burned and not((active.type1==ty.fire)or(active.type2==ty.fire))):
                active.handle_attack(active.max_hp/16)
                print("Player's "+active.name+" is hurt by burn",r=255,g=0,b=0)
                print("Took "+str(active.max_hp/16)+" damage",r=255,g=0,b=0)
            if(opponent.burned and not((active.type1==ty.fire)or(active.type2==ty.fire))):
                opponent.handle_attack(opponent.max_hp/16)
                print(opponent_name+"'s "+active.name+" is hurt by burn",r=255,g=0,b=0)
                print("Took "+str(active.max_hp/16)+" damage",r=255,g=0,b=0)
            prnt("Player's "+active.name+"'s HP: "+str(int(active.hp))+"/"+str(int(active.max_hp)))
            prnt(opponent_name+"'s "+opponent.name+"'s HP: "+str(int(opponent.hp))+"/"+str(int(opponent.max_hp)))
        elif(action=="2"):
            while(True):
                print(pokemon_party[0].name+" (1)")
                print(pokemon_party[1].name+" (2)")
                print(pokemon_party[2].name+" (3)")
                switch = input("")
                try:
                    prnt(active.name+", return")
                    active = pokemon_party[int(switch)-1]
                    prnt("Go "+active.name)
                    opponent_attack()
                    break
                except:
                    prnt("Invalid input")
while(True):
    lcg = LCG(seed=random.randint(0,99999))
    pokemon_party = trainers.red()
    active = pokemon_party[0]
    for i in range(0,15,1):
        print(trainers.trainer_names[i]+" ("+str(i+1)+")")
    while(True):
        opponent_select = input("Opponent: ")
        try:
            opponent_party = trainers.trainer_list[int(opponent_select)-1]
            opponent_name = trainers.trainer_names[int(opponent_select)-1]
            break
        except:
            print("Invalid Input")
    opponent = opponent_party[0]
    battle()
    if(active.hp>0):
        prnt("You win",r=0,g=255,b=0)
    else:
        prnt("You lose",r=255,g=0,b=0)
    time.sleep(5)
