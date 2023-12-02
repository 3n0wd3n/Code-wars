/*
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
*/

function getCount(str) {
  let counter = 0;
  let vowel = "aeiou";
  [...str].forEach((letter) => {
    if (vowel.includes(letter)){
      counter += 1;
    }
  })
  return counter;
}
