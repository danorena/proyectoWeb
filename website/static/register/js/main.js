function validate(e){

    console.log('Validando ...');
    e.preventDefault();

    form  = document.getElementById('form-detail');
    select = document.getElementById('rol');
    var value = select.options[select.selectedIndex].value;
    rolS = document.getElementById('rolS').value = value;

    lVali = true;
        form.submit();
    }
