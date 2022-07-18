function validate(e){

    console.log('Validando ...');
    e.preventDefault();
    // Obtenemos todos los datos de la 
    form  = document.getElementById('asistencia-form');
    date = document.getElementById('date');
    select = document.getElementById('state');
    var value = select.options[select.selectedIndex].value;
    ficha = document.getElementById('ficha').value = value;

    fecha = document.getElementById('date').value;

    lVali = true;
    // Verifica que no este vacio, si no el lVali es false
    if (date.value==""){
        date.style.borderColor="red";
        ohSnap('Ingresar la fecha', {color: 'red'});  // alert will have class 'alert-color'
        lVali = false;
    }
    // Verifica que no este vacio, si no el lVali es false
    if (select.value==""){
        select.style.borderColor="red";
        ohSnap('Ingresar la fecha', {color: 'red'});  // alert will have class 'alert-color'
        lVali = false;
    }

    // Si el lVali es verdadero entonces deja mandar, si no es porq falta algun dato
    if(lVali){
        form.submit();
    }

}
