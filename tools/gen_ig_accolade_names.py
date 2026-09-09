from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAMES = {
    "axe": [
        "Felling Crown",
        "Crescent Bit",
        "Timber Warden",
        "Blooded Hewer",
        "Imperial Cleaver",
        "Oakbreaker",
        "War-Hatchet",
        "Raven's Bite",
        "Stone Hewer",
        "Red Axe",
        "Gate-Splitter",
        "Winter Chop",
        "Boar's Tooth",
        "High Hewer",
        "Ash-Cutter",
        "Shield-Biter",
        "Moon Bit",
        "Iron Crescent",
        "Hall-Breaker",
        "Wolf Hatchet",
        "Pile-Driver",
        "Saint's Hewer",
        "Bronze Bit",
        "Siege Axe",
        "Greenwood",
        "Skull-Notch",
        "Border Hewer",
        "Deep Cut",
        "Emperor's Hatchet",
        "Hill-Splitter",
        "Frost Bit",
        "Banner Axe",
        "Pale Hewer",
        "Chain-Breaker",
        "Grove Warden",
        "Black Bit",
        "Keep-Cutter",
        "Oath Hatchet",
        "Thunder Hewer",
        "Salt Axe",
        "Vigil Bit",
        "Long-Haft",
        "Martyr's Hewer",
        "Gold Crescent",
        "Watch-Cleaver",
        "Night Hatchet",
        "River Axe",
        "Proud Hewer",
        "Ivory Bit",
        "Unyielding Chop",
    ],
    "hammer": [
        "Anvil Oath",
        "Thunder Maul",
        "Bell-Striker",
        "Forge Warden",
        "Imperial Maul",
        "Stone-Singer",
        "War Hammer",
        "Crown Crusher",
        "Smith-King",
        "Iron Peal",
        "Gate-Breaker",
        "Saint's Maul",
        "Mountain Hammer",
        "Gold Anvil",
        "Law-Giver",
        "Keep-Smasher",
        "Dawn Maul",
        "Bronze Peal",
        "Wall-Breaker",
        "Oath Hammer",
        "Storm-Striker",
        "Silent Forge",
        "Ivory Maul",
        "Banner Hammer",
        "Deep Strike",
        "High Anvil",
        "Winter Maul",
        "Faith-Striker",
        "Pale Hammer",
        "Eagle's Peal",
        "Vault-Breaker",
        "Red Forge",
        "Vigil Maul",
        "Marble Strike",
        "Thorn Hammer",
        "Night Peal",
        "Bound Anvil",
        "River Maul",
        "Proud Strike",
        "Chapel Hammer",
        "Ash Forge",
        "Lion's Maul",
        "Swift Hammer",
        "Hollow Peal",
        "Emperor's Anvil",
        "White Maul",
        "Last Strike",
        "Mosaic Hammer",
        "Watch-Forge",
        "Unbroken Bell",
    ],
    "sword": [
        "Gilded Edge",
        "Lion Brand",
        "Imperial Brand",
        "Silver Cut",
        "Crown's Blade",
        "Oathsteel",
        "Dawn Sabre",
        "Vigil Edge",
        "Eagle's Brand",
        "Saint's Sword",
        "Ivory Hilt",
        "Red Marcher",
        "Night Watch Brand",
        "High Guard",
        "Pearl Edge",
        "Wrath of Kings",
        "Quiet Blade",
        "Sunsteel",
        "Banner Cut",
        "Thorn of Empire",
        "Pale Brand",
        "River Edge",
        "Falcon Sword",
        "Last Ward",
        "Goldthread",
        "Keep's Honour",
        "Winter Brand",
        "Mercy Cut",
        "Ashen Edge",
        "Dragon's Line",
        "Courtly Brand",
        "Swift Justice",
        "Marble Edge",
        "Vowkeeper",
        "Eastern Brand",
        "Hollow Crown Cut",
        "Basilica Edge",
        "Rose Steel",
        "Bound Oath",
        "White Company",
        "Heir's Brand",
        "Storm Cut",
        "Mosaic Edge",
        "Proud Watch",
        "Laurel Brand",
        "Silent Guard",
        "Copper Edge",
        "Triumph Brand",
        "Chapel Steel",
        "Unbroken Line",
    ],
    "spear": [
        "Long Point",
        "Imperial Pike",
        "Lance of Dawn",
        "Ward-Spear",
        "Eagle's Reach",
        "Saint's Pike",
        "Gold Point",
        "Wall of Shafts",
        "Huntress Line",
        "Red Lance",
        "Keep-Pike",
        "Moon Point",
        "Border Spear",
        "Ivory Shaft",
        "High Guard Pike",
        "Boar-Stick",
        "River Point",
        "Banner Lance",
        "Pale Spear",
        "Thorn Pike",
        "Vigil Point",
        "Lion's Lance",
        "Deep Reach",
        "Chapel Pike",
        "Ash Spear",
        "Crown Point",
        "Night Lance",
        "Bound Shaft",
        "Winter Pike",
        "Falcon Point",
        "Gate-Pike",
        "Mercy Point",
        "Bronze Lance",
        "Proud Shaft",
        "Hollow Spear",
        "Emperor's Reach",
        "White Pike",
        "Last Point",
        "Mosaic Lance",
        "Watch-Spear",
        "Salt Pike",
        "Swift Point",
        "Martyr's Lance",
        "Gold Shaft",
        "Hill-Pike",
        "Quiet Point",
        "Storm Lance",
        "Laurel Pike",
        "Far Ward",
        "Horizon Pike",
    ],
    "mace": [
        "Iron Orb",
        "Holy Flail",
        "Skull-Cracker",
        "Law-Mace",
        "Imperial Knob",
        "Saint's Orb",
        "Gold Flail",
        "Crown-Smasher",
        "Chapel Mace",
        "Red Orb",
        "Gate-Mace",
        "Dawn Flail",
        "Ivory Head",
        "High Justice",
        "Thorn Mace",
        "Vigil Orb",
        "Lion's Club",
        "Deep Blow",
        "Banner Mace",
        "Pale Orb",
        "Faith-Flail",
        "Keep-Breaker",
        "Bronze Knob",
        "Oath-Mace",
        "Night Orb",
        "Bound Flail",
        "Winter Mace",
        "Eagle's Head",
        "Vault-Mace",
        "Proud Orb",
        "River Flail",
        "Marble Head",
        "Emperor's Justice",
        "White Mace",
        "Last Blow",
        "Mosaic Orb",
        "Watch-Mace",
        "Salt Flail",
        "Swift Blow",
        "Hollow Crown",
        "Laurel Mace",
        "Quiet Orb",
        "Storm Flail",
        "Martyr's Head",
        "Gold Knob",
        "Hill-Mace",
        "Ash Orb",
        "Far Justice",
        "Unyielding Blow",
        "Courtly Mace",
    ],
}

