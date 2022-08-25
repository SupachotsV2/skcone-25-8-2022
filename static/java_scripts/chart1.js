// create bar chart
// create function to import api
function buildList_1() {
    let url = "http://localhost:8000/api/chartDocstatus";
    fetch(url)
        .then((res) => res.json())
        .then(function (data1) {
            // console.log("Data1", data1);
            let list = data1;
            //end import api
            //create doughnut chart

            // const result = words.filter(word => word.length > 6);
            console.log("From js", list)

            const total_label = [...new Set(list.map(x => x.system))];
            console.log("Total label", total_label)
            // end process unique data

            // list data after filter
            let total_approved = list.map(
                function (index) { return index.Approved; });
            // console.log("approve_data", approve_data);
            console.log("Total approve", total_approved);

            let total_reject = list.map(
                function (index) { return index.Reject; });
            console.log("Total reject", total_reject)

            // end process list data 

            var ctx = document.getElementById('bar').getContext('2d');
            var bar = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: total_label,
                    datasets: [{
                        label: 'Approved 👍',
                        data: total_approved,
                        backgroundColor: [
                            '#3ccc37',
                            '#3ccc37',
                            '#3ccc37',
                        ],
                        borderWidth: 1
                    },
                    {
                        label: 'Reject 👎',
                        data: total_reject,
                        backgroundColor: [
                            '#eb3f3f',
                            '#eb3f3f',
                            '#eb3f3f',
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    categoryPercentage: 0.6,
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    },
                    // maintainAspectRatio: false,
                    responsive: true
                }
            });
        });

}
// end function and bar chart

$(document).ready(function waitapprove_count() {
    let url = "http://localhost:8000/api/chartDocstatus";
    fetch(url)
        .then((res) => res.json())
        .then(function (data1) {
            let list = data1;
            let wait_count = list.map(
                function (index) { return index.Wait; })
            console.log("Count", wait_count.reduce((a, b) => a + b, 0));
            const waitcount = wait_count.reduce((a, b) => a + b, 0);
            document.getElementById("waitrequest").innerHTML = waitcount;
            let approved_count = list.map(
                function (index) { return index.Approved; })
            const approvedcount = approved_count.reduce((a, b) => a + b, 0);
            document.getElementById("approvedrequest").innerHTML = approvedcount;
            let reject_count = list.map(
                function (index) { return index.Reject; })
            const rejectcount = reject_count.reduce((a, b) => a + b, 0);
            document.getElementById("rejectrequest").innerHTML = rejectcount;
            document.getElementById("allrequest").innerHTML = waitcount + approvedcount + rejectcount;


            let valueDisplays1 = document.querySelectorAll(".number1");
            let interval1 = 300;
            valueDisplays1.forEach((valueDisplays1) => {
                let startValue = -1;
                let endValue = parseInt(valueDisplays1.getAttribute("allrequest")).innerHTML = waitcount + approvedcount + rejectcount;
                let duration = Math.floor(interval1 / endValue);
                let counter = setInterval(function () {
                    startValue += 1;
                    valueDisplays1.textContent = startValue;
                    if (startValue == endValue) {
                        clearInterval(counter);
                    }
                }, duration);
            });

            let valueDisplays2 = document.querySelectorAll(".number2");
            let interval2 = 300;
            valueDisplays2.forEach((valueDisplays2) => {
                let startValue = -1;
                let endValue = parseInt(valueDisplays2.getAttribute("approvedrequest")).innerHTML = approvedcount;
                let duration = Math.floor(interval2 / endValue);
                let counter = setInterval(function () {
                    startValue += 1;
                    valueDisplays2.textContent = startValue;
                    if (startValue == endValue) {
                        clearInterval(counter);
                    }
                }, duration);
            });

            let valueDisplays3 = document.querySelectorAll(".number3");
            let interval3 = 300;
            valueDisplays3.forEach((valueDisplays3) => {
                let startValue = -1;
                let endValue = parseInt(valueDisplays3.getAttribute("rejectrequest")).innerHTML = rejectcount;
                let duration = Math.floor(interval3 / endValue);
                let counter = setInterval(function () {
                    startValue += 1;
                    valueDisplays3.textContent = startValue;
                    if (startValue == endValue) {
                        clearInterval(counter);
                    }
                }, duration);
            });

            let valueDisplays4 = document.querySelectorAll(".number4");
            let interval4 = 300;
            valueDisplays4.forEach((valueDisplays4) => {
                let startValue = -1;
                let endValue = parseInt(valueDisplays4.getAttribute("waitrequest")).innerHTML = waitcount;
                let duration = Math.floor(interval4 / endValue);
                let counter = setInterval(function () {
                    startValue += 1;
                    valueDisplays4.textContent = startValue;
                    if (startValue == endValue) {
                        clearInterval(counter);
                    }
                }, duration);
            });



            
        }
        )
})


