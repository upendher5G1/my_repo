import java.util.Scanner;
public class calculator{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        System.out.println("....Simple Calculator....");
        System.out.print("enter a value:");
        int a=sc.nextInt();
        System.out.print("enter b value:");
        int b=sc.nextInt();
        System.out.print("enter your choice:");
        char choice=sc.next().charAt(0);
        if(choice=='+'){
            System.out.println("Result:"+(a+b));
        }
        else if(choice=='-'){
            System.out.println("Result:"+(a-b));
        }
        else if(choice=='*'){
            System.out.println("Result:"+(a*b));
        }
        else if(choice=='/'){
            if (b != 0){
                System.out.println("Result:"+(a/b));
            }
            else {
                System.out.println("Error: Division by zero");
            }
        }
        else if(choice=='%'){
            System.out.println("Result:"+(a%b));
        }
        else{
            System.out.println("invalid choice");
        }
        }
    }