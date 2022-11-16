< !DOCTYPE html >
    <
    html >
    <
    head >
    <
    title > Take Picture using webcam.js < /title> <
    /head> <
    style > #camera {
        width: 350 px;
        height: 350 px;
        border: 1 px solid black;
    } <
    /style> <
    body >
    <
    div id = "camera" > < /div> <
    button onclick = "take_snapshot()" > Take Picture < /button> <
    div id = "results" > < /div> <
    /body> <
    script src = "https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.26/webcam.min.js" > < /script> <
    script >

    Webcam.set({
        width: 350,
        height: 350,
        image_format: 'jpeg',
        jpeg_quality: 90
    })
Webcam.attach("#camera")

function take_snapshot() {

    Webcam.snap(function(data_uri) {
        document.getElementById('results').innerHTML =
            '<img id="imageprev" src="' + data_uri + '"/>';
    });

} <
/script> <
/html>