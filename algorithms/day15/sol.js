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
  // get rid of decimals
  const int = parseInt(num);
  // base case
  if (int < 1) {
    return 0;
  }
  return int + recursiveSigma(int - 1);
}

var first = recursiveSigma(num1)
var second = recursiveSigma(num2)
var third = recursiveSigma(num3)
