//
//
//
int[] time = new int[10];
int n = 0;
float k = 0.0;
float b= 0.0;
float[] x1 = new float[10];
float[] y1 = new float[10];
float[] x2 = new float[10];
float[] y2 = new float[10];
float[] dis = new float[10]; 
import java.io.File; 
import java.io.IOException;
import java.util.List;
import java.io.BufferedWriter;
import java.io.FileWriter;

void settings(){                
  size (750,750);              //Set the size of the Applet
}

void draw(){
 background(255);                             
 GameStart();
}

public void GameStart(){ 
   textSize(25);
   fill(0);
   text("Press space bar", width/2 - 110, height/2);
   if(key == ' ') {
     background(255);
     Makecircle();
     GameScore();
     noLoop(); 
    }
   }


public void mousePressed() { 
  if(n < 10){
    measureTime();
    x2[n] = mouseX;
    y2[n] = mouseY;
    n++;
    Makecircle();
  }
  else{
    showResult();
    }
  }


public void measureTime(){
  int m = millis();
  if(n < time.length){
      time[n] = m;
   }
}

public void Makecircle(){
  loop();
  fill(0,161,241);
  if(n < 10){
    float r = random(25, 725);
    float a = random(25, 725);
    circle(r,a,50);
    fill(255,1,35);
    circle(r,a,33);
    fill(255,222,0);
    circle(r,a,12);
    fill(0,0,0);
    circle(r,a,1);
    x1[n] = r;
    y1[n] = a;
  }
  
}

public void showResult(){
  for(int l = 0; l < 10; l++){
    dis[l] = sqrt(sq(x1[l] - x2[l]) + sq(y1[l] - y2[l]));
    println("The accuracy of " + l + "th is " + dis[l]);
  }
  
  ShowScore();
  
}
public void ShowScore(){
  fill(0,0,0);
  textSize(15);
  text("Data Saved", 180, 230);
  SaveData();
}

public void GameScore(){
  fill(0,0,0);
  textSize(12);
  if(n < 10){
    text(n+1 + "/10", 10, 15);
  }
}


public void SaveData(){
  try{
  BufferedWriter writer = new BufferedWriter(new FileWriter(sketchPath("User1.txt"), true));
  for(int i =0; i < 10; i++){
    String q = str(dis[i]);
    String a = str(time[i]);
    writer.write(q + ", " + a);  
    writer.newLine();

  }
  writer.flush();
  writer.close();
  println("Saved Data Successfully...");
  }catch (IOException e) {
          println("Error");
          e.printStackTrace();
        }
  noLoop();
}
