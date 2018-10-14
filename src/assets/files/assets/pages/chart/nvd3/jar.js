
function thisconnect(){
   var mysql =  require('mysql')
    var con =  mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'tweets'
    })
    con.connect();
    con.query('select * from corpus', function(err, results){
        
        console.log(results);
    });
    con.end();
}
thisconnect();
