public class factorial{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
       int res =1;
        while(n>0){
            res =res*n;
            n--; 
        }
        System.out.println(res);
    }
}