/*
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
*/

function solution(str, ending){
  var reversedString = str.split("").reverse();
  var reversedEnding = ending.split("").reverse();
  var counter = 0;
  for (var i = 0; i < reversedEnding.length; i++){
    if (reversedString[i] == reversedEnding[i]){
        counter = counter + 1;
    }
  }
  return counter == reversedEnding.length
}
