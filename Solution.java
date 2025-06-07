// User function Template for Java
class Solution {
    static int temp2 = 0;
    static int temp1 = 1;
    static void gfSeries(int N) {
        // code here
        if(N == 1){
            System.out.print("0 ");
            return;
        }else if(N == 2){
            gfSeries(N-1);
            System.out.print("1 ");
            return;
        }
        gfSeries(N-1);
        int temp = temp2 * temp2 - temp1;
        temp2 = temp1;
        temp1 = temp;
        System.out.print(temp+ " ");
        return;
    }
    public static void main(String[] args){
        gfSeries(6);
    }
}