import moves as mv
import type_matrix as ty
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
        self.move_list = [self.move1,self.move2,self.move3,self.move4]
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
#list of pokemon, by number
class bulbasaur(pokemon):
    def __init__(self):
        super().__init__(45,49,49,65,45,mv.vine_whip(),mv.tackle(),mv.leech_seed(),mv.growl(),"Bulbasaur",ty.grass)
class ivysaur(pokemon):
    def __init__(self):
        super().__init__(60,62,63,80,60,mv.razor_leaf(),mv.body_slam(),mv.sleep_powder(),mv.solar_beam(),"Ivysaur",ty.grass,t2=ty.poison)
class venusaur(pokemon):
    def __init__(self):
        super().__init__(80,82,83,100,80,mv.solar_beam(),mv.mega_drain(),mv.double_edge(),mv.earthquake(),"Venusaur",ty.grass,t2=ty.poison)
class charmander(pokemon):
    def __init__(self):
        super().__init__(39,52,43,50,65,mv.ember(),mv.scratch(),mv.growl(),mv.leer(),"Charmander",ty.fire)
class charmeleon(pokemon):
    def __init__(self):
        super().__init__(58,64,58,65,80,mv.flamethrower(),mv.slash(),mv.body_slam(),mv.dig(),"Charmeleon",ty.fire)
class charizard(pokemon):
    def __init__(self):
        super().__init__(78,84,78,85,100,mv.fire_blast(),mv.fly(),mv.earthquake(),mv.hyper_beam(),"Charizard",ty.fire,t2=ty.flying)
class squirtle(pokemon):
    def __init__(self):
        super().__init__(44,48,65,50,43,mv.water_gun(),mv.tackle(),mv.tail_whip(),mv.bubble(),"Squirtle",ty.water)
class wartortle(pokemon):
    def __init__(self):
        super().__init__(59,63,80,65,58,mv.surf(),mv.bite(),mv.withdraw(),mv.ice_beam(),"Wartortle",ty.water)
class blastoise(pokemon):
    def __init__(self):
        super().__init__(79,83,100,85,78,mv.hydro_pump(),mv.blizzard(),mv.seismic_toss(),mv.skull_bash(),"Blastoise",ty.water)
class caterpie(pokemon):
    def __init__(self):
        super().__init__(45,30,35,20,45,mv.tackle(),mv.string_shot(),None,None,"Caterpie",ty.bug)
class metapod(pokemon):
    def __init__(self):
        super().__init__(50,20,55,25,30,mv.harden(),None,None,None,"Metapod",ty.bug)
class butterfree(pokemon):
    def __init__(self):
        super().__init__(60,45,50,80,70,mv.psybeam(),mv.sleep_powder(),mv.stun_spore(),mv.swift(),"Butterfree",ty.bug,t2=ty.flying)
class weedle(pokemon):
    def __init__(self):
        super().__init__(40,35,30,20,50,mv.poison_sting(),mv.string_shot(),None,None,"Weedle",ty.bug,t2=ty.poison)
class kakuna(pokemon):
    def __init__(self):
        super().__init__(45,25,50,25,35,mv.harden(),None,None,None,"Kakuna",ty.bug,t2=ty.poison)
class beedrill(pokemon):
    def __init__(self):
        super().__init__(65,80,40,45,75,mv.twineedle(),mv.hyper_beam(),mv.rage(),mv.toxic(),"Beedrill",ty.bug,t2=ty.poison)
class pidgey(pokemon):
    def __init__(self):
        super().__init__(40,45,40,35,56,mv.gust(),mv.quick_attack(),mv.sand_attack(),mv.tackle(),"Pidgey",ty.normal,t2=ty.flying)
class pidgeotto(pokemon):
    def __init__(self):
        super().__init__(63,60,55,50,71,mv.wing_attack(),mv.quick_attack(),mv.whirlwind(),mv.feather_dance(),"Pidgeotto",ty.normal,t2=ty.flying)
class pidgeot(pokemon):
    def __init__(self):
        super().__init__(83,80,75,70,101,mv.sky_attack(),mv.quick_attack(),mv.mirror_move(),mv.feather_dance(),"Pidgeot",ty.normal,t2=ty.flying)
class rattata(pokemon):
    def __init__(self):
        super().__init__(30,56,35,25,72,mv.quick_attack(),mv.hyper_fang(),mv.bite(),mv.focus_energy(),"Rattata",ty.normal)
