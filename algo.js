/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) { }

/*****************************************************************************/

function zipArraysIntoMap(keys, values) {
    let result = {};
    for (let i = 0; i < keys.length; i++) {
        result[keys[i]] = values[i];
    }
    return result;
}
// 1 let result = {}: This line declares a new empty object named result.This object will be used to store the key - value pairs.
// 2 for (let i = 0; i < keys.length; i++): This line starts a for loop that will iterate n times, where n is the length of the keys array.i is the loop index variable that starts from 0 and increments by 1 in each iteration.
// 3 result[keys[i]] = values[i]: This line adds a new key - value pair to the result object.The key is taken from the keys array at the index i and the value is taken from the values array at the same index i.
// 4 return result: This line returns the result object that now contains all the key - value pairs from the keys and values arrays.
// So, in each iteration of the loop, the function takes a key from the keys array and a value from the values array and adds them as a new key - value pair to the result object.When the loop finishes, the result object will contain all the key - value pairs from the two arrays.