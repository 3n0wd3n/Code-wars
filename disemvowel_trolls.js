function disemvowel(troll_str) {
  var new_str = "";
  var vowels = "aeiou"
  for (var i = 0; i < troll_str.length; i++){
    if (!vowels.includes(troll_str[i].toLowerCase())){
      new_str += troll_str[i];
    }
  }
  return new_str;
}
