# Identify_User_By_Game_Pattern
This project has been started from the idea that is it possible to identify the user from the gaming pattern


Korea and Japanese descriptions are followed by the English.


## Problem:

Nowadays, game has bigger meaning and importance than just amusement.

Some of the game players regard the game world as a second life.

The players want that the game (especially in the competitive games) should be fair to every player.

However, there are many approaches for finding and blocking the hacks and bots. 

But, relatively few number of detecting the unauthenticated user such as the act called boosting.

The necessity of second authentication is emerging.


## Suggested Approach:

It should be additional authentication system. 

- It analyzes the gamers' behavioral aspects (biometrics) while they playing game without requiring additional equipment.

Possible to certify the user

- without interruption, awareness, and giving stress.


## The diagram of the idea


![image](https://user-images.githubusercontent.com/90700648/183899747-2919e162-c4cf-41ac-8c92-70a560a612a6.png)


## Factors to be measured (and for future study):

1. Reaction Time

2. Accuracy

(3). Click per minute

(4). Key settting

(5). Social activity


## Data Flow Diagram:

<img width="561" alt="스크린샷 2022-08-10 오후 9 28 19" src="https://user-images.githubusercontent.com/90700648/183901148-240ed19c-0a06-4e68-b97c-33649658b4a7.png">


## Processing Module Diagram:

<img width="571" alt="스크린샷 2022-08-10 오후 9 29 24" src="https://user-images.githubusercontent.com/90700648/183901385-9dc78f0d-7be9-4146-91fb-a82fae6f882f.png">


## Implemented System

Self Organizing Map (SOM)

* One of Artificial neural network using unsupervised learning

* Display high dimensional dataset into 2-dimensional space


<img width="438" alt="스크린샷 2022-08-11 오후 8 19 18" src="https://user-images.githubusercontent.com/90700648/184122148-6a1b9bf1-8d78-4e29-a43f-6f9fb6c9ee39.png">



## Experimentation (1)
* Data collection
** Simple click game by using Processing


<img width="390" alt="스크린샷 2022-08-11 오후 8 20 21" src="https://user-images.githubusercontent.com/90700648/184122341-087a6645-e6c0-49fd-872d-bfd0d9f9a52f.png">

* Example of the game screen


<img width="495" alt="스크린샷 2022-08-11 오후 8 21 22" src="https://user-images.githubusercontent.com/90700648/184122505-3a2a1af4-5d76-47c9-b130-27a73cc197d6.png">


* Clustering

- Organize the saved dataset by user

- Data:
 
 -- Three users
 
 -- 200 game play data by user
 
- Use the program named "Living for SOM"

- SOM setting:

-- 40 number of trainings

-- 0.6 learning rate

-- 0.1 neighbor width


## Result


<img width="629" alt="스크린샷 2022-08-11 오후 8 26 13" src="https://user-images.githubusercontent.com/90700648/184123306-32ad6edc-da92-4e43-8630-939cc4387a1d.png">


## Limitation and Future Work

- The SOM has advantage in classifying the user by clustering the dataset

-- Not enough to use as the authentication

-- Other technical method is required

-- decision of the boundary for cluster is essential


- One or two behavioral aspects are not enough to be biometric authentication

-- Need more behavioral aspects to consider
