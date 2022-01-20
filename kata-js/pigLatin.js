// Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
// https://www.codewars.com/kata/520b9d2ad5c005041100000f

function pigIt(str) {
    let words = str.split(" ")
    let letters = words.map(word => word.split(""))
    
    for (let i = 0; i < words.length; i++) {
        if (letters[i][0].toUpperCase() != letters[i][0].toLowerCase()) {
            letters[i].push(letters[i][0])
            letters[i].push('ay')
            letters[i].shift()
        }

    }

    let modifiedWords = letters.map(word => word.join(""))
    let modifiedStr = modifiedWords.join(" ")

    return modifiedStr
}

console.log(pigIt('Pig latin is cool !'))

// Testing library
// let modified = words.map(word => word+'ay')
// console.log("!".toUpperCase() != "!".toLowerCase())