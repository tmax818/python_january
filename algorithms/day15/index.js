/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    if(num < 1){
        return 0;
    }
    return num + recursiveSigma(num - 1)
}

console.log(recursiveSigma(num1))
console.log(recursiveSigma(num2))
console.log(recursiveSigma(num3))

/*
5 + recursiveSig(4)
    4 + recursiveSig(3)
        3 + recursiveSig(2)
            2 + recursiveSig(1)
                1 + recursiveSig(0)
                    0 is returned - base case reached, can start summing now
                    - call stack "unwinds" now with .pop LIFO (matching indentation)
                1 + 0 = 1 <- this sum becomes the right side of the next addition
            2 + 1 = 3
        3 + 3 = 6
    4 + 6 = 10
5 + 10 = 15
*/