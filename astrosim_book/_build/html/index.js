const express = require('express');
const app = express();
const path = require('path');

PORT = 8000;

app.use(express.static(__dirname))
app.get('/', (req, res) => {
    const filePath = path.resolve(__dirname, 'index.html')
    res.sendFile(filePath)
})

app.listen(PORT, () => {
    console.log(`Strežnik zagnan na ${PORT}`)
})