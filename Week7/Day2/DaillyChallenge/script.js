document.querySelector("Form").addEventListener("submit", handleSubmit);

function handleSubmit(e) {
    e.preventDefault()
    const formData = new FormData(document.querySelector("form"));
    const entries = formData.entries();
    const data = Object.fromEntries(entries);
    const json = JSON.stringify(data);
    const display = document.querySelector("p");
    display.innerText = json;
    document.body.appendChild(display);
}