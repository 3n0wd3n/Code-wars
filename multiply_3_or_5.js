function solution(number){
  var finalSum = 0
  for (var i = 0; i < number; i++){
    if (i % 3 == 0 || i % 5 == 0){
      finalSum += i;
    }
  }
  return finalSum
}
