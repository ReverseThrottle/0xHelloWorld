GNU nano 4.8                                                                 Project_4.2.js                                                                  Modified  
/*
##############################################
#    Zachary Hopping                         #
#     Project 4.1                            #
# Take 2 numbers and return their sum        #
# if both nums are the same triple their sum #
##############################################
*/

//This function allows me to take user input from the console
//I was struggling to get this to work and was doing research and found this on Stackoverflow 
function readline()
{
        var ist = new java.io.InputStreamReader(java.lang.System.in);
        var bre = new java.io.BufferedReader(ist);
        var line = bre.readLine();
        return line;
}

//Takes user input and stores in num1
print("Please enter a number: ");
var num1=readline();
//Takes user input and stores in num2
print("Please enter another number: ");
var num2=readline();
//Value of num1 and num2 combined 
var num3 = Number(num1) + Number(num2);

//IF statement that checks num to to if it is the same value 
if (num1 == num2)
{ 
        //If num is the same we triple the value of the sum
        print("The sum of " +  num1 + " and " + num2 + " is: ");
        print(num3);
        print("The sum of your numbers tripled is: ");
        print(Number(num3) * 3);
}
else
{
        //If num is not the same we just add them
        print("The sum of " +  num1 + " and " + num2 + " is: ");
        print(num3);
}
