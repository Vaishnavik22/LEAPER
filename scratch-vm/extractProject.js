var fs=require('fs');
var http = require('http');
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

http.createServer( function (request, response) {  
	var id = '146242971';
	var url = 'https://projects.scratch.mit.edu/internalapi/project/' +
	        id + '/get/';
	    var r = new XMLHttpRequest();
	    var responseText="";
	    r.onreadystatechange = function() {
	        if (this.readyState === 4) {
	            if (r.status === 200) {
	            	console.log("Response recieved1");
	            	console.log(this.responseText);
	                fs.appendFile("./project.txt",this.responseText,function(err){
	                if (err)
	                {
	                    return console.error(err);
	                    console.log("error");
	                }});
	                console.log("finished writing");
	            }
	        }
	    };
	    r.open('GET', url);
	    r.send();
	}).listen(8088);

console.log("server running");