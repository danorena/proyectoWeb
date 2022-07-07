function validate(e){

    console.log('Validando ...');
    e.preventDefault();

    form  = document.getElementById('asistencia-form');
    date = document.getElementById('date');
    select = document.getElementById('state');
    var value = select.options[select.selectedIndex].value;

    console.log(value);

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

        // Segun el valor seleccionado en el select de asistencia nos redirige

        switch (value) {

            case '01':
                window.location.replace('../asistenciaFicha01/');
                break;
    
            case '02':
                window.location.replace('../asistenciaFicha02/');
            break;
    
            case '03':
                window.location.replace('../asistenciaFicha03/');
            break;
        
            default:
                break;
        }

        //form.submit();

    }

}