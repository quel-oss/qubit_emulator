"use strict";

var myInit = { method: 'GET', headers: {'Conten-Type': 'application/json'}, mode: 'cors', cache:'default'};
let myRequest = new Request("./data.json");

fetch(myRequest)
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        document.getElementById('text2').innerHTML = data.clients;
    });

