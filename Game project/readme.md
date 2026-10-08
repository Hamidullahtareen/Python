# Hunt for the Gold

A command-line text adventure game written in Python.

## Idea


You play an explorer searching for a legendary treasure hidden in
Green Valley, a forest full of rivers, trees and caves. Each of the 
three routes (River, Forest, Mountain) is made up of three small
challenges based on real environmental issues, and every choice you
make raises or lowers your "game point," which decide your ending.

At the end of every route, all paths meet in a shared cave with
two more challenges of its own:
1. A medium challenge: cross a mushroom-lit ledge carefully to find an
   iron key.
2. A medium-hard challenge: solve a number-sequence riddle carved
   into a stone panel to unlock a golden key.

The treasure chest has two locks. Both keys are required to open
it — if you're missing either one, the game ends in a locked
ending, no matter how many game point you earned.

## Objective

Find the treasure. Along the way, try to make choices that protect
Green Valley's animals and plants instead of harming them. Your
final "game point" score decides which of three endings you get:
Good, Neutral, or Bad.

## How to play

** For playing the game you have to download the VScode(VisualStudio). Open the file with vscode and run it in the terminal and the play.

1. Run the game:
   python game.py

2. From the main menu, choose 1 to start a new game.
3. Enter your name and age when asked.
4. At the fork in the valley, choose one of three paths:
   River, Forest, or Mountain.
5. Make a choice in the small story event on that path.
6. All paths lead into a shared cave, then the treasure room
   see your ending.
7. From the main menu, choose 2 at any time to see the list of
   previous explorers and their results, saved in (scores.txt).

## Routes
You start by picking one of 3 different paths (River, Forest,
Mountain). Whichever one you pick, it leads into the same shared
cave, where two more challenges reward the iron key and golden key
needed to open the treasure chest. If you have both keys, your
final ending Good / Neutral / Baddepends on your game points. If you're missing a key, you get the Locked ending
instead, regardless of your points. This gives multiple different
ways to experience and finish the game.

## Project structure

Everything is in one file, game.py, organized top to bottom into
sections: the Player class, story text, the three path challenges
(river/forest/mountain), the cave and treasure room, file
saving/loading, and finally the menu and main loop.

(scores.txt )is created automatically the first time someone
finishes the game.
