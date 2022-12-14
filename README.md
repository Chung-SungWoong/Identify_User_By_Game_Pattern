# Identify_User_By_Game_Pattern
This project has been started from the idea that is it possible to identify the user from the gaming pattern

Korean and Japanese descriptions are followed by the English.


이 프로젝트는 플레이어의 게임 습관 혹은 게임 패턴으로 본인 확인이 가능한지에 대한 아이디어에서 출발하였습니다.


このプロジェクトは、プレイヤーのゲーム習慣またはゲームパターンで本人確認が可能かどうかの疑問から始まりました。


## Problem:

Nowadays, game has bigger meaning and importance than just amusement.

Some of the game players regard the game world as a second life.

The players want that the game (especially in the competitive games) should be fair to every player.

However, there are many approaches for finding and blocking the hacks and bots. 

But, relatively few number of detecting the unauthenticated user such as the act called boosting.

The necessity of second authentication is emerging.



날이 갈수록 게임은 사람들에게 단순한 유희를 넘는 의미를 가지며 또 하나의 세상으로 여겨지기도 합니다.

게이머들은 특히 게임의 공평성을 매우 중요하게 생각해 게임의 공평성을 해치는 행위인 봇, 핵, 혹은 대리 (게임을 다른 사람이 대신 해주는 행위)같은 행위에 분노를 느끼기도 합니다.

그러나 상대적으로 핵과 봇을 잡는 기술은 많은 발전과 여러 방식이 있지만 대리를 적발하는 방식은 아직까지 미흡한 경우가 많습니다.

대리 행위를 방지하기 위한 이중 인증의 필요가 늘어가고 있습니다.



最近、ゲームは人に単純な遊戯を越える意味を持ち、もう一つの世の中と見なされることもあります。

ゲーマーたちは特にゲームの公平性を非常に重要視し、ゲームの公平性を害する行為であるボット、ハック、あるいは代理(ゲームを他人が代わりにしてくれる行為)のような行為に怒りを感じることもあります。

しかし、相対的に核とボットを握る技術は多くの発展と様々な方式がありますが、代理を摘発する方式はまだ不十分な場合が多いです。

代理行為を防止するための二重認証の必要が増えています。


## Suggested Approach:

It should be additional authentication system. 

- It analyzes the gamers' behavioral aspects (biometrics) while they playing game without requiring additional equipment.

Possible to certify the user

- without interruption, awareness, and giving stress.


여기서 제안하는 방식은 주된 인증 방식이 아닌 본인 인증을 보완하는 시스템으로 게임 유저의 행동적 측면을 측정(생체 측정)하여 게임중 또 다른 장비나 요구없이 본인 인증을 하는 것입니다.

- 플레이어에게 최대한의 방해, 인식, 그리고 스트레스를 줄이는 것이 주요한 목적입니다.


提案する方法は主な認証方式ではなく本人認証を補完するシステムでゲームユーザーの行動的側面を測定（生体測定）してゲーム中他の装備や要求なしにゲームプレイヤーを確認することです

- プレイヤーに妨害、認識、またはストレスを最大限に減らすことが大事です。



## The diagram of the idea


![image](https://user-images.githubusercontent.com/90700648/183899747-2919e162-c4cf-41ac-8c92-70a560a612a6.png)


## Factors to be measured (and for future study):

1. Reaction Time  반응 속도  反応速度

2. Accuracy  정확도  正確度

(3). Click per minute  매분마다의 클릭 숫자  毎分ごとのクリック数

(4). Keyboard settting  키보드 세팅  キーボードセティング

(5). Social activity  게임 내에서의 사회적 활동  ゲームの中での社会的な活動


## Data Flow Diagram:

<img width="561" alt="스크린샷 2022-08-10 오후 9 28 19" src="https://user-images.githubusercontent.com/90700648/183901148-240ed19c-0a06-4e68-b97c-33649658b4a7.png">


## Processing Module Diagram:

<img width="571" alt="스크린샷 2022-08-10 오후 9 29 24" src="https://user-images.githubusercontent.com/90700648/183901385-9dc78f0d-7be9-4146-91fb-a82fae6f882f.png">


## Implemented System

Self Organizing Map (SOM)

* Sort of Artificial neural network using unsupervised learning

* Display high-dimensional dataset into 2-dimensional space

* The winner-take-all process, a sort of competitive neural network, choose a node closest to the input vector as a winner and adjust the weight so that the winner is closer to the input vector.

* Each node is related to the neighbors, so when a node wins a competition, the weight of the neighbor's node also changes, however, the changing value gets smaller as the neighbor is far away from the winner.

* This process will be repeated for each input vector.



자기조직화 지도 (SOM)

* 비지도 학습을 이용한 인공신경망 중 하나

* 2차원 공간에 고차원 데이터 세트 표시 가능

*  일종의 경쟁신경망 (competitive network) 인 승자독식 과정은 입력벡터에 가장 가까운 가중치 벡터를 가지는 노드를 승자 (winner) 로 선언하고, 그 값이 입력벡터에 더 가까워지도록 가중치가 조정된다. 

* 각 노드는 이웃의 집합을 가지므로 노드가 경쟁에서 이길 때 이웃의 가중치도 함께 변화되지만 이웃이 승자에서 멀어질수록 그 가중치는 더 작게 변화된다. 

* 이러한 과정이 각 입력벡터에 대해 반복되어 많은 사이클을 수행한다.  


自己組織化指導（SOM)

* 非指導学習を利用する人工神経網中の一つ

* 2次元空間に高次元のデータを表紙可能

