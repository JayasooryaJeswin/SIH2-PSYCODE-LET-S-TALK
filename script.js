document.getElementById("start-btn").addEventListener("click", function () {
    fetch('/speech', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        const textOutput = document.getElementById("text-output");
        const instruction = document.getElementById("instruction");

        if (data.error) {
            instruction.textContent = data.error;
            instruction.style.color = "red";
            textOutput.textContent = "";
        } else {
            textOutput.textContent = data.text;
            instruction.textContent = "Displaying the sign language video.";
            instruction.style.color = "#555";

            // Set video source and play the video
            const videoSource = document.getElementById("video-source");
            videoSource.src = data.video;
            document.getElementById("sign-video").load();
        }
    });
});
