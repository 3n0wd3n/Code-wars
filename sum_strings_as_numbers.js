// function sumStrings(a,b) { 
//   if (a.length > 0 & b.length > 0){
//     let num = parseInt(a) + parseInt(b)
//     return num.toString()
//   } if (a.length == 0 && b.length > 0){
//     return parseInt(b).toString()
//   } if (b.length == 0 && a.length > 0){
//     return parseInt(a).toString()
//   }
  
// }

function sumStrings(a,b) { 
  if (a.length > 0 & b.length > 0){
    let num = BigInt(a) + BigInt(b)
    return num.toString()
  } if (a.length == 0 && b.length > 0){
    return BigInt(b).toString()
  } if (b.length == 0 && a.length > 0){
    return BigInt(a).toString()
  }
}