class raticate(pokemon):
    def __init__(self):
        super().__init__(55,81,60,50,97,mv.hyper_fang(),mv.super_fang(),mv.swords_dance(),mv.quick_attack(),"Raticate",ty.normal)
class spearow(pokemon):
    def __init__(self):
        super().__init__(40,60,30,31,70,mv.peck(),mv.leer(),mv.fury_attack(),mv.pursuit(),"Spearow",ty.normal,t2=ty.flying)
class fearow(pokemon):
    def __init__(self):
        super().__init__(65,90,65,61,100,mv.drill_peck(),mv.agility(),mv.mirror_move(),mv.fury_attack(),"Fearow",ty.normal,t2=ty.flying)
class ekans(pokemon):
    def __init__(self):
        super().__init__(35,60,44,40,55,mv.poison_sting(),mv.bite(),mv.glare(),mv.wrap(),"Ekans",ty.poison)
class arbok(pokemon):
    def __init__(self):
        super().__init__(60,85,69,65,80,mv.poison_fang(),mv.bite(),mv.glare(),mv.acid(),"Arbok",ty.poison)
class pikachu(pokemon):
    def __init__(self):
        super().__init__(35,55,40,50,90,mv.thunderbolt(),mv.quick_attack(),mv.double_team(),mv.thunder_wave(),"Pikachu",ty.electric)
class raichu(pokemon):
    def __init__(self):
        super().__init__(60,90,55,90,110,mv.thunder(),mv.quick_attack(),mv.agility(),mv.thunder_wave(),"Raichu",ty.electric)
class sandshrew(pokemon):
    def __init__(self):
        super().__init__(50,75,85,30,40,mv.slash(),mv.dig(),mv.sand_attack(),mv.poison_sting(),"Sandshrew",ty.ground)
class sandslash(pokemon):
    def __init__(self):
        super().__init__(75,100,110,55,65,mv.earthquake(),mv.slash(),mv.sand_attack(),mv.poison_sting(),"Sandslash",ty.ground)
class nidoran_f(pokemon):
    def __init__(self):
        super().__init__(55,47,52,40,41,mv.poison_sting(),mv.tackle(),mv.scratch(),mv.double_kick(),"Nidoran♀",ty.poison)
class nidorina(pokemon):
    def __init__(self):
        super().__init__(70,62,67,55,56,mv.poison_sting(),mv.bite(),mv.double_kick(),mv.fury_swipes(),"Nidorina",ty.poison)
class nidoqueen(pokemon):
    def __init__(self):
        super().__init__(90,82,87,75,76,mv.body_slam(),mv.earthquake(),mv.thunder(),mv.thrash(),"Nidoqueen",ty.poison,t2=ty.ground)
class nidoran_m(pokemon):
    def __init__(self):
        super().__init__(46,57,40,40,50,mv.poison_sting(),mv.tackle(),mv.scratch(),mv.double_kick(),"Nidoran♂",ty.poison)
class nidorino(pokemon):
    def __init__(self):
        super().__init__(61,72,57,55,65,mv.poison_sting(),mv.horn_attack(),mv.double_kick(),mv.fury_attack(),"Nidorino",ty.poison)
class nidoking(pokemon):
    def __init__(self):
        super().__init__(81,92,77,85,85,mv.mega_punch(),mv.earthquake(),mv.thunder(),mv.thrash(),"Nidoking",ty.poison,t2=ty.ground)
class clefairy(pokemon):
    def __init__(self):
        super().__init__(70,45,48,60,35,mv.pound(),mv.double_slap(),mv.sing(),mv.metronome(),"Clefairy",ty.normal)
class clefable(pokemon):
    def __init__(self):
        super().__init__(95,70,73,85,60,mv.hyper_beam(),mv.moonblast(),mv.sing(),mv.metronome(),"Clefable",ty.normal)
class vulpix(pokemon):
    def __init__(self):
        super().__init__(38,41,40,65,65,mv.ember(),mv.quick_attack(),mv.confuse_ray(),mv.flamethrower(),"Vulpix",ty.fire)
class ninetales(pokemon):
    def __init__(self):
        super().__init__(73,76,75,100,100,mv.fire_blast(),mv.quick_attack(),mv.confuse_ray(),mv.flamethrower(),"Ninetales",ty.fire)
