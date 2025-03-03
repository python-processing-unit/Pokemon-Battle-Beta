import pokemon as pkmn
import random
#gym leaders
def brock():
    return([pkmn.geodude(),pkmn.onix(),pkmn.kabuto()])
def misty():
    return([pkmn.starmie(),pkmn.golduck(),pkmn.seaking()])
def lt_surge():
    return([pkmn.raichu(),pkmn.magneton(),pkmn.electrode()])
def erika():
    return([pkmn.vileplume(),pkmn.tangela(),pkmn.victreebel()])
def koga():
    return([pkmn.muk(),pkmn.weezing(),pkmn.venomoth()])
def sabrina():
    return([pkmn.alakazam(),pkmn.mr_mime(),pkmn.hypno()])
def blaine():
    if(random.randint(1,1000)==1):
       return([pkmn.mewtwo(),pkmn.rapidash(),pkmn.ninetales()])#Pokémon Adventures/Pokémon SP easter egg
    else:
        return([pkmn.arcanine(),pkmn.rapidash(),pkmn.ninetales()])
def giovanni():
    return([pkmn.rhydon(),pkmn.dugtrio(),pkmn.nidoking()])
#elite four
def lorelei():
    return([pkmn.dewgong(),pkmn.cloyster(),pkmn.lapras()])
def bruno():
    return([pkmn.hitmonlee(),pkmn.machamp(),pkmn.onix()])
def agatha():
    return([pkmn.gengar(),pkmn.arbok(),pkmn.haunter()])
def lance():
    return([pkmn.dragonite(),pkmn.aerodactyl(),pkmn.gyarados()])
#other notable trainers
def blue():
    return([pkmn.exeggutor(),pkmn.arcanine,pkmn.alakazam()])
def red():
    return([pkmn.venusaur(),pkmn.charizard(),pkmn.blastoise()])
def professor_oak():
    return([pkmn.tauros(),pkmn.exeggutor(),pkmn.arcanine()])
trainer_list = [brock(),misty(),lt_surge(),erika(),koga(),sabrina(),blaine(),giovanni(),lorelei(),bruno(),agatha(),lance(),blue(),red(),professor_oak()]
trainer_names = ["Brock","Misty","Lt. Surge","Erika","Koga","Sabrina","Blaine","Giovanni","Lorelei","Bruno","Agatha","Lance","Blue","Red","Professor Oak"]
