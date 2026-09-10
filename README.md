# Knights & Squires

A Crusader Kings III 1.19.0.6 mod. Knights have a rolled **Gift at Arms** (a maximum for prowess without weapons), and a patron can fund training so that number grows toward the cap.

## Managing knights

Use the **Manage Knight Decision**. It opens a window with two tabs.

**Funding** lists you, your courtiers, and your direct vassals who are already knights with a cap, split into **Fundable Knights** (can be paid for; not too old) and **Not Fundable** (Old Age prowess loss or imprisoned). Fundable knights can be sorted by total prowess or by Gift at Arms (Potential). Not Fundable is sorted by total prowess. You can fund them one by one or use Fund All / Disable All. Each funded knight costs **0.5 gold per month**. The stipend continues after they reach their cap. Knights in a vassal's court are not in your reach.

**Potential** lists male courtiers and vassals who can receive knighthood. Filter by age, sort by prowess or age, then knight them. That uses the same kit as **Offer Knighthood**.

Per-character **Fund Knight** and **Disable Funding** interactions still work.

A funded knight also gets the Funded Knight health bonus. If they leave your reach, paid funding stops. If the patron is in debt (`gold < 0`), that year pays no skill gain.

**Prodigious knights** get patronage stories (memories, 100 flavors) that last a random **5–15 years**. If nobody is paying their stipend, that term trains them at **no gold cost**. If you already fund them, your 0.5 gold stays the only stipend and they get a **Patron's Purse** instead (0.5 gold and 1 prestige each month). New patronage events stop at **age 50**; a term already running keeps going. Disable All does not end a free patronage term.

Knights who **can take the Old Age prowess penalty** (from age **45**) cannot be funded or trained. Existing funding is cancelled automatically (birthday, quarterly pulse, or when you open Manage Knights): the stipend stops and the Funded Knight health bonus is removed. Knights who **do not lose prowess from age** (Graceful Aging / `no_prowess_loss_from_age`, including Immortal) can still be funded past 45.

## Gift at Arms (the cap)

When a character becomes a knight, the game rolls `kns_prowess_cap` from **1 to 50**. That number is their natural ceiling. It is **not** based on current prowess. If prowess without weapons is already above the roll, the cap is not raised; they simply have no training room.

The knight who dubs them can raise that roll. **Inept** and **Mediocre** mentors add nothing. **Able** adds **+2** if the roll is 29 or lower. **Formidable** adds **+4** if the roll is 29 or lower. **Prodigious** adds **+5** if the roll is 35 or lower; if that is still under **15**, the cap is **15**. The talent trait is then assigned from the new cap (so Able 29 + 4 becomes Formidable 33). Self-dubbing, the Pope with no Gift, and game-start knights get no mentor bonus. The papal youth tourney still forces 50.

The roll also assigns a talent trait:

| Trait | Cap |
|---|---|
| Inept | 1–5 |
| Mediocre | 6–14 |
| Able | 15–29 |
| Formidable | 30–49 |
| Prodigious | 50 |

## Prowess without weapons, not character-sheet Base

Training still calls `add_prowess_skill`. The cap is compared to **`prowess_no_portrait`**: displayed prowess with portrait artifacts (weapons/armor on the model) stripped.

That number includes traits, dynasty perks, Has a Squire, and other non-gear bonuses. Script cannot read tooltip Base, and cannot sum those lines one by one, so this is the value that is compared to the Gift at Arms roll.

```
room = max(0, cap − prowess_no_portrait)
```

Equipped weapons can still push the shown total above the cap. They do not count toward the cap.

Old Age (`PROWESS_AGE`, from 45) can lower `prowess_no_portrait` and would reopen training room, which is why knights who can take that penalty are not funded.

- Training: `Training 15 / 17 - Weapons Strength 10 - Total Prowess 25`
- Peak: `Peak 17 / 17 - Weapons Strength 10 - Total Prowess 27`
- Surpassed (traits after the cap): `Surpassed 20 / 17 - Weapons Strength 10 - Total Prowess 30`

## Yearly training

On the knight's birthday, if they are funded, in reach, not subject to Old Age prowess loss, the patron can pay, and they are not at peak, they roll a yearly gain. That gain is then **clamped to remaining room**, so prowess without weapons never passes the cap.

