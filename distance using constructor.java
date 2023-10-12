import java.lang.Math;
import java.util.Scanner;
public class point{
  public double x1;
  public double y1;

  public static void main(String args[]){
    System.out.println("enter the value for fields x1,x2,y1,y2");
    Scanner x=new Scanner(System.in);
    double x1=x.nextDouble();
    double y1=x.nextDouble();
    double x2=x.nextDouble();
    double y2=x.nextDouble();
    point p1=new point(x1,y1);
    point p2=new point(x2,y2);
    dis(p1,p2);
    
  }
  public point(double x1,double y1){
    this.x1=x1;
    this.y1=y1;

  }
  
  
  public static void dis(point p1,point p2){
    double b=Math.sqrt(Math.pow((p2.x1-p1.x1),2)+Math.pow((p2.y1-p1.y1),2));
    System.out.println(b);



  } 

}