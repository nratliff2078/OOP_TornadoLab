"use strict";

console.log(document.location.pathname);


function submit(){
    let fname = document.getElementById("name").value;
    //console.log("Name:",fname);
    let J = {
        name: fname 
    };
    fetch( document.location.pathname,
        {   method: "POST",
            body: JSON.stringify(J)
        }
    ).then( (resp) => {
        //can also use text(), blob(), or arrayBuffer()
        resp.json().then( (J) => {
            console.log("Server said:",J);
        });
    }).catch( (err) => {
        console.log("Uh oh",err);
    })

}






