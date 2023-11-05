
async function getRandomId(id) {
    const url = "https://www.swapi.tech/api/people/" + id;
    console.log("url:", url);
        try{    
            const data = await fetch(url).then((response) => response.json());
            const dataElement = data.result.properties; 
            const homeWorldName = await fetchHomeWorld(dataElement.homeworld);
            displayProperties(dataElement.name, dataElement.height, dataElement.gender, dataElement.birth_year, homeWorldName);
        } catch (error) {
            console.log(`We got the error ${error}`);
        };
}

async function  fetchHomeWorld(homeworld) {
    try {
        const res = await fetch (homeworld) ;
        const resJson = await res.json();
        const HomeWoldName = resJson.result.properties.name;
        return HomeWoldName;
    } catch (error) {
        console.log(error)
    }
}

async function displayProperties(name, height, gender, birth_year , homeworld ) {
    const nameId = document.getElementById("name");
    nameId.innerText = `${name}`;
    const heightId = document.getElementById("height");
    heightId.innerText = `Height : ${height}`;
    const genderId = document.getElementById("gender");
    genderId.innerText = `Gender : ${gender}`;
    const birthYearId = document.getElementById("birth_year");
    birthYearId.innerText = `Birth Year : ${birth_year}`;
    const homeWorldId = document.getElementById("homeworld");
    homeWorldId.innerText = `Home World : ${homeworld}`;
}

function handleClick (e) {
    const randomId = getRandomNumber();
    getRandomId(randomId);
}
    

function getRandomNumber () {
    const MAX_NUMBER = 83;
    return Math.floor(Math.random() * MAX_NUMBER + 1);
}

function button () {
    const bnt = document.getElementById("button");
    bnt.addEventListener("click", handleClick);
}

button()