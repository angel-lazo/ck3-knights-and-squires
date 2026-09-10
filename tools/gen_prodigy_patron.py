# Generates 100 prodigy patronage memory types, flavor roll, memory create, custom loc, and English loc (UTF-8 BOM).
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FLAVORS = [
    ("the mayor sent a purse after I cleared the bandit camps", "you received a purse after clearing the bandit camps", "received a purse after clearing the bandit camps"),
    ("the merchant guild paid my training after I guarded their caravan", "you were paid for guarding a merchant caravan", "was paid for guarding a merchant caravan"),
    ("the bishop kept me in the yard after I escorted his shrine", "you were kept in training after escorting a shrine", "was kept in training after escorting a shrine"),
    ("the abbot funded my drill after I drove raiders from the monastery", "you were funded after driving raiders from a monastery", "was funded after driving raiders from a monastery"),
    ("the port master paid me after I hunted river pirates", "you were paid after hunting river pirates", "was paid after hunting river pirates"),
    ("the village reeve sent coin after I killed the wolf pack", "you received coin after killing a wolf pack", "received coin after killing a wolf pack"),
    ("the hospice warden paid my keep after I made the pilgrim road safe", "you were kept after making a pilgrim road safe", "was kept after making a pilgrim road safe"),
    ("the lists steward gave me the tourney purse to stay in training", "you were given a tourney purse for training", "was given a tourney purse for training"),
    ("a dying knight left me his last purse for the yard", "a dying knight left you a purse for training", "was left a dying knight's purse for training"),
    ("the court sent a purse in a consort's name to keep me at arms", "the court sent you a purse in a consort's name", "was sent a court purse in a consort's name"),
    ("the cathedral canons paid my training after I stood for their chapter", "the cathedral canons paid your training", "was paid by cathedral canons"),
    ("the bridge warden funded me after I kept the tolls from thieves", "you were funded after keeping a bridge from thieves", "was funded after keeping a bridge from thieves"),
    ("the pit master of the salt works paid me after I held the pits", "you were paid after holding the salt pits", "was paid after holding the salt pits"),
    ("the vinedresser sent gold after I drove thieves from the vines", "you received gold after driving thieves from the vines", "received gold after driving thieves from the vines"),
    ("the flock-reeve paid my keep after I brought the sheep home", "you were paid after bringing the sheep home", "was paid after bringing the sheep home"),
    ("the fair bailiff funded me after I kept the market peace", "you were funded after keeping market peace", "was funded after keeping market peace"),
    ("the forester sent a purse after I hunted the forest outlaws", "you received a purse after hunting forest outlaws", "received a purse after hunting forest outlaws"),
    ("the miller paid my training after I pulled a child from the river", "you were paid after pulling a child from the river", "was paid after pulling a child from the river"),
    ("the fishermen funded me after I drove off sea raiders", "you were funded after driving off sea raiders", "was funded after driving off sea raiders"),
    ("the huntsman kept me in meat and coin after the royal hunt", "you were kept after a royal hunt", "was kept after a royal hunt"),
    ("the infirmarian paid me after I stood between raiders and the leper-house", "you were paid after defending a leper-house", "was paid after defending a leper-house"),
    ("the marcher reeve sent silver after I held a border hamlet", "you received silver after holding a border hamlet", "received silver after holding a border hamlet"),
    ("the cathedral schoolmasters paid my drill after I escorted their pupils", "you were paid after escorting schoolmasters", "was paid after escorting schoolmasters"),
    ("a knight's widow gave me her last gold to keep me in the yard", "a knight's widow paid your training", "was paid by a knight's widow"),
    ("the sacristan funded me after I brought back a stolen reliquary", "you were funded after returning a stolen reliquary", "was funded after returning a stolen reliquary"),
    ("the bakers' guild paid me after I put down a grain riot", "you were paid after putting down a grain riot", "was paid after putting down a grain riot"),
    ("the dyke-reeve sent a purse after I held the broken dike", "you received a purse after holding a broken dike", "received a purse after holding a broken dike"),
    ("the stablemaster funded me after I caught the horse thieves", "you were funded after catching horse thieves", "was funded after catching horse thieves"),
    ("the falconer paid my keep after I recovered a stolen falcon", "you were paid after recovering a stolen falcon", "was paid after recovering a stolen falcon"),
    ("the parish priest sent alms after I calmed a panic in the churchyard", "you received alms after calming a parish panic", "received alms after calming a parish panic"),
    ("the town watch paid me after I ended a riot at the lists", "you were paid after ending a tourney riot", "was paid after ending a tourney riot"),
    ("the customs officer funded me after I broke a smuggling ring", "you were funded after breaking a smuggling ring", "was funded after breaking a smuggling ring"),
    ("the master mason paid me after I pulled men from a quarry fall", "you were paid after a quarry rescue", "was paid after a quarry rescue"),
    ("the pit captain sent gold after I led men out of a mine fire", "you received gold after a mine fire", "received gold after a mine fire"),
    ("the physician paid my training after I escorted the plague-carts", "you were paid after escorting plague-carts", "was paid after escorting plague-carts"),
    ("a foreign envoy funded me after I saved his embassy from ambush", "you were funded after saving an embassy from ambush", "was funded after saving an embassy from ambush"),
    ("the sheriff sent a purse after I put down tax rebels", "you received a purse after putting down tax rebels", "received a purse after putting down tax rebels"),
    ("the herd-lord paid me after I turned back a cattle raid", "you were paid after turning back a cattle raid", "was paid after turning back a cattle raid"),
    ("the bride's kin funded me after I broke an ambush at the wedding", "you were funded after breaking a wedding ambush", "was funded after breaking a wedding ambush"),
    ("the sexton paid my keep after I guarded a funeral procession", "you were paid after guarding a funeral", "was paid after guarding a funeral"),
    ("the librarian monk sent coin after I saved the books from fire", "you received coin after saving a library from fire", "received coin after saving a library from fire"),
    ("the illuminator funded me after I drove thieves from the scriptorium", "you were funded after defending a scriptorium", "was funded after defending a scriptorium"),
    ("the money-changers paid me after I kept their exchange from a mob", "you were paid after keeping the exchange from a mob", "was paid after keeping the exchange from a mob"),
    ("the silk merchants sent a purse after I saw their bales to market", "you received a purse from silk merchants", "received a purse from silk merchants"),
    ("the spice convoy paid my training after I rode as their guard", "you were paid for guarding a spice convoy", "was paid for guarding a spice convoy"),
    ("the amber-traders funded me after I held the coast road", "you were funded after holding the amber coast", "was funded after holding the amber coast"),
    ("the wine barge master paid me after I kept the casks from wreckers", "you were paid after keeping a wine barge from wreckers", "was paid after keeping a wine barge from wreckers"),
    ("the ale-wives sent silver after I cleared their street of bravos", "you received silver after clearing the ale-wives' street", "received silver after clearing the ale-wives' street"),
    ("the masters of arts paid me after I escorted a disputation in peace", "you were paid after escorting a disputation", "was paid after escorting a disputation"),
    ("a hermit of the hills gave me his hoard to keep me at arms", "a hermit paid your training", "was paid by a hermit of the hills"),
    ("the foundling house funded me after I brought their children home", "you were funded after aiding a foundling house", "was funded after aiding a foundling house"),
    ("alms for the blind were pressed into my hand to keep me in the yard", "you received alms after aiding the blind", "received alms after aiding the blind"),
    ("the crutch-maker paid my keep after I stood in his shop against thieves", "you were paid after defending a crutch-maker", "was paid after defending a crutch-maker"),
    ("a smith paid my training after I saved his apprentice from the fire", "you were paid after saving a smith's apprentice", "was paid after saving a smith's apprentice"),
    ("the armorers' guild sent a purse after I kept their forges from a feud", "you received a purse from the armorers' guild", "received a purse from the armorers' guild"),
    ("the fletchers funded me after I guarded their shafts to the muster", "you were funded by the fletchers", "was funded by the fletchers"),
    ("the tanners paid me after I drove ruffians from the pits", "you were paid after driving ruffians from the tanners' pits", "was paid after driving ruffians from the tanners' pits"),
    ("the weavers sent coin after I ended a brawl in their hall", "you received coin after ending a brawl in the weavers' hall", "received coin after ending a brawl in the weavers' hall"),
    ("the dyers funded me after I saved their vats from sabotage", "you were funded after saving the dyers' vats", "was funded after saving the dyers' vats"),
    ("the glassblowers paid my drill after I kept their kiln from a riot", "you were paid after keeping a glass kiln from a riot", "was paid after keeping a glass kiln from a riot"),
    ("the bell-founders sent gold after I held their yard through a fire", "you received gold after a bell-foundry fire", "received gold after a bell-foundry fire"),
    ("the beacon warden funded me after I kept the hill-fire lit", "you were funded after keeping a beacon lit", "was funded after keeping a beacon lit"),
    ("the lighthouse keeper paid me after I pulled wreckers from the rocks", "you were paid after a night at the lighthouse", "was paid after a night at the lighthouse"),
    ("a marsh guide sent a purse after I saw travelers through the fen", "you received a purse after a marsh crossing", "received a purse after a marsh crossing"),
    ("the pass warden funded me after I held the mountain road", "you were funded after holding a mountain pass", "was funded after holding a mountain pass"),
    ("a snowbound priory paid my keep after I brought them food", "you were paid after relieving a snowbound priory", "was paid after relieving a snowbound priory"),
    ("well-keepers sent coin after I held the water against raiders", "you received coin after holding a well", "received coin after holding a well"),
    ("both hosts at a ford paid me to keep the crossing from slaughter", "you were paid to keep a ford from slaughter", "was paid to keep a ford from slaughter"),
    ("the defenders of a broken siege sent their last purse for my training", "you received a defenders' purse after a broken siege", "received a defenders' purse after a broken siege"),
    ("the garrison funded me after I led a sortie under the walls", "you were funded after a sortie under the walls", "was funded after a sortie under the walls"),
    ("a family paid my drill after I helped ransom their squire", "you were paid after helping ransom a squire", "was paid after helping ransom a squire"),
    ("the banner-bearer of a host sent gold after I brought their color home", "you received gold after returning a stolen banner", "received gold after returning a stolen banner"),
    ("the market paid me after I killed a bear that broke its stall", "you were paid after killing a bear in the market", "was paid after killing a bear in the market"),
    ("the lane's folk funded me after I put down a mad dog", "you were funded after putting down a mad dog", "was funded after putting down a mad dog"),
    ("the chapter paid my keep after I held the crowd when a gallery fell", "you were paid after a church gallery fell", "was paid after a church gallery fell"),
    ("the relic-bearers funded me after I walked in their translation", "you were funded after a relic translation", "was funded after a relic translation"),
    ("Palm Sunday alms were given me after I kept the procession whole", "you received Palm Sunday alms for keeping a procession", "received Palm Sunday alms for keeping a procession"),
    ("Christmas alms were sent to keep me in the yard through winter", "you received Christmas alms for training", "received Christmas alms for training"),
    ("the Easter sepulchre wardens paid me after I guarded the watch", "you were paid after guarding the Easter sepulchre", "was paid after guarding the Easter sepulchre"),
    ("the parish funded me after I beat the bounds in peace", "you were funded after beating the bounds", "was funded after beating the bounds"),
    ("the midsummer fair paid my training after I kept the booths from fire", "you were paid after a midsummer fair", "was paid after a midsummer fair"),
    ("harvest home sent a purse after I walked the last wagons in", "you received a harvest-home purse", "received a harvest-home purse"),
    ("the Martinmas butchers funded me after I kept the slaughter-yard", "you were funded after Martinmas slaughter", "was funded after Martinmas slaughter"),
    ("Candlemas alms were pressed on me after I lit the way for the poor", "you received Candlemas alms", "received Candlemas alms"),
    ("shipwreck survivors gave me what they had left for my training", "shipwreck survivors paid your training", "was paid by shipwreck survivors"),
    ("castaways sent coin once they had a roof, to keep me at arms", "castaways paid your training", "was paid by castaways"),
    ("freed corsair captives funded me from their first wages", "freed captives paid your training", "was paid by freed corsair captives"),
    ("the mint paid me after I took a nest of false coiners", "you were paid after taking false coiners", "was paid after taking false coiners"),
    ("the ridge wardens sent a purse after I cleared the highway", "you received a purse after clearing a ridge highway", "received a purse after clearing a ridge highway"),
    ("folk left a purse at a haunted mill after I slept there and lived", "you received a folk purse after a night in a haunted mill", "received a folk purse after a night in a haunted mill"),
    ("the orchard-keeper funded me after I drove off the night-thieves", "you were funded after driving orchard thieves", "was funded after driving orchard thieves"),
    ("ice-cutters paid my keep after I pulled a team from the river", "you were paid after pulling a team from river ice", "was paid after pulling a team from river ice"),
    ("charcoal burners sent silver after I kept their pits from outlaws", "you received silver from charcoal burners", "received silver from charcoal burners"),
    ("the bee-keepers funded me after I stood between raiders and the hives", "you were funded after defending bee-hives", "was funded after defending bee-hives"),
    ("a potter paid my drill after I saved his kiln from a spark-fire", "you were paid after saving a potter's kiln", "was paid after saving a potter's kiln"),
    ("the shipyard funded me after I kept the rope-walk from a feud", "you were funded after a shipyard feud", "was funded after a shipyard feud"),
    ("leper-bell walkers sent alms after I walked the road with them", "you received alms after walking the leper-bell road", "received alms after walking the leper-bell road"),
    ("an anonymous purse was left at my door to keep me in training", "an anonymous purse was left for your training", "was left an anonymous purse for training"),
    ("a military preceptory sent alms after I rode as their guest-guard", "a preceptory paid your training", "was paid by a military preceptory"),
    ("the nuns' dower from a cloister garden was given to keep me at arms", "a cloister paid your training from a nuns' dower", "was paid from a nuns' dower"),
]

