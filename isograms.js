/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
*/

function isIsogram(str){
  for (var i = 0; i < str.length; i++){
    var counter = 0;
    for (var j = 0; j < str.length; j++){
      if (str[i] == str[j] || str[i].toUpperCase() == str[j] || str[i].toLowerCase() == str[j]){
        counter += 1;
        if (counter == 2){
          return false;
        }
      }
    }
  }
  return true
}
