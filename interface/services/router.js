const express = require('express');
const router = new express.Router();
const hosts = require('../controllers/hosts.js');
const query = require('../controllers/query.js');

  
router.route('/hosts/:id?')
  .get(hosts.get);
 
 router.route('/query/:q?')
  .get(query.get);

  
module.exports = router;