WEAPONS = ["axe", "hammer", "sword", "spear", "mace"]


NICK_DESC = "Chosen as the title of this Imperial Guard Accolade."


def nick_id(weapon: str, i: int) -> str:
    return f"nick_kns_ig_acc_{weapon}_{i:02d}"


def write_loc() -> None:
    lines = ["l_english:"]
    for weapon in WEAPONS:
        names = NAMES[weapon]
        if len(names) != 50:
            raise SystemExit(f"{weapon} has {len(names)} names, need 50")
        for i, name in enumerate(names, start=1):
            lines.append(f' kns_ig_acc_{weapon}_{i:02d}:0 "{name}"')
            lines.append(f' kns_ig_acc_{weapon}_{i:02d}_armor:0 "{name}\'s Armor"')
            nid = nick_id(weapon, i)
            lines.append(f' {nid}:0 "{name}"')
            lines.append(f' {nid}_desc:0 "{NICK_DESC}"')
    path = ROOT / "localization" / "english" / "kns_ig_accolade_names_l_english.yml"
    text = "\n".join(lines) + "\n"
    path.write_bytes(b"\xef\xbb\xbf" + text.encode("utf-8"))
    print("wrote", path)


def write_nicknames() -> None:
    lines = [
        "#############################################\n",
        "# Imperial Guard Accolade titles as nicknames\n",
        "#############################################\n",
        "\n",
    ]
    for weapon in WEAPONS:
        for i in range(1, 51):
            lines.append(f"{nick_id(weapon, i)} = {{}}\n")
        lines.append("\n")
    path = ROOT / "common" / "nicknames" / "kns_ig_accolade_nicknames.txt"
    path.write_text("".join(lines), encoding="utf-8", newline="\n")
    print("wrote", path)


