import type_matrix as ty
normal = ty.normal
fighting = ty.fighting
flying = ty.flying
poison = ty.poison
ground = ty.ground
rock = ty.rock
bug = ty.bug
ghost = ty.ghost
fire = ty.fire
water = ty.water
grass = ty.grass
electric = ty.electric
psychic = ty.psychic
ice = ty.ice
dragon = ty.dragon
na = None
class move():
    def __init__(self,move_t,damage,acc,nm,s1=False,d1=None,s2=False,d2=None,s3=False,d3=None):
        self.move_type = move_t
        self.power = damage
        self.accuracy = acc
        self.stat1 = s1
        self.stat2 = s2
        self.stat3 = s3
        self.dif1 = d1
        self.dif2 = d2
        self.dif3 = d3
        self.name = nm
#list of moves, alphabeticaly
class absorb(move):
    def __init__(self):
        super().__init__(grass,20,100,"Absorb")
class acid(move):
    def __init__(self):
        super().__init__(poison,40,100,"Acid")
class acid_armor(move):
    def __init__(self):
        super().__init__(poison,na,na,"Acid Armor",s1=1,d1=2)
class agility(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Agility")
class amnesia(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Amnesia")
class aurora_beam(move):
    def __init__(self):
        super().__init__(ice,65,100,"Aurora Beam")
class barrage(move):
    def __init__(self):
        super().__init__(normal,15,85,"Barrage")
class barrier(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Barrier")
class bide(move):
    def __init__(self):
        super().__init__(normal,na,100,"Bide")
class bind(move):
    def __init__(self):
        super().__init__(normal,15,85,"Bind")
class bite(move):
    def __init__(self):
        super().__init__(normal,60,100,"Bite")
class blizzard(move):
    def __init__(self):
        super().__init__(ice,120,90,"Blizzard")
class body_slam(move):
    def __init__(self):
        super().__init__(normal,85,100,"Body Slam")
class bone_club(move):
    def __init__(self):
        super().__init__(ground,65,85,"Bone Club")
class bonemerang(move):
    def __init__(self):
        super().__init__(ground,50,90,"Bonemerang")
class bubble(move):
    def __init__(self):
        super().__init__(water,20,100,"Bubble")
class bubble_beam(move):
    def __init__(self):
        super().__init__(water,65,100,"Bubble Beam")
class clamp(move):
    def __init__(self):
        super().__init__(water,35,75,"Clamp")
class comet_punch(move):
    def __init__(self):
        super().__init__(normal,18,85,"Comet Punch")
class confuse_ray(move):
    def __init__(self):
        super().__init__(ghost, na, 100, "Confuse Ray")
class confusion(move):
    def __init__(self):
        super().__init__(psychic,50,100,"Confusion")
class constrict(move):
    def __init__(self):
        super().__init__(normal,10,100,"Constrict")
class conversion(move):
    def __init__(self):
        super().__init__(normal,na,100,"Conversion")
class counter(move):
    def __init__(self):
        super().__init__(fighting,na,100,"Counter")
class crabhammer(move):
    def __init__(self):
        super().__init__(water,90,85,"Crabhammer")
class cross_chop(move):
    def __init__(self):
        super().__init__(fighting,100,80,"Cross Chop")
class cut(move):
    def __init__(self):
        super().__init__(normal,50,95,"Cut")
class defense_curl(move):
    def __init__(self):
        super().__init__(normal,na,100,"Defense Curl")
class dig(move):
    def __init__(self):
        super().__init__(ground,100,100,"Dig")
class disable(move):
    def __init__(self):
        super().__init__(normal,na,55,"Disable")
class dizzy_punch(move):
    def __init__(self):
        super().__init__(normal,70,100,"Dizzy Punch")
class double_kick(move):
    def __init__(self):
        super().__init__(fighting,30,100,"Double Kick")
class double_slap(move):
    def __init__(self):
        super().__init__(normal,15,85,"Double Slap")
class double_team(move):
    def __init__(self):
        super().__init__(normal,na,100,"Double Team")
class double_edge(move):
    def __init__(self):
        super().__init__(normal,100,100,"Double-Edge")
class dragon_rage(move):
    def __init__(self):
        super().__init__(dragon,na,100,"Dragon Rage")
class dream_eater(move):
    def __init__(self):
        super().__init__(psychic,100,100,"Dream Eater")
class drill_peck(move):
    def __init__(self):
        super().__init__(flying,80,100,"Drill Peck")
class dynamic_punch(move):
    def __init__(self):
        super().__init__(fighting,100,50,"Dynamic Punch")
class earthquake(move):
    def __init__(self):
        super().__init__(ground,100,100,"Earthquake")
class egg_bomb(move):
    def __init__(self):
        super().__init__(normal,100,75,"Egg Bomb")
class ember(move):
    def __init__(self):
        super().__init__(fire,40,100,"Ember")
class explosion(move):
    def __init__(self):
        super().__init__(normal,170,100,"Explosion")
class extreme_speed(move):
    def __init__(self):
        super().__init__(normal,80,100,"Extreme Speed")
class feather_dance(move):
    def __init__(self):
        super().__init__(flying, na, 100, "Feather Dance", s1=2, d1=-2)
class fire_blast(move):
    def __init__(self):
        super().__init__(fire,120,85,"Fire Blast")
class fire_punch(move):
    def __init__(self):
        super().__init__(fire,75,100,"Fire Punch")
class fire_spin(move):
    def __init__(self):
        super().__init__(fire,15,70,"Fire Spin")
class fissure(move):
    def __init__(self):
        super().__init__(ground,na,30,"Fissure")
class flamethrower(move):
    def __init__(self):
        super().__init__(fire,95,100,"Flamethrower")
class flash(move):
    def __init__(self):
        super().__init__(normal,na,70,"Flash")
class fly(move):
    def __init__(self):
        super().__init__(flying,70,95,"Fly")
class focus_energy(move):
    def __init__(self):
        super().__init__(normal,na,100,"Focus Energy")
class fury_attack(move):
    def __init__(self):
        super().__init__(normal,15,85,"Fury Attack")
class fury_swipes(move):
    def __init__(self):
        super().__init__(normal,18,80,"Fury Swipes")
class glare(move):
    def __init__(self):
        super().__init__(normal,na,75,"Glare")
class growl(move):
    def __init__(self):
        super().__init__(normal,na,100,"Growl")
class growth(move):
    def __init__(self):
        super().__init__(normal,na,100,"Growth")
class guillotine(move):
    def __init__(self):
        super().__init__(normal,na,30,"Guillotine")
class gust(move):
    def __init__(self):
        super().__init__(flying,40,100,"Gust")
class harden(move):
    def __init__(self):
        super().__init__(normal,na,100,"Harden")
class haze(move):
    def __init__(self):
        super().__init__(ice,na,100,"Haze")
class headbutt(move):
    def __init__(self):
        super().__init__(normal,70,100,"Headbutt")
class high_jump_kick(move):
    def __init__(self):
        super().__init__(fighting,85,90,"High Jump Kick")
class horn_attack(move):
    def __init__(self):
        super().__init__(normal,65,100,"Horn Attack")
class horn_drill(move):
    def __init__(self):
        super().__init__(normal,na,30,"Horn Drill")
class hydro_pump(move):
    def __init__(self):
        super().__init__(water,120,80,"Hydro Pump")
class hyper_beam(move):
    def __init__(self):
        super().__init__(normal,150,90,"Hyper Beam")
class hyper_fang(move):
    def __init__(self):
        super().__init__(normal,80,90,"Hyper Fang")
class hypnosis(move):
    def __init__(self):
        super().__init__(psychic,na,60,"Hypnosis")
class ice_beam(move):
    def __init__(self):
        super().__init__(ice,95,100,"Ice Beam")
class ice_punch(move):
    def __init__(self):
        super().__init__(ice,75,100,"Ice Punch")
class jump_kick(move):
    def __init__(self):
        super().__init__(fighting,70,95,"Jump Kick")
class karate_chop(move):
    def __init__(self):
        super().__init__(normal,50,100,"Karate Chop")
class kinesis(move):
    def __init__(self):
        super().__init__(psychic,na,80,"Kinesis")
class leech_life(move):
    def __init__(self):
        super().__init__(bug,20,100,"Leech Life")
class leech_seed(move):
    def __init__(self):
        super().__init__(grass,na,90,"Leech Seed")
class leer(move):
    def __init__(self):
        super().__init__(normal,na,100,"Leer")
class lick(move):
    def __init__(self):
        super().__init__(ghost,20,100,"Lick")
class light_screen(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Light Screen")
class lovely_kiss(move):
    def __init__(self):
        super().__init__(normal,na,75,"Lovely Kiss")
class low_kick(move):
    def __init__(self):
        super().__init__(fighting,50,90,"Low Kick")
class meditate(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Meditate")
class mega_drain(move):
    def __init__(self):
        super().__init__(grass,40,100,"Mega Drain")
class mega_kick(move):
    def __init__(self):
        super().__init__(normal,120,75,"Mega Kick")
class mega_punch(move):
    def __init__(self):
        super().__init__(normal,80,85,"Mega Punch")
class metronome(move):
    def __init__(self):
        super().__init__(normal,na,100,"Metronome")
class mimic(move):
    def __init__(self):
        super().__init__(normal,na,100,"Mimic")
class minimize(move):
    def __init__(self):
        super().__init__(normal,na,100,"Minimize")
class mirror_move(move):
    def __init__(self):
        super().__init__(flying,na,100,"Mirror Move")
class mist(move):
    def __init__(self):
        super().__init__(ice,na,100,"Mist")
class moonblast(move):
    def __init__(self):
        super().__init__(normal,95,100,"Moonblast")
class night_shade(move):
    def __init__(self):
        super().__init__(ghost,na,100,"Night Shade")
class pay_day(move):
    def __init__(self):
        super().__init__(normal,40,100,"Pay Day")
class peck(move):
    def __init__(self):
        super().__init__(flying,35,100,"Peck")
class petal_dance(move):
    def __init__(self):
        super().__init__(grass,70,100,"Petal Dance")
class pin_missile(move):
    def __init__(self):
        super().__init__(bug,14,85,"Pin Missile")
class poison_fang(move):
    def __init__(self):
        super().__init__(poison, 50, 100, "Poison Fang")
class poison_gas(move):
    def __init__(self):
        super().__init__(poison,na,55,"Poison Gas")
class poison_sting(move):
    def __init__(self):
        super().__init__(poison,15,100,"Poison Sting")
class poison_powder(move):
    def __init__(self):
        super().__init__(poison,na,75,"Poison Powder")
class pound(move):
    def __init__(self):
        super().__init__(normal,40,100,"Pound")
class pursuit(move):
    def __init__(self):
        super().__init__(normal, 40, 100, "Pursuit")
class psybeam(move):
    def __init__(self):
        super().__init__(psychic,65,100,"Psybeam")
class psychic_attack(move):
    def __init__(self):
        super().__init__(psychic,90,100,"Psychic")
class psywave(move):
    def __init__(self):
        super().__init__(psychic,na,80,"Psywave")
class quick_attack(move):
    def __init__(self):
        super().__init__(normal,40,100,"Quick Attack")
class rage(move):
    def __init__(self):
        super().__init__(normal,20,100,"Rage")
class razor_leaf(move):
    def __init__(self):
        super().__init__(grass,55,95,"Razor Leaf")
class razor_wind(move):
    def __init__(self):
        super().__init__(normal,80,100,"Razor Wind")
class recover(move):
    def __init__(self):
        super().__init__(normal,na,100,"Recover")
class reflect(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Reflect")
class rest(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Rest")
class roar(move):
    def __init__(self):
        super().__init__(normal,na,100,"Roar")
class rock_slide(move):
    def __init__(self):
        super().__init__(rock,75,90,"Rock Slide")
class rock_throw(move):
    def __init__(self):
        super().__init__(rock,50,90,"Rock Throw")
class rolling_kick(move):
    def __init__(self):
        super().__init__(fighting,60,85,"Rolling Kick")
class sand_attack(move):
    def __init__(self):
        super().__init__(normal,na,100,"Sand Attack")
class scratch(move):
    def __init__(self):
        super().__init__(normal,40,100,"Scratch")
class screech(move):
    def __init__(self):
        super().__init__(normal,na,85,"Screech")
class seismic_toss(move):
    def __init__(self):
        super().__init__(fighting,na,100,"Seismic Toss")
class self_destruct(move):
    def __init__(self):
        super().__init__(normal,130,100,"Self-Destruct")
class sharpen(move):
    def __init__(self):
        super().__init__(normal,na,100,"Sharpen")
class sing(move):
    def __init__(self):
        super().__init__(normal,na,55,"Sing")
class skull_bash(move):
    def __init__(self):
        super().__init__(normal,100,100,"Skull Bash")
class sky_attack(move):
    def __init__(self):
        super().__init__(flying,140,90,"Sky Attack")
class slam(move):
    def __init__(self):
        super().__init__(normal,80,75,"Slam")
class slash(move):
    def __init__(self):
        super().__init__(normal,70,100,"Slash")
class sleep_powder(move):
    def __init__(self):
        super().__init__(grass,na,75,"Sleep Powder")
class sludge(move):
    def __init__(self):
        super().__init__(poison,65,100,"Sludge")
class smog(move):
    def __init__(self):
        super().__init__(poison,20,70,"Smog")
class smokescreen(move):
    def __init__(self):
        super().__init__(normal,na,100,"Smokescreen")
class soft_boiled(move):
    def __init__(self):
        super().__init__(normal,na,100,"Soft-Boiled")
class solar_beam(move):
    def __init__(self):
        super().__init__(grass,120,100,"Solar Beam")
class sonic_boom(move):
    def __init__(self):
        super().__init__(normal,na,90,"Sonic Boom")
class spike_cannon(move):
    def __init__(self):
        super().__init__(normal,20,100,"Spike Cannon")
class splash(move):
    def __init__(self):
        super().__init__(normal,na,100,"Splash")
class spore(move):
    def __init__(self):
        super().__init__(grass,na,100,"Spore")
class stomp(move):
    def __init__(self):
        super().__init__(normal,65,100,"Stomp")
class strength(move):
    def __init__(self):
        super().__init__(normal,80,100,"Strength")
class string_shot(move):
    def __init__(self):
        super().__init__(bug,na,95,"String Shot")
class struggle(move):
    def __init__(self):
        super().__init__(normal,50,100,"Struggle")
class stun_spore(move):
    def __init__(self):
        super().__init__(grass,na,75,"Stun Spore")
class submission(move):
    def __init__(self):
        super().__init__(fighting,80,80,"Submission")
class substitute(move):
    def __init__(self):
        super().__init__(normal,na,100,"Substitute")
class super_fang(move):
    def __init__(self):
        super().__init__(normal,na,90,"Super Fang")
class supersonic(move):
    def __init__(self):
        super().__init__(normal,na,55,"Supersonic")
class surf(move):
    def __init__(self):
        super().__init__(water,95,100,"Surf")
class swift(move):
    def __init__(self):
        super().__init__(normal,60,100,"Swift")
class swords_dance(move):
    def __init__(self):
        super().__init__(normal,na,100,"Swords Dance")
class tackle(move):
    def __init__(self):
        super().__init__(normal,35,95,"Tackle")
class tail_whip(move):
    def __init__(self):
        super().__init__(normal,na,100,"Tail Whip")
class tackle(move):
    def __init__(self):
        super().__init__(normal,35,95,"Tackle")
class tail_whip(move):
    def __init__(self):
        super().__init__(normal,na,100,"Tail Whip")
class take_down(move):
    def __init__(self):
        super().__init__(normal,90,85,"Take Down")
class teleport(move):
    def __init__(self):
        super().__init__(psychic,na,100,"Teleport")
class thrash(move):
    def __init__(self):
        super().__init__(normal,90,100,"Thrash")
class thunder(move):
    def __init__(self):
        super().__init__(electric,120,70,"Thunder")
class thunder_punch(move):
    def __init__(self):
        super().__init__(electric,75,100,"Thunder Punch")
class thunder_shock(move):
    def __init__(self):
        super().__init__(electric,40,100,"Thunder Shock")
class thunder_wave(move):
    def __init__(self):
        super().__init__(electric,na,90,"Thunder Wave")
class thunderbolt(move):
    def __init__(self):
        super().__init__(electric,95,100,"Thunderbolt")
class toxic(move):
    def __init__(self):
        super().__init__(poison,na,90,"Toxic")
class transform(move):
    def __init__(self):
        super().__init__(normal,na,100,"Transform")
class tri_attack(move):
    def __init__(self):
        super().__init__(normal,80,100,"Tri Attack")
class twineedle(move):
    def __init__(self):
        super().__init__(bug,25,100,"Twineedle")
class vice_grip(move):
    def __init__(self):
        super().__init__(normal,55,100,"Vice Grip")
class vine_whip(move):
    def __init__(self):
        super().__init__(grass,35,100,"Vine Whip")
class water_gun(move):
    def __init__(self):
        super().__init__(water,40,100,"Water Gun")
class waterfall(move):
    def __init__(self):
        super().__init__(water,80,100,"Waterfall")
class whirlwind(move):
    def __init__(self):
        super().__init__(normal,na,85,"Whirlwind")
class wing_attack(move):
    def __init__(self):
        super().__init__(flying,35,100,"Wing Attack")
class withdraw(move):
    def __init__(self):
        super().__init__(water,na,100,"Withdraw")
class wrap(move):
    def __init__(self):
        super().__init__(normal,15,85,"Wrap")
