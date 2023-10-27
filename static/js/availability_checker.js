
$(document).ready(function () {
    let isAvailable = true;

    $('#id_date, #id_time').change(function () {
        let date = $('#id_date').val();
        let time = $('#id_time').val();

        if (date && time) {
            $.get('/check_availability/', { date: date, time: time }, function (data) {
                if (data.available) {
                    alert('Date and Time are available!');
                    isAvailable = true;
                    $('form button[type="submit"]').prop('disabled', false);  // Enable the submit button
                } else {
                    alert('Date and Time are not available.');
                    isAvailable = false;
                    $('form button[type="submit"]').prop('disabled', true);  // Disable the submit button
                }
            });
        }
    });

    $('form').submit(function (e) {
        if (!isAvailable) {
            e.preventDefault();
            alert('Please choose a different date or time.');
        }
    });
});