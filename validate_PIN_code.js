/*
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
*/
function validatePIN (pin) {
  let validNumbers = "01234567890";
  //   pin.forEach()
  let counter = 0;

  for (let i = 0; i < pin.length; i++){
    if (validNumbers.includes(pin[i])){
      counter += 1;
    }

  }
  if ((counter === 4 || counter === 6) && counter === pin.length){
    return true
  }else{
    return false
  }
  
}