def append_title_block(chunks: list[str], name: str, idx_var: str, fallback: str) -> None:
    chunks.append(f"{name} = {{\n")
    chunks.append("	type = character\n")
    chunks.append("	random_valid = no\n")
    for weapon in WEAPONS:
        for i in range(1, 51):
            chunks.append(
                "	text = {\n"
                "		trigger = {\n"
                f"			has_character_flag = kns_ig_post_{weapon}\n"
                f"			var:{idx_var} = {i}\n"
                "		}\n"
                f"		localization_key = kns_ig_acc_{weapon}_{i:02d}\n"
                "	}\n"
            )
    chunks.append(
        "	text = {\n"
        f"		localization_key = {fallback}\n"
        "	}\n"
        "}\n\n"
    )


def write_custom_loc() -> None:
    chunks: list[str] = []
    append_title_block(chunks, "KnsIgHallTitle", "kns_ig_acc_name_idx", "kns_ig_hall_title_fallback")
    for slot in range(1, 5):
        append_title_block(
            chunks,
            f"KnsIgAccPick{slot}",
            f"kns_ig_acc_pick_{slot}",
            "kns_ig_acc_pick_fallback",
        )
    path = ROOT / "common" / "customizable_localization" / "kns_ig_accolade_titles.txt"
    path.write_text("".join(chunks), encoding="utf-8", newline="\n")
    print("wrote", path)


def random_list_set_var(var_name: str, exclude_vars: list[str], indent: str) -> str:
    inner = indent + "\t"
    lines = [f"{indent}random_list = {{\n"]
    for i in range(1, 51):
        lines.append(f"{inner}1 = {{\n")
        if exclude_vars:
            lines.append(f"{inner}\ttrigger = {{\n")
            for ex in exclude_vars:
                lines.append(f"{inner}\t\tNOT = {{ var:{ex} = {i} }}\n")
            lines.append(f"{inner}\t}}\n")
        lines.append(f"{inner}\tset_variable = {{\n")
        lines.append(f"{inner}\t\tname = {var_name}\n")
        lines.append(f"{inner}\t\tvalue = {i}\n")
        lines.append(f"{inner}\t}}\n")
        lines.append(f"{inner}}}\n")
    lines.append(f"{indent}}}\n")
    return "".join(lines)


