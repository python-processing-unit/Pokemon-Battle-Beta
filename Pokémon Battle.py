import moves as mv
import os
import pokemon as pkmn
import random
import sys
import trainers
import type_matrix as ty
path = os.path.abspath(sys.argv[0])
path = path.replace("Pokémon Battle.py","")
def effective(e,t1,t2=None): # e attacking t1 and t2 (if present)
    list_index1 = -1 # Initialize with a default value
    list_index2 = -1 # Initialize with a default value
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
def calc_stat(BaseStat):
    return(((((BaseStat+15)*2+31.5)*50)/100)+5)
def calc_health(BaseStat):
    return(((((BaseStat+15)*2+31.5)*50)/100)+60)
class pokemon():
    def __init__(self,hp,atk,dfn,spe,spd,atk1,atk2,atk3,atk4,nm,t1,t2=None):
        self.attack = round(calc_stat(atk),0)
        self.defense = round(calc_stat(dfn),0)
        self.speed = round(calc_stat(spd),0)
        self.special = round(calc_stat(spe),0)
        self.hp = round(calc_health(hp),0)
        self.max_hp = self.hp
        self.stats = [self.attack,self.defense,self.speed,self.special,self.hp]
        self.move1 = atk1
        self.move2 = atk2
        self.move3 = atk3
        self.move4 = atk4
        self.type1 = t1 if isinstance(t1,int) else ty.types.index(t1)
        self.type2 = t2 if isinstance(t2,int) else(ty.types.index(t2) if t2 else None)
        self.name = str(nm)
    def handle_attack(self,damage):
        if(damage >= 0):
            self.hp = self.hp-round(damage,0)
            if(self.hp<0):
                self.hp = 0
        else:
            print("Cannot apply negative damage")
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
def physical_attack(pokea,poked,attack_name):
    try:
        damage = (((14.285714285714286*attack_name.power*(pokea.attack/poked.defense))/50)+2)
        try:
            damage = damage * effective(attack_name.move_type,poked.type1,poked.type2)
        except:
            damage = damage * effective(attack_name.move_type,poked.type1)
        if((attack_name.move_type == pokea.type1) or (attack_name.move_type==pokea.type1)):
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
def special_attack(pokea,poked,attack_name):
    damage = (((14.285714285714286*attack_name.power*(pokea.special/poked.special))/50)+2)
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
def attack(pokea,poked,attack_name):
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
def opponent_attack():
    atk_select = random.randint(1,4)
    if(atk_select == 1):
        attack(opponent,active,opponent.move1)
    elif(atk_select == 2):
        attack(opponent,active,opponent.move2)
    elif(atk_select == 3):
        attack(opponent,active,opponent.move3)
    else:
        attack(opponent,active,opponent.move4)
def battle():
    global active
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
pkmn1, pkmn2, pkmn3 = trainers.red()
pokemon_party = [pkmn1,pkmn2,pkmn3]
active = pokemon_party[0]
opkmn1, opkmn2, opkmn3 = trainers.blue()
opponent_party = [opkmn1,opkmn2,opkmn3]
opponent = opkmn1#opponent_party[0]
battle()
