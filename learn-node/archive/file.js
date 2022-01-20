const fs = require('fs');

//create a file
// fs.writeFile('example.txt', "this is an example", (err)=>{
//     if(err)
//         console.log(err);
//     else
//         console.log('File sucessfully created')
//         fs.readFile('example.txt', 'utf8', (err, file)=>{
//             if(err)
//                 console.log(err);
//             else
//                 console.log(file);
//         })
// })

//rename a file
// fs.rename('example.txt', 'example2.txt', (err)=>{
//     if(err)
//         console.log(err);
//     else
//         console.log('successfully renamed the file')
// })

//append file
// fs.appendFile('example2.txt', '\nSome data being appended', (err)=>{
//     if(err)
//         console.log(err);
//     else
//         console.log('Appended')
// })

//delete file
fs.unlink('example2.txt', (err)=>{
    if(err)
        console.log(err);
    else
        console.log('deleted')
})