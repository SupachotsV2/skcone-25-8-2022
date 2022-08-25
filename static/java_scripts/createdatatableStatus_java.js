
function buildList(status='w'){
let url = "http://localhost:8000/api/testRequest-list";
    fetch(url)
      .then((res) => res.json())
        .then(function(data){ 
        let list = data;
        // if (list.docStatus.toLowerCase() == 'wait approve'){ 
        var data_use = list.filter(function(el){
            // console.log(el.docStatus.toLowerCase().startsWith(status))
            return el.docStatus.toLowerCase().startsWith(status);
         });
        //  const test = data_use.filter(data_use =>data_use.id == 2);
        //  const test2 = Array.from(test)
        //  console.log("Test is ",test['system']);
         $(document).ready(function () {
            $('#example').DataTable({
                data: data_use,
                // responsive: true,
                destroy: true,
                scrollX: true,
                // scrollCollapse: true,
                order: [[5, 'desc']],
                fixedColumns:   {
                  left: 1,
              },
                columnDefs:[{
                     "targets":0,
                     "data":"detail_link",
                     "render": function(data,type,row,meta){
                        return'<a href="'+data+'"target="_blank"><img src="/static/image/file.png" style="width: 35px; height: 35px;"></a>';
                      
                     }
                   },{
                    "targets":-1,
                     "data":"Approve_btn",
                     "render": function(data,type,row,meta){
                        return'<button type="button" class="btn bg-success text-light" onclick="changeStatusapprove('+data+')">✔</button><span>     </span><button type="button" class="btn bg-danger text-light" onclick="changeStatusreject('+data+')">✖</button>'; //<img src="/static/image/checkbox.png" style="width: 30px; height: 30px;">
                     }
                   },
                  //  {
                  //   "targets":-1,
                  //    "data":"Reject_btn",
                  //    "render": function(data,type,row,meta){
                  //       return'<button type="button" class="btn bg-danger text-light" onclick="changeStatusreject('+data+')">Reject</button>'; //<img src="/static/image/checkbox.png" style="width: 30px; height: 30px;">
                  //    }
                  //  }
                  ],
                   columns:[
                        {data:'detailUrl',"width":"40px"},
                        {data:'docNumber'},
                        {data:'title',"width":"200px"},
                        {data:'department'},
                        {data:'requester'},
                        {data:'requestDate',"width":"40px"},
                        {data:'lastUpdate',"width":"40px"},
                        {data:'system',"width":"100px"},
                        {data:'docStatus',"width":"100px"},
                        {data:'attachment',"width":"15px"},
                        {data:'approver'},
                        {data:'id',"width":"70px"},
                        // {data:'id'}
                    ],
                    
                });
            });
        // }
            // setTimeout(function() {
            //     location.reload();
            //     }, 10000);
        });
      }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
              }
            }
          }
      return cookieValue;
        }
        
const csrftoken = getCookie("csrftoken");

function changeStatusapprove(task){
  // task = id
  console.log("Task",task);
  let status = "Approve";
  let url = `http://localhost:8000/api/testRequest-update/${task}/`;
  fetch(url,{
    method:"POST",
    headers:{
      "Content-type" : "application/json",
      "X-CSRFToken" : csrftoken,
    },
    body:JSON.stringify({title:task , docStatus: status}),
  }).then(function(){
    // console.log("Yeah!!!")
    buildList();
  });
}

function changeStatusreject(task){
  // task = id
  console.log("Task",task);
  let status = "Reject";
  let url = `http://localhost:8000/api/testRequest-update/${task}/`;
  fetch(url,{
    method:"POST",
    headers:{
      "Content-type" : "application/json",
      "X-CSRFToken" : csrftoken,
    },
    body:JSON.stringify({title:task , docStatus: status}),
  }).then(function(){
    // console.log("Yeah!!!")
    buildList();
  });
}
