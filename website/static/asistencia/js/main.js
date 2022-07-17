function validate(e){

    console.log('Validando ...');
    e.preventDefault();

    form  = document.getElementById('asistencia-form');
    date = document.getElementById('date');
    select = document.getElementById('state');
    var value = select.options[select.selectedIndex].value;
    ficha = document.getElementById('ficha').value = value;

    fecha = document.getElementById('date').value;

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

        form.submit();

    }
