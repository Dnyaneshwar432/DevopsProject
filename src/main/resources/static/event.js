
 function sendData() {
            console.log("Sending data to Python...");
            const userInput = document.getElementById('in1').value;
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
                document.getElementById("d1").innerText = data.result;

               // alert("Python Output: " + data.result);
            })
            .catch(error => {
                console.error("Error:", error);
            });


        }