class jigglypuff(pokemon):
    def __init__(self):
        super().__init__(115,45,20,45,20,mv.pound(),mv.disable(),mv.defense_curl(),mv.double_slap(),"Jigglypuff",ty.normal)
class wigglytuff(pokemon):
    def __init__(self):
        super().__init__(140,70,45,85,45,mv.double_edge(),mv.hyper_beam(),mv.sing(),mv.double_slap(),"Wigglytuff",ty.normal)
class zubat(pokemon):
    def __init__(self):
        super().__init__(40,45,35,30,55,mv.leech_life(),mv.bite(),mv.wing_attack(),mv.confuse_ray(),"Zubat",ty.poison,t2=ty.flying)
class golbat(pokemon):
    def __init__(self):
        super().__init__(75,80,70,65,90,mv.leech_life(),mv.bite(),mv.wing_attack(),mv.confuse_ray(),"Golbat",ty.poison,t2=ty.flying)
class oddish(pokemon):
    def __init__(self):
        super().__init__(45,50,55,75,30,mv.absorb(),mv.poison_powder(),mv.stun_spore(),mv.sleep_powder(),"Oddish",ty.grass,t2=ty.poison)
class gloom(pokemon):
    def __init__(self):
        super().__init__(60,65,70,85,40,mv.absorb(),mv.poison_powder(),mv.stun_spore(),mv.petaldance(),"Gloom",ty.grass,t2=ty.poison)
class vileplume(pokemon):
    def __init__(self):
        super().__init__(75,80,85,100,50,mv.petaldance(),mv.poison_powder(),mv.stun_spore(),mv.solar_beam(),"Vileplume",ty.grass,t2=ty.poison)
class paras(pokemon):
    def __init__(self):
        super().__init__(35,70,55,55,25,mv.leech_life(),mv.stun_spore(),mv.scratch(),mv.growth(),"Paras",ty.bug,t2=ty.grass)
class parasect(pokemon):
    def __init__(self):
        super().__init__(60,95,80,80,30,mv.leech_life(),mv.spore(),mv.scratch(),mv.growth(),"Parasect",ty.bug,t2=ty.grass)
class venonat(pokemon):
    def __init__(self):
        super().__init__(60,55,50,40,45,mv.tackle(),mv.disable(),mv.psychic_attack(),mv.leech_life(),"Venonat",ty.bug,t2=ty.poison)
class venomoth(pokemon):
    def __init__(self):
        super().__init__(70,65,60,90,90,mv.psybeam(),mv.stun_spore(),mv.psychic_attack(),mv.leech_life(),"Venomoth",ty.bug,t2=ty.poison)
class diglett(pokemon):
    def __init__(self):
        super().__init__(10,55,25,45,95,mv.scratch(),mv.growl(),mv.dig(),mv.sand_attack(),"Diglett",ty.ground)
class dugtrio(pokemon):
    def __init__(self):
        super().__init__(35,80,50,70,120,mv.earthquake(),mv.tri_attack(),mv.dig(),mv.sand_attack(),"Dugtrio",ty.ground)
class meowth(pokemon):
    def __init__(self):
        super().__init__(40,45,35,40,90,mv.scratch(),mv.bite(),mv.pay_day(),mv.screech(),"Meowth",ty.normal)
class persian(pokemon):
    def __init__(self):
        super().__init__(65,70,60,65,115,mv.slash(),mv.bite(),mv.fury_swipes(),mv.screech(),"Persian",ty.normal)
class psyduck(pokemon):
    def __init__(self):
        super().__init__(50,52,48,50,55,mv.scratch(),mv.tail_whip(),mv.water_gun(),mv.confusion(),"Psyduck",ty.water)
class golduck(pokemon):
    def __init__(self):
        super().__init__(80,82,78,95,85,mv.hydro_pump(),mv.confusion(),mv.fury_swipes(),mv.hypnosis(),"Golduck",ty.water)
class mankey(pokemon):
    def __init__(self):
        super().__init__(40,80,35,35,70,mv.scratch(),mv.low_kick(),mv.karate_chop(),mv.fury_swipes(),"Mankey",ty.fighting)
class primeape(pokemon):
    def __init__(self):
        super().__init__(65,105,60,60,95,mv.cross_chop(),mv.low_kick(),mv.karate_chop(),mv.fury_swipes(),"Primeape",ty.fighting)
