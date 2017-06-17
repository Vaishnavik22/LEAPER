var Blocks = require('./src/engine/blocks');
//var csv = require('ya-csv');
var http = require('http');
var url=require('url');
var fs=require('fs');
var prevcoor="";
var server=http.createServer(function (req, res){

    console.log('Request received');
    console.log(prevcoor);
    var url_parts = url.parse(req.url, true);
    var query = url_parts.query;
     var blockIDs=Object.keys(query);
    //console.log(query);             //query is a json object
   /* var arr=query['jsonData[]'];
    var date=Date.now();
    var timestamp=arr[0];             // string
    var blockData=arr[1];   */          //string

   /* //To retrieve the json data,first convert the string to JSON
    var jsonObj=JSON.parse(blockData);
    
    //Get all the block IDs   
    var blockIDs=Object.keys(jsonObj['_blocks']);
    //var val=jsonObj['_scripts'];
    
    //Calling blocks.js functions to retrieve all the properties of a block
    var blockObj = new Blocks();
    
    var dataArray;
    //console.log(blockIDs);
    for (var i = 0; i < blockIDs.length; i++) {
      //To retrieve,first create the block with that received data
      blockObj.createBlock(jsonObj['_blocks'][blockIDs[i]]);
      
      //use all the functions defined in blocks.js
      var id=blockObj.getBlock(blockIDs[i])['id'];
      var opcode=blockObj.getBlock(blockIDs[i])['opcode'];
      var inputs=blockObj.getBlock(blockIDs[i])['inputs'];
      var fields=blockObj.getBlock(blockIDs[i])['fields'];
      var next=blockObj.getBlock(blockIDs[i])['next'];
      var toplevel=blockObj.getBlock(blockIDs[i])['toplevel'];
      var parent=blockObj.getBlock(blockIDs[i])['parent'];
      var shadow=blockObj.getBlock(blockIDs[i])['shadow'];
      var X=blockObj.getBlock(blockIDs[i])['x'];
      var Y=blockObj.getBlock(blockIDs[i])['y'];


      // TODO : retrieve all these params and write it into a csv file
      var onlyData=id+" "+opcode+" "+JSON.stringify(inputs)+" "+JSON.stringify(fields)+" "+next+" "+toplevel+" "+parent+" "+shadow;
      var coordinates=X+" "+Y;
      
      
        dataArray=date+" "+onlyData;

        fs.appendFileSync('./InteractionData.csv',dataArray+"\n");

    

    fs.appendFile('./input.txt',JSON.stringify(query)+"\n",function(err) {
    if (err)
    {
      return console.error(err);
    }
  });
}*/
for(i=0;i<blockIDs.length;i++)
{
fs.appendFile('./input.txt',String(query[blockIDs[i]]) +"\n",function(err){
 if (err)
    {
      return console.error(err);
    }
  });
}
}).listen({port:8083, host:'localhost', agent:false},server);
console.log('Server running at http://localhost');