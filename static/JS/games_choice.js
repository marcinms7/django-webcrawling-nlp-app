window.onclick = e => {
    console.log(e.target.id);  // to get the element id


// Checking if clicked id is numeric. Then saving id and opening new page with the search
if(Math.floor(e.target.id) == e.target.id && $.isNumeric(e.target.id)) 
{  console.log('yes its an int!');
  var chosen = e.target.id
  localStorage.setItem('requestQueue',chosen);

  window.open('/search');
}
} 