class growlithe(pokemon):
    def __init__(self):
        super().__init__(55,70,45,70,60,mv.bite(),mv.roar(),mv.ember(),mv.takedown(),"Growlithe",ty.fire)
class arcanine(pokemon):
    def __init__(self):
        super().__init__(90,110,80,100,95,mv.extreme_speed(),mv.roar(),mv.flamethrower(),mv.take_down(),"Arcanine",ty.fire)
class poliwag(pokemon):
    def __init__(self):
        super().__init__(40,50,40,40,90,mv.water_gun(),mv.hypnosis(),mv.bubble(),mv.double_slap(),"Poliwag",ty.water)
class poliwhirl(pokemon):
    def __init__(self):
        super().__init__(65,65,65,50,90,mv.water_gun(),mv.hypnosis(),mv.bubble(),mv.body_slam(),"Poliwhirl",ty.water)
class poliwrath(pokemon):
    def __init__(self):
        super().__init__(90,85,95,70,70,mv.hydro_pump(),mv.submission(),mv.hypnosis(),mv.body_slam(),"Poliwrath",ty.water,t2=ty.fighting)
class abra(pokemon):
    def __init__(self):
        super().__init__(25,20,15,105,90,mv.teleport(),None,None,None,"Abra",ty.psychic)
class kadabra(pokemon):
    def __init__(self):
        super().__init__(40,35,30,120,105,mv.confusion(),mv.teleport(),mv.disable(),mv.psybeam(),"Kadabra",ty.psychic)
class alakazam(pokemon):
    def __init__(self):
        super().__init__(55,50,45,135,120,mv.psychic_attack(),mv.recover(),mv.disable(),mv.psybeam(),"Alakazam",ty.psychic)
class machop(pokemon):
    def __init__(self):
        super().__init__(70,80,50,35,35,mv.karate_chop(),mv.low_kick(),mv.seismic_toss(),mv.fissure(),"Machop",ty.fighting)
class machoke(pokemon):
    def __init__(self):
        super().__init__(80,100,70,50,45,mv.low_kick(),mv.karate_chop(),mv.seismic_toss(),mv.fissure(),"Machoke",ty.fighting)
class machamp(pokemon):
    def __init__(self):
        super().__init__(90,130,80,65,55,mv.cross_chop(),mv.dynamic_punch(),mv.earthquake(),mv.hyper_beam(),"Machamp",ty.fighting)
class bellsprout(pokemon):
    def __init__(self):
        super().__init__(50,75,35,70,40,mv.razor_leaf(),mv.solar_beam(),mv.stun_spore(),mv.swords_dance(),"Bellsprout",ty.grass,t2=ty.poison)
class weepinbell(pokemon):
    def __init__(self):
        super().__init__(65,90,50,85,55,mv.razor_leaf(),mv.solar_beam(),mv.stun_spore(),mv.swords_dance(),"Weepinbell",ty.grass,t2=ty.poison)
class victreebel(pokemon):
    def __init__(self):
        super().__init__(80,105,65,100,70,mv.razor_leaf(),mv.solar_beam(),mv.stun_spore(),mv.swords_dance(),"Victreebel",ty.grass,t2=ty.poison)
class tentacool(pokemon):
    def __init__(self):
        super().__init__(40,40,35,100,70,mv.wrap(),mv.acid(),mv.bubble_beam(),mv.barrier(),"Tentacool",ty.water,t2=ty.poison)
class tentacruel(pokemon):
    def __init__(self):
        super().__init__(80,70,65,120,100,mv.wrap(),mv.acid(),mv.bubble_beam(),mv.barrier(),"Tentacruel",ty.water,t2=ty.poison)
class geodude(pokemon):
    def __init__(self):
        super().__init__(40,80,100,30,20,mv.tackle(),mv.earthquake(),mv.rock_slide(),mv.explosion(),"Geodude",ty.rock,t2=ty.ground)
class graveler(pokemon):
    def __init__(self):
        super().__init__(55,95,115,45,35,mv.tackle(),mv.earthquake(),mv.rock_slide(),mv.explosion(),"Graveler",ty.rock,t2=ty.ground)
class golem(pokemon):
    def __init__(self):
        super().__init__(80,110,130,55,45,mv.tackle(),mv.earthquake(),mv.rock_slide(),mv.explosion(),"Golem",ty.rock,t2=ty.ground)
