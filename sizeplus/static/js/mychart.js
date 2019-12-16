new Chart(document.getElementById("mychart"), {
    type: 'line',
    data: {
        labels: ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],
        datasets: [{ 
            data: [82,50,11,52,35,89,47,58,37,67,55,70],
            label: "Adesão",
            borderColor: "#3e95cd",
            fill: false
        }, { 
            data: [06,14,16,16,40,11,33,21,20,23,18,10],
            label: "Remoção",
            borderColor: "#8e5ea2",
            fill: false
        }
        ]
    },
    options: {
        title: {
        display: true,
        text: 'Fluxos de instalações e remoções durante 2018.'
        }
    }
    });