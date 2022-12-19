$(document).ready(function ($) {

    var table = $("#table").DataTable({
        ajax: "/manage_mangas/list",
        processing:true,
        serverSide:true,
        columns:[
            {data:"id", name:"id"},
            {data:"name", name:"name"},
            {data:"capitulos", name:"capitulos"},
            {data:"status", name:"status"},
            {data:"data_lancamento", name:"data_lancamento"},
            {data:"opcoes", name:"opcoes"},

        ],
    });

});