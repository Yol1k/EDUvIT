// function manyChecks() {
//   let a = Math.floor(Math.random() * 20) + 1;
//   console.log(`a = ${a}`);
  
//   return (
//     a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' + (a === 5 ? 'an example of a special case' : '')) 
//     + (a === 15 ? 'but a is not 15' : '')+ (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ') 
//     + (a % 2 ? ' and a is odd' : ' and a is even ');
// }

// manyChecks();
// условие с условным (тернарным) оператором перевести в if...else И switch()
// результат выводить в консоль, с пощью console.log()

function manyChecks() {
  let a = Math.floor(Math.random() * 20) + 1;
  console.log(`a = ${a}
    `);

  let result = "";

  if (a > 10) {
    result += "a is bigger than 10 ";
  } else {
    result += "a is less than or equal to 10 ";
    if (a === 5) {
      result += "an example of a special case";
    }
  }

  if (a === 15) {
    result += "but a is not 15 ";
  }

  if (a > 5) {
    result += "and a is greater than 5 ";
  } else {
    result += "and a is less than or equal to 5 ";
  }

  if (a % 2) {
    result += "and a is odd";
  } else {
    result += "and a is even";
  }

  console.log(`if..else
Результат: ${result}
`);

    let resultSwitch = "";

    if (a > 10) {
        resultSwitch += "a is bigger than 10 ";
    } else {
        resultSwitch += "a is less than or equal to 10 ";
        switch (a) {
            case 5:
                resultSwitch += "an example of a special case";
                break;
            default:
                break;
        }
    }

    switch (a) {
        case 15:
            resultSwitch += "but a is not 15 ";
            break;
        default:
            break;
    }

    if (a > 5) {
        resultSwitch += "and a is greater than 5 ";
    } else {
        resultSwitch += "and a is less than or equal to 5 ";
    }


    switch (a % 2) {
        case 0:
            resultSwitch += "and a is even";
            break;
        default:
            resultSwitch += "and a is odd";
            break;
    }
    console.log(`Switch
Результат: ${resultSwitch}`);

}

manyChecks();