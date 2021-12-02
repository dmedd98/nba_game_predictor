# Utilizing Machine Learning to Predict NBA Scores

![image](https://user-images.githubusercontent.com/79603572/139289078-528110ad-bcd9-4c9a-9737-cdec72054902.png)

The sports world has not been an exception to the growing impact Data Science has had across the world in the last few decades. The 'Moneyball' Oakland A's are perhaps the most well-known example for their success in the early 2000's despite having one of the lowest payrolls in the MLB. The 2004-05 Phoenix Suns are another example of an early user of analytics to change their style of play. While those two examples were early to the wave of analytics, the rest of the sports world, and specifically the NBA did not take long to follow suit. Advanced metrics have shifted the NBA to higher-volume shooting, a strong emphasis on three-pointers and much higher scoring games. Here's a comparision chart of an average game in the NBA last season compared to 2001.

![image](https://user-images.githubusercontent.com/79603572/139291060-1ff3a229-6e20-4db7-8506-2f0a2366479f.png)

# Business Problem

Knowing that advanced analytics are used by NBA front offices, coaches and players to make major franchise and career decision, I wondered if I would be able to produce a prediction model that could accurately predict results of NBA games. Given the large amount of games, constant shifting of team's performance and utter randomness that comes along with sport, this is not an easy task. However, for my final project with the Flatiron School, I took on the challenge of using Machine Learning to predict the winning team and margin of victory of NBA regular reason games.

# Data

This project used Data obtained from the nba.com API, traditional, advanced and 'four factors' box scores were collected from approxiametly 4,300 games over the previous five seasons (2016-2021). Each box score contained Since the model would not be able to use any data that was not known prior to the game, columns were feature engineered to represent the average from the previous 7 games for team statistics, and the average so far in that season for player statistics. Below you can find a few of team statistics used in the model and their correlation with winning over the course of the 2020-21 season.

![image](https://user-images.githubusercontent.com/79603572/139293117-9df58e0a-6176-4bfe-b41e-da612837f5c8.png)

# EDA

One of the decisions in producing this model was whether or not to include players statisitcs in addition to team statistics when training the prediction models. Using 'load management' to protect top quality players has become commonplace and injuries are unfortunately part of the game. As a result team's are constantly shifting their starting lineups. Testing to see how much one player could impact a team's success, I took a look at the Los Angelas Lakers 2020-21 season, the organization that is home to a 36 year old Lebron James. Despite his age, Lebron was undoubtedly one of the best talents in the league, but he missed 27 of the 72 regular season games with various injuries. The visuals below display the averages of the Lakers in the games he played, the games he didn't as well as the league average. The stark difference between the two versions of the Lakers made it clear that the model must be fed information about the which players were active to be successful.

![image](https://user-images.githubusercontent.com/79603572/139297224-e23126f9-54a2-486f-99bf-ecc575b81ca8.png)


# Model Result

Two models were produced from this project, the first used a Logistic Regression Classifier with the target being the result (Win/Loss) of the Home Team. This model returned an accuracy of 64.375% on a test set of 480 games. Confusion Matrix shown below.


![image](https://user-images.githubusercontent.com/79603572/139298191-0bc35c1a-cc60-434e-adac-3b97c1a6b050.png)

The second model used a lasso regression to predict the margin of victory (or defeat) of the Home Team. This model returned a Root Mean Square Error of 12.9.
It was hard to know whether or not that was low enough to consider the model a success or not, so I compared the model predictions to the spread for each game in the test set. FYI, the spread is the amount of points sportsbooks will give or take from a team to 'even the playing field.' For example, if the home team is favored by 5.5 points, the home team must win by 6 or more for a bet on them to win. I tested the results of using the model's predictions to place a hypothetical $100 wager on each game in the test set. It is standard for sportsbooks to have a 5% 'vig' on spread bets, meaning a risk of $100 would pay out $90.91 and to be profitable in the long run you must be correct > 52.4% of the time. Fortunately, the model's prediction has a 56.14% success rate on the spread bets. The chart below shows the monetary result of the model predictions over the test set.

![image](https://user-images.githubusercontent.com/79603572/139301918-1bd86abf-efab-401a-9ef4-50c86e553ab0.png)


# Next Steps:

To bring the model along further I would use more and more test data, experiment with different combinations of features, specifically would like to bring in strength of teams played in previous games as well as matchup specifics into the mix to take the model to the next level. 

# Contributor

For more information, take a look at the [Final Notebook](https://github.com/dmedd98/nba_game_predictor/blob/main/Final_Notebook.ipynb) and [Non-Technical-Presentation](https://github.com/dmedd98/nba_game_predictor/blob/main/Capstone%20PP%20Dillon%20Medd.pdf) 

Dillon Medd
-  [GitHub](https://github.com/dmedd98)
-  [LinkedIn](https://www.linkedin.com/in/dillon-medd/)

