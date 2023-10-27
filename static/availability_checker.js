
$(document).ready(function () {
    $('#id_date, #id_time').change(function () {
        let date = $('#id_date').val();
        let time = $('#id_time').val();

        if (date && time) {
            $.get('/check_availability/', { date: date, time: time }, function (data) {
                if (data.available) {
                    alert('Date and Time are available!');
                } else {
                    alert('Date and Time are not available.');
                }
            });
        }
    });
});