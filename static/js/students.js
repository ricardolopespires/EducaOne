var start = document.querySelector("#start");
var c_video = document.querySelector(".c-video");
// Get the video element with id="myVideo"
var vid = document.getElementById("myVideo");
var lesson = document.querySelector("#lesson").innerText;
var id = document.querySelector("#id").innerText;
var course = document.querySelector('#id-course').innerText;



var views = 0



function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}


async function concluida(dados){

    
    console.log('Aula Concuida')
   var csrftoken = readCookie('csrftoken');

    const rawResponse = await fetch('http://localhost:8000/courses/lesson/'+dados.id+'/update/', {

        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
            },
            body: JSON.stringify({"id":dados.id,"title": dados.title,"concluded": true })
            }).then(result => result.json())
            
            
        }





async function vizualizada(dados){

    
    console.log('Aula Vizualizada')
    console.log(dados)
    var csrftoken = readCookie('csrftoken');

    const rawResponse = await fetch('http://localhost:8000/courses/lesson/analytics/'+ dados.id +'/update/', {

        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
            },
            body: JSON.stringify({"id":dados.id,"course":dados.course,"views":dados.views })
            }).then(result => result.json())
            
            
        }


async function Analytics(){

    const response = await fetch('http://localhost:8000/courses/lesson/analytics/list/');
    
    const data = await response.json()
   
    data.map((dataset) =>{

        if(course == dataset.course){

            if( views == 0 ){

                var total = dataset.views + 1;            
                dados ={'id':dataset.id,'course':course,'views':total}
                vizualizada(dados);

                views = 1

            }

        }      

              
    });
     
}



vid.addEventListener('timeupdate', function(){

    var tempo = vid.currentTime / vid.duration;
    var duracao = parseInt(tempo * 100);

    
    if( duracao === 90){


        dados ={'id':id,'title':lesson}
        concluida(dados)
        Analytics()
       
    }
    
})




