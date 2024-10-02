function toasters(text) {
    Toastify({
        text: text, // Use the parameter directly
        className: "info",
        style: {
            backgroundColor: 'rgb(255, 255, 255)',
            borderRadius: '4px',
            paddingLeft: '24px',
            paddingRight: '24px',
            paddingTop: '6px',
            paddingBottom: '6px',
            border: 'none'
        },
        duration: 3000,
        gravity: "top",
        position: 'right',
        onClick: function() {} 
    }).showToast();
}


$(document).ready(function () {
    'use strict';
    
    // Validate forms
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Handle Start Session form submission
    $('#sessionForm').on('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        $.ajax({
            type: 'POST',
            url: '/api/startsession',
            data: $(this).serialize(),
            success: function (response) {
                $('#output').text(response.output);
                toasters("Session Started")
            },
            error: function (xhr) {
                let errorMsg = 'Error: ' + (xhr.responseJSON ? xhr.responseJSON.error : xhr.statusText);
                $('#output').text(errorMsg);
            }
        });
    });

    // Handle Stop Session button click
    $('#stopsessions').on('click', function (event) {
        event.preventDefault(); // Prevent default button action

        $.ajax({
            type: 'POST',
            url: '/api/stopsession',
            data: $('#sessionForm').serialize(), // Send form data
            success: function (response) {
                $('#output').text(response.output);
            },
            error: function (xhr) {
                let errorMsg = 'Error: ' + (xhr.responseJSON ? xhr.responseJSON.error : xhr.statusText);
                $('#output').text(errorMsg);
            }
        });
    });

    // Handle Current Sessions button click
    $('#currentSessionButton').on('click', function (event) {
        event.preventDefault(); // Prevent default button action

        $.ajax({
            type: 'POST',
            url: '/api/runningsessions',
            success: function (response) {
                $('#output').text(response.output);
            },
            error: function (xhr) {
                let errorMsg = 'Error: ' + (xhr.responseJSON ? xhr.responseJSON.error : xhr.statusText);
                $('#output').text(errorMsg);
            }
        });
    });
});
