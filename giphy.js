

// const $gifArea = $("#gif-area");
// const $searchInput = $("#search");

// /* use ajax result to add a gif */

// function addGif(res) {
//   let numResults = res.data.length;
//   if (numResults) {
//     let randomIdx = Math.floor(Math.random() * numResults);
//     let $newCol = $("<div>", { class: "col-md-4 col-12 mb-4" });
//     let $newGif = $("<img>", {
//       src: res.data[randomIdx].images.original.url,
//       class: "w-100"
//     });
//     $newCol.append($newGif);
//     $gifArea.append($newCol);
//   }
// }

// /* handle form submission: clear search box & make ajax call */

// $("form").on("submit", async function(evt) {
//   evt.preventDefault();

//   let searchTerm = $searchInput.val();
//   $searchInput.val("");

//   const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
//     params: {
//       q: searchTerm,
//       api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
//     }
//   });
//   console.log(response)

//   addGif(response.data);
// });

// /* remove gif */

// $("#remove").on("click", function() {
//   $gifArea.empty();
// });


// create a Gif search forum

// allow the user to search for a Gif , and when the form is submitted , 
// use AJAX  to make a request to giphy , then append the gif ( one ) to the page



async function gif(searchTerm){
    const res = await axios.get("http://api.giphy.com/v1/gifs/search" , {params: {q:searchTerm,api_key:"MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"}} )
    console.log(res)
    const length = (res.data.data.length) -1
    //console.log(length)
    const randomGif = (res.data.data[Math.floor(Math.random() * length)].images.original.url)
    console.log(randomGif)
    const body = document.querySelector("body")
    const imagePlace = document.createElement("div")
    imagePlace.id = "pictureBox"
    imagePlace.innerHTML = (`<img src = ${randomGif} id = "picture" >`)
    body.append(imagePlace)

    return(randomGif)

   
    
}



const searchButton = document.getElementById("searchBtn")
searchButton.addEventListener("click", function(e){
    e.preventDefault()
    const userInput = document.getElementById("searchBar").value
    const image = document.getElementById("image")
    return (gif(userInput))
})

const removeButton = document.getElementById("removeBtn")
removeButton.addEventListener("click", function(e){
    e.preventDefault()
    let Pics = (Array.from(document.querySelectorAll("img")))
    for(let i = 0; i < Pics.length; i++){
        Pics[i].remove(Pics[i])
    }
})






