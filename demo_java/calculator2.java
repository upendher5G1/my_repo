import java.util.Scanner;
public class calculator2 {
    public static void main(String[]args){
        System.out.println("....CALCULATOR....");
        Scanner sc=new Scanner(System.in);
        System.out.print("enter a value:");
        int a=sc.nextInt();
        System.out.print("enter b value:");
        int b=sc.nextInt();
        System.out.print("enter your choice:");
        char choice=sc.next().charAt(0);
        switch (choice) {
            case '+':
                 System.out.println("Result:"+(a+b));
                break;
            case '-':
                 System.out.println("Result:"+(a-b));
                break;
            case '*':
                 System.out.println("Result:"+(a*b));
                break;
            case '/':
                if (b != 0)
                        System.out.println("Result: " + (a / b));
                    else
                        System.out.println("Error:Cannot Divide By Zero");
                break;
            default:
                System.out.println("invalid choice");
                break;
        }
    }
}
