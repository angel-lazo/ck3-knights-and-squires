$ErrorActionPreference = "Stop"
$Vanilla = "C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"
$Mod = Split-Path $PSScriptRoot -Parent
$ClothesPath = Join-Path $Vanilla "gfx\portraits\portrait_modifiers\04_clothes_armor.txt"
$HeadgearPath = Join-Path $Vanilla "gfx\portraits\portrait_modifiers\04_headgear_armor.txt"
$Skip = @("chinese_war_low_nobles_no_dlc")

$DlcPrefixes = @(
    @{ Prefix = "ep2_"; Trigger = "has_ep2_dlc_trigger" },
    @{ Prefix = "ep3_"; Trigger = "has_ep3_dlc_trigger" },
    @{ Prefix = "fp1_"; Trigger = "has_fp1_dlc_trigger" },
    @{ Prefix = "fp2_"; Trigger = "has_fp2_dlc_trigger" },
    @{ Prefix = "fp3_"; Trigger = "has_fp3_dlc_trigger" },
    @{ Prefix = "mpo_"; Trigger = "has_mpo_dlc_trigger" },
    @{ Prefix = "tgp_"; Trigger = "has_tgp_dlc_trigger" },
    @{ Prefix = "ccp4_"; Trigger = "has_cp4_dlc_trigger" },
    @{ Prefix = "ccp5_"; Trigger = "has_cp5_dlc_trigger" },
    @{ Prefix = "cp7_"; Trigger = "has_cp7_dlc_trigger" },
    @{ Prefix = "afr_"; Trigger = "has_afr_dlc_trigger" },
    @{ Prefix = "pol_"; Trigger = "has_pol_dlc_trigger" }
)

$Groups = @(
    @{ Prefix = "dde_hre"; Name = "Holy Roman" },
    @{ Prefix = "western_crusades"; Name = "Western" },
    @{ Prefix = "ep2_western"; Name = "Western" },
    @{ Prefix = "western"; Name = "Western" },
    @{ Prefix = "ep3_byzantine"; Name = "Byzantine" },
    @{ Prefix = "ep2_byzantine"; Name = "Byzantine" },
    @{ Prefix = "byzantine"; Name = "Byzantine" },
    @{ Prefix = "ep2_indian"; Name = "Indian" },
    @{ Prefix = "indian"; Name = "Indian" },
    @{ Prefix = "dde_abbasid"; Name = "Arabic" },
    @{ Prefix = "ep2_mena"; Name = "Arabic" },
    @{ Prefix = "mena"; Name = "Arabic" },
    @{ Prefix = "mpo_mongol"; Name = "Steppe" },
    @{ Prefix = "ep2_steppe"; Name = "Steppe" },
    @{ Prefix = "steppe"; Name = "Steppe" },
    @{ Prefix = "fp1_norse"; Name = "Northern" },
    @{ Prefix = "northern"; Name = "Northern" },
    @{ Prefix = "fp2_iberian"; Name = "Iberian" },
    @{ Prefix = "afr_berber"; Name = "African" },
    @{ Prefix = "sub_saharan"; Name = "African" },
    @{ Prefix = "pol_west"; Name = "West Slavic" },
    @{ Prefix = "ccp4_khanty"; Name = "Khanty" },
    @{ Prefix = "fp3_iranian"; Name = "Iranian" },
    @{ Prefix = "tgp_chinese"; Name = "East Asia" },
    @{ Prefix = "tgp_japanese"; Name = "East Asia" },
    @{ Prefix = "tgp_southeast"; Name = "East Asia" },
    @{ Prefix = "tgp_ainu"; Name = "East Asia" },
    @{ Prefix = "ccp5_"; Name = "High Medieval" },
    @{ Prefix = "cp7_"; Name = "North Pacific" }
)

function Get-DlcTrigger([string]$Key) {
    foreach ($p in $DlcPrefixes) {
        if ($Key.StartsWith($p.Prefix)) { return $p.Trigger }
    }
    return $null
}

function Get-ArmorGroup([string]$Key) {
    foreach ($g in $Groups) {
        if ($Key.StartsWith($g.Prefix)) { return $g.Name }
    }
    return "Other"
}

