 const query = require('../db_apis/query.js');
 
async function get(req, res, next) {
  try {
    const context = {};
    context.q = req.params.q;

    const rows = await query.find(context);
 
    if (req.params.id) {
      if (rows.length === 1) {
        res.status(200).json(rows[0]);
      } else {
        res.status(404).end();
      }
    } else {
      res.status(200).json(rows);
    }
  } catch (err) {
    next(err);
  }
}
 
module.exports.get = get;

