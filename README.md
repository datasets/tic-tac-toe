This dataset contains tic-tac-toe endgame snapshots. 
First nine attributes are representing nine fields on tic-tac-toe board 
and tenth is class attribute which contains information if x player won.  

## Data

This dataset was found on [UCI - Tic-Tac-Toe Endgame Data set](https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame)

This database encodes the complete set of possible board configurations at the end of tic-tac-toe games, where "x" is assumed to have played first. The target concept is "win for x" (i.e., true when "x" has one of 8 possible ways to create a "three-in-a-row"). 

Interestingly, this raw database gives a stripped-down decision tree algorithm (e.g., ID3) fits. However, the rule-based CN2 algorithm, the simple IB1 instance-based learning algorithm, and the CITRE feature-constructing decision tree algorithm perform well on it.

### Attribute information

* TL : top left square {x,o,b}
* TM : top middle square {x,o,b}
* TR : top right square {x,o,b}
* ML : middle left square {x,o,b}
* MM : middle middle square {x,o,b}
* MR : middle right square {x,o,b}
* BL : bottom left square {x,o,b}
* BM : bottom middle square {x,o,b}
* BR : bottom right square {x,o,b}
* class : 
    * true: x won
    * false: x lost
    
Values are:
* x : x player
* o : o player
* b : blank field

Data is located in directory `data`

`data/hepatitis.csv`

## Preparation

This script should be run using Python 3.

Scripts are in directory `scripts`

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and Licence][pddl] (assuming
either no rights or public domain licence in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/