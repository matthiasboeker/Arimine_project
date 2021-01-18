# Code test - Quantitative Model Developer

## Task 1 - Coding

The python script distance_calc.py is a command line program. It imports geoloc.csv or creates geolocation randomly.
The distance between every location is calculated and the pair with the according distance are printed out in an ascending order.
Moreover, the average distance and the closest pair to the average distance is printed out in the bottom line.
In order to calculate the distance, the Haversine formula is used. The earth radius is assumed to be 6372.8 km.

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


## Task 2 - Forecasting Air Quality
  * Describe model approach
  * Answer questions A and B

### Forecasting global Air Quality
Before the modeling starts various questions need to be answered.
1. How is the data quality?
   - Is there missing data?
   - Is the given data reliable?
2. How can we access the data?
   - Do we have streaming data or batches?
   - What data format are we dealing with?
3. Is there access to additional data?
   - Temperature and humidity data
   - Wind data

#### Preprocessing
The air quality is collected from various locations and gathered in a database.
For each air quality data stream the data preprocessed.
Potential outliers are detected and processed and the data is formatted in convenient way for the analysis.

#### Feature Engieering
The data set can be enriched with additional data on external factors, which correlate with the measurements of PM2.5. Once different features are determined, the feature engineering can take place.
The feature engineering can help selecting relevant features for the forecast and enhance potential expert knowledge.

#### Train/Test Split
Split the data set in train and test data set. The test data set will be needed for the evaluation of the predictions. The train data set can now also be applied to evaluate performance between different model approaches.

#### Hyperparameter tuning/ Model fitting
Depending on the used forecasting model, the hyperparameters of the according model have to be fitted and tuned. Cross-Validation can be applied to find the best set of hyperparameter with gird search or gradient searches for example.

#### Testing
Once the model/ models are tuned, their performance can be tested on the yet untouched test data set.
The best performing model is chosen.

#### Deployment
The chosen model has to be deployed and evaluated again over time. Concept drift and shifting paradigms must be avoided.


**Key Challenges for Air Quality Forecasting**
One challenge is the interpolation of the given forecasts.
The forecast will be given for a grid in which only in a few grid cells the measurements are taken. For the other grid cell interpolation has to be conducted to calculate likely air pollution.

It is known that different areas are differently affected by air pollution. The forecast must consider the difference between urban and rural areas but also climate characteristics and topological characteristics. This depends on the scale of the model and how local and accurate the model is supposed to be.

Air pollution is affected by seasons. Air pollution is next to external factors like temperature also affected by time factors. The pollution within cities rises during the rush hour and decreases during holidays. This can lead to complicated seasonal affects.

**Impact on complexity**
The time series are only measuring the air quality at a specific place. The models are only temporal, whereas the timelapse considers a spacial-temporal model. Next to the time dependency a spacial dependency has to be considered. The effects of dispersion comes in to play, which would be ignored in the pure measurement of time series. Thus the complexity rises with the integration of spacial information. Futhermore, the amount of data rises to which brings up different challenges, too.


## Task 3 - Forecasting Pollen

The main difference between pollen and air quality is their presence in different locations. It is assumed that PM2.5 can be measured all over the world, whereas different pollen species can vary locally.
Furthermore, the spread of pollen comes with a different set of characteristics. The time dependency in pollen fly is even more seasonal than the air quality. Different pollen species begin and stop blooming in different times. Their occurrence is less affected by human behavior than the air quality. 
The effect of external factors like rainfall can be differently affect the pollen fly, so reliable weather forecasting is crucial for the pollen forecast.
