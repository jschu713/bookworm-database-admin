// function deleteRow()    {
// may add back in later
//     // removes row from table by targeting parent node; will be done only after removing the entry from the DB in final version
//     let td = event.target.parentNode;
//     let tr = td.parentNode;
//     tr.parentNode.removeChild(tr);
// }

// I'm sure I could've made these functions more modular but I took the easiest solution for this temporary front end
function addRow() {
  let table = document.getElementById("table");

  let row = document.createElement("tr");

  let td1 = document.createElement("td");
  let td2 = document.createElement("td");
  let td3 = document.createElement("td");
  let td4 = document.createElement("td");
  let td5 = document.createElement("td");
  let td6 = document.createElement("td");

  td1.innerHTML = document.getElementById("fname").value;
  td2.innerHTML = document.getElementById("lname").value;
  td3.innerHTML = document.getElementById("address").value;
  td4.innerHTML = document.getElementById("phone").value;
  td5.innerHTML = '<button type="button" class="btn btn-primary">Delete</button>'; 
  td6.innerHTML = '<button type="button" class="btn btn-primary">Edit</button>'; 

  row.appendChild(td1);
  row.appendChild(td2);
  row.appendChild(td3);
  row.appendChild(td4);
  row.appendChild(td5);
  row.appendChild(td6);
  table.children[0].appendChild(row);
}
 
function addAuthorRow() {
  let table = document.getElementById("table");

  let row = document.createElement("tr");

  let td1 = document.createElement("td");
  let td2 = document.createElement("td");
  let td3 = document.createElement("td");
  let td4 = document.createElement("td");

  td1.innerHTML = document.getElementById("fname").value;
  td2.innerHTML = document.getElementById("lname").value;
  td3.innerHTML = '<button type="button" class="btn btn-primary">Delete</button>'; 
  td4.innerHTML = '<button type="button" class="btn btn-primary">Edit</button>'; 

  row.appendChild(td1);
  row.appendChild(td2);
  row.appendChild(td3);
  row.appendChild(td4);
  table.children[0].appendChild(row);
}

function addRentalRow() {
  let table = document.getElementById("table");

  let row = document.createElement("tr");

  let td1 = document.createElement("td");
  let td2 = document.createElement("td");
  let td3 = document.createElement("td");
  let td4 = document.createElement("td");
  let td5 = document.createElement("td");

  td1.innerHTML = document.getElementById("rentalDate").value;
  td2.innerHTML = document.getElementById("rentalLength").value;
  td3.innerHTML = document.getElementById("subscriberId").value;
  td4.innerHTML = '<button type="button" class="btn btn-primary">Delete</button>'; 
  td5.innerHTML = '<button type="button" class="btn btn-primary">Edit</button>'; 

  row.appendChild(td1);
  row.appendChild(td2);
  row.appendChild(td3);
  row.appendChild(td4);
  row.appendChild(td5);
  table.children[0].appendChild(row);
}

function addBookRow() {
  let table = document.getElementById("table");

  let row = document.createElement("tr");

  let td1 = document.createElement("td");
  let td2 = document.createElement("td");
  let td3 = document.createElement("td");
  let td4 = document.createElement("td");
  let td5 = document.createElement("td");
  let td6 = document.createElement("td");
  let td7 = document.createElement("td");
  let td8 = document.createElement("td");

  td1.innerHTML = document.getElementById("name").value;
  td2.innerHTML = document.getElementById("pages").value;
  td3.innerHTML = document.getElementById("publisher").value;
  td4.innerHTML = document.getElementById("genre").value;
  td5.innerHTML = document.getElementById("authorFname").value;
  td6.innerHTML = document.getElementById("authorLname").value;
  td7.innerHTML = '<button type="button" class="btn btn-primary">Delete</button>'; 
  td8.innerHTML = '<button type="button" class="btn btn-primary">Edit</button>';  

  row.appendChild(td1);
  row.appendChild(td2);
  row.appendChild(td3);
  row.appendChild(td4);
  row.appendChild(td5);
  row.appendChild(td6);
  row.appendChild(td7);
  row.appendChild(td8);
  table.children[0].appendChild(row);
}