assert len(FLAVORS) == 100, len(FLAVORS)


def pad(i):
    return f"{i:03d}"


def mem_block(i):
    n = pad(i)
    return f"""kns_prodigy_patron_{n} = {{
	categories = {{ positive martial }}
	icon = "martial.dds"
	description = {{ desc = kns_prodigy_patron_{n}_desc }}
	second_perspective_description = {{ desc = kns_prodigy_patron_{n}_desc_second }}
	third_perspective_description = {{ desc = kns_prodigy_patron_{n}_desc_third }}
	duration = {{ years = 75 }}
}}
"""


def flavor_roll_entry(i):
    n = i
    return f"""		1 = {{
			modifier = {{
				factor = 0
				exists = var:kns_last_patron_flavor
				var:kns_last_patron_flavor = {n}
			}}
			set_variable = {{ name = kns_patron_flavor value = {n} }}
		}}"""


def memory_create_entry(i):
    n = pad(i)
    return f"""	else_if = {{
		limit = {{ var:kns_patron_flavor = {i} }}
		create_character_memory = {{
			type = kns_prodigy_patron_{n}
		}}
	}}"""


def custom_loc_entry(i, first):
    return f"""	text = {{
		trigger = {{ var:kns_patron_flavor = {i} }}
		localization_key = kns_prodigy_patron_story_{pad(i)}
	}}"""