class ponyta(pokemon):
    def __init__(self):
        super().__init__(50,85,55,65,90,mv.stomp(),mv.fire_spin(),mv.take_down(),mv.agility(),"Ponyta",ty.fire)
class rapidash(pokemon):
    def __init__(self):
        super().__init__(65,100,70,80,105,mv.stomp(),mv.fire_spin(),mv.take_down(),mv.agility(),"Rapidash",ty.fire)
class slowpoke(pokemon):
    def __init__(self):
        super().__init__(90,65,65,40,15,mv.confusion(),mv.disable(),mv.headbutt(),mv.amnesia(),"Slowpoke",ty.water,t2=ty.psychic)
class slowbro(pokemon):
    def __init__(self):
        super().__init__(95,75,110,80,30,mv.psychic_attack(),mv.surf(),mv.amnesia(),mv.thunder_wave(),"Slowbro",ty.water,t2=ty.psychic)
class magnemite(pokemon):
    def __init__(self):
        super().__init__(25,35,70,95,45,mv.thunder_shock(),mv.sonic_boom(),mv.thunder_wave(),mv.swift(),"Magnemite",ty.electric,t2=ty.steel)
class magneton(pokemon):
    def __init__(self):
        super().__init__(50,60,95,120,70,mv.thunder_shock(),mv.sonic_boom(),mv.thunder_wave(),mv.swift(),"Magneton",ty.electric,t2=ty.steel)
class farfetchd(pokemon):
    def __init__(self):
        super().__init__(52,65,55,58,60,mv.slash(),mv.swords_dance(),mv.fly(),mv.agility(),"Farfetch'd",ty.normal,t2=ty.flying)
class doduo(pokemon):
    def __init__(self):
        super().__init__(35,85,45,35,75,mv.peck(),mv.growl(),mv.fury_attack(),mv.tri_attack(),"Doduo",ty.normal,t2=ty.flying)
class dodrio(pokemon):
    def __init__(self):
        super().__init__(60,110,70,60,100,mv.drill_peck(),mv.fury_attack(),mv.tri_attack(),mv.agility(),"Dodrio",ty.normal,t2=ty.flying)
class seel(pokemon):
    def __init__(self):
        super().__init__(65,45,55,70,45,mv.headbutt(),mv.aurora_beam(),mv.rest(),mv.takedown(),"Seel",ty.water)
class dewgong(pokemon):
    def __init__(self):
        super().__init__(90,70,80,95,70,mv.headbutt(),mv.aurora_beam(),mv.rest(),mv.takedown(),"Dewgong",ty.water,t2=ty.ice)
class grimer(pokemon):
    def __init__(self):
        super().__init__(80,80,50,40,25,mv.sludge(),mv.disable(),mv.minimize(),mv.harden(),"Grimer",ty.poison)
class muk(pokemon):
    def __init__(self):
        super().__init__(105,105,75,65,50,mv.sludge(),mv.disable(),mv.minimize(),mv.harden(),"Muk",ty.poison)
class shellder(pokemon):
    def __init__(self):
        super().__init__(30,65,100,45,40,mv.tackle(),mv.supersonic(),mv.clamp(),mv.aurora_beam(),"Shellder",ty.water)
class cloyster(pokemon):
    def __init__(self):
        super().__init__(50,95,180,85,70,mv.tackle(),mv.supersonic(),mv.clamp(),mv.aurora_beam(),"Cloyster",ty.water,t2=ty.ice)
class gastly(pokemon):
    def __init__(self):
        super().__init__(30,35,30,100,80,mv.night_shade(),mv.confuse_ray(),mv.hypnosis(),mv.dream_eater(),"Gastly",ty.ghost,t2=ty.poison)
class haunter(pokemon):
    def __init__(self):
        super().__init__(45,50,45,115,95,mv.night_shade(),mv.confuse_ray(),mv.hypnosis(),mv.dream_eater(),"Haunter",ty.ghost,t2=ty.poison)
class gengar(pokemon):
    def __init__(self):
        super().__init__(60,65,60,130,110,mv.night_shade(),mv.confuse_ray(),mv.hypnosis(),mv.dream_eater(),"Gengar",ty.ghost,t2=ty.poison)
class onix(pokemon):
    def __init__(self):
        super().__init__(35,45,160,30,70,mv.rock_throw(),mv.bind(),mv.slam(),mv.harden(),"Onix",ty.rock,t2=ty.ground)
