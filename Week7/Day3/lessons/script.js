// console.log("Starting ...")

// const data = {
//     icon_url : "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
//     id : "HRL1A1MJSWO5Nxt5tuPZlQ",
//     url : "",
//     value: "Chuck Norris and Sasquatch are maternal cousins."


// }

// const objBody = {
//    const body = JSON.(data) 
// }

// const addArticle = () => {
//     console.log("Working ...")
//     fetch("https://jsonplaceholder.typicode.com/posts", objBody)
//         .then((response) => {
//             console.log(response);
//             if(response.ok === true){
//                 return response.json()
//             } else {
//                 throw new Error("Wrong post")
//             }
//         })
//         .then((obj) => {
//             console.log(obj);
//         })
//         .catch((error)  => {
//             console.log(error);
//         });
//     console.log("Work Done ...")
// }

// addArticle()



const button = document.getElementById("btn")

const fetchJoke = () => {
    fetch("https://api.chucknorris.io/jokes/random?category={category}")
    (Response => {
        console.log(Response);
        if (Response.ok) {
            return Response.json();
        }else {
            throw new Error("error fetching category");
        }
    })
    .then(response) =>
    .then ((data)=> {
        const randomNum = Math.floor(Math.random() * data.length);
        const category = data[randomNum];

    })
    .catch((e)=> console.log(e));
}
button.addEventListener("click", fetchJoke)