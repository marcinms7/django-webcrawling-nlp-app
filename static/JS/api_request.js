
console.log("START")
// grabing search button
var x = document.querySelector('.search');

const s_button = document.querySelector('.s_button');
// settting url for search 
let key = "?key=cef45661b4354e669cac1b77d398b285"
let api = "https://api.rawg.io/api/games"
var searching = "&search=" + x


// setting search options
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

var id = ""
var htmlname = ""




// for click button it loops through the game titles and populates them with fetched names
  s_button.addEventListener('click', function(e){  
  var x = document.querySelector('#search');


  var searching = "&search=" + x.value
// fetches by search
  fetch(api + key + searching, requestOptions)
  .then(response => response.json())
  .then(result => {




    var list = result;
    for (let i = 1; i < 10; i++) { 
  console.log(result.results[i].name)
  htmlname = "game" + i.toString();

// sets name to fetched name and id to fetched id
  document.getElementsByClassName(htmlname)[0].innerHTML = result.results[i].name;
  document.getElementsByClassName(htmlname)[0].id = result.results[i].id;
  document.getElementsByClassName(htmlname)[0].classList.add('list-group-item');
  document.getElementsByClassName(htmlname)[0].classList.add('list-group-item-action');
  document.getElementsByClassName(htmlname)[0].classList.add('list-group-item-info');
};










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

    for (let j = 1; j < 10; j++) { 

var send = result.results[j]
console.log("REQUEST:")
// console.log(result.results[i])
// $(document).ready(function() {
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
// });
};




    id = result.results[0]
  })
  .catch(error => console.log('error', error));
})
















