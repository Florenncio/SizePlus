/* Formatting function for row details - modify as you need */
function format () {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            '<td>Enredeço:</td>'+
            '<td>{% cliente.endr_cliente %}</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Numero:</td>'+
            '<td>{% cliente.num_cliente %}</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Sexo:</td>'+
            '<td>{% cliente.sexo_cliente %}</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Estado Civil:</td>'+
            '<td>{% cliente.estd_civil_cliente %}</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Nascido(a):</td>'+
            '<td>{% cliente.data_nasc_cliente %}</td>'+
        '</tr>'+

    '</table>';
}

$(document).ready(function() {
    var table = $('#mytable').DataTable( {
        "ajax": "http://127.0.0.1:8000/cliente/json/",
        "columns": [
            {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": ''
            },
            { "data": "name" },
            { "data": "position" },
            { "data": "office" },
            { "data": "salary" }
        ],
        "order": [[1, 'asc']]
    } );
 
    $(document).ready(function() {     
        // Add event listener for opening and closing details
        $('#mytable tbody').on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = table.row( tr );
    
            if ( row.child.isShown() ) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            }
            else {
                // Open this row
                row.child( format(row.data()) ).show();
                tr.addClass('shown');
            }
        } );
    } );
} );