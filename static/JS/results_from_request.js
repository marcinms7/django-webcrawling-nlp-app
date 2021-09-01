// Getting saved request item
var item_id = window.localStorage.getItem('requestQueue')

console.log("ITEM IS ")
console.log(item_id)

// getting request for reddit page
let key = "?key=cef45661b4354e669cac1b77d398b285"
let api = "https://api.rawg.io/api/games/"
let item_id_string = item_id.toString()

// setting url for reddit search
let reddit =  "/reddit"

// fetches the searched id
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

  fetch(api + item_id_string + key , requestOptions)
  .then(response => response.json())
  .then(result => {
  	console.log("REquest");
  	console.log(result);
    console.log("img");
    console.log(result.background_image);
    document.body.style.backgroundImage = "url('" + result.background_image.toString() + "')"
    document.getElementsByClassName("bg")[0].style.background = "url('" + result.background_image.toString() + "')"
    document.getElementById("h1_id").innerHTML = result.name
    document.getElementById("p_1").innerHTML = result.website
    document.getElementById("p_2").innerHTML = "Release date:  " + result.released;
    document.getElementById("p_3").innerHTML = "Avg Rating:  " + result.rating;
    document.getElementById("p_4").innerHTML = "Metacritic score:  " + result.metacritic




let btn = document.createElement("button");
btn.innerHTML = "Run NLP algorithm!";
// btn.type = "submit";
btn.name = "runningNLP";
btn.className ="btn btn-warning";
var myDiv = document.getElementById("box1");
// creating form for get
var form = document.createElement("form");
form.setAttribute("method", "get");
form.setAttribute("action", "#");

myDiv.appendChild(form);
form.appendChild(btn);

btn.addEventListener("click", function () {
  alert("Comments extracting - this might take 1-3 minutes ");
});



// generating cookie for csrftoken and sending request
function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
const csrftoken = getCookie('csrftoken');

var send = result
    $.ajax({
          async: false,

        method: 'POST',
        url: '',
      headers:{
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
          'X-CSRFToken': csrftoken,
  },
        data: {'yourJavaScriptArrayKey': send,
                  // 'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
        'dataType': 'json',
        success: function (data) {
             //this gets called when server returns an OK response
             console.log("it worked!");
             console.log(send);
        },
        error: function (data) {
             console.log("it didnt work");
             console.log(send);
             console.log(csrftoken)
        }
    });







  })
  .catch(error => console.log('error', error));

