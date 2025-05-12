
 function sendData() {
            const userInput = document.getElementById('userInput').value;
            const tools = document.getElementById("devops-tools").value
            fetch('http://localhost:5000/run-python', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input: userInput,
                                       devtools:tools
                                     })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Response from Python:", data);
                alert("Python Output: " + data.result);
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }

function sendData1(){

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