function Get-HumanLabel([string]$Key) {
    $labels = @{
        "western_crusades" = "Crusader"
        "fp1_norse_war" = "Norse"
        "afr_berber_war" = "Berber"
        "pol_west_slavic_war" = "West Slavic"
        "fp3_iranian_war" = "Iranian"
        "tgp_japanese_war_nobles" = "Japanese"
        "tgp_southeast_war_nobles" = "Southeast Asian"
        "tgp_ainu_war_nobles" = "Ainu"
        "cp7_emishi_war_nobles" = "Emishi"
        "cp7_nivkh_war_nobles" = "Nivkh"
    }
    if ($labels.ContainsKey($Key)) { return $labels[$Key] }
    $repl = [ordered]@{
        "ep2_western_era1_war_" = "Western Early "
        "ep2_western_era2_war_" = "Western High "
        "ep2_western_era3_war_" = "Western Late "
        "ep2_western_era4_war_" = "Western Plate "
        "ep2_byzantine_war_" = "Byzantine Tourney "
        "ep3_byzantine_era1_war_" = "Byzantine Early "
        "ep3_byzantine_era2_war_" = "Byzantine Late "
        "ep2_indian_war_" = "Indian Tourney "
        "ep2_mena_war_" = "MENA Tourney "
        "ep2_steppe_war_" = "Steppe Tourney "
        "mpo_mongol_war_" = "Mongol "
        "dde_hre_war_" = "HRE "
        "dde_abbasid_war_" = "Abbasid "
        "western_war_" = "Western "
        "byzantine_war_" = "Byzantine "
        "indian_war_" = "Indian "
        "mena_war_" = "MENA "
        "steppe_war_" = "Steppe "
        "northern_war_" = "Northern "
        "fp2_iberian_christian_war_" = "Iberian Christian "
        "fp2_iberian_muslim_war_" = "Iberian Muslim "
        "sub_saharan_war_" = "West African "
        "ccp4_khanty_war_" = "Khanty "
        "tgp_chinese_war_" = "Chinese "
        "ccp5_french_late_era3_war_" = "French Late "
        "ccp5_french_era3_war_" = "French "
        "ccp5_german_era3_war_" = "German "
        "ccp5_english_era3_war_" = "English "
        "ccp5_english_era4_war_" = "English Plate "
    }
    $s = $Key
    foreach ($a in $repl.Keys) {
        if ($s.StartsWith($a)) {
            $s = $repl[$a] + $s.Substring($a.Length)
            break
        }
    }
    $s = $s.Replace("_", " ")
    $s = $s.Replace("low nobles", "Low")
    $s = $s.Replace("high nobles", "High")
    $s = $s.Replace("commoners", "Common")
    $s = $s.Replace("royalty", "Royal")
    $s = $s.Replace("nobles", "").Trim()
    $s = [regex]::Replace($s, "\s+", " ").Trim()
    return $s
}

function Get-DnaInner([string]$Block) {
    $idx = $Block.IndexOf("dna_modifiers")
    if ($idx -lt 0) { return $null }
    $brace = $Block.IndexOf("{", $idx)
    if ($brace -lt 0) { return $null }
    $depth = 0
    for ($j = $brace; $j -lt $Block.Length; $j++) {
        $c = $Block[$j]
        if ($c -eq "{") { $depth++ }
        elseif ($c -eq "}") {
            $depth--
            if ($depth -eq 0) {
                $inner = $Block.Substring($brace + 1, $j - $brace - 1)
                return (Normalize-Dna $inner)
            }
        }
    }
    return $null
}

function Normalize-Dna([string]$Inner) {
    $lines = $Inner -replace "`r`n", "`n" -replace "`r", "`n" -split "`n"
    $parsed = @()
    foreach ($line in $lines) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $raw = $line -replace "    ", "`t"
        $t = 0
        while ($t -lt $raw.Length -and $raw[$t] -eq "`t") { $t++ }
        $parsed += ,@{ Tabs = $t; Rest = $raw.Substring($t).TrimEnd() }
    }
    if ($parsed.Count -eq 0) { return $null }
    $mint = ($parsed | ForEach-Object { $_.Tabs } | Measure-Object -Minimum).Minimum
    $out = foreach ($p in $parsed) {
        ("`t" * (4 + ($p.Tabs - $mint))) + $p.Rest
    }
    return ($out -join "`n")
}

