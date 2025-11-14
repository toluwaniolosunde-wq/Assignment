//FUNCTION calculatedYears(fatherAge, sonAge)
//years= ageFather - (2* ageSon)
RETURN years

//MAIN
//INPUT fathers age
//INPUT sons age 
//years= calculatedYears(fathers age, son's age)
//IF years >= 0 THEN 
//PRINT "In" + years _+ "years, the father will be twica as old as his son."
//ELSE
//PRINT "In" + years + " years, the father was twice as old as his son."
//END IF
//END MAIN 

import java.util.Scanner;
public class TwoAges{
public static void main (String [] args){
Scanner input= new Scanner (System.in);
System.out.print("Enter fathers age: ");
int ageFather= input.nextInt();
System.out.print("Enter sons age: ");
int ageSon= input.nextInt();


if (0>ageFather && ageFather>80){
System.out.print ("Input age between 1 and 80");
}
int years= ageFather- (2* ageSon);
if (years>=0){
System.out.println("In " + years + " years ,the father will be twice as old as his son.");
}else{
System.out.println(Math.abs(years) + "years ago, the father was twice as old as his son.") ;
}
 }
   }