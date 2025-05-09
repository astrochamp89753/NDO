const http = require('http');
const fs = require('fs');
const path = require('path');

const port = 8000;

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        const filePath = path.join(__dirname, 'intro.html');
        fs.readFile(filePath, (err, data) => {
            if(err) {
                res.writeHead(500);
                res.end('Napaka pri branju datoteke!');
                return;
            }

            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end(data);
        });
    } else {
        res.writeHead(404);
        res.end('Stran ni bila najdena!');
    }
});

server.listen(port, () => {
    console.log('Spletna stran dosegljiva na http://localhost:${port}');
});