/*
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
*/

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
