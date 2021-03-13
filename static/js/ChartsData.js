$(function () {
  'use strict';
  //Estadistica para inversion
  function float2dollar(value) {
    return "Q. " + (value).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
}
    var consigno = {
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        callback: function (value, index, values) {
                            return float2dollar(value);
                        }
                    }
                }
            ]
        },
        legend: {
            display: false
        },
        elements: {
            point: {
                radius: 0
            }
        }
    };
        var sinsigno = {
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    }
                }
            ]
        },
        legend: {
            display: false
        },
        elements: {
            point: {
                radius: 0
            }
        }
    };
    $("#form").submit(function(event){
        event.preventDefault();
        var $beneficiadosChart = $("#areaChart");
        var dataForm = {
            year: parseInt(document.getElementById("year").value),
            identificador: parseInt(document.getElementById("identificador").value),
            aldea: parseInt(document.getElementById("aldea").value),
            canton: parseInt(document.getElementById("canton").value)
        }
        $.ajax({
            type: "POST",
            url: $beneficiadosChart.data("url"),
            data: dataForm,
            success: function (data){
                var ctx = $beneficiadosChart[0].getContext("2d");
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'No. Beneficiados',
                            data: data.data,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255,99,132,1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            fill: true, // 3: no fill
                        }]
                    },
                    options: sinsigno
                });
                data: []
                labels: []
            }
        })
    })


    /* INVERSION */
    $("#formInversion").submit(function(event){
        event.preventDefault();
        var $inversionChart = $("#estadistica_inversion");
        var dataForm = {
            year: parseInt(document.getElementById("year").value),
            identificador: parseInt(document.getElementById("identificador").value),
            aldea: parseInt(document.getElementById("aldea").value),
            canton: parseInt(document.getElementById("canton").value),
        }
        $.ajax({
            type: "POST",
            url: $inversionChart.data("url"),
            data: dataForm,
            success: function (data){
                var ctx = $inversionChart[0].getContext("2d");
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Total inversion',
                            data: data.data,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255,99,132,1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            fill: true, // 3: no fill
                        }]
                    },
                    options: consigno
                });
                data: []
                labels: []
            }
        })
    })
    /* INVERSION */
    $("#formGruposTotal").submit(function(event){
        event.preventDefault();
        var $comunidadesChart = $("#comunidadesChart");
        var dataForm = {
            year: parseInt(document.getElementById("year").value),
            identificador: parseInt(document.getElementById("identificador").value)
        }
        $.ajax({
            type: "POST",
            url: $comunidadesChart.data("url"),
            data: dataForm,
            success: function (data){
                var ctx = $comunidadesChart[0].getContext("2d");
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: '# Grupos',
                            data: data.data,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255,99,132,1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1,
                            fill: true, // 3: no fill
                        }]
                    },
                    options: sinsigno
                });
                data: []
                labels: []
            }
        })
    })
});