Age 30 is grouped with 31–45 so there is no one-year hole between "below 30" and "31–45". Knights who can take Old Age prowess loss still cannot be funded from 45. The 46+ band is for those who age without that penalty.

| Age | Range | Average | Weights |
|---|---|---|---|
| Under 30 | 0–5 | 3 | 1, 3, 5, 8, 6, 4 |
| 30–45 | 0–3 | 2 | 1, 2, 4, 4 |
| 46+ | 0–1 | 0.5 | 1, 1 |

A 4 or 5 on a young knight with only 2 room left becomes +2.

---

## Math: yearly growth

Chance is `weight / sum of weights` for that age band. Mean is `Σ (gain × chance)`.

### Under 30 (sum 27, mean 3)

| Gain | Weight | Chance | Contribution |
|---|---|---|---|
| 0 | 1 | 1/27 ≈ 3.70% | 0 |
| 1 | 3 | 3/27 ≈ 11.11% | 0.111 |
| 2 | 5 | 5/27 ≈ 18.52% | 0.370 |
| 3 | 8 | 8/27 ≈ 29.63% | 0.889 |
| 4 | 6 | 6/27 ≈ 22.22% | 0.889 |
| 5 | 4 | 4/27 ≈ 14.81% | 0.741 |
| **Total** | **27** | **100%** | **3.000** |

Expected value:

`(0×1 + 1×3 + 2×5 + 3×8 + 4×6 + 5×4) / 27 = 81 / 27 = 3`

### 30–45 (sum 11, mean 2)

| Gain | Weight | Chance | Contribution |
|---|---|---|---|
| 0 | 1 | 1/11 ≈ 9.09% | 0 |
| 1 | 2 | 2/11 ≈ 18.18% | 0.182 |
| 2 | 4 | 4/11 ≈ 36.36% | 0.727 |
| 3 | 4 | 4/11 ≈ 36.36% | 1.091 |
| **Total** | **11** | **100%** | **2.000** |

Expected value:

`(0×1 + 1×2 + 2×4 + 3×4) / 11 = 22 / 11 = 2`

### 46+ (sum 2, mean 0.5)

| Gain | Weight | Chance | Contribution |
|---|---|---|---|
| 0 | 1 | 50% | 0 |
| 1 | 1 | 50% | 0.500 |
| **Total** | **2** | **100%** | **0.500** |

### How long training takes

Ignore clamping and missed years (debt, prison, leaving reach). Expected years to close `R` points of room:

| Age | Mean per year | Years for R room |
|---|---|---|
| Under 30 | 3 | `R / 3` |
| 30–45 | 2 | `R / 2` |
| 46+ | 0.5 | `2R` |

Example: prowess without weapons 10, cap 22 (`R = 12`).

- Funded from 18 to 29: about 4 years.
- Funded from 30 to 45: about 6 years.
- Funded from 46: about 24 years.

Near the cap the last roll is often clipped, so real time is a little longer than `R / mean`.

---

## Math: Gift at Arms roll

The cap is two nested `random_list`s.

1. **1 in 1000** rolls Prodigious (cap **50**).
2. **999 in 1000** rolls 1–49 on a curve centered at 15.

Inner weights for 1–49 (sum **1460**):

| Cap | Weight | Cap | Weight | Cap | Weight |
|---|---|---|---|---|---|
| 1 | 6 | 18 | 86 | 35 | 3 |
| 2 | 8 | 19 | 77 | 36 | 3 |
| 3 | 13 | 20 | 66 | 37 | 3 |
| 4 | 20 | 21 | 55 | 38 | 3 |
| 5 | 26 | 22 | 44 | 39 | 3 |
| 6 | 26 | 23 | 35 | 40 | 3 |
| 7 | 35 | 24 | 26 | 41 | 3 |
| 8 | 44 | 25 | 19 | 42 | 3 |
| 9 | 55 | 26 | 14 | 43 | 3 |
| 10 | 66 | 27 | 9 | 44 | 3 |
| 11 | 77 | 28 | 6 | 45 | 3 |
| 12 | 86 | 29 | 4 | 46 | 3 |
| 13 | 94 | 30 | 10 | 47 | 3 |
| 14 | 98 | 31 | 6 | 48 | 3 |
| 15 | 100 | 32 | 6 | 49 | 3 |
| 16 | 98 | 33 | 3 | | |
| 17 | 94 | 34 | 3 | | |

