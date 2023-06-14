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
