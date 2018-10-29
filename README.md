# Apocalyptech's Starbound Mods

Just a collection of mods that I've been using for my own use.  There are
doubtless already Steam Workshop versions of many of these; I admit that
I didn't actually look for existing mods, preferring to just whip up my
own when I wanted something done.

These are pretty much invariably all basically cheat mods.  Some are
extremely OP, others only a bit so.  Anyway, just distributed as text,
so feel free to edit to suit.  Put 'em in your Starbound `mods` folder
if you want to use 'em.

All of these use the `.patch` syntax where appropriate, so they should be
as compatible as possible with any other Starbound mods.

## Faster Crafting

Increases the crafting time to be nearly instant for all crafting operations.
This is actually generated by the Python script `generate.py` in the mod
dir, which finds all the crafting recipes in an unpacked Starbound asset dir
and creates the `.patch` files appropriately.  Source/Dest dirs are hardcoded
at the top.

## Fossil Tweaks

This one's not actually general-purpose; I'd just used it to alter the
probabilities of some specific fossils, to complete my collection without
as much fuss.  Won't do you any good unless you happen to be missing the
last few that I was missing.

## More Boneboo

Boneboo was the hardest seed type for me to find -- I'd been to many Bones
biomes, but there was never Boneboo there.  Anyway, this mod increases
Boneboo density within Bones biomes, which let it pop right up on the next
one I visited.

## More Durasteel

Durasteel's got a ton of uses, and I thought it'd be nice to have more of
it.  This one's not *extreme*, just increases Durasteel quantity by 1.5x.

## More Fossils

I enjoyed fossil hunting but wanted more fossils around to excavate.  This
increases their probability by 3x.

## More Iron

Iron is one of the harder resources to accumulate, so this bumps its quantity
by about 1.5x.

## No Need to Hunt

Folds the hunting loot pools into the "main" loot pools for creatures, so that
hunting-specific weapons are mostly useless.  Technically the hunting-specific
drop rates will be a little less than what hunting weapons use, since the
creatures still drop their non-hunting loot, too, but it should be better than
stock.  Chances for action figures have been buffed a bit as well, for the
creature types that the mod touches.

This mod's generated with `generate.py` and requires an uncompressed vanilla
data package to do its stuff.  Various paths are hardcoded in the code.

## Omega Augment

An augment for your EPP which includes literally every augment status effect.
Very balanced!  Doesn't drop anywhere ingame, so it must be spawned manually
while in admin mode, with `/spawnitem omegaaugment`.  Note that the effects
stack a bit weirdly in water - you'll fall rather slowly, and rise/jump
*very* quickly.  You'll be launching yourself in the air from puddles.

## OP Mech Beam Drill

Improves the Mech's Beam Drill.  Hardly tested, actually, as I find the mech
bits quite dull.

## OP Mech Intrepid / OP Mech Protector / OP Mech Zero

Makes the Intrepid Mech Legs, Protector Mech Body, and the Zero Mech Booster
quite OP, respectively.  Balance!

## OP Mech Tesla

Makes the Tesla Stream Mech Arm quite OP.  Tear through those enemies!

## OP Plasma

Makes the Plasma Assault Rifle (yes, I know, already an extremely good
weapon) quite OP.

## OP Protector

Makes the Protector's Broadsword (yes, I know, already an extremely good
weapon) quite OP.

## OP Seeker's Set

Makes the Seeker's armor set quite OP (double stats on everything, basically).

## Trivial Archaeology

Even though I did enjoy fossil hunting, by the end I was a bit tired of the
minigame, so this simplifies it by giving effectively unlimited tool uses for
all tools, and gets rid of all rock cover which isn't actually right on top
of the fossils/chests.  Replaces the main Fossil Minigame LUA file
entirely (since obviously those can't be `.patch`ed), so this won't be
compatible with anything else which does the same.  With a bit more work I
could probably have just made the minigame automatically succeed or something,
or reduce the covered tiles to a single square or something, but meh.  This
was good enough.