Overall chance for a common cap `C` is:

`(999 / 1000) × (weight(C) / 1460)`

Overall chance for Prodigious (50):

`1 / 1000 = 0.10%`

Peak at 15:

`(999 / 1000) × (100 / 1460) ≈ 6.84%`

### Talent-band chances

Among the 999/1000 common rolls:

| Trait | Caps | Inner weight | Share of common rolls |
|---|---|---|---|
| Inept | 1–5 | 73 | 5.00% |
| Mediocre | 6–14 | 581 | 39.79% |
| Able | 15–29 | 733 | 50.21% |
| Formidable | 30–49 | 73 | 5.00% |
| Prodigious | 50 | — | 0.10% of all knights |

Most knights land Able or Mediocre. Inept and Formidable are each about 5%. Prodigious is 1 in 1000.

---

## Names

Unlanded knights are styled **Sir** (men) or **Dame** (women) in titled and unlanded names. Landed titles keep Count, Duke, and so on. Close family of a living king or emperor keep Prince or Princess instead of Sir.

## Other systems

- **Squires:** Christian youths train on the Squire trait. Each birthday they take an Arms lesson (about 45–55 XP on a good day, 25–35 on a poor one), so the track fills in about **2–4 years**. A player’s squire shows a toast only. **Train Squire** is still there for extra sessions. At **16**, if the track is full they are dubbed automatically; if not, training continues and they are dubbed as soon as it fills.
- **Knight ranks:** Knight (0–9), Proven (10–19), Renowned (20–49), Famous (50–99), Legendary (100). Glory comes from Imperial Olympic bout wins and titles (losses subtract the same as a win, except Legendary is locked), a +2 birthday stipend for Imperial Guard or Prodigious knights, Papal/Gift-at-Arms Prodigious floor of 50, and Guard appointment floor of 30.
- **Offer Knighthood / Ask Liege:** character interactions for knighthood. Ask Liege still has a cooldown; Offer Knighthood does not.
- **Buy Knighthood:** a paid decision for some characters to knight themselves.
- **Papal youth tourney:** if no living Prodigious knight exists, a papal tourney can create one and raise their prowess toward 30.
- **Imperial Guard:** a player **emperor or hegemon** may keep **five** unlanded court knights as Imperial Guard, **one post each** for **axe, hammer, sword, spear, and mace**. **Manage Imperial Guard** opens the hall: vacant posts are silhouettes (click to hire). The hall hides while you pick a knight. Hired guards stand full-body, centered, each in that post's pose. **Customize** under a hired guard opens a second window for war harness. **Appoint / Dismiss / Attire Imperial Guard** also work from the character menu. **Appoint** spends **1500 gold** and fills the first vacant post. Appointment gifts **that post's illustrious weapon** plus **illustrious plate**. The Imperial Guard modifier is a rank of honor with **no extra bonuses**. The attire window lists every vanilla war harness (DLC pieces only if you own that DLC). Culture Default uses ordinary culture armor. The post frees if they die, take land, leave court, or you lose the empire. They keep the gifted steel if dismissed.
- **Imperial Olympic Games:** a player **emperor or hegemon** may **found** a Christian single-elimination duel bracket as a lasting institution. At founding you choose bracket size (**128** / **256**), cycle (**every 2, 3, or 4 years**), fund (**1000–5000 gold**), and venue (**capital**, or any **realm county** via a title picker; capital if none is chosen). After that the games **auto-start** when due; **Manage Imperial Olympic Games** changes settings or raises the lists early. If the organizer dies mid-bracket, a **player heir** finishes that tournament; afterwards only a **player emperor or hegemon** may **Continue the Imperial Olympic Games** (free — re-pick cycle and purse). AI rulers do not keep the custom. Use **Select Imperial Olympic Champions** to pick up to **four** court knights (and optionally yourself). **Every Prodigious knight** fit to fight is entered automatically, then the **thirty** strongest Christian knights **aged 35 or under** (prowess without weapons). Invited rulers fill remaining slots by rank (**count 1**, **duke 2**, **king 3**, **empire/hegemony 4**). The victor takes **5000 prestige** and **40% of the fund**; the rest pays for the event. The host county gets a tax bonus for **6 months** (max **+50%** at 5000 gold). Knight effectiveness scales with the full fund (**5000 gold = +100%**). Bout winners, the tournament champion, and the hosting emperor keep memories. **View Hall of Legends** opens a ranked GUI. No DLC required.

