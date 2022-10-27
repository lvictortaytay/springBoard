let showing = 1
$("#searchButton").on("click", function (e){
    $("#showArea").html("")
    e.preventDefault();
    const value = $("#searchForm").val();
    $(".container").append(getShows(value))
    

})





async function getId(value){
    const response = await axios.get(`https://api.tvmaze.com/search/shows?q=${value}`)
    let episodes = response.data.map(episode => ({ 
        id: episode.id,
        name: episode.name,
        season: episode.season,
        number: episode.number,
      }));
    
      return episodes; 

}


async function getShows(value){

    const response = await axios.get(`https://api.tvmaze.com/search/shows?q=${value}`)
    for(let i = 0 ;  i < response.data.length ; i++){
        const show = (response.data[i])
        const image = (response.data[i].show.image.original)
        const text = (`

        <div class="card col-md-6 col-lg-3">
          <img src="${image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${show.show.name}</h5>
             <p class="card-text" data-show-id="${show.show.id}" >${show.show.summary}</p>
            <button class="btn btn-primary" id="${i}" >See Episodes!</button>
           <ul id="cardEpisodes${i}">
         </ul>
        </div>
        </div>
        `)
      
        $("#showArea").append(text)

       
        $(`#${i}`).on("click" , function(e){
       
          const card = (e.target.closest(".card-body"))
          const ul = card.querySelector("ul")
          console.log(ul)


      



          async function getEpisodes(){
            
             
            const response = await axios.get(`https://api.tvmaze.com/shows/${show.show.id}/episodes`)
            for(let i=0 ; i < response.data.length ; i++){
                const eName = (response.data[i].name)
                const text = (`
          
                <li class="text-primary">
                ${eName}
                </li>
        
            `)
            
            if(showing === 1){
               
                $(ul).append(text)
                const button = (e.target.closest(".btn"))
                $(button).html("Hide episodes")
                
            }
            if(showing === 2){
                $(ul).html("")
                const button = (e.target.closest(".btn"))
                $(button).html("See episodes!")
                
            }
            
           
            
            }
            
            showing = showing === 1? 2:1
        
        }






      
          
            getEpisodes()
            
      
       console.log(showing)

        })
      
        
    }
 
    
     
}



// const val = $("#searchForm").val();
//               const response1 = await axios.get(`https://api.tvmaze.com/search/shows?q=${val}`)
//               for(let i = 0 ; i < response1.data.length ; i++){
//                 console.log(response1.data[i].show.id)
//               }
             
// async function getEpisodes(){
//     const vall = $("#searchForm").val();
//     const response =  await axios.get(`https://api.tvmaze.com/search/shows?q=${vall}`)
//     for(let i = 0 ; i < response.data.length ; i++){
//         console.log(response.data[i].show.id)
//     }
//     const response2 = await axios.get(`https://api.tvmaze.com/shows/${1}/episodes`)
//     for(let i=0 ; i < response.data.length ; i++){
//         const eName = (response.data[i].show.name)
//         const text = (`
  
//         <li class="text-primary">
//         ${eName}
//         </li>

//     `)
//     $(ul).append(text)
    
//     }








