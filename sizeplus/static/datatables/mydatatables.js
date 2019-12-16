$(document).ready(function() {
    responsive: true
    
    
    $('#mytable').DataTable( {
        "language": {
            "lengthMenu": "_MENU_",
            "zeroRecords": "Nao foi possivel encontrar nenhum cadastro com essas caracterisiticas.",
            "info": "",
            "infoEmpty": "",
            "infoFiltered": "",
            "search": "",
            "paginate":{
            "first": "Primeiro",
            "last": "Ultimo",
            "next": "Proximo",
            "previous": "Anterior"
            }, 
        },
        bLengthChange : false,
        pageLength : 15,
    } );
    
    var dataTable = $('#mytable').dataTable();
    $("#mysearch").keyup(function() {
        dataTable.fnFilter(this.value);
    });
    
    $('.dataTables_paginate').addClass('pagination');
    
} );