def write_name_effect() -> None:
    parts = [
        "kns_ig_clear_accolade_name_picks_effect = {\n",
        "	remove_variable = kns_ig_acc_pick_1\n",
        "	remove_variable = kns_ig_acc_pick_2\n",
        "	remove_variable = kns_ig_acc_pick_3\n",
        "	remove_variable = kns_ig_acc_pick_4\n",
        "}\n\n",
        "kns_ig_roll_accolade_title_effect = {\n",
        "	if = {\n",
        "		limit = { NOT = { has_variable = kns_ig_acc_name_idx } }\n",
        random_list_set_var("kns_ig_acc_name_idx", [], "		"),
        "	}\n",
        "}\n\n",
        "kns_ig_roll_accolade_name_picks_effect = {\n",
        "	kns_ig_clear_accolade_name_picks_effect = yes\n",
        random_list_set_var("kns_ig_acc_pick_1", [], "	"),
        random_list_set_var("kns_ig_acc_pick_2", ["kns_ig_acc_pick_1"], "	"),
        random_list_set_var(
            "kns_ig_acc_pick_3",
            ["kns_ig_acc_pick_1", "kns_ig_acc_pick_2"],
            "	",
        ),
        random_list_set_var(
            "kns_ig_acc_pick_4",
            ["kns_ig_acc_pick_1", "kns_ig_acc_pick_2", "kns_ig_acc_pick_3"],
            "	",
        ),
        "}\n\n",
    ]
    parts.append("kns_ig_name_kit_weapon_from_title_effect = {\n")
    parts.append("	if = {\n")
    parts.append("		limit = { exists = var:kns_imperial_guard_liege }\n")
    parts.append("		kns_ig_relink_and_dedupe_all_post_kit_effect = { EMPEROR = var:kns_imperial_guard_liege }\n")
    parts.append("		kns_ig_link_knight_kit_vars_from_post_effect = { EMPEROR = var:kns_imperial_guard_liege }\n")
    parts.append("	}\n")
    parts.append("	if = {\n")
    parts.append("		limit = {\n")
    parts.append("			exists = var:kns_ig_acc_name_idx\n")
    parts.append("			OR = {\n")
    parts.append("				exists = var:kns_ig_kit_weapon\n")
    parts.append("				exists = var:kns_ig_kit_armor\n")
    parts.append("			}\n")
    parts.append("		}\n")
    first_weapon = True
    for weapon in WEAPONS:
        keyword = "if" if first_weapon else "else_if"
        first_weapon = False
        parts.append(f"		{keyword} = {{\n")
        parts.append(f"			limit = {{ has_character_flag = kns_ig_post_{weapon} }}\n")
        first_idx = True
        for i in range(1, 51):
            idx_kw = "if" if first_idx else "else_if"
            first_idx = False
            parts.append(f"			{idx_kw} = {{\n")
            parts.append(f"				limit = {{ var:kns_ig_acc_name_idx = {i} }}\n")
            parts.append("				if = {\n")
            parts.append("					limit = { exists = var:kns_ig_kit_weapon }\n")
            parts.append(f"					var:kns_ig_kit_weapon = {{ set_artifact_name = kns_ig_acc_{weapon}_{i:02d} }}\n")
            parts.append("				}\n")
            parts.append("				if = {\n")
            parts.append("					limit = { exists = var:kns_ig_kit_armor }\n")
            parts.append(f"					var:kns_ig_kit_armor = {{ set_artifact_name = kns_ig_acc_{weapon}_{i:02d}_armor }}\n")
            parts.append("				}\n")
            parts.append("			}\n")
        parts.append("		}\n")
    parts.append("	}\n")
    parts.append("}\n\n")
    parts.append("kns_ig_give_accolade_title_nickname_effect = {\n")
    parts.append("	if = {\n")
    parts.append("		limit = { exists = var:kns_ig_acc_name_idx }\n")
    first_weapon = True
    for weapon in WEAPONS:
        keyword = "if" if first_weapon else "else_if"
        first_weapon = False
        parts.append(f"		{keyword} = {{\n")
        parts.append(f"			limit = {{ has_character_flag = kns_ig_post_{weapon} }}\n")
        first_idx = True
        for i in range(1, 51):
            idx_kw = "if" if first_idx else "else_if"
            first_idx = False
            parts.append(f"			{idx_kw} = {{\n")
            parts.append(f"				limit = {{ var:kns_ig_acc_name_idx = {i} }}\n")
            parts.append(f"				give_nickname = {nick_id(weapon, i)}\n")
            parts.append("			}\n")
        parts.append("		}\n")
    parts.append("	}\n")
    parts.append("	kns_ig_name_kit_weapon_from_title_effect = yes\n")
    parts.append("}\n")
    path = ROOT / "common" / "scripted_effects" / "kns_imperial_guard_accolade_names_effects.txt"
    path.write_text("".join(parts), encoding="utf-8", newline="\n")
    print("wrote", path)


if __name__ == "__main__":
    write_loc()
    write_nicknames()
    write_custom_loc()
    write_name_effect()
