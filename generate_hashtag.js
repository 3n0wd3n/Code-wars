function generateHashtag(strnxs){
  if (!strnxs.trim().length || strnxs.length == 0){
    return false
  }
  var newStr = "#";
  var strnxs = strnxs.split(" ")
  for (var i = 0; i < strnxs.length; i++){
    newStr += strnxs[i].toLowerCase().charAt(0).toUpperCase() + strnxs[i].slice(1);
  }
  if (newStr.length > 140){
    return false
  }
  return newStr
  }