class drowzee(pokemon):
    def __init__(self):
        super().__init__(60,48,45,90,42,mv.hypnosis(),mv.headbutt(),mv.psychic_attack(),mv.disable(),"Drowzee",ty.psychic)
class hypno(pokemon):
    def __init__(self):
        super().__init__(85,73,70,115,67,mv.hypnosis(),mv.headbutt(),mv.psychic_attack(),mv.disable(),"Hypno",ty.psychic)
class krabby(pokemon):
    def __init__(self):
        super().__init__(30,105,90,25,50,mv.crabhammer(),mv.stomp(),mv.vice_grip(),mv.guillotine(),"Krabby",ty.water)
class kingler(pokemon):
    def __init__(self):
        super().__init__(55,130,115,50,75,mv.crabhammer(),mv.stomp(),mv.vice_grip(),mv.guillotine(),"Kingler",ty.water)
class voltorb(pokemon):
    def __init__(self):
        super().__init__(40,30,50,55,100,mv.tackle(),mv.screech(),mv.sonic_boom(),mv.self_destruct(),"Voltorb",ty.electric)
class electrode(pokemon):
    def __init__(self):
        super().__init__(60,50,70,80,140,mv.tackle(),mv.screech(),mv.sonic_boom(),mv.self_destruct(),"Electrode",ty.electric)
class exeggcute(pokemon):
    def __init__(self):
        super().__init__(60,40,80,60,40,mv.barrage(),mv.hypnosis(),mv.stun_spore(),mv.psychic_attack(),"Exeggcute",ty.grass,t2=ty.psychic)
class exeggutor(pokemon):
    def __init__(self):
        super().__init__(95,95,85,125,55,mv.stomp(),mv.hypnosis(),mv.stun_spore(),mv.psychic_attack(),"Exeggutor",ty.grass,t2=ty.psychic)
class cubone(pokemon):
    def __init__(self):
        super().__init__(50,50,95,40,35,mv.bone_club(),mv.headbutt(),mv.bonemerang(),mv.swords_dance(),"Cubone",ty.ground)
class marowak(pokemon):
    def __init__(self):
        super().__init__(60,80,110,50,45,mv.bone_club(),mv.headbutt(),mv.bonemerang(),mv.swords_dance(),"Marowak",ty.ground)
class hitmonlee(pokemon):
    def __init__(self):
        super().__init__(50,120,53,35,87,mv.double_kick(),mv.rolling_kick(),mv.jump_kick(),mv.hi_jump_kick(),"Hitmonlee",ty.fighting)
class hitmonchan(pokemon):
    def __init__(self):
        super().__init__(50,105,79,35,76,mv.comet_punch(),mv.fire_punch(),mv.ice_punch(),mv.thunder_punch(),"Hitmonchan",ty.fighting)
class lickitung(pokemon):
    def __init__(self):
        super().__init__(90,55,75,60,30,mv.stomp(),mv.disable(),mv.wrap(),mv.hyper_beam(),"Lickitung",ty.normal)
class koffing(pokemon):
    def __init__(self):
        super().__init__(40,65,95,60,35,mv.tackle(),mv.smog(),mv.sludge(),mv.haze(),"Koffing",ty.poison)
class weezing(pokemon):
    def __init__(self):
        super().__init__(65,90,120,85,60,mv.tackle(),mv.smog(),mv.sludge(),mv.haze(),"Weezing",ty.poison)
class rhyhorn(pokemon):
    def __init__(self):
        super().__init__(80,85,95,30,25,mv.stomp(),mv.rock_slide(),mv.fury_attack(),mv.horn_drill(),"Rhyhorn",ty.ground,t2=ty.rock)
class rhydon(pokemon):
    def __init__(self):
        super().__init__(105,130,120,45,40,mv.stomp(),mv.rock_slide(),mv.fury_attack(),mv.horn_drill(),"Rhydon",ty.ground,t2=ty.rock)
class chansey(pokemon):
    def __init__(self):
        super().__init__(250,5,5,35,50,mv.pound(),mv.sing(),mv.softboiled(),mv.counter(),"Chansey",ty.normal)
class tangela(pokemon):
    def __init__(self):
        super().__init__(65,55,115,100,60,mv.constrict(),mv.bind(),mv.slam(),mv.stun_spore(),"Tangela",ty.grass)
