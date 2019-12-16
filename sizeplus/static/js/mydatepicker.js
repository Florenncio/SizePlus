$(function(){
    // Initialize materialize data picker
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        i18n: {
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Outubro', 'Setembro', 'Novembro', 'Dezembro'],
            monthsShort:['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
            weekdaysShort: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
            weekdaysAbbrev:['S','T','Q','Q','S','S','D'],
            cancel: 'Cancelar'



        }
    
    });
    $('select').formSelect();
});

