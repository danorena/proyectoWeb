function validate(e){
    console.log('Validando ...');
    e.preventDefault();

    form  = document.getElementById('asistencia-form');
    date = document.getElementById('date');
    select = document.getElementById('state');

    lVali = true;

    if (date.value==""){
        date.style.borderColor="red";
        ohSnap('Ingresar la fecha', {color: 'red'});  // alert will have class 'alert-color'
        lVali = false;
    }

    if (select.value==""){
        select.style.borderColor="red";
        ohSnap('Ingresar la fecha', {color: 'red'});  // alert will have class 'alert-color'
        lVali = false;
    }

    if (lVali==true){
        form.submit();
    }

    window.open('../../../template/asistenciaFicha.html','_blank');
}

function loadHTML(){
    fetch('home.html')
    .then(response=> response.text())
    .then(text=> document.getElementById('homePage').innerHTML = text);
  }
  