mem_txt = "# Generated. Do not edit by hand; run tools/gen_prodigy_patron.py\n\n"
mem_txt += "".join(mem_block(i) for i in range(1, 101))

roll_parts = "\n".join(flavor_roll_entry(i) for i in range(1, 101))
create_first = f"""	if = {{
		limit = {{ var:kns_patron_flavor = 1 }}
		create_character_memory = {{
			type = kns_prodigy_patron_001
		}}
	}}
"""
create_rest = "\n".join(memory_create_entry(i) for i in range(2, 101))

effects = f"""# Generated. Do not edit by hand; run tools/gen_prodigy_patron.py

kns_roll_prodigy_patron_flavor_effect = {{
	random_list = {{
{roll_parts}
	}}
	set_variable = {{
		name = kns_last_patron_flavor
		value = var:kns_patron_flavor
	}}
}}

kns_create_prodigy_patron_memory_effect = {{
{create_first}{create_rest}
}}
"""

custom = "# Generated. Do not edit by hand; run tools/gen_prodigy_patron.py\n\n"
custom += "KnsProdigyPatronStory = {\n\ttype = character\n"
custom += "\n".join(custom_loc_entry(i, FLAVORS[i - 1][0]) for i in range(1, 101))
custom += """
	text = {
		localization_key = kns_prodigy_patron_story_fallback
	}
}
"""

