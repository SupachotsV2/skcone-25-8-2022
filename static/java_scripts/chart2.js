// create doughnut chart
// create function to import api
function buildList_2() {
    let url = "http://localhost:8000/api/chartSystems";
    fetch(url)
        .then((res) => res.json())
        .then(function (data) {
            // console.log("Data", data);
            let list = data;
            //change data 
            for (let i in list) {
                if (list[i].system == '1') {
                    list[i].system = 'myDas';
                } else if (list[i].system == '2') {
                    list[i].system = 'e-Inventory';
                } else if (list[i].system == '3') {
                    list[i].system = 'e-Procurement';
                }
            }
            //end change data
            //end import api

            // console.log("From pie", list)
            let total_all = list.map(
                function (index) { return index.system; });
            // console.log("Total all", total_all);

            // console.log("From pie", list)
            let total_sys = list.map(
                function (index) { return index.total; });
            // console.log("Total sys", total_sys);


            var ctx2 = document.getElementById('doughnut').getContext('2d');
            var doughnut = new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: total_all,

                    datasets: [{
                        data: total_sys,
                        backgroundColor: [
                            '#EFCA08',
                            '#00a8ab',
                            '#eb603f'

                        ],
                        borderWidth: 1
                    }]

                },
                options: {
                    responsive: true
                }
            });
        });
}