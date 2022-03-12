/*
const $formularioCurso = document.getElementById("formularioCurso");
const $txtNombre = document.getElementById("txtNombre");
const $numCreditos = document.getElementById("numCreditos");
*/

const btnsEliminacion = document.querySelectorAll(".btnEliminacion");

(function () {
    notificacionSwal(document.title, "Cursos listados con éxito", "success", "Ok");

    formularioCurso.addEventListener("submit", function (e) {
        let nombre = String(txtNombre.value).trim();
        if (nombre.length < 3) {
            notificacionSwal(document.title, "El nombre del curso no puede ir vacío...", "warning", "Ok");
            e.preventDefault();
        } else {
            let creditos = parseInt(numCreditos.value);
            if (creditos < 1 || creditos > 10) {
                notificacionSwal(document.title, "Los créditos deben ser un número entero entre 1 y 10...", "warning", "Ok");
                e.preventDefault();
            }
        }
    });

    /*
    btnsEliminacion.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            let confirmacion = confirm("¿Confirma la eliminación del curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    */

    btnsEliminacion.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            Swal.fire({
                title: "¿Confirma la eliminación del curso?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });
})();
