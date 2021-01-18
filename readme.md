# Code test - Quantitative Model Developer

## Task 1

The python script distance_calc.py is a command line program. It imports geoloc.csv or creates geolocation randomly.
The distance between every location is calculated and the pair with the according distance are printed out in an ascending order.
Moreover, the average distance and the closest pair to the average distance is printed out in the bottom line.

### How to use
The python script distance_calc.py is written in python3 and can be executed through the terminal.
The input of the function calc_distances() determines whether geoloc.csv is imported or random geolocations are used to calculate the pair distances.

### calc_distances
**calc_distances(n='import')**

    * Input:
      - n: integer
        The integer n determines how many random location entities are generated.
        By default n='import' the geoloc.csv is imported.

    * Output:
      Prints out the distances for each pair of locations within the data.
      Prints out the average distance and the closest location pair to the average.


## Task 2
