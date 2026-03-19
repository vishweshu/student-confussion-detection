function updateStats() {

    fetch("/stats")
        .then(response => response.json())
        .then(data => {

            document.getElementById("confused").innerText = data.confused;
            document.getElementById("attentive").innerText = data.attentive;
            document.getElementById("percent").innerText = data.confusion;

        })
        .catch(error => console.log(error));

}

setInterval(updateStats, 2000);