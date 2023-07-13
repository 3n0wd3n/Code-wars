/*
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
*/

function isPangram(pangramString){
  
  let alphabet = "abcdefghijklmnopqtuvwxyz";
  let counter = 0;
  
  // to lower case
  pangramString = pangramString.toLowerCase()
  
  // remove spaces
  const stringWithoutSpaces = pangramString.replace(/\s/g, "");
    
  // remove duplicates
  const uniqueString = [...new Set(stringWithoutSpaces)].join("");
  
  for (let i = 0; uniqueString.length > i; i++){
    if (alphabet.includes(uniqueString[i])){
      counter += 1;
    }
  }
  if (alphabet.length == counter){
    return true
  }
  return false
}
