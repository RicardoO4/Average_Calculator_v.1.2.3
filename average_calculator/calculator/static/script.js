document.addEventListener('DOMContentLoaded', function() {

    const container = document.getElementById('notas');
    const btnAgregar = document.getElementById('agregar');

    btnAgregar.addEventListener('click', () => {
        const inputNota= document.createElement('input');
        console.log('Agregando nueva nota');
        inputNota.type = 'text';
        inputNota.className = 'nota';
        inputNota.placeholder = 'Ingresa la nota';
        inputNota.name = 'grades';
        inputNota.addEventListener('keypress', esNumero)

        const inputPorcentaje = document.createElement('input');
        inputPorcentaje.type = 'text';
        inputPorcentaje.className = 'porcentaje';
        inputPorcentaje.placeholder = '%';
        inputPorcentaje.name = 'weights';
        inputPorcentaje.required = true;
        inputPorcentaje.addEventListener('keypress', esNumeroEntero);

        const saltoLinea = document.createElement('br');
        const saltoLinea2 = document.createElement('br');
        const fila = document.createElement('div');
        fila.className = 'fila';
        

        fila.appendChild(inputNota);
        fila.appendChild(inputPorcentaje);
        fila.appendChild(saltoLinea);
        fila.appendChild(saltoLinea2);
        container.appendChild(fila);
     });
});

function esNumero(e){
    const tecla = e.key;
    return (tecla >= '0' && tecla <= '9') || tecla === '.' || tecla === '-' || tecla === 'Backspace' || tecla === 'Delete';
}

function esNumeroEntero(e){
    const tecla = e.key;
    return (tecla >= '0' && tecla <= '9') || tecla === '-' || tecla === 'Backspace' || tecla === 'Delete';
}


