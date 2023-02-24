const $form_Registro = document.getElementById('form_Registro');
const $txtNombre = document.getElementById('txtNombre');
const $eliminar = document.querySelectorAll('.eliminar');
const $fotoPer = document.getElementById('fotoPer');
const $id_foto = document.getElementById('id_foto');

(function (){

    $fotoPer.addEventListener('submit', function(e){
        let foto = String($id_foto.value).trim();
        if (foto.length == 0){
            alert("No has seleccionado una foto");
            e.preventDefault();
            
        }
        
    });
})();



(function (){

    $form_Registro.addEventListener('submit', function(e){
        let nombre = String($txtNombre.value).trim();
        if (nombre.length == 0){
            alert("El nombre del curso no puede estar vacio");
            e.preventDefault();
            
        }
        
    });
    $eliminar.forEach(btn => {
        btn.addEventListener('click',function(e){
            let confirmacion = confirm("¿Está seguro que desea eliminar este curso?");
            if (!confirmacion){
                e.preventDefault();
            }
        })
    });
})();
