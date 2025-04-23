// when we click on "Ask Chellam Sir" that time this function will run.

function sendData(){

const name = document.getElementById("searchbar").value;

        fetch('/api/journal/run-command',{

            method:'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({ name: name })
        })
            .then(response => response.text())
            .then(data => alert(data));









}