Each bracket round is fought on **one day**: 256 fighters on day 1, 128 on day 2, and so on (a 128-bracket starts at 128). Assigned champions and every pairing that is not **your own Finals bout** are **fake duels** (a prowess roll, no minigame). If you are in a fake duel, you get an event that you won and advance, or that you lost. If **you** reach the Finals, that last bout is a real first-blood single combat.

**Fake duel odds** use overall prowess (the armed character-sheet total, including weapons):

```
base(X) = 5 + (prowess_X × 2)
tens    = floor(max(0, foe − me) / 10)
weight(X) = max(5, base(X) − (tens × 5))
P(A wins) = weight(A) / (weight(A) + weight(B))
```

The weaker side loses **5 weight per full 10** they are behind. A 1–9 gap has no extra penalty. `max(5, …)` keeps every fighter in the roll (never 0 or negative). After about a 50 gap the underdog sits on that floor; the favorite still gets heavier as prowess rises. Chance the **10** wins:

| Match | P(10 wins) |
|---|---|
| 10 vs 10 | 50% |
| 10 vs 20 | 31% |
| 10 vs 30 | 19% |
| 10 vs 40 | 11% |
| 10 vs 50 | 5% |
| 10 vs 60 | 4% |
| 10 vs 70 | 3% |
| 10 vs 80 | 3% |
| 10 vs 90 | 3% |
| 10 vs 100 | 2% |

## Key files

| File | Role |
|---|---|
| `common/scripted_effects/kns_prowess_effects.txt` | Cap roll, talent trait, funding, yearly gain |
| `common/scripted_effects/kns_olympic_effects.txt` | Imperial Olympic gather, bracket, duel resolution, Hall of Legends lists |
| `common/scripted_guis/kns_hof_gui.txt` | Hall of Legends window actions |
| `gui/window_kns_imperial_hof.gui` | Hall of Legends UI |
| `common/script_values/kns_values.txt` | Compared prowess, training room, stipend cost, Olympic quota |
| `common/scripted_triggers/kns_triggers.txt` | Peak, Old Age block, can-train, funding reach, Sir style, Olympic eligibility |
| `common/customizable_localization/kns_honorific_custom_loc.txt` | Sir / Dame name prefix |
| `localization/english/kns_character_names_l_english.yml` | Character name formats with honorifics |
| `common/scripted_guis/kns_funding_gui.txt` | Manage Knights window actions |
| `gui/window_kns_fund_knights.gui` | Funding / Potential UI |
| `common/scripted_guis/kns_olympic_champion_picker_gui.txt` | Select Olympic champions window |
| `gui/window_kns_olympic_champion_picker.gui` | Champion picker UI |
| `common/scripted_effects/kns_imperial_guard_effects.txt` | Appoint, dismiss, illustrious plate kit, window lists |
| `common/scripted_guis/kns_imperial_guard_gui.txt` | Manage Imperial Guard window actions |
| `gui/window_kns_imperial_guard.gui` | Imperial Guard hall (five weapon posts) |
| `gui/window_kns_imperial_guard_hire.gui` | Hire list for a vacant post |
| `gui/window_kns_imperial_guard_attire.gui` | Armor picker for a hired guard |
| `common/decisions/kns_decisions.txt` | Manage Knight Decision, Select Olympic Champions, Hold/Continue/Manage Olympic Games, Hall of Legends, Manage Imperial Guard |
| `events/kns_imperial_olympic_events.txt` | Imperial Olympic setup, bracket, duels, and results |
| `common/scripted_effects/kns_prodigy_patron_effects.txt` | Prodigious patronage terms, expire, player event routing |
| `common/scripted_effects/kns_prodigy_patron_generated_effects.txt` | Flavor roll and 100 memory creates |
| `common/character_memory_types/kns_prodigy_patron_memories.txt` | Patronage origin-story memories |
| `localization/english/kns_prodigy_patron_l_english.yml` | Patronage memory and story text |
| `localization/english/kns_prowess_l_english.yml` | Player-facing text |
| `localization/english/kns_imperial_olympic_l_english.yml` | Imperial Olympic text |
| `localization/english/kns_imperial_guard_l_english.yml` | Imperial Guard text |
