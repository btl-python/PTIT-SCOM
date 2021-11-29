window.SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.interimResults = true;
recognition.continuous = true;
recognition.lang = 'vi-VN';
var inputsearch = $('#search-focus')
recognition.addEventListener("result", (e) => {
    const text = Array.from(e.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join("");
    inputsearch.val(text)
});
var t = document.getElementById("microbutton");

function micro() {
    if (t.value == "YES") {
        recognition.stop();
        t.value = "NO";
        $('#search-focus').prop('disabled', false);
        $('#submitbutton').prop('disabled', false);
        document.getElementById('microbutton').setAttribute("style", "color:black;border: 5px solid #e3342f;width: 50px; height: 50px;border-radius: 100%;margin-right: 10px;");
    } else if (t.value == "NO") {
        t.value = "YES";
        recognition.start();
        $('#search-focus').prop('disabled', true);
        $('#submitbutton').prop('disabled', true);

        document.getElementById('microbutton').setAttribute("style", "color:red;border: 5px solid #e3342f;width: 50px; height: 50px;border-radius: 100%;margin-right: 10px;");
    }

}