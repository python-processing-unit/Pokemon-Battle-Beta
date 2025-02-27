import moves as mv
import os
import pokemon as pkmn
import random
import sys
import trainers
import type_matrix as ty
path = os.path.abspath(sys.argv[0])
path = path.replace("Pokémon Battle.py","")
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
            print("Invalid input")
#Code for a physical attack
def physical_attack(pokea,poked,attack_name):#Attacking Pokemon, Defending Pokemon, Attack
    try:
        damage = (((14.285714285714286*attack_name.power*(pokea.attack/poked.defense))/50)+2)
        try:
            damage = damage * effective(attack_name.move_type,poked.type1,poked.type2)
        except:
            damage = damage * effective(attack_name.move_type,poked.type1)
        if((attack_name.move_type == pokea.type1) or (attack_name.move_type==pokea.type2)):
            damage = damage * 1.5
        poked.handle_attack(damage)
        print(pokea.name+" used "+attack_name.name)
        if((effective(attack_name.move_type,poked.type1) == 2.0) or (effective(attack_name.move_type,poked.type2) == 2.0)):
            print("It's Super Effective!!!")
        elif((effective(attack_name.move_type,poked.type1) == 0.5) or (effective(attack_name.move_type,poked.type2) == 0.5)):
            print("It's not very effective.")
        print("Did "+str(int(damage))+" damage to "+poked.name)
        print(pokea.name+"'s HP: "+str(int(pokea.hp))+"/"+str(int(pokea.max_hp)))
        print(poked.name+"'s HP: "+str(int(poked.hp))+"/"+str(int(poked.max_hp)))
    except Exception as E:
        print(pokea.name+" used "+attack_name.name)
        print("But it did nothing")
        print(pokea.name+"'s HP: "+str(int(pokea.hp))+"/"+str(int(pokea.max_hp)))
        print(poked.name+"'s HP: "+str(int(poked.hp))+"/"+str(int(poked.max_hp)))
#Code for a special attack
def special_attack(pokea,poked,attack_name):#Attacking Pokemon, Defending Pokemon, Attack
    damage = (((14.285714285714286*attack_name.power*(pokea.special/poked.special))/50)+2)*(random.randint(85,100)/100)
    try:
        damage = damage * effective(attack_name.move_type,poked.type1,poked.type2)
    except:
        damage = damage * effective(attack_name.move_type,poked.type1)
    if((attack_name.move_type == pokea.type1) or (attack_name.move_type==pokea.type2)):
        damage = damage * 1.5
    poked.handle_attack(damage)
    print(pokea.name+" used "+attack_name.name)
    eff = effective(attack_name.move_type,poked.type1)
    eff2 = effective(attack_name.move_type,poked.type2)
    if(((eff == 2.0) or (eff2 == 2.0)) and (not ((eff == 0.5) or (eff2 == 0.5)))):
        print("It's Super Effective!!!")
    elif(((eff == 0.5) or (eff2 == 0.5)) and (not ((eff == 2.0) or (eff2 == 2.0)))):
        print("It's not very effective.")
    print("Did "+str(int(damage))+" damage to "+poked.name)
    print(pokea.name+"'s HP: "+str(int(pokea.hp))+"/"+str(int(pokea.max_hp)))
    print(poked.name+"'s HP: "+str(int(poked.hp))+"/"+str(int(poked.max_hp)))
def attack(pokea,poked,attack_name):#Attacking Pokemon, Defending Pokemon, Attack
    ran = lcg.next()
    if(attack_name == None):
        pass
    else:
        if(ran <= (attack_name.accuracy * 2.5)):
            if(attack_name.move_type in [ty.fire, ty.water, ty.grass, ty.electric, ty.psychic]):
                special_attack(pokea,poked,attack_name)
            else:
                physical_attack(pokea,poked,attack_name)
        else:
            print(pokea.name+" used "+attack_name.name)
            print("But it missed")
            print(pokea.name+"'s HP: "+str(int(pokea.hp))+"/"+str(int(pokea.max_hp)))
            print(poked.name+"'s HP: "+str(int(poked.hp))+"/"+str(int(poked.max_hp)))
def opponent_attack1():
    try:
        attack(opponent,active,opponent.move1)
    except:
        print(opponent.name+" used "+opponent.move1.name+", but it did nothing")
def opponent_attack2():
    try:
        attack(opponent,active,opponent.move1)
    except:
        print(opponent.name+" used "+opponent.move1.name+", but it did nothing")
def opponent_attack3():
    try:
        attack(opponent,active,opponent.move1)
    except:
        print(opponent.name+" used "+opponent.move1.name+", but it did nothing")
def opponent_attack4():
    try:
        attack(opponent,active,opponent.move1)
    except:
        print(opponent.name+" used "+opponent.move1.name+", but it did nothing")
#Opponent Logic
def opponent_attack():
    atk_select = random.randint(1,4)
    if(atk_select == 1):
        opponent_attack1()
    elif(atk_select == 2):
        opponent_attack2()
    elif(atk_select == 3):
        opponent_attack3()
    else:
        opponent_attack4()
#Code to launch a battle, and the battle logic
def battle():
    global active
    print(active.name+"'s HP: "+str(int(active.hp))+"/"+str(int(active.max_hp)))
    print(opponent.name+"'s HP: "+str(int(opponent.hp))+"/"+str(int(opponent.max_hp)))
    while((active.hp > 0) and (opponent.hp > 0)):
        print("Attack (1)")
        print("Switch (2)")
        action = input("")
        if(action=="1"):
            got_attack = get_attack(active)
            if(active.speed > opponent.speed):
                attack(active,opponent,got_attack)
                if((active.hp > 0) and (opponent.hp > 0)):
                    opponent_attack()
                else:
                    break
            else:
                opponent_attack()
                if((active.hp > 0) and (opponent.hp > 0)):
                    attack(active,opponent,got_attack)
        elif(action=="2"):
            while(True):
                print(pokemon_party[0].name+" (1)")
                print(pokemon_party[1].name+" (2)")
                print(pokemon_party[2].name+" (3)")
                switch = input("")
                try:
                    print(active.name+", return")
                    active = pokemon_party[int(switch)-1]
                    print("Go "+active.name)
                    opponent_attack()
                    break
                except:
                    print("Invalid input")
lcg = LCG(seed=random.randint(0,99999))
pokemon_party = trainers.red()
active = pokemon_party[0]
opponent_party = trainers.red()
opponent = opponent_party[0]
battle()
