//Hi, I wrote this code with Js

alert('Hi,to get the roots of a quadratic equation in the form ax^2 + bx + c please enter the coefficients.')

let a = Number(prompt('a : '))  //Prompt user for coefficient 'a' 
let b = Number(prompt('b : '))  //Prompt user for coefficient 'b' 
let c = Number(prompt('c : '))  //Prompt user for coefficient 'c'

let delta = Math.pow(b,2) - 4*a*c   //calculating delta

if (delta > 0) {    //if we have too real roots
    x1 = (-1*b + Math.sqrt(delta))/ (2*a)
    x2 = (-1*b - Math.sqrt(delta))/ (2*a)
    console.log('there are two real roots=>\n\n' + 'x1 : ' + x1 + '\n' + 'x2 : ' + x2)

} else if (delta ==0) {    //if we have one real root and delta is 0
   x = (-1*b / (2*a))
    console.log('there is just 1 real root=>\n\n' + 'x : ' + x)

} else {              //if delta < 0 we have two complex roots
    real_x = (-1*b / (2*a))
    imaginary_x = (Math.sqrt(-1*delta)) / (2*a)
    console.log('we have two complex roots=>\n\n' + 'x1 : ' + real_x + '+' + `${imaginary_x}j` + '\n' + 'x2 : ' + real_x + '+' + `${-1*imaginary_x}j`)
}


alert('Hi, to get the roots of a quadratic equation in the form ax^2 + bx + c, please enter the coefficients.');