loc_lines = ["l_english:"]
loc_lines.append(' kns_prodigy_patron_story_fallback:0 "A nameless purse was sent to keep this knight in training."')
for i, (first, second, third) in enumerate(FLAVORS, 1):
    n = pad(i)
    loc_lines.append(f' kns_prodigy_patron_{n}_desc:0 "I remember how {first}."')
    loc_lines.append(f' kns_prodigy_patron_{n}_desc_second:0 "You remember how {second}."')
    loc_lines.append(f' kns_prodigy_patron_{n}_desc_third:0 "[owner.GetShortUIName|U] {third}."')
    loc_lines.append(f' kns_prodigy_patron_story_{n}:0 "{first[0].upper() + first[1:]}."')

loc_body = "\n".join(loc_lines) + "\n"

(ROOT / "common/character_memory_types/kns_prodigy_patron_memories.txt").write_text(mem_txt, encoding="utf-8")
(ROOT / "common/scripted_effects/kns_prodigy_patron_generated_effects.txt").write_text(effects, encoding="utf-8")
(ROOT / "common/customizable_localization/kns_prodigy_patron_custom_loc.txt").write_text(custom, encoding="utf-8")
loc_path = ROOT / "localization/english/kns_prodigy_patron_l_english.yml"
loc_path.write_bytes(b"\xef\xbb\xbf" + loc_body.encode("utf-8"))
print("wrote 100 flavors")
