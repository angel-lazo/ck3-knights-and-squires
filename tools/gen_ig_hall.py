from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = "GuiScope.SetRoot( GetPlayer.MakeScope ).End"

# Cameras: yaw N = steps from center (2 deg). zoom 0 = radius 420.
# Sword used yaw -2 (idx 15 looked like a copy of axe).
# pan_px is the hall portrait widget x (from pan idx; loc px was idx-40 without *2).
CAMERAS = {
    "axe": {"angle": 10, "radius": 420, "anim": "throne_room_one_handed_passive_2", "pan_px": -20},
    "hammer": {"angle": -6, "radius": 420, "anim": "aggressive_hammer", "pan_px": -48},
    "sword": {"angle": -4, "radius": 420, "anim": "chudan_no_kamae", "pan_px": -44},
    "spear": {"angle": 20, "radius": 420, "anim": "relaxed_spear", "pan_px": -68},
    "mace": {"angle": -6, "radius": 420, "anim": "menacing", "pan_px": -32},
}
WEAPONS = ["axe", "hammer", "sword", "spear", "mace"]
HEIGHT = -48
FOV = 22


def camera_block(name: str, angle: int, radius: int) -> str:
    return f"""{name} = {{
	camera = {{
		position = cylindrical{{ {radius} {HEIGHT} {angle} }}
		position_node = {{
			default = camera_torso_look_at
		}}
		look_at = {{ 0 {HEIGHT} 0 }}
		look_at_node = {{
			default = camera_torso_look_at
		}}
		fov = {FOV}
		camera_near_far = {{ 10 1200 }}
	}}

	unknown = "gfx/portraits/unknown_portraits/unknown_unclickable_small.dds"
}}
"""


