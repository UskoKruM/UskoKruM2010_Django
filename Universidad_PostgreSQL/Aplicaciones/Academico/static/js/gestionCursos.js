const $formularioCurso = document.getElementById('formularioCurso');
const $txtNombre = document.getElementById('txtNombre');
const $numCreditos = document.getElementById('numCreditos');

const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function () {

    $formularioCurso.addEventListener('submit', function (e) {
        let nombre = String($txtNombre.value).trim();
        if (nombre.length < 3) {
            alert("El nombre del curso no puede ir vacío...");
            e.preventDefault();
        } else {
            let creditos = parseInt($numCreditos.value);
            if (creditos < 1 || creditos > 10) {
                alert("Los créditos deben ser un número entero entre 1 y 10...");
                e.preventDefault();
            }
        }
    });

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function (e) {
            let confirmacion = confirm("¿Confirma la eliminación del curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        })
    });

})();