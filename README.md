Infinite map within a finite amount of memory. All locations stay the same. 

Press the directional arrows to move the player sprite. When the sprite reaches the end of the screen, the map changes.

Concepts:

    - A list of random numbers is generated when the game starts.

    - Sprite randomization is based on the initial random number grid and the current player coordinates. A new number list is generated each time the screen changes (when the player leaves the screen)

    - Calculations for sprite type, position and color are determined by the numbers in the number list. In certain cases, numbers from the original list are used. 

    - The only static memory is the original number list, coordinates (x, y) and player sprite attributes. 

    - Current, non-static memory changes for each map. This is the npc/map sprites. 

    - To prevent large numbers and to keep values within acceptable ranges for calculations in this demo, map keys are kept within a range of 1-999. For more detailed applications, the ceiling for these values can be higher. 
    

Notes:

    - Randomization quality can be increased further by making more complex math-based algorithms for sprite generation.

    - Theorhetically, an infinite map is impossible, at least in this sense. Eventually, the calculations would match another map exactly. Even with a large range of calculation values. This may not happen for any user, but it is possible. This idea raises the real-life question of alternate universes existing out there somewhere in space (or time? or elsewhere?). I'm not saying this code is how the universe is, but it could share similar concepts.

    - This is only a conceptual demo (as you can probably guess by the basic 2-d sprites and blank background :) ). This type of code can definitely be applied in more complex cases, and provides the building blocks for the logic in other, potenitally more advanced algorithms.




Created by Jason Dunn

JGD Designs

https://www.github.com/jgddesigns

jgd.email24@gmail.com
