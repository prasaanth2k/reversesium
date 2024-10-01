$(document).ready(function () {
    (function () {
        'use strict';
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
    })();

    $('#sessionForm').on('submit', function (event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/api/startsession',
            data: $(this).serialize(),
            success: function (response) {
                $('#output').text(response.output);
            },
            error: function (xhr) {
                let errorMsg = 'Error: ' + (xhr.responseJSON ? xhr.responseJSON.error : xhr.statusText);
                $('#output').text(errorMsg);
            }
        });
    });
    $('#currentSessionButton').on('click', function () {
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


$(document).ready(function () {

    (function () {
        'use strict';
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
    })();

    $('#sessionForm').on('submit', function (event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/api/stopsession',
            data: $(this).serialize(),
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