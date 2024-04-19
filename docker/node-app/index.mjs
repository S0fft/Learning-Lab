import fs from 'fs'


fs.appendFile('my-file.txt', 'The file have been created', (err) => {
    if (err) throw err
    console.log('The file unsaved!')
})

setTimeout(() => console.log('Finish'), 30000)