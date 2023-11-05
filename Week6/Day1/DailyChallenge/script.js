const planets = [
    { name: "Mercury",color: "red" },
    { name: "Venus",color: "orange" },
    { name: "Earth", color: "yellow" },
    { name: "Mars", color: "green"},
    { name: "Jupiter", color: "blue"},
    { name: "Saturn", color: "purple"},
    { name: "Uranus", color: "pink"},
    { name: "Neptune",color: "black"},
    { name: "Pluto",color: "grey" }
];

function createPlanet(planet) {
    const universeSection = document.getElementById("universe");
    const newPlanet = document.createElement("div");
    newPlanet.classList.add("planet");
    newPlanet.textContent = planet.name;
    newPlanet.style.backgroundColor = planet.color; 
    universeSection.appendChild(newPlanet);
}

planets.forEach((planet) => {
    createPlanet(planet);
});


