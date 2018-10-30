$(function() {
  $.get("/actividades/get_clientes_x_actividad", {}, function(data) {
      let deportes = [];
      let cantidad = [];

      $.each(data, function(index, value) {
        if (index) {
          deportes.push(index);
        }
        if (value) {
          cantidad.push(value);
        }
      });

      let ctx = document.getElementById('myChart').getContext('2d');

      let myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: deportes,
          datasets: [{
              backgroundColor: [
                'rgb(255, 99, 132)',
                'rgba(54, 162, 235, 0.2)',
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgba(54, 162, 235, 0.2)',
              ],
              data: cantidad,
          }]
        },
        options: {}
      });
  });
});