def write_cameras() -> None:
    parts = []
    for weapon, cfg in CAMERAS.items():
        parts.append(camera_block(f"kns_camera_ig_{weapon}", cfg["angle"], cfg["radius"]))
    path = ROOT / "gfx" / "portraits" / "cameras" / "kns_cameras.txt"
    path.write_text("\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    print("wrote", path)


def hired_portrait(weapon: str) -> str:
    cfg = CAMERAS[weapon]
    cam = f"kns_camera_ig_{weapon}"
    anim = cfg["anim"]
    px = cfg["pan_px"]
    return f"""									portrait_button = {{
										parentanchor = center
										position = {{ {px} 0 }}
										size = {{ 320 520 }}
										using = portrait_base
										alwaystransparent = yes
										effectname = "NoHighlight"
										portrait_texture = "[Character.GetAnimatedPortrait('environment_body', '{cam}', '{anim}', PdxGetWidgetScreenSize(PdxGuiWidget.Self))]"
										mask = "gfx/portraits/portrait_mask_body.dds"
									}}"""


def col(weapon: str) -> str:
    shown = f"GetScriptedGui('kns_gui_ig_has_slot_{weapon}').IsShown( {SCOPE} )"
    vacant = f"Not( {shown} )"
    open_hire = f"GetScriptedGui('kns_gui_ig_open_hire_{weapon}')"
    return f'''						vbox = {{
							layoutpolicy_horizontal = expanding
							layoutpolicy_vertical = expanding
							minimumsize = {{ 280 0 }}
							spacing = 4
							background = {{
								using = Background_Area_Dark
							}}

							text_single = {{
								layoutpolicy_horizontal = expanding
								align = center
								text = "kns_ig_window_post_{weapon}"
								default_format = "#high"
							}}

							widget = {{
								size = {{ 280 520 }}
								parentanchor = hcenter
								allow_outside = yes

								widget = {{
									size = {{ 100% 100% }}
									allow_outside = yes
									alwaystransparent = yes
									visible = "[{shown}]"
									datacontext = "[GetPlayer.MakeScope.Var('kns_ig_slot_{weapon}').Char]"

{hired_portrait(weapon)}
								}}

								button = {{
									parentanchor = center
									size = {{ 195 282 }}
									visible = "[{vacant}]"
									enabled = "[{open_hire}.IsValid( {SCOPE} )]"
									gfxtype = framedbuttongfx
									effectname = "NoHighlight"
									texture = "gfx/portraits/unknown_portraits/unknown_spouse.dds"
									framesize = {{ 554 780 }}
									upframe = 1
									overframe = 2
									alpha = 0.8
									tooltip = "kns_ig_window_vacant_tt"
									onclick = "[{open_hire}.Execute( {SCOPE} )]"

									button_plus = {{
										parentanchor = center
										alwaystransparent = yes
									}}
								}}
							}}

							text_single = {{
								layoutpolicy_horizontal = expanding
								align = center
								visible = "[{shown}]"
								datacontext = "[GetPlayer.MakeScope.Var('kns_ig_slot_{weapon}').Char]"
								text = "[Character.GetShortUINameNoTooltip]"
								default_format = "#high"
							}}

							hbox = {{
								layoutpolicy_horizontal = expanding
								spacing = 4
								visible = "[{shown}]"

								button_standard = {{
									layoutpolicy_horizontal = expanding
									text = "kns_ig_window_customize"
									onclick = "[GetScriptedGui('kns_gui_ig_open_attire_{weapon}').Execute( {SCOPE} )]"
								}}

								button_standard = {{
									text = "kns_ig_window_dismiss"
									enabled = "[GetScriptedGui('kns_gui_ig_dismiss_{weapon}').IsValid( {SCOPE} )]"
									onclick = "[GetScriptedGui('kns_gui_ig_dismiss_{weapon}').Execute( {SCOPE} )]"
								}}
							}}
						}}'''


def write_hall() -> None:
    header = f'''window = {{
	name = "kns_imperial_guard_window"
	size = {{ 1780 950 }}
	parentanchor = center
	position = {{ 0 0 }}
	movable = yes
	layer = top
	allow_outside = yes
	visible = "[And( GetPlayer.MakeScope.Var('kns_imperial_guard_window_open').IsSet, Not( Or( GetPlayer.MakeScope.Var('kns_ig_hire_window_open').IsSet, GetPlayer.MakeScope.Var('kns_ig_attire_window_open').IsSet ) ) )]"

	using = Window_Background_Subwindow

		vbox = {{
			margin = {{ 10 10 }}
			spacing = 8
			layoutpolicy_horizontal = expanding
			layoutpolicy_vertical = expanding

			hbox = {{
				layoutpolicy_horizontal = expanding
				spacing = 8

				text_single = {{
					layoutpolicy_horizontal = expanding
					align = center
					text = "kns_ig_window_title"
					fontsize = 22
				}}

				button_close = {{
					onclick = "[GetScriptedGui('kns_close_imperial_guard_window').Execute( {SCOPE} )]"
					shortcut = "close_window"
					visible = "[And( GetPlayer.MakeScope.Var('kns_imperial_guard_window_open').IsSet, Not( Or( GetPlayer.MakeScope.Var('kns_ig_hire_window_open').IsSet, GetPlayer.MakeScope.Var('kns_ig_attire_window_open').IsSet ) ) )]"
				}}
			}}

			vbox = {{
				layoutpolicy_horizontal = expanding
				background = {{
					using = Background_Area_Dark
				}}

				text_single = {{
					layoutpolicy_horizontal = expanding
					align = center
					text = "kns_ig_window_quota"
					default_format = "#high"
				}}

				text_single = {{
					layoutpolicy_horizontal = expanding
					align = center
					text = "kns_ig_window_kit_cost"
				}}
			}}

			hbox = {{
				layoutpolicy_horizontal = expanding
				layoutpolicy_vertical = expanding
				spacing = 8

'''
    footer = """
			}
		}
}
"""
    path = ROOT / "gui" / "window_kns_imperial_guard.gui"
    path.write_text(header + "\n\n".join(col(w) for w in WEAPONS) + footer, encoding="utf-8", newline="\n")
    print("wrote", path)


if __name__ == "__main__":
    write_cameras()
    write_hall()
