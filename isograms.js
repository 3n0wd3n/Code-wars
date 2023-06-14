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