function Get-PortraitEntries([string]$Path) {
    $text = [IO.File]::ReadAllText($Path) -replace "`r`n", "`n" -replace "`r", "`n"
    $entries = [ordered]@{}
    $rx = [regex]::new('(?:(?<=\n)(?:\t(?!\t)| {4})|(?<=\n)[ \t]{0,3}\t)([a-z0-9_]+) = \{', [Text.RegularExpressions.RegexOptions]::Multiline)
    foreach ($m in $rx.Matches($text)) {
        $key = $m.Groups[1].Value
        if ($key -in @("usage", "selection_behavior", "priority", "fallback")) { continue }
        $lineStart = $text.LastIndexOf("`n", $m.Index)
        $prefix = if ($lineStart -ge 0) { $text.Substring($lineStart + 1, $m.Index - $lineStart - 1 + 0) } else { "" }
        # Skip two-tab nested keys: line indent is more than one tab-equivalent
        $indent = ($prefix + $m.Value.Substring(0, $m.Value.IndexOf($key))).Replace(" ", "")
        if ($indent.StartsWith("`t`t")) { continue }
        $brace = $m.Index + $m.Length - 1
        $depth = 0
        for ($j = $brace; $j -lt $text.Length; $j++) {
            if ($text[$j] -eq "{") { $depth++ }
            elseif ($text[$j] -eq "}") {
                $depth--
                if ($depth -eq 0) {
                    $block = $text.Substring($brace + 1, $j - $brace - 1)
                    $dna = Get-DnaInner $block
                    if ($dna -and -not $entries.Contains($key) -and ($Skip -notcontains $key)) {
                        $entries[$key] = $dna
                    }
                    break
                }
            }
        }
    }
    return $entries
}

function Get-HeadgearMatch([string]$ClothesKey, $Headgear) {
    if ($Headgear.Contains($ClothesKey)) { return $ClothesKey }
    $suffixes = @("_low_nobles", "_high_nobles", "_royalty", "_commoners", "_nobles", "_common")
    foreach ($suf in $suffixes) {
        if ($ClothesKey.EndsWith($suf)) {
            $stem = $ClothesKey.Substring(0, $ClothesKey.Length - $suf.Length)
            if ($Headgear.Contains($stem)) { return $stem }
            if ($Headgear.Contains($stem + "_war")) { return ($stem + "_war") }
        }
    }
    $map = @{
        "western_crusades" = "crusades_western_war"
        "western_war_low_nobles" = "western_war"
        "western_war_high_nobles" = "western_war"
        "ep2_western_era1_war_low_nobles" = "ep2_western_era1_war"
        "ep2_western_era1_war_high_nobles" = "ep2_western_era1_war"
        "ep2_western_era2_war_low_nobles" = "ep2_western_era2_war"
        "ep2_western_era2_war_high_nobles" = "ep2_western_era2_war"
        "ep2_western_era3_war_low_nobles" = "ep2_western_era3_war_low_nobles"
        "ep2_western_era3_war_high_nobles" = "ep2_western_era3_war_high_nobles"
        "ep2_western_era4_war_low_nobles" = "ep2_western_era4_war"
        "ep2_western_era4_war_high_nobles" = "ep2_western_era4_war"
        "ep2_byzantine_war_low_nobles" = "ep2_byzantine_war"
        "ep2_byzantine_war_high_nobles" = "ep2_byzantine_war"
        "ep3_byzantine_era1_war_low_nobles" = "ep3_byzantine_era1_war"
        "ep3_byzantine_era1_war_high_nobles" = "ep3_byzantine_era1_war"
        "ep3_byzantine_era2_war_low_nobles" = "ep3_byzantine_era2_war"
        "ep3_byzantine_era2_war_high_nobles" = "ep3_byzantine_era2_war"
        "ep2_indian_war_low_nobles" = "ep2_indian_war"
        "ep2_indian_war_high_nobles" = "ep2_indian_war"
        "ep2_mena_war_low_nobles" = "ep2_mena_war"
        "ep2_mena_war_high_nobles" = "ep2_mena_war"
        "ep2_steppe_war_low_nobles" = "ep2_steppe_war"
        "ep2_steppe_war_high_nobles" = "ep2_steppe_war"
        "mpo_mongol_war_low_nobles" = "mpo_mongol_war"
        "mpo_mongol_war_high_nobles" = "mpo_mongol_war"
        "fp1_norse_war" = "fp1_norse_war"
        "fp3_iranian_war" = "fp3_iranian_war"
        "sub_saharan_war_low_nobles" = "sub_saharan_war"
        "sub_saharan_war_high_nobles" = "sub_saharan_war"
        "tgp_japanese_war_nobles" = "tgp_japanese_war_high_nobles"
        "tgp_southeast_war_nobles" = "tgp_southeast_war_low_nobles"
        "ccp4_khanty_war_com" = "ccp4_ugro_permian_war_commoner"
        "ccp4_khanty_war_low_nobles" = "ccp4_ugro_permian_war_low_nobility"
        "ccp4_khanty_war_high_nobles" = "ccp4_ugro_permian_war_high_nobility"
    }
    if ($map.ContainsKey($ClothesKey) -and $Headgear.Contains($map[$ClothesKey])) {
        return $map[$ClothesKey]
    }
    return $null
}

