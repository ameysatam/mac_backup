public class LeapYear {
    public static boolean isLeapYear(int year){
        boolean validYear = (year >= 1 && year <= 9999);

        if (validYear){
            if (year%4 ==0){
                if (year%100 ==0){
                    return year % 400 == 0;
                } else{
                    return true;
                }
            } else{
                return false;
            }
        } else{
            return false;
        }
    }

}