class kangaskhan(pokemon):
    def __init__(self):
        super().__init__(105,95,80,40,90,mv.comet_punch(),mv.bite(),mv.dizzy_punch(),mv.hyper_beam(),"Kangaskhan",ty.normal)
class horsea(pokemon):
    def __init__(self):
        super().__init__(30,40,70,70,60,mv.bubble(),mv.smokescreen(),mv.leer(),mv.water_gun(),"Horsea",ty.water)
class seadra(pokemon):
    def __init__(self):
        super().__init__(55,65,95,95,85,mv.bubble(),mv.smokescreen(),mv.leer(),mv.water_gun(),"Seadra",ty.water)
class goldeen(pokemon):
    def __init__(self):
        super().__init__(45,67,60,50,63,mv.peck(),mv.supersonic(),mv.horn_attack(),mv.fury_attack(),"Goldeen",ty.water)
class seaking(pokemon):
    def __init__(self):
        super().__init__(80,92,65,80,68,mv.peck(),mv.supersonic(),mv.horn_attack(),mv.fury_attack(),"Seaking",ty.water)
class staryu(pokemon):
    def __init__(self):
        super().__init__(30,45,55,70,85,mv.tackle(),mv.water_gun(),mv.harden(),mv.recover(),"Staryu",ty.water)
class starmie(pokemon):
    def __init__(self):
        super().__init__(60,75,85,100,115,mv.tackle(),mv.water_gun(),mv.harden(),mv.psybeam(),"Starmie",ty.water,t2=ty.psychic)
class mr_mime(pokemon):
    def __init__(self):
        super().__init__(40,45,65,100,90,mv.confusion(),mv.double_slap(),mv.meditate(),mv.light_screen(),"Mr. Mime",ty.psychic)
class scyther(pokemon):
    def __init__(self):
        super().__init__(70,110,80,55,105,mv.slash(),mv.swords_dance(),mv.agility(),mv.double_team(),"Scyther",ty.bug,t2=ty.flying)
class jynx(pokemon):
    def __init__(self):
        super().__init__(65,50,35,115,95,mv.lovely_kiss(),mv.ice_punch(),mv.body_slam(),mv.blizzard(),"Jynx",ty.ice,t2=ty.psychic)
class electabuzz(pokemon):
    def __init__(self):
        super().__init__(65,83,57,85,105,mv.thunder_punch(),mv.quick_attack(),mv.light_screen(),mv.thunder_wave(),"Electabuzz",ty.electric)
class magmar(pokemon):
    def __init__(self):
        super().__init__(65,95,57,85,93,mv.fire_punch(),mv.smokescreen(),mv.smokescreen(),mv.fire_blast(),"Magmar",ty.fire)
class pinsir(pokemon):
    def __init__():
        super().__init__(65,125,100,55,85,mv.vice_grip(),mv.seismic_toss(),mv.swords_dance(),mv.guillotine(),"Pinsir",ty.bug)
class tauros(pokemon):
    def __init__(self):
        super().__init__(75,100,95,40,110,mv.stomp(),mv.tail_whip(),mv.leer(),mv.take_down(),"Tauros",ty.normal)
class magikarp(pokemon):
    def __init__(self):
        super().__init__(20,10,55,20,80,mv.splash(),mv.tackle(),None,None,"Magikarp",ty.water)
class gyarados(pokemon):
    def __init__(self):
        super().__init__(95,125,79,60,81,mv.bite(),mv.dragon_rage(),mv.hydro_pump(),mv.hyper_beam(),"Gyarados",ty.water,t2=ty.flying)
class lapras(pokemon):
    def __init__(self):
        super().__init__(130,85,80,85,60,mv.body_slam(),mv.confuse_ray(),mv.ice_beam(),mv.hydro_pump(),"Lapras",ty.water,t2=ty.ice)
class ditto(pokemon):
    def __init__(self):
        super().__init__(48,48,48,48,48,mv.transform(),None,None,None,"Ditto",ty.normal)
class eevee(pokemon):
    def __init__(self):
        super().__init__(55,55,50,65,55,mv.tackle(),mv.quick_attack(),mv.tail_whip(),mv.bite(),"Eevee",ty.normal)
