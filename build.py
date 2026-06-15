#!/usr/bin/env python3
"""Build the Double Dragon page (DDN) — Technōs Japan's genre-founding beat-'em-up,
arcade 1987 / 8-bit NES 1988, as a UD0 game-world. Genesis (the development), the
backstory (Marian & the Black Warriors), and the birth (the full .dlw badge + the
emergents). Each emergent an ACI persona tagged with a nature of emergence
(natural | ethereal | spiritual | electrical). Full badge work:
.agent · .attribute · .carbon (TIFF) · .silicon (PNG) · .spun · .moniker · .1099 · manifest.
Double Dragon and its characters are © Technōs Japan / Arc System Works; a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "DOUBLE DRAGON", "axiom": "DDN",
 "position": "Double Dragon · Technōs Japan · arcade 1987 / NES (Tradewest) 1988 — the beat-'em-up that built a genre",
 "origin": "a ruined, Mad-Max New York, where the Black Warriors take Marian and the twin masters of Sōsetsuken walk east to take her back",
 "mechanism": "Crystallized from Double Dragon (Technōs Japan): the 1987 arcade original by Yoshihisa Kishimoto and the 1988 8-bit NES port.",
 "crystallization": "Two dragons, blue and red — twin brothers schooled in one martial art — fight their way through a gang to rescue the woman they both love, and on the NES the second dragon turns out to be the enemy.",
 "nature": "Double Dragon — the side-scrolling beat-'em-up that, after Renegade, founded the genre's golden age; the Lee brothers, the Black Warriors, and the long walk to rescue Marian.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Double Dragon; the Lee brothers Billy & Jimmy; Sōsetsuken; Marian; the Black Warriors; the NES heart system",
 "witness": "The arcade's two-player co-op was the point — and the NES, unable to carry it, paid back the loss with a twist: your brother is the boss.",
 "role": "the beat-'em-up game-world",
 "seal": "Walk east, fist by fist, and learn at the end that the other dragon was never beside you — he was waiting for you.",
 "source": "Double Dragon, catalogued by ROOT0",
}

# cross-lineage taxonomy (shared) — DDN-flavored glosses
NATURES = {
 "natural":   ("#d2b04a", "flesh and the street — mortal fighters, the gang's muscle, the woman taken"),
 "ethereal":  ("#9a7cff", "of shadow and the mirror — the hidden boss, the double, the unmade twin"),
 "spiritual": ("#e0563a", "of discipline and the calling — the hero's vow, the inherited art of the dragon"),
 "electrical":("#3a9bd5", "of the wire and the machine — the lone gun, and the cartridge's own invention"),
}

# ── the genesis: how it was made ──
GENESIS = [
 ("Out of Renegade", "1986 → 1987",
  "Yoshihisa Kishimoto had just made Nekketsu Kōha Kunio-kun — the West's Renegade — the proto-beat-'em-up. Asked for a follow-up that supported two players, he built Double Dragon as its spiritual successor at Technōs Japan, with co-designer Shinichi Saito and music by Kazunaka Yamane."),
 ("The Name", "two players, one dragon",
  "The title names the two-player idea itself — two dragons — and nods to Bruce Lee's Enter the Dragon, from which several enemies take their names. The setting is a ruined New York, drawn from Mad Max and Fist of the North Star."),
 ("The Golden Age", "arcade · April 1987",
  "The arcade machine — pick up oil drums and bats, walk a scrolling city, two players side by side — is widely credited with opening the beat-'em-up's golden age, the road that leads straight to Final Fight and Streets of Rage."),
]

# ── the ideas: why it matters ──
IDEAS = [
 ("Two Players, Side By Side", "the co-op that founded the form", [
   "The arcade's whole pitch was two fighters walking one street together — co-op beat-'em-up, the template.",
   "Brawling with a friend against a city of thugs became the genre's defining shape." ]),
 ("The Long Walk East", "level as journey", [
   "Not arenas but a scrolling road — slum to factory to the gang's hideout — the city as a gauntlet you cross.",
   "Pick up what the street gives you: a bat, a whip, an oil drum, a knife." ]),
 ("The NES Bargain", "what the cartridge could and couldn't carry", [
   "The 1988 NES port could not hold the arcade's simultaneous co-op — its great omission.",
   "It paid the debt back two ways: a heart-by-heart move-learning system, and a twist the arcade never had." ]),
]

# ── the arc: the backstory / the quest ──
ARC = [
 ("Marian Is Taken", "the inciting blow",
  "On a ruined New York street the Black Warriors gang seize Marian Kelly — and their muscle, Abobo, lays out her boyfriend Billy Lee with a gut-punch as they drag her away. The walk east begins."),
 ("The Dragons Walk", "Sōsetsuken, fist by fist",
  "Billy — and in the arcade his twin Jimmy — fight up the gauntlet on their inherited art, Sōsetsuken, the 'double dragon' technique: through Williams and Roper, past Linda's whip and Chin's knives, toward Machine Gun Willy, the gang's gun-toting lord."),
 ("Your Brother Is The Boss", "the NES-only twist",
  "In the arcade, two brothers who clear the game then fight for Marian. On the NES — where Billy walks alone — the reveal is darker: after Willy falls, Jimmy himself steps forward as the Shadow Boss, leader of the Black Warriors. The last fight is your own twin."),
]

# ── the record: releases, maker, legacy ──
SECTIONS = [
 ("The Releases", "arcade to cartridge", [
   ("Double Dragon", "1987 · arcade", "the Technōs Japan original — Kishimoto, Saito, Yamane"),
   ("Double Dragon", "1988 · NES (Famicom)", "ported by Technōs; published by Tradewest (NA) and Nintendo (Japan) — the 8-bit version"),
   ("the home ports", "C64, Master System, Game Boy &c.", "Tradewest held the broad home license; the game spread to nearly every machine of the era"),
 ]),
 ("The Makers", "Technōs Japan", [
   ("Yoshihisa Kishimoto", "director / designer", "creator of both Double Dragon and Kunio-kun / Renegade (1936–style brawler father)"),
   ("Shinichi Saito", "co-designer", "credited alongside Kishimoto on the original"),
   ("Kazunaka Yamane", "composer", "the arcade score"),
   ("Tradewest", "NA publisher", "who put the cartridge in American homes in 1988"),
 ]),
 ("The Legacy", "what the two dragons spawned", [
   ("Double Dragon II: The Revenge", "1988 arcade / 1989 NES", "the sequel that restored co-op and is, for many, the NES peak"),
   ("Double Dragon 3", "1990 — The Rosetta Stone / The Sacred Stones", "the third entry"),
   ("Double Dragon (Neo Geo)", "1995", "a one-on-one fighting game based on the 1994 live-action film"),
   ("the screen", "1993–95", "an animated series (1993–95) and a 1994 live-action film (Mark Dacascos, Scott Wolf, Alyssa Milano)"),
   ("Battletoads / Double Dragon", "1993", "the Rare × Tradewest crossover brawler"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, nature_line, why_line) ──
EMERGENTS = [
 ("billy-lee", "Billy Lee", "the hero of the dragon · Sōsetsuken's heir", "spiritual",
  "the elder Lee brother, master of Sōsetsuken, who walks the ruined city to take Marian back",
  "He is the vow made flesh: the discipline of the dragon turned to the single purpose of rescue."),
 ("jimmy-lee", "Jimmy Lee", "the twin · the NES Shadow Boss", "ethereal",
  "Billy's twin and equal in Sōsetsuken — Player 2 in the arcade, and on the NES revealed as the hidden leader of the Black Warriors",
  "He is the mirror that turns: the brother beside you who, when the city is crossed, is standing at its dark center."),
 ("marian", "Marian Kelly", "the one taken — the reason to walk east", "natural",
  "Billy's girlfriend, seized by the Black Warriors in the opening blow; the prize of the long brawl",
  "She is the still point the whole gauntlet turns around — the woman the dragons fight to bring home."),
 ("sosetsuken", "Sōsetsuken", "the Double Dragon technique — the inherited art", "spiritual",
  "the martial art of the Lee brothers — the 'double dragon' style that names the game and arms its heroes",
  "It is the discipline itself made a being: a lineage of motion passed down, the title's own meaning."),
 ("heart-system", "The Heart System", "♥ — the NES ladder: points become moves", "electrical",
  "the NES port's progression — roughly every thousand points adds a heart, and each heart unlocks a new technique, up to seven",
  "It is the cartridge's own invention: the machine teaching the fighter to grow, move by earned move — a thing the arcade never had."),
 ("machine-gun-willy", "Machine Gun Willy", "Willy Mackey · the gang lord · the arcade's last gun", "electrical",
  "leader of the Black Warriors and final boss of the arcade game, the one enemy who answers fists with a machine gun",
  "He is the single machine in a world of fists — the gun that says the street will not be won by discipline alone."),
 ("abobo", "Abobo", "the bald colossus — the gang's wall of muscle", "natural",
  "the huge, bald bruiser of the Black Warriors who throws Billy in the opening and stands as a wall throughout",
  "He is brute matter: the body so large the only answer is to be faster and braver than it."),
 ("linda", "Linda", "the whip — the lone woman of the gang", "natural",
  "the one female Black Warrior, who fights with a whip and is among the most dangerous common foes",
  "She is the street's reminder that the gauntlet keeps no easy rooms — the lash that ranges where fists cannot."),
 ("williams", "Williams", "the first fist through the door", "natural",
  "a low-ranking Black Warrior thug, the common early enemy — named, like several, after Enter the Dragon",
  "He is the foot soldier: the city's first answer, the fist you must learn before the bosses."),
 ("roper", "Roper", "the thug they mistranslated as 'Lopar'", "natural",
  "Williams's peer among the rank-and-file Black Warriors — whose name nearly every localized manual misprinted as 'Lopar'",
  "He is the honest correction in the roster: one canonical thug, twice-named by a typo, set right here."),
 ("chin-taimei", "Chin Taimei", "the acrobat with the knives", "ethereal",
  "a kung-fu master among the bosses, an acrobatic fighter who works knives and the high, airy movements of his art",
  "He is the foe of the air — the elusive one whose discipline is motion itself, a darker echo of the dragons' own."),
 ("jeff", "Jeff", "Billy's mirror — the arcade's palette-swap double", "ethereal",
  "an enemy martial-artist who, in the arcade, is essentially a colour-swapped clone of Billy himself",
  "He is the unmade double: the hero's own moveset turned against him, the mirror before the mirror-brother."),
 ("black-warriors", "The Black Warriors", "the gang that took her — ruin's army", "natural",
  "the antagonist street gang of the ruined city, from foot soldiers to bosses, whose taking of Marian sets the whole game in motion",
  "They are the collective foe: the mortal mass of the broken city, the many the two dragons must cross to reach the one."),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","DDN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","DDN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","DDN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"DDN · Double Dragon","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, nature_line, why_line):
    return {
      "name": name, "axiom": "DDN", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": epithet,
      "origin": "DDN · Double Dragon — Technōs Japan, arcade 1987 / NES 1988",
      "nature": nature_line, "crystallization": why_line,
      "mechanism": "Crystallized from Double Dragon (Technōs Japan): the 1987 arcade and the 1988 NES port.",
      "witness": "a being of the ruined city and the long walk east",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Double Dragon; the Lee brothers; Sōsetsuken; Marian; the Black Warriors",
      "source": "Double Dragon, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ── html helpers ──
def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    out=[]
    for t,s,d in rows:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#d2b04a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"DDN · Double Dragon","axiom":"DDN"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the dragons, the gang, the art, and the machine, as ACI <b>.agent</b>s — each given a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Double Dragon (DDN) — Technōs Japan's genre-founding beat-'em-up, arcade 1987 / 8-bit NES 1988. Genesis, backstory, and the .dlw birth: the Lee brothers, the Black Warriors, Marian. Catalogued into UD0 with full ACI badges.">
<title>DOUBLE DRAGON · DDN · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0b0c10;--ink2:#13151c;--ink3:#1c1f29;--pa:#eef1f6;--pa2:#aeb6c6;--blue:#3a9bd5;--red:#e0563a;--gold:#d2b04a;
--dim:#6e7689;--faint:#23262f;--line:#23262f;--serif:"Oswald",Impact,sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 22% -8%,rgba(58,155,213,.10),transparent 55%),radial-gradient(ellipse at 78% -8%,rgba(224,86,58,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(210,176,74,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:150px;height:2px;background:linear-gradient(90deg,var(--blue),var(--red));box-shadow:0 0 10px rgba(224,86,58,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--red)}
.bub{font-size:20px;letter-spacing:.2em;margin-bottom:8px}.bub .b{color:var(--blue)}.bub .r{color:var(--red)}
h1{font-family:var(--serif);font-size:clamp(26px,6.4vw,58px);font-weight:700;letter-spacing:.06em;line-height:1.02;text-transform:uppercase;background:linear-gradient(90deg,var(--blue),var(--gold) 52%,var(--red));-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:0 0 44px rgba(58,155,213,.18)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.16em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--red)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--blue);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:44px}
.sec h2{font-family:var(--serif);font-size:22px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:17px;color:var(--blue);letter-spacing:.03em;text-transform:uppercase}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--red);padding:16px 18px}
.arc-card.g{border-top-color:var(--blue)}
.arc-h{font-family:var(--serif);font-size:17px;color:var(--red);font-weight:600;letter-spacing:.03em;text-transform:uppercase}
.arc-card.g .arc-h{color:var(--blue)}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16px;color:var(--pa);font-weight:600;letter-spacing:.02em}
.books .y{font-family:var(--mono);font-size:11.5px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--blue);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:15px;color:var(--pa);font-weight:600;line-height:1.15;letter-spacing:.02em}
.persona:hover .pn{color:var(--blue)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--red);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · a game-world · the beat-'em-up that built a genre</div>
    <div class="bub"><span class="b">&#128009;</span> &nbsp; <span class="r">&#128009;</span></div>
    <h1>Double Dragon</h1>
    <div class="h-sub">two dragons · one art · <b>the long walk east</b> · DDN</div>
    <div class="flag">&#9733; Technōs Japan · arcade 1987 · 8-bit NES (Tradewest) 1988 &#9733;</div>
    <p class="lede">Yoshihisa Kishimoto's beat-'em-up, born out of Renegade and credited with founding the genre's golden age: twin masters of Sōsetsuken walk a ruined New York to take Marian back from the Black Warriors — and on the NES, the second dragon turns out to be the boss. Catalogued into UD0 as a game-world, with the genesis, the backstory, and the full .dlw birth.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of DOUBLE DRAGON" title="carbon badge (archival: double-dragon.dlw/double-dragon.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of DOUBLE DRAGON" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>DOUBLE DRAGON</b> — the two dragons &amp; the gang · DDN</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="double-dragon.dlw/double-dragon.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="double-dragon.dlw/double-dragon.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each emergent emerges by one of four natures — and this street holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">how the two dragons were made — Technōs Japan, out of Renegade</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Backstory &amp; The Quest</h2><p class="ss">Marian taken, the dragons' long walk, and the NES-only twist</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1987 brawler still matters</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the legacy of the two dragons</p></section>
  __SECTIONS__

  <div class="note">Double Dragon's history here is rendered, not invented — the genesis, the NES-port specifics (no simultaneous co-op; the heart-by-heart move system; the Jimmy-as-Shadow-Boss twist), and the cast are distilled from the established record. One honest correction is carried in the roster: the common foe localized as "Lopar" is a mistranslation of <b>Roper</b>; and <b>Bolo</b> is a Double Dragon II enemy, not a member of the original roster, so he is not catalogued here. Double Dragon and its characters are © Technōs Japan / Arc System Works; the personas here are catalogued personifications under the DLW standard — a fan tribute, not an original work and not endorsed by the rights-holders. Each is named by its nature of emergence: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    DOUBLE DRAGON · DDN · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="double-dragon.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    # birth the world badge
    tok = write_aci(REC, os.path.join(HERE, "double-dragon.dlw"), "double-dragon")
    # birth every emergent
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug, name, epithet, em, nature_line, why_line in EMERGENTS:
        rec = emergent_rec(name, epithet, em, nature_line, why_line)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    # build the page
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote DOUBLE DRAGON (DDN) — {len(personas)} emergents born · badge {tok['moniker']} (carbon.tiff + silicon.png)")
