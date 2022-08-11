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
  size (500,500);              //Set the size of the Applet
}

void draw(){
 background(255);                             
 GameStart();
}

public void GameStart(){ 
   textSize(25);
   fill(0);
   text("Press", width/2 - 110, height/2);
    char c = ' '; 
    fill(255,0,0);
    textSize(40);
    text("space bar", width/2 - 30 , height/2);
    if(key == c) {
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
    //println(n + "th" + x2[n] + "," + y2[n]);
    n++;
    Makecircle();
  }
  }


public void measureTime(){
  int m = millis();
  if(n < time.length){
      time[n] = m;
      println(time[n]);
   }
}

public void Makecircle(){
  loop();
  fill(0,161,241);
  if(n < 10){
    float r = random(25, 475);
    float a = random(25, 475);
    circle(r,a,50);
    fill(255,1,35);
    circle(r,a,33);
    fill(255,222,0);
    circle(r,a,12);
    fill(0,0,0);
    circle(r,a,1);
    x1[n] = r;
    y1[n] = a;
    //println (n + "th" + x1[n] + ","+ y1[n]);
  }
  if(n == 10){
    showResult();
  }
}

public void showResult(){
  for(int i = 0; i < dis.length; i++){
    k += time[i];
  }
  k = k / 10;

  for(int l = 0; l < dis.length; l++){
    dis[l] = sqrt(sq(x1[l] - x2[l]) + sq(y1[l] - y2[l]));
    println("The accuracy of " + l + "th is " + dis[l]);
    //println(l + "th " + x1[l] + "  "  + y1[l]);
    //println(l + "th " + x2[l] + "  "  + y2[l]);
  }
  for(int i = 0; i< dis.length; i++){
    b += dis[i];
  }
  b = b / dis.length;
  ShowScore();
  
}
public void ShowScore(){
  fill(0,0,0);
  textSize(15);
  text("Average score: " + k, 180, 230);
  text("Average accuracy: " + b,180, 250);
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
  BufferedWriter writer = new BufferedWriter(new FileWriter( sketchPath("User1.txt"), true));
  for(int i =0; i < dis.length; i++){
    String q = str(dis[i]);
    writer.write(q);
    writer.write(" ,");
  }
  String sb = str(b);
  writer.write(sb);
  writer.write(" ,");
  for(int j =0; j < dis.length; j++){
    String a = str(time[j]);
    writer.write(a);
    writer.write(" ,");
  } 
  String sk = str(k);
  writer.write(sk);
  writer.newLine();
  writer.flush();
  writer.close();
  println("Saved Data Successfully...");
  }catch (IOException e) {
          println("Error");
          e.printStackTrace();
        }
  noLoop();
}
