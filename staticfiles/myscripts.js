document.addEventListener('DOMContentLoaded', () => {
    console.log("myscripts.js carregado");

    const ctx = document.getElementById('graficoNumVolumes');
    if (!ctx) {
        console.log("Canvas não encontrado");
        return;
    }

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Carros Alugados', 'Carros Disponíveis', 'Clientes', 'Locações Ativas'],
            datasets: [{
                label: 'Estatísticas',
                data: [
                    dadosDashboard.carrosAlugados,
                    dadosDashboard.carrosDisponiveis,
                    dadosDashboard.totalClientes,
                    dadosDashboard.locacoesAtivas
                ],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(255, 99, 132, 0.7)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
