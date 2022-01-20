const fs = require('fs');
// fs.mkdir('tutorial', (err)=>{
//     if(err)
//         console.log(err);
//     else{
//         fs.writeFile('./tutorial/example.txt', 'test', (err)=>{
//             if(err)
//                 console.log(err);
//             else{
//                 console.log('created folder and file')
//             }
//         })
//     }
// })

fs.readdir('tutorial', (err, files)=>{
    if(err)
        console.log(err);
    else{
        console.log(files)
    }
})