function Write-PortraitFile([string]$Path, [string]$Group, [int]$Priority, $Items) {
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("$Group = {")
    [void]$sb.AppendLine("`tusage = game")
    [void]$sb.AppendLine("`tselection_behavior = max")
    [void]$sb.AppendLine("`tpriority = $Priority")
    [void]$sb.AppendLine("")
    foreach ($item in $Items) {
        $key = $item.Key
        $dna = $item.Dna
        [void]$sb.AppendLine("`t$key = {")
        [void]$sb.AppendLine("`t`tdna_modifiers = {")
        [void]$sb.AppendLine($dna)
        [void]$sb.AppendLine("`t`t}")
        [void]$sb.AppendLine("`t`tignore_outfit_tags = yes")
        [void]$sb.AppendLine("`t`tweight = {")
        [void]$sb.AppendLine("`t`t`tbase = 0")
        [void]$sb.AppendLine("`t`t`tmodifier = {")
        [void]$sb.AppendLine("`t`t`t`tadd = 200")
        [void]$sb.AppendLine("`t`t`t`thas_character_flag = kns_is_imperial_guard")
        [void]$sb.AppendLine("`t`t`t`thas_character_flag = kns_ig_armor_$key")
        [void]$sb.AppendLine("`t`t`t}")
        [void]$sb.AppendLine("`t`t}")
        [void]$sb.AppendLine("`t}")
        [void]$sb.AppendLine("")
    }
    [void]$sb.AppendLine("}")
    $dir = Split-Path $Path -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    [IO.File]::WriteAllText($Path, $sb.ToString().Replace("`r`n", "`n"), [Text.UTF8Encoding]::new($false))
}

$clothes = Get-PortraitEntries $ClothesPath
$headgear = Get-PortraitEntries $HeadgearPath
Write-Host "clothes=$($clothes.Count) headgear=$($headgear.Count)"
Write-Host ($clothes.Keys -join ", ")

$clothesItems = foreach ($k in $clothes.Keys) { @{ Key = $k; Dna = $clothes[$k] } }
$hgItems = @()
foreach ($k in $clothes.Keys) {
    $match = Get-HeadgearMatch $k $headgear
    if ($match) {
        $hgItems += @{ Key = $k; Dna = $headgear[$match] }
    }
}

Write-PortraitFile (Join-Path $Mod "gfx\portraits\portrait_modifiers\kns_imperial_guard_clothes.txt") "kns_imperial_guard_clothes" 8 $clothesItems
Write-PortraitFile (Join-Path $Mod "gfx\portraits\portrait_modifiers\kns_imperial_guard_headgear.txt") "kns_imperial_guard_headgear" 8 $hgItems

$clear = New-Object System.Text.StringBuilder
[void]$clear.AppendLine("kns_clear_imperial_guard_armor_flags_effect = {")
foreach ($k in $clothes.Keys) {
    [void]$clear.AppendLine("`tremove_character_flag = kns_ig_armor_$k")
}
[void]$clear.AppendLine("}")
[IO.File]::WriteAllText((Join-Path $Mod "common\scripted_effects\kns_imperial_guard_armor_flags_effects.txt"), $clear.ToString().Replace("`r`n", "`n"), [Text.UTF8Encoding]::new($false))

