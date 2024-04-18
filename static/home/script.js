document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("addTaskBtn").addEventListener("click", function() {
        document.getElementById("addTaskForm").style.display = "block";
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const deleteLinks = document.querySelectorAll('.delete-link');

    deleteLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); 

            const url = this.getAttribute('data-url');
            const csrfToken = this.getAttribute('data-csrf');
            const method = this.getAttribute('data-method').toUpperCase();

            const form = document.createElement('form');
            form.setAttribute('method', 'POST');
            form.setAttribute('action', url);

            const csrfInput = document.createElement('input');
            csrfInput.setAttribute('type', 'hidden');
            csrfInput.setAttribute('name', 'csrfmiddlewaretoken');
            csrfInput.setAttribute('value', csrfToken);

            const methodInput = document.createElement('input');
            methodInput.setAttribute('type', 'hidden');
            methodInput.setAttribute('name', '_method');
            methodInput.setAttribute('value', method);

            form.appendChild(csrfInput);
            form.appendChild(methodInput);

            document.body.appendChild(form);
            form.submit();
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const containerTarefas = document.querySelector('.tarefas');

    containerTarefas.addEventListener('click', function(event) {
        const botaoTarefa = event.target.closest('.tarefa-btn');
        if (!botaoTarefa) return;

        event.preventDefault(); 
        const idTarefa = botaoTarefa.dataset.tarefa;
        const descricaoTarefa = document.getElementById('descricao' + idTarefa);

        if (descricaoTarefa.style.display === 'none' || descricaoTarefa.style.display === '') {
            descricaoTarefa.style.display = 'block';
        } else {
            descricaoTarefa.style.display = 'none';
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            this.closest('form').submit();
        });
    });
});


