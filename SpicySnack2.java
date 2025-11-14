import java.util.Scanner;
public class Average{
public static void main (String [] args){
Scanner input= new Scanner (System.in);
System.out.print("Enter first score: ");
int firstScore= input.nextInt();
System.out.print("Enter second score: ");
int secondScore= input.nextInt();
System.out.print("Enter third score: ");
int thirdScore= input.nextInt();
if (firstScore<0 || firstScore>100){
System.out.println ("Input score from 0-100");
}if (0>secondScore || secondScore>100){
System.out.println ("Input score from 0-100");
}if (0>thirdScore || thirdScore>100){
System.out.println ("Input score from 0-100");
}int average = (firstScore + secondScore  + thirdScore)/3;
if (90 <= average && average <= 100){
System.out.print (average + " You got an A");
}if (80 <= average && average <= 90){
System.out.print (average + " You goat a B");
}if (70 <= average && average <= 80){
System.out.print (average + " You got a C");
}if (60 <= average && average <= 70){
System.out.print (average + " You got a D");
}if (0 <= average && average <= 60){
System.out.print (average + " You got an F");
}
 }
  }







