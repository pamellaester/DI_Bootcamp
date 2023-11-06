document.getElementById("libform").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const noun = document.getElementById("noun").value;
    const adjective = document.getElementById("adjective").value;
    const person = document.getElementById("person").value;
    const verb = document.getElementById("verb").value;
    const place = document.getElementById("place").value;
    
    if (noun !== "" && adjective !== "" && person !== "" && verb !== "" && place !== "") {
        const story = `Once upon a time in a ${adjective} land, there lived a ${noun} named ${person}. ${person} loved to ${verb} in the beautiful ${place}.`;
        document.getElementById("story").textContent = story;
    } else {
        console.log("Please fill in all the fields.");
    }
});