class vaporeon(pokemon):
    def __init__(self):
        super().__init__(130,65,60,110,65,mv.hydro_pump(),mv.quick_attack(),mv.bite(),mv.aurora_beam(),"Vaporeon",ty.water)
class jolteon(pokemon):
    def __init__(self):
        super().__init__(65,65,60,110,130,mv.thunder(),mv.quick_attack(),mv.bite(),mv.pin_missile(),"Jolteon",ty.electric)
class flareon(pokemon):
    def __init__(self):
        super().__init__(65,130,60,110,65,mv.fire_blast(),mv.quick_attack(),mv.bite(),mv.body_slam(),"Flareon",ty.fire)
class porygon(pokemon):
    def __init__(self):
        super().__init__(65,60,70,75,40,mv.psybeam(),mv.recover(),mv.thunder_wave(),mv.tri_attack(),"Porygon",ty.normal)
class omanyte(pokemon):
    def __init__(self):
        super().__init__(35,40,100,90,35,mv.water_gun(),mv.ice_beam(),mv.spike_cannon(),mv.rest(),"Omanyte",ty.rock,t2=ty.water)
class omastar(pokemon):
    def __init__(self):
        super().__init__(70,60,125,115,55,mv.surf(),mv.ice_beam(),mv.spike_cannon(),mv.hyper_beam(),"Omastar",ty.rock,t2=ty.water)
class kabuto(pokemon):
    def __init__(self):
        super().__init__(30,80,90,55,45,mv.scratch(),mv.hydro_pump(),mv.rock_slide(),mv.absorb(),"Kabuto",ty.rock,t2=ty.water)
class kabutops(pokemon):
    def __init__(self):
        super().__init__(60,115,105,65,80,mv.scratch(),mv.hydro_pump(),mv.rock_slide(),mv.absorb(),"Kabutops",ty.rock,t2=ty.water)
class aerodactyl(pokemon):
    def __init__(self):
        super().__init__(80,105,65,60,130,mv.hyper_beam(),mv.sky_attack(),mv.take_down(),mv.bite(),"Aerodactyl",ty.rock,t2=ty.flying)
class snorlax(pokemon):
    def __init__(self):
        super().__init__(160,110,65,65,30,mv.hyper_beam(),mv.body_slam(),mv.earthquake(),mv.rest(),"Snorlax",ty.normal)
class articuno(pokemon):
    def __init__(self):
        super().__init__(90,85,100,125,85,mv.blizzard(),mv.fly(),mv.sky_attack(),mv.hyper_beam(),"Articuno",ty.ice,t2=ty.flying)
class zapdos(pokemon):
    def __init__(self):
        super().__init__(90,90,85,125,100,mv.thunder(),mv.fly(),mv.drill_peck(),mv.hyper_beam(),"Zapdos",ty.electric,t2=ty.flying)
class moltres(pokemon):
    def __init__(self):
        super().__init__(90,100,90,125,90,mv.fire_blast(),mv.fly(),mv.sky_attack(),mv.hyper_beam(),"Moltres",ty.fire,t2=ty.flying)
class dratini(pokemon):
    def __init__(self):
        super().__init__(41,64,45,50,50,mv.wrap(),mv.hyper_beam(),mv.thunder_wave(),mv.surf(),"Dratini",ty.dragon)
class dragonair(pokemon):
    def __init__(self):
        super().__init__(61,84,65,70,70,mv.wrap(),mv.hyper_beam(),mv.thunder_wave(),mv.surf(),"Dragonair",ty.dragon)
class dragonite(pokemon):
    def __init__(self):
        super().__init__(91,134,95,100,80,mv.hyper_beam(),mv.fly(),mv.thunder_wave(),mv.surf(),"Dragonite",ty.dragon,t2=ty.flying)
class mewtwo(pokemon):
    def __init__(self):
        super().__init__(106,110,90,154,130,mv.psychic_attack(),mv.blizzard(),mv.thunderbolt(),mv.recover(),"Mewtwo",ty.psychic)
class mew(pokemon):
    def __init__(self):
        super().__init__(100,100,100,100,100,mv.psychica_attack(),mv.blizzard(),mv.thunderbolt(),mv.soft_boiled(),"Mew",ty.psychic)
class missingno(pokemon):
    def __init__(self):
        super().__init__(33,136,0,6,29,mv.water_gun(),mv.water_gun(),mv.sky_attack(),None,"MissingNo",ty.normal)
