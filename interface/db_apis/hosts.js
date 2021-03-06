const database = require('../services/database.js');
 
const baseQuery = 
 `select *
  from Hosts`;
 
async function find(context) {
  let query = baseQuery;
  const binds = {};
 
  if (context.id) {
    binds.hid = context.id;
 
    query += `\nwhere hid = :hid`;
  }
  	console.log(`\n query=${query} \n`);  

   if (context.skip) {
    binds.row_offset = context.skip;
 
    query += '\noffset :row_offset rows';
  }
 
  const limit = (context.limit > 0) ? context.limit : 30;
 
  binds.row_limit = limit;
 
  query += '\nfetch next :row_limit rows only';
 
  const result = await database.simpleExecute(query, binds);
 
  return result.rows;
}
 
module.exports.find = find;
