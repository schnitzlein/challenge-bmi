# challenge-bmi
Challenge Solution from lat get-in-engineering Challenge from 2020

## Challenge Task
Task is to solve a challenge with two logistical storage transporter.

+ Transporter1 = Driver1 + Cargo
+ Transporter2 = Driver2 + Cargo

Cargo is a fixed table with elements
Each Transporter can only transport 1100 kg or 1100000 g including driver + cargo


## Main Challenge

Ger:
Main Task:
Was ist die optimale Beladung (Summe der Nutzwerte),
wenn die beiden Transporter jeweils einmal fahren können?
Erstelle einen Algorithmus,
der die bestmögliche Ladeliste für jeden der beiden Transporter ermittelt.

En:
Main Task:
Estimate the optimum Cargo load (sum up all weights)
if both transporter can only drive once?
Create algorithm which calculates the best cargolist for both transporter.

Assuming the high priority cargo is most important this is taken at first, than the second. priority ...
and so on.

## Solution
quick and dirty python program with todo for develop this prototype to fully grown up software application.
"Algorithm" is a simple ordering solution.
Order the list in priority, (or you could create a hashmap for it), 
pick the items with highest priority.
If it doesnt fit in current cargo space, split it and take the rest in cargo space 2.
If there is free space? which can be filled from lower priority cargo it will be filled.


![PlantUML model](https://raw.githubusercontent.com/schnitzlein/challenge-bmi/main/algo_plantuml.png)