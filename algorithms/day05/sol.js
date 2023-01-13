/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {
  const freq_table = {}
  for(let i = 0; i < arr.length; i++){
    if(!freq_table[arr[i]]){
      freq_table[arr[i]] = 1
    } else {
      freq_table[arr[i]]++
    }
  }
  return freq_table
}

console.log(makeFrequencyTable(arr1))
console.log(makeFrequencyTable(arr2))
console.log(makeFrequencyTable(arr3))

module.exports = {makeFrequencyTable}