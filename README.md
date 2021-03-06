# welcome to dunces and dungeons!

master: [![Build Status](https://travis-ci.org/microwaveabletoaster/dunces-and-dungeons.svg?branch=master)](https://travis-ci.org/microwaveabletoaster/dunces-and-dungeons)



# about
dnd is a command-line randomly generated rpg with an emphasis on teamwork. players work together to defeat scores of monsters with unique qualities in sprawling procedurally generated dungeons, and collect plenty of loot in the process!

# play the game from the command line
if you're on any post-xp version of windows, you can head over to the <a href='https://github.com/microwaveabletoaster/dunces-and-dungeons/releases'>release</a> page and download the latest binary for windows. if you're on some sort of *nix system, you're going to need to download the source code from the latest release, run `pip install -r requirements.txt` and run `dunces-and-dungeons.py` with python 2.7.

the source code on the latest release is considered to be the most stable version, but might be behind on some features. clone the repo to play the game at your own risk!

# play WEBDUNCE
ever get tired of staring at a terminal, brainlessly pressing number keys for hours on end? we do too. so, we built webdunce! webdunce is a html frontend for our game, powered by the Flask framework, jquery ui, coffeescript, and redis- and let me tell you, it's pretty great.

however, as with many good things, this takes a little work to experience. luckily for you, i've laid it all out here in a handy <a href='WEBDUNCE.md'>guide</a>.

![loot!](https://dl.dropboxusercontent.com/s/68p3mj77rhvzosi/Screen%20Shot%202016-06-02%20at%206.47.25%20PM.png?dl=0)
![monsters!](https://dl.dropboxusercontent.com/s/kibxynvolqp8gm0/Screen%20Shot%202016-06-02%20at%206.49.34%20PM.png?dl=0)

# contributing
if you encounter a bug or crash, open an <a href="https://github.com/microwaveabletoaster/dunces-and-dungeons/issues">issue</a> and let us know exactly what happened. this helps us out a lot, so thanks!

this repository was a project by cameron egger and john dikeman for their highschool independent study course, and isn't really being actively developed anymore. feel free to mess around with the code, and submit a pull request if you've implemented a feature or made some balance changes that you feel make the game better. i've added some features that we would like to see added in the issues section, so if you need a place to start, check over there! we're probably going to be very accepting of pull requests, so please feel free to contribute.

we're working hard to make the internal documentation better, but at this stage you'll find that most things are commented in the code and everything is relatively easy to follow. if you have any specific questions, open an <a href="https://github.com/microwaveabletoaster/dunces-and-dungeons/issues">issue</a>.
