const HEIGHT = 6;
const WIDTH = 7;
const cataId = []
let button = 1;







async function populateTable(){
    const catResponse = await axios.get(`http://jservice.io/api/categories?count=${100}`)

    const catArr = catResponse.data.map(function(a){
        return a.id
    })
    //console.log(catArr)

$("#button").on("click" , function(e){
    
    button = button === 1? 2:1;
    if(button === 2){
        $("#button").text("Restart Game")
        $("#button").on("click" , function(e){
            location.reload()
        })
    }



    
    for(let x = 0 ; x < 1 ; x++){
        const $trow = $("<tr>")
        $("#table").addClass("text-primary col-9 justify-content-center")
 

        $($trow).mouseover(function(e){
            $($trow).addClass("blue")
        })

        $("#thead").append($trow)

        for(let y = 0; y < WIDTH; y++){
        async function getClue(){
            const response1 = await axios.get(`http://jservice.io/api/categories?count=${100}`)
            const responseLength1 = (response1.data.length)
            const randomIdx1 = Math.floor(Math.random() * responseLength1)
            const targetId1 = response1.data[randomIdx1].id
            const cata = response1.data[randomIdx1].title
           
   
       
            
            const $th = $("<th>").text(cata)
            $($th).addClass(`text-center headerCell `)
            $($th).attr(`id` , `${targetId1}`)
           
            
            cataId.push(targetId1)



            $($th).on("click" , function(e){

                $($th).addClass("text-danger")
                console.log(e.target)
                
                
            })
            $($trow).append($th)
       
       
     
         
          
            
        }
   
        getClue()
    }


    }

    for(let x = 0; x < HEIGHT -1 ; x++){
        const $tbRow = $("<tr>")
        $("#tbody").append($tbRow)

        for(let y = 0; y < WIDTH  ; y++){
          
            const $trD = $("<td>").text("?")
            $($trD).addClass("trd")
            $($trD).attr("id", `${y}`)

            




            $($trD).on("click" , function(e){

               
                const headerCell = document.querySelectorAll("th")
                const trdId = $trD.attr('id')
                console.log(trdId)
                const matchedHeader = (headerCell[trdId])
                const matchedHeaderId = matchedHeader.getAttribute("id")
                console.log(matchedHeaderId)
                console.log(matchedHeader)
                console.log(e.target)
                async function getClue(){
                    const response = await axios.get(`http://jservice.io/api/category?id=${matchedHeaderId}`)
                    console.log(response.data.clues)
                    const responseLength = (response.data.clues.length)
                    const randomIdx = Math.floor(Math.random() * responseLength)
                    const targetId = response.data.clues[randomIdx].id
                    console.log(targetId)
                    const clue = response.data.clues[randomIdx].question
                    const answer = response.data.clues[randomIdx].answer
                    console.log(answer)
                    console.log(clue)
                    console.log(response.data[randomIdx])
                    
                    
                  
                   function populateBoxClue(){
                       
                       if(x === 2){
                    $($trD).text(`${clue}`)
                $($trD).removeClass("trd")
                $($trD).addClass(`text-center trd2 transition`)
                $($trD).off();
                   }
                   x = 1
                }
           
                        
                
                   
            

                
              //  $($trD).attr(`id`, `${targetId}`)
                       
                   function populateBoxAnsw(){
                    $($trD).on("click" , function(e){
                       
                       if(x === 1){
                        $($trD).text(`${answer}`)
                           
                           $($trD).off();
                           
                       }
                       
                    })
                 
                }

                    
                   let x = 2;

                
                    populateBoxClue()
                   
                  
                       populateBoxAnsw()
                   


              

                       
                       
                        
                    
                }

                
                
                getClue()
             
                

                
            })

          
        
                $($trD).addClass("text-center blue selection")
           
        
            $($tbRow).append($trD)
            
        }
    }
})
}


//try to find a way to connect the id for the catagory to the selection



populateTable()

const cell = document.getElementById("thead")
cell.addEventListener("click" , function(e){
async function test1(){
    const target = e.target
    const id = target.getAttribute("id")
    console.log(id)
    const response = await axios.get(`http://jservice.io/api/category?id=${id}`)
    console.log(response.data)

    //console.log(response.data.clues[0].question)
}
test1()
})

