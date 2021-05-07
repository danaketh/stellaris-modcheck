# Stellaris Mod Check
Because modded multiplayer is still pain in the butt even after PI implemented
mod profiles (playsets), I've decided to build tools to help with the issue.

Main problem when playing modded multiplayer sessions is difference in versions.
I can't tell if the culprit here is Steam or Paradox Interactive. What I can tell
is the problem - updates. Sometimes no matter how much you try, Steam just won't
update your mods but there is no way for you to find out where the problem is.

That's where this tool comes in. Just run the script (if you have Python installed)
or download the binary. You should end up with file called `playsets.json`.

Tell your friends to do the same. Now wait until my lazy ass has time to also write
and publish the frontend for comparing the files with files from your friends.

## Requirements
- Python 3.7
- pyinstaller 4.2 (if you want to build it)