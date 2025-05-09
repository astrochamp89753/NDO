const readFile = require('fs');
const express = require('express')

const app = express();
const port = 8000;

app.use(express.static(__dirname));

app.get('/', (req, res) => {
    readFile('./intro.html', 'utf-8', (err, html) => {
        if (err) {
            res.status(500).send('Stran trenutno ne deluje!')
        }

        res.send(html);
    })
});

app.listen(process.env.PORT || port, () => {
    console.log('Spletna stran dosegljiva na http://localhost:'+port+'!');
});