* 一種の競争神経網(competitive network)であるwinner-take-allは入力ベクトルに最も近い加重値ベクトルを持つノードを勝者(winner)と宣言し、その値が入力ベクトルにより近づくよう加重値が調整される。

* 各ノードは隣人の集合を持つため、ノードが競争で勝つ時、隣人の加重値も共に変化するが、隣人がwinnerから遠ざかるほど、その加重値はさらに小さく変化する。

* このような過程が各入力ベクトルに対して繰り返され、多くのcycleを遂行する。



<img width="438" alt="스크린샷 2022-08-11 오후 8 19 18" src="https://user-images.githubusercontent.com/90700648/184122148-6a1b9bf1-8d78-4e29-a43f-6f9fb6c9ee39.png">



## Experimentation (1)
* Data collection

** Simple click game by using Processing


* 데이터 수집

** 프로세싱을 이용한 간단한 정확도 연습 게임 


* データ収集

** プロセシングを利用した簡単な正確度練習ゲーム

<img width="390" alt="스크린샷 2022-08-11 오후 8 20 21" src="https://user-images.githubusercontent.com/90700648/184122341-087a6645-e6c0-49fd-872d-bfd0d9f9a52f.png">

* Example of the game screen


<img width="495" alt="스크린샷 2022-08-11 오후 8 21 22" src="https://user-images.githubusercontent.com/90700648/184122505-3a2a1af4-5d76-47c9-b130-27a73cc197d6.png">


* Clustering

- Organize the saved dataset by user

- Three users play 200 game data (total of 2000 click count) by each user
 
- Use the program named "Living for SOM"

- SOM setting:

- 40 number of trainings, 0.6 learning rate, 0.1 neighbor width


* 군집화

- 유저별로 수집한 데이터를 정리

- 3명의 유저에게서 200번의 게임 플레이, 총 2000번의 반응 속도, 정확도 기록

- 'Living for SOM' 이라는 이름의 프로그램 사용

- 40번의 반복, 0.6 학습률, 0.1의 폭을 사용


* 群集化

- ユーザーごとに収集したデータを整理

- 3人のユーザーから各々200回のゲームプレイ、総合2000の反応速度、正確度記録

- ‘Living for SOM’という名前のプログラムを使用

- 40回の反復、0.6の学習率、0.1の幅を使う


* Clasficication

- Use multiclassification method to classificy the user with multiple class

- In this dataset, the accuracy and reaction time is set as a x data and user is y data

- Use one-hot-encoding for y data

- Input layer with 16 node use relu activation, hidden layer 8 node use relu activation, output layer 3 node with sigmoid


* 분류

- 데이터셋에 두개 이상의 클래스가 있으므로 다중 분류를 사용하여 유저 구분

- 데이터셋중 정확도와 반응속도를 x값으로 유저를 y값으로 설정

- 원 핫 인코딩으로 y 데이터셋 변환

- 인풋 레이어 16개의 노드로 relu 사용, 히든 레이어 8개의 노드로 relu, 아웃풋 레이어 3개의 노드 sigmoid 사용




## Result


<img width="629" alt="스크린샷 2022-08-11 오후 8 26 13" src="https://user-images.githubusercontent.com/90700648/184123306-32ad6edc-da92-4e43-8630-939cc4387a1d.png">


<img width="147" alt="스크린샷 2022-11-28 오후 3 48 39" src="https://user-images.githubusercontent.com/90700648/204411811-6c20b432-57b6-49ef-96cc-3043bfd0d6bd.png">


- Get 50% of accuracy from multiclassification

- 다중 분류를 통해 50%의 정확도를 흭득

- 複数分類を使用し、50％の正確度を得る


## Limitation and Future Work

- The SOM has advantage in classifying the user by clustering the dataset

-- Not enough to use as the authentication

-- Other technical method is required

-- decision of the boundary for cluster is essential


- One or two behavioral aspects are not enough to be biometric authentication

-- Need more behavioral aspects to consider



- SOM은 데이터의 집합을 클러스터링 하여 구분하는데 강점이 있다

-- 하지만 유저 인증을 가능하게 할 정도의 정확성을 보여주지 못함

-- 다른 기술이나 인풋이 필요할 것으로 보임

-- 클러스터의 바운더리를 어떻게 확정할 것인지에 관한 자세한 연구 필요


- 하나 혹은 두개의 행동적 측면은 생체 인식으로는 부족한면을 보인다

-- 다른 추가적 행동적 측면이 필요할 것으로 생각됨


- Trajectory how the mouse move
-- longterm game play -> is there change of performance?


- SOMはデータの集合をクラスタリングして区分することに強みがある

-- しかしユーザー認証へ使うほどの正確度を示していない

-- 他の技術やインプットが必要そうだ

-- クラスターの境界設定への詳しい研究必要


- 一つ二つの行動的な側面は生体認証に足りない面を見せる

-- 他の追加的なインプットが必要なものと思われる


## Further Study

- FPS game  


-- Mouse Movement + alpha


-- for FPS, map can be the variant for change keystroke dynamics. 


-- Another aspect can be used for combine with the mouse dynamics


## 후속 공부

- FPS 게임을 목표로


-- 마우스 이동 + 추가 인풋 활용


-- FPS 게임의 경우 맵의 차이가 키 인풋의 차이를 야기할 수 있다.


-- 다른 것들이 마우스 인풋과 결합되어 사용될 수 있습니다.


##詳細に検討します

- FPSゲームで実験


-- マウスの移動 + キーボードインプット


-- FPSゲームの場合、マップの違いがキーインプットの違いを引き起こす可能性があります


-- 別の側面をマウスのダイナミクスと組み合わせることもできます