$gui = New-Object System.Text.StringBuilder
[void]$gui.AppendLine(@"
kns_gui_ig_set_armor_default = {
	scope = character
	is_valid = {
		exists = var:kns_ig_attire_target
		var:kns_ig_attire_target = {
			kns_is_imperial_guard_of_trigger = { EMPEROR = root }
		}
	}
	effect = {
		var:kns_ig_attire_target = {
			kns_clear_imperial_guard_armor_flags_effect = yes
		}
	}
}

kns_gui_ig_armor_default_selected = {
	scope = character
	is_shown = {
		exists = var:kns_ig_attire_target
		var:kns_ig_attire_target = {
			kns_is_imperial_guard_of_trigger = { EMPEROR = root }
			NOR = {
"@)
foreach ($k in $clothes.Keys) {
    [void]$gui.AppendLine("`t`t`t`thas_character_flag = kns_ig_armor_$k")
}
[void]$gui.AppendLine(@"
			}
		}
	}
}
"@)

foreach ($k in $clothes.Keys) {
    $dlc = Get-DlcTrigger $k
    $shown = if ($dlc) { "`t`t$dlc = yes" } else { "`t`talways = yes" }
    [void]$gui.AppendLine(@"
kns_gui_ig_set_armor_$k = {
	scope = character
	is_shown = {
$shown
	}
	is_valid = {
		exists = var:kns_ig_attire_target
		var:kns_ig_attire_target = {
			kns_is_imperial_guard_of_trigger = { EMPEROR = root }
		}
	}
	effect = {
		var:kns_ig_attire_target = {
			kns_clear_imperial_guard_armor_flags_effect = yes
			add_character_flag = kns_ig_armor_$k
		}
	}
}

kns_gui_ig_armor_${k}_selected = {
	scope = character
	is_shown = {
		exists = var:kns_ig_attire_target
		var:kns_ig_attire_target = {
			has_character_flag = kns_ig_armor_$k
		}
	}
}
"@)
}

[IO.File]::WriteAllText((Join-Path $Mod "common\scripted_guis\kns_imperial_guard_armor_gui.txt"), $gui.ToString().Replace("`r`n", "`n"), [Text.UTF8Encoding]::new($false))

$btn = New-Object System.Text.StringBuilder
[void]$btn.AppendLine(@"
							button_standard = {
								layoutpolicy_horizontal = expanding
								text = "kns_ig_armor_default"
								down = "[GetScriptedGui('kns_gui_ig_armor_default_selected').IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"
								enabled = "[GetScriptedGui('kns_gui_ig_set_armor_default').IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"
								onclick = "[GetScriptedGui('kns_gui_ig_set_armor_default').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]"
							}
"@)
$lastGroup = ""
foreach ($k in $clothes.Keys) {
    $g = Get-ArmorGroup $k
    if ($g -ne $lastGroup) {
        $lastGroup = $g
        $locG = "kns_ig_armor_group_" + ($g.ToLower() -replace " ", "_")
        [void]$btn.AppendLine("")
        [void]$btn.AppendLine("`t`t`t`t`t`t`ttext_single = {")
        [void]$btn.AppendLine("`t`t`t`t`t`t`t`tlayoutpolicy_horizontal = expanding")
        [void]$btn.AppendLine("`t`t`t`t`t`t`t`ttext = `"$locG`"")
        [void]$btn.AppendLine("`t`t`t`t`t`t`t`tdefault_format = `"#high`"")
        [void]$btn.AppendLine("`t`t`t`t`t`t`t}")
    }
    [void]$btn.AppendLine("`t`t`t`t`t`t`tbutton_standard = {")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`tlayoutpolicy_horizontal = expanding")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`ttext = `"kns_ig_armor_$k`"")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`tvisible = `"[GetScriptedGui('kns_gui_ig_set_armor_$k').IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]`"")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`tdown = `"[GetScriptedGui('kns_gui_ig_armor_${k}_selected').IsShown( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]`"")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`tenabled = `"[GetScriptedGui('kns_gui_ig_set_armor_$k').IsValid( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]`"")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t`tonclick = `"[GetScriptedGui('kns_gui_ig_set_armor_$k').Execute( GuiScope.SetRoot( GetPlayer.MakeScope ).End )]`"")
    [void]$btn.AppendLine("`t`t`t`t`t`t`t}")
}
[IO.File]::WriteAllText((Join-Path $Mod "tools\kns_imperial_guard_armor_buttons.inc"), $btn.ToString().Replace("`r`n", "`n"), [Text.UTF8Encoding]::new($false))

$loc = New-Object System.Text.StringBuilder
[void]$loc.AppendLine(' kns_ig_armor_default:0 "Culture Default"')
$groupsDone = @{}
foreach ($k in $clothes.Keys) {
    $g = Get-ArmorGroup $k
    $gk = "kns_ig_armor_group_" + ($g.ToLower() -replace " ", "_")
    if (-not $groupsDone.ContainsKey($gk)) {
        $groupsDone[$gk] = $true
        [void]$loc.AppendLine(" ${gk}:0 `"$g`"")
    }
    $label = Get-HumanLabel $k
    [void]$loc.AppendLine(" kns_ig_armor_${k}:0 `"$label`"")
}
[IO.File]::WriteAllText((Join-Path $Mod "tools\kns_imperial_guard_armor_loc_fragment.yml"), $loc.ToString().Replace("`r`n", "`n"), [Text.UTF8Encoding]::new($false))
Write-Host "wrote generated armor files, headgear matched=$($hgItems.Count)"
