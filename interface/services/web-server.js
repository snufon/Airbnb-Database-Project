const http = require('http');
const express = require('express');
const webServerConfig = require('../config/web-server.js');
const morgan = require('morgan');
const database = require('./database.js');
const router = require('./router.js');
 
let httpServer;
 
function initialize() {
  return new Promise((resolve, reject) => {
    const app = express();
    httpServer = http.createServer(app);
   
     // Combines logging info from request and response
    app.use(morgan('combined'));
    
     // Mount the router at /api so all its routes start with /api
    app.use('/api', router);
 
    //app.get('/', (req, res) => {
     // res.end('Hello World!');
    //});
    
    /*
     app.get('/', async (req, res) => {
      const result = await database.simpleExecute('select user, systimestamp from dual');
      const user = result.rows[0].USER;
      const date = result.rows[0].SYSTIMESTAMP;
 
      res.end(`Hello Dream Team\n
      DB user: ${user}\n
      Date: ${date}`);
    });
    * 
    * */
    
   //  app.set('views',__dirname + '/views');
	app.set('view engine', 'ejs');
	app.engine('html', require('ejs').renderFile);

    app.get('/', async (req, res) => {
      res.render('index.html');
    });
 
    httpServer.listen(webServerConfig.port)
      .on('listening', () => {
        console.log(`Web server listening on localhost:${webServerConfig.port}`);
 
        resolve();
      })
      .on('error', err => {
        reject(err);
      });
  });
}
 
module.exports.initialize = initialize;



function close() {
  return new Promise((resolve, reject) => {
    httpServer.close((err) => {
      if (err) {
        reject(err);
        return;
      }
 
      resolve();
    });
  });
}
 
module.exports.close = close;
