var doughnutChartctx = document.getElementById('doughnutChart').getContext('2d');
  new Chart(doughnutChartctx, {
    type: 'doughnut',
    data: {
      labels: {{user_list|safe}},
      datasets: [
        {
          label: "2046 CE Selection",
          backgroundColor: ["#3273DC", "#00D1B2","#FFDD57"],
          data: {{data|safe}}
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'CE Selection in 2046'
      }
    }
});

var stackedChartctx = document.getElementById('stackedChart').getContext('2d');
var chart = new Chart(stackedChartctx, {
    type: 'line',
    data: {
        labels: ["1 min", "2 mins", "3 mins", "4 mins", "5 mins", "6 mins", "7 mins","8 mins","9 mins","10 mins"],
        datasets: [
        {
            label: "{{user_list[0]|safe}}",
            backgroundColor: '#3273DC',
            borderColor: '#3273DC',
            data: [0, 1, 3, 5, 3, 0, 3, 0, 2, 4],
        },
        {
            label: "{{user_list[1]|safe}}",
            backgroundColor: '#00D1B2',
            borderColor: '#00D1B2',
            data: [0, 4, 8, 12, 49, 29, 1, 2, 5, 0],
        },
        {
            label: "{{user_list[2]|safe}}",
            backgroundColor: '#FFDD57',
            borderColor: '#FFDD57',
            data: [0, 10, 5, 2, 20, 30, 45, 2, 3, 4],
        }

        ]
    },
    options: {}
});