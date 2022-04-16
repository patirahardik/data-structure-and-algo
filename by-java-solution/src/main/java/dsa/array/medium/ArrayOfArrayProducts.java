package dsa.array.medium;

import java.util.Arrays;

/**
 * @author gautamarj - ssdbad
 * Given an array of integers arr, you’re asked to calculate for each index i
 * the product of all integers except the integer at that index (i.e. except arr[i]).
 * Implement a function arrayOfArrayProducts that takes an array of integers and
 * returns an array of the products.
 *
 * NOTE : Solve without using division and analyze your solution’s time and space complexities.
 */
public class ArrayOfArrayProducts {
    public static void main(String[] args) {
        int array[] = {2,7,3,4};
        array = findArrayOfArrayProducts(array);
        // Final TC : O(n), SC : O(n)
        System.out.println(Arrays.toString(array));
    }

    private static int[] findArrayOfArrayProducts(int[] array) {
        /**
         * Finding left product array with left-most index value 1
         */
        int leftArray[] = new int[array.length];
        int product = 1;
        for (int leftArrayIndex = 0 ; leftArrayIndex < array.length ; leftArrayIndex++) {
            leftArray[leftArrayIndex] = product;
            product *= array[leftArrayIndex];
        }
        System.out.println(Arrays.toString(leftArray));

        /**
         * Finding right product array with right-most index value 1
         */
        int rightArray[] = new int[array.length];
        product = 1;
        for (int rightArrayIndex = array.length - 1 ; rightArrayIndex >= 0 ; rightArrayIndex--) {
            rightArray[rightArrayIndex] = product;
            product *= array[rightArrayIndex];
        }
        System.out.println(Arrays.toString(rightArray));

        /**
         * At the time of output, we can use both array for multiplication
         */
        int outputArray[] = new int[array.length];
        for (int index = 0 ; index < array.length ; index++) {
            outputArray[index] = leftArray[index] * rightArray[index];
        }

        return outputArray;
    }
}

/*
Input       :     Output        :   Hint
{8,10,2}    :     {20,16,80}    :   # by calculating = [10*2, 8*2, 8*10]
{2,7,3,4}   :     {84,24,56,42} :   # by calculating = [7*3*4, 2*3*4, 2*7*4, 2*7*3]
*/