$(document).ready(function() {
    $('#mytable').dataTable( {
        "ajax": {
          "url": "http://127.0.0.1:8000/cliente/json/",
          "type": "GET"
        }
      } );
});