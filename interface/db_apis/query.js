const database = require('../services/database.js');
 
const baseQuery = 
 ``;
   
async function find(context) {
  let query = baseQuery;
  const binds = {};
 
  if (context.q) {
    binds.q = context.q;

    query += `:q`;
  }
	console.log(`\n query=${query} \n`);  
  const result = await database.simpleExecute(query, binds);
 
  return result.rows;
}
 
module.